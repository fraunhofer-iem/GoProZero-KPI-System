#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["lxml>=5"]
# ///
"""Strip personal and internal-infrastructure metadata from an .xlsx package.

Why this exists
---------------
Excel embeds a surprising amount of provenance in the package that is invisible
in the grid AND invisible in `snapshot/*.tsv` (which captures cell values and
formulas only). Before publishing the workbook, four things have to go:

1. ``xl/persons/person.xml`` -- threaded-comment authors carry a work **email
   address** and an **Entra/Azure-AD object GUID** per person
   (``userId="S::first.last@example.org::<guid>"``).
2. ``xl/printerSettings/*.bin`` -- the DEVMODE blob names the **print server and
   queue** the file was last printed to (an internal UNC hostname).
3. ``xl/workbook.xml`` -> ``x15ac:absPath`` -- the **local Windows path** the file
   was last saved from, including the account name in ``C:\\Users\\<id>\\``.
   ``xr:revisionPtr/@documentId`` likewise identifies the doc for co-authoring.
4. ``customXml/*`` + ``docProps/custom.xml`` -- **SharePoint/M365 document-library
   metadata**: content-type id, site/list GUIDs, taxonomy term-store id.

Excel regenerates 2 and 3 on **every save**, so this is a step to re-run before
each publish, not a one-off cleanup.

How it does it safely
---------------------
Same philosophy as ``xlsx_edit.py``: treat the .xlsx as the zip package it is and
copy every part byte-for-byte, rewriting ONLY the handful of parts that carry the
offending data. Nothing goes through openpyxl, so **threaded comments, fill
colours, charts, data validation, tables and hyperlinks are preserved**.

Removing a part means fixing everything that points at it, or Excel reports a
corrupt file. This script keeps the package consistent:

* drops the ``[Content_Types].xml`` entries for removed parts;
* drops the ``<Relationship>`` entries that targeted them, in ``_rels/.rels``,
  ``xl/_rels/workbook.xml.rels`` and the per-sheet rels;
* strips ``<pageSetup r:id="...">`` from each worksheet whose printerSettings
  relationship was removed (a dangling ``r:id`` is the usual corruption cause).

``--verify`` then re-checks the written package end to end: every part has a
content type, every relationship target resolves, every ``r:id`` referenced in a
part exists in that part's rels, and every XML part parses. It also byte-compares
against the source so you can see exactly which parts were touched.

CLI use
-------
    # inspect only -- what would change, and what identities are embedded
    uv run tools/scripts/xlsx_scrub_metadata.py "data/KPI List.xlsx" --report

    # write a scrubbed copy, anonymising every comment author
    uv run tools/scripts/xlsx_scrub_metadata.py "data/KPI List.xlsx" \
        output/KPI-List-public.xlsx --anonymize

    # ...but keep your own name on your own comments
    uv run tools/scripts/xlsx_scrub_metadata.py "data/KPI List.xlsx" \
        output/KPI-List-public.xlsx --anonymize --rename "Doe, Jane=Jane Doe"

Emails and AD GUIDs are ALWAYS removed. ``--anonymize`` additionally replaces the
display names with ``Reviewer 1..N``; without it the display names are kept as-is
(a name with no email attached), which may be fine for internal authors.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

from lxml import etree

PKGRELS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
TC_NS = "http://schemas.microsoft.com/office/spreadsheetml/2018/threadedcomments"

PERSON_PART = "xl/persons/person.xml"
CONTENT_TYPES = "[Content_Types].xml"
ROOT_RELS = "_rels/.rels"
WORKBOOK = "xl/workbook.xml"
WORKBOOK_RELS = "xl/_rels/workbook.xml.rels"

# Parts removed wholesale. printerSettings carry the print-server UNC path;
# customXml/ and docProps/custom.xml carry the SharePoint library metadata.
DROP_PREFIXES = ("xl/printerSettings/", "customXml/")
DROP_EXACT = ("docProps/custom.xml",)


def is_dropped(name: str) -> bool:
    return name.startswith(DROP_PREFIXES) or name in DROP_EXACT


# ---- person.xml ----------------------------------------------------------

def read_persons(data: bytes) -> list[dict[str, str]]:
    """Parse person.xml into [{id, displayName, userId, providerId}, ...]."""
    root = etree.fromstring(data)
    out = []
    for p in root.findall(f"{{{TC_NS}}}person"):
        out.append({
            "id": p.get("id") or "",
            "displayName": p.get("displayName") or "",
            "userId": p.get("userId") or "",
            "providerId": p.get("providerId") or "",
        })
    return out


def rewrite_persons(persons: list[dict[str, str]], names: list[str]) -> bytes:
    """Rebuild person.xml with new display names and no identity attributes.

    The ``id`` of each person is preserved verbatim -- threaded comments
    reference it via ``personId``, so changing it would orphan the comments.
    ``providerId="None"`` is what Excel itself writes for a person with no
    directory identity behind them.
    """
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
        f'<personList xmlns="{TC_NS}" '
        'xmlns:x="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    ]
    for person, name in zip(persons, names):
        parts.append(
            f'<person displayName="{escape_attr(name)}" '
            f'id="{person["id"]}" providerId="None"/>'
        )
    parts.append("</personList>")
    return "".join(parts).encode("utf-8")


def escape_attr(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def plan_names(persons: list[dict[str, str]], anonymize: bool,
               renames: dict[str, str]) -> list[str]:
    """Decide the new display name for each person, in document order.

    Explicit ``--rename`` wins. Otherwise ``--anonymize`` assigns
    ``Reviewer N`` numbered over the persons that were NOT renamed, so the
    numbering has no gaps. Without ``--anonymize`` the name is left alone.
    """
    out: list[str] = []
    n = 0
    for p in persons:
        original = p["displayName"]
        if original in renames:
            out.append(renames[original])
        elif anonymize:
            n += 1
            out.append(f"Reviewer {n}")
        else:
            out.append(original)
    return out


# ---- surgical string edits on the affected XML parts ---------------------

def strip_content_types(text: str) -> str:
    """Drop the Overrides for removed parts and the now-unused .bin Default."""
    def keep(m: re.Match) -> str:
        tag = m.group(0)
        pn = re.search(r'PartName="([^"]*)"', tag)
        if pn and is_dropped(pn.group(1).lstrip("/")):
            return ""
        return tag

    text = re.sub(r"<Override\b[^>]*/>", keep, text)
    # Nothing but printerSettings used the .bin extension.
    text = re.sub(
        r'<Default\s+Extension="bin"[^>]*printerSettings"\s*/>', "", text)
    return text


def strip_rels(text: str, predicate) -> tuple[str, list[str]]:
    """Remove <Relationship> elements whose Target matches; return removed Ids."""
    removed: list[str] = []

    def keep(m: re.Match) -> str:
        tag = m.group(0)
        tgt = re.search(r'Target="([^"]*)"', tag)
        rid = re.search(r'Id="([^"]*)"', tag)
        if tgt and predicate(tgt.group(1)):
            if rid:
                removed.append(rid.group(1))
            return ""
        return tag

    return re.sub(r"<Relationship\b[^>]*/>", keep, text), removed


def strip_workbook_provenance(text: str) -> str:
    """Remove the absPath AlternateContent block and the revisionPtr."""
    def drop_alt(m: re.Match) -> str:
        # Only the block that actually carries absPath -- leave any other
        # AlternateContent (they can carry real features) alone.
        return "" if "absPath" in m.group(0) else m.group(0)

    text = re.sub(r"<mc:AlternateContent\b.*?</mc:AlternateContent>",
                  drop_alt, text, flags=re.DOTALL)
    text = re.sub(r"<xr:revisionPtr\b[^>]*/>", "", text)
    return text


def strip_pagesetup_rid(text: str, rid: str) -> str:
    """Remove r:id="<rid>" from the <pageSetup> tag of a worksheet.

    Left in place it would be a relationship reference with no relationship --
    exactly what makes Excel declare the file unreadable.
    """
    def fix(m: re.Match) -> str:
        return re.sub(rf'\s+r:id="{re.escape(rid)}"', "", m.group(0))

    return re.sub(r"<pageSetup\b[^>]*/?>", fix, text)


# ---- the scrub -----------------------------------------------------------

def scrub(src: Path, dst: Path, anonymize: bool,
          renames: dict[str, str]) -> dict:
    report: dict = {"dropped": [], "rewritten": [], "persons": []}

    with zipfile.ZipFile(src) as zin:
        names = zin.namelist()
        blobs = {n: zin.read(n) for n in names}
        infos = {i.filename: i for i in zin.infolist()}

    # -- which printerSettings relationship does each worksheet use?
    # Collected first, because dropping it also means editing the worksheet.
    sheet_rid: dict[str, str] = {}
    for name in names:
        m = re.fullmatch(r"xl/worksheets/_rels/(sheet\d+)\.xml\.rels", name)
        if not m:
            continue
        text = blobs[name].decode("utf-8")
        new_text, removed = strip_rels(
            text, lambda t: t.lstrip("./").startswith("printerSettings/")
                            or "printerSettings" in t)
        if removed:
            blobs[name] = new_text.encode("utf-8")
            report["rewritten"].append(name)
            sheet_rid[f"xl/worksheets/{m.group(1)}.xml"] = removed[0]

    for sheet, rid in sheet_rid.items():
        text = blobs[sheet].decode("utf-8")
        new_text = strip_pagesetup_rid(text, rid)
        if new_text != text:
            blobs[sheet] = new_text.encode("utf-8")
            report["rewritten"].append(sheet)

    # -- root rels: docProps/custom.xml
    text = blobs[ROOT_RELS].decode("utf-8")
    new_text, removed = strip_rels(
        text, lambda t: t.lstrip("/") == "docProps/custom.xml")
    if removed:
        blobs[ROOT_RELS] = new_text.encode("utf-8")
        report["rewritten"].append(ROOT_RELS)

    # -- workbook rels: customXml items
    text = blobs[WORKBOOK_RELS].decode("utf-8")
    new_text, removed = strip_rels(
        text, lambda t: t.lstrip("./").startswith("customXml/"))
    if removed:
        blobs[WORKBOOK_RELS] = new_text.encode("utf-8")
        report["rewritten"].append(WORKBOOK_RELS)

    # -- workbook.xml: absPath + revisionPtr
    text = blobs[WORKBOOK].decode("utf-8")
    new_text = strip_workbook_provenance(text)
    if new_text != text:
        blobs[WORKBOOK] = new_text.encode("utf-8")
        report["rewritten"].append(WORKBOOK)

    # -- content types
    text = blobs[CONTENT_TYPES].decode("utf-8")
    new_text = strip_content_types(text)
    if new_text != text:
        blobs[CONTENT_TYPES] = new_text.encode("utf-8")
        report["rewritten"].append(CONTENT_TYPES)

    # -- person.xml
    if PERSON_PART in blobs:
        persons = read_persons(blobs[PERSON_PART])
        new_names = plan_names(persons, anonymize, renames)
        blobs[PERSON_PART] = rewrite_persons(persons, new_names)
        report["rewritten"].append(PERSON_PART)
        for p, new in zip(persons, new_names):
            report["persons"].append({
                "was": p["displayName"], "now": new,
                "identity_removed": p["userId"] or "(none)",
            })

    # -- write, preserving entry order and per-entry compression
    dst.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dst, "w") as zout:
        for name in names:
            if is_dropped(name):
                report["dropped"].append(name)
                continue
            src_info = infos[name]
            info = zipfile.ZipInfo(name, date_time=src_info.date_time)
            info.compress_type = src_info.compress_type
            info.external_attr = src_info.external_attr
            info.create_system = src_info.create_system
            zout.writestr(info, blobs[name])

    return report


# ---- verification --------------------------------------------------------

R_ATTR = re.compile(rb'r:(?:id|embed|link)="([^"]+)"')


def rels_path_for(part: str) -> str:
    p = Path(part)
    return str(p.parent / "_rels" / (p.name + ".rels")).replace("\\", "/")


def _norm(rels_part: str, target: str) -> str:
    # rels live at <dir>/_rels/<name>.rels, so targets resolve against <dir>
    base_dir = Path(rels_part).parent.parent
    parts: list[str] = []
    for seg in (str(base_dir / target)).replace("\\", "/").split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if parts:
                parts.pop()
        else:
            parts.append(seg)
    return "/".join(parts)


def verify(path: Path) -> list[str]:
    """Check OPC integrity the way Excel does before it opens a file."""
    problems: list[str] = []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())

        # 1. every part parses, and every part has a content type
        ct = etree.fromstring(z.read(CONTENT_TYPES))
        defaults = {d.get("Extension", "").lower(): d.get("ContentType")
                    for d in ct.findall(f"{{{CT_NS}}}Default")}
        overrides = {o.get("PartName", "").lstrip("/"): o.get("ContentType")
                     for o in ct.findall(f"{{{CT_NS}}}Override")}

        for name in sorted(names):
            if name == CONTENT_TYPES:
                continue
            ext = name.rsplit(".", 1)[-1].lower()
            if name not in overrides and ext not in defaults:
                problems.append(f"no content type for part: {name}")
            if name.endswith((".xml", ".rels", ".vml")):
                try:
                    etree.fromstring(z.read(name))
                except etree.XMLSyntaxError as e:
                    problems.append(f"malformed XML in {name}: {e}")

        for pn in sorted(overrides):
            if pn not in names:
                problems.append(f"Content_Types Override for missing part: {pn}")

        # 2. every relationship target resolves to a real part
        rel_ids: dict[str, set[str]] = {}
        for name in sorted(n for n in names if n.endswith(".rels")):
            root = etree.fromstring(z.read(name))
            ids = set()
            for r in root.findall(f"{{{PKGRELS}}}Relationship"):
                ids.add(r.get("Id"))
                if (r.get("TargetMode") or "").lower() == "external":
                    continue
                tgt = _norm(name, r.get("Target", ""))
                if tgt not in names:
                    problems.append(
                        f"{name}: relationship {r.get('Id')} -> missing part {tgt}")
            rel_ids[name] = ids

        # 3. every r:id referenced by a part exists in that part's rels
        for name in sorted(n for n in names
                           if n.endswith(".xml") and not n.endswith(".rels")):
            refs = set(m.decode() for m in R_ATTR.findall(z.read(name)))
            if not refs:
                continue
            rp = rels_path_for(name)
            have = rel_ids.get(rp, set())
            for rid in sorted(refs - have):
                problems.append(
                    f"{name}: references {rid} but {rp} does not declare it")

    return problems


def diff_parts(src: Path, dst: Path) -> tuple[list[str], list[str], list[str]]:
    """Return (removed, modified, unchanged) part lists between two packages."""
    with zipfile.ZipFile(src) as a, zipfile.ZipFile(dst) as b:
        an, bn = a.namelist(), set(b.namelist())
        removed = [n for n in an if n not in bn]
        modified, unchanged = [], []
        for n in an:
            if n not in bn:
                continue
            (modified if a.read(n) != b.read(n) else unchanged).append(n)
    return removed, modified, unchanged


# ---- residue scan -------------------------------------------------------

PATTERNS = {
    "email address": re.compile(
        rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "UNC host path": re.compile(rb"\\\\[A-Za-z0-9._-]{2,}\\[A-Za-z0-9._-]+"),
    "Windows user path": re.compile(rb"C:\\Users\\[A-Za-z0-9._-]+", re.IGNORECASE),
    "absPath": re.compile(rb"absPath"),
    "SharePoint contentTypeId": re.compile(rb"ContentTypeId"),
}


def scan_residue(path: Path) -> list[str]:
    """Re-scan a package for the categories this script is meant to remove.

    Each part is scanned twice: as-is, and with NUL bytes stripped. The printer
    DEVMODE blob stores the device name as UTF-16LE, so the print-server UNC
    path is invisible to a plain byte scan.
    """
    hits: list[str] = []
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            raw = z.read(name)
            seen: set[str] = set()
            for data in (raw, raw.replace(b"\x00", b"")):
                for label, pat in PATTERNS.items():
                    for m in pat.findall(data):
                        text = m.decode("utf-8", "replace")
                        key = f"{label}: {text}"
                        if key in seen:
                            continue
                        seen.add(key)
                        hits.append(f"{name}: {key}")
    return hits


# ---- CLI ----------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Strip personal and internal metadata from an .xlsx.")
    ap.add_argument("src", help="source workbook")
    ap.add_argument("dst", nargs="?", help="output workbook (omit with --report)")
    ap.add_argument("--anonymize", action="store_true",
                    help="replace comment-author display names with 'Reviewer N'")
    ap.add_argument("--rename", action="append", default=[], metavar="OLD=NEW",
                    help="keep a specific author under a chosen name (repeatable)")
    ap.add_argument("--report", action="store_true",
                    help="show what is embedded and what would change; write nothing")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_file():
        print(f"error: no such file: {src}", file=sys.stderr)
        return 2

    renames: dict[str, str] = {}
    for r in args.rename:
        if "=" not in r:
            print(f"error: --rename needs OLD=NEW, got {r!r}", file=sys.stderr)
            return 2
        old, new = r.split("=", 1)
        renames[old] = new

    if args.report:
        print(f"== embedded metadata in {src}\n")
        with zipfile.ZipFile(src) as z:
            if PERSON_PART in z.namelist():
                print("comment authors (xl/persons/person.xml):")
                for p in read_persons(z.read(PERSON_PART)):
                    print(f"  {p['displayName']!r}")
                    print(f"      identity: {p['userId'] or '(none)'}")
                print()
            dropped = [n for n in z.namelist() if is_dropped(n)]
            if dropped:
                print(f"parts that would be removed ({len(dropped)}):")
                for n in dropped:
                    print(f"  {n}")
                print()
        print("residue scan of the SOURCE:")
        for h in scan_residue(src) or ["  (clean)"]:
            print(f"  {h}")
        return 0

    if not args.dst:
        print("error: provide an output path, or use --report", file=sys.stderr)
        return 2

    dst = Path(args.dst)
    report = scrub(src, dst, args.anonymize, renames)

    print(f"== scrubbed {src} -> {dst}\n")
    if report["persons"]:
        print("comment authors:")
        for p in report["persons"]:
            arrow = "kept as" if p["was"] == p["now"] else "->"
            print(f"  {p['was']!r} {arrow} {p['now']!r}")
            print(f"      identity removed: {p['identity_removed']}")
        print()

    removed, modified, unchanged = diff_parts(src, dst)
    print(f"parts removed  ({len(removed)}):")
    for n in removed:
        print(f"  - {n}")
    print(f"\nparts rewritten ({len(modified)}):")
    for n in modified:
        print(f"  ~ {n}")
    print(f"\nparts byte-identical to source: {len(unchanged)}")

    print("\n== package integrity")
    problems = verify(dst)
    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        print(f"\n{len(problems)} problem(s) -- do NOT promote this file.")
        return 1
    print("  OK  every part has a content type")
    print("  OK  every relationship target resolves")
    print("  OK  every r:id reference is declared")
    print("  OK  every XML part parses")

    print("\n== residue scan of the OUTPUT")
    hits = scan_residue(dst)
    if hits:
        for h in hits:
            print(f"  FAIL {h}")
        return 1
    print("  OK  no emails, UNC paths, user paths, absPath or SharePoint ids")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
