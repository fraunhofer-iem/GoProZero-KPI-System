#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["lxml>=5"]
# ///
"""Delete a cell comment from an .xlsx without disturbing anything else.

Why this exists
---------------
A comment is anchored to a cell *address*, not to a row's content. When a sheet is
regenerated with different rows under it -- which is exactly what
``sync_metrics_list.py`` does to ``Metrics List`` -- the rows move and the comments
stay put, so a comment can end up describing an unrelated metric. Deleting the
stale one by hand in Excel works, but every Excel save also rewrites
``absPath`` and printer settings (see ``xlsx_scrub_metadata.py``), so a one-cell
cleanup drags unrelated churn into the diff.

A comment lives in up to three parts, and all three have to agree or Excel reports
a repair:

1. ``xl/threadedComments/threadedCommentN.xml`` -- the real comment and its replies.
2. ``xl/commentsN.xml`` -- the legacy shim Excel writes per thread so that old
   clients can still display something.
3. ``xl/drawings/vmlDrawingN.vml`` -- the little yellow note shape, anchored by
   0-based row and column.

This script removes the entry from all three and copies every other part
byte-for-byte, the same philosophy as ``xlsx_edit.py``. The ``<authors>`` list in
the legacy part is deliberately left alone: comments reference authors by list
*index*, so removing an entry would silently re-point every later comment.

Usage:
    uv run tools/scripts/xlsx_delete_comment.py "data/KPI List.xlsx" --report
    uv run tools/scripts/xlsx_delete_comment.py "data/KPI List.xlsx" output/cleaned.xlsx \
        --delete "Metrics List!C40"
    uv run tools/scripts/xlsx_delete_comment.py "data/KPI List.xlsx" output/cleaned.xlsx --all
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from xlsx_edit import PKGRELS, sheet_part_map  # noqa: E402  (sibling uv script, library use)

TC_NS = "http://schemas.microsoft.com/office/spreadsheetml/2018/threadedcomments"
COMMENTS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
TC_REL = "http://schemas.microsoft.com/office/2017/10/relationships/threadedComment"
VML_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/vmlDrawing"


def cell_to_rowcol(ref: str) -> tuple[int, int]:
    """'C40' -> (39, 2), the 0-based row and column the VML shape is anchored by."""
    m = re.fullmatch(r"([A-Za-z]+)(\d+)", ref)
    if not m:
        sys.exit(f"error: {ref!r} is not a cell reference")
    col = 0
    for ch in m.group(1).upper():
        col = col * 26 + (ord(ch) - 64)
    return int(m.group(2)) - 1, col - 1


def sheet_rels_path(sheet_part: str) -> str:
    return f"{Path(sheet_part).parent.as_posix()}/_rels/{Path(sheet_part).name}.rels"


def sheet_comment_rels(z: zipfile.ZipFile, sheet_part: str) -> dict[str, tuple[str, str]]:
    """Map 'comments' / 'threaded' / 'vml' -> (relationship id, part path) for one sheet."""
    rels_path = sheet_rels_path(sheet_part)
    if rels_path not in z.namelist():
        return {}
    rels = etree.fromstring(z.read(rels_path))
    found = {}
    for r in rels.findall(f"{{{PKGRELS}}}Relationship"):
        target = r.get("Target").replace("../", "xl/").lstrip("/")
        kind = {COMMENTS_REL: "comments", TC_REL: "threaded", VML_REL: "vml"}.get(r.get("Type"))
        if kind:
            found[kind] = (r.get("Id"), target)
    return found


def sheet_comment_parts(z: zipfile.ZipFile, sheet_part: str) -> dict[str, str]:
    """Map 'comments' / 'threaded' / 'vml' -> part path, for one worksheet."""
    return {k: v[1] for k, v in sheet_comment_rels(z, sheet_part).items()}


def purge_all(src: Path, dst: Path) -> None:
    """Remove every comment in the workbook by dropping the parts that hold them.

    Editing the parts is not enough here. An empty commentList is not something Excel
    writes, so the parts themselves go, and then every reference to them has to go too or
    Excel reports a repair: the [Content_Types].xml overrides, the relationship entries in
    the sheet rels and in xl/_rels/workbook.xml.rels, and the <legacyDrawing> element in
    the worksheet that pointed at the VML.

    xl/persons/person.xml goes as well. It exists only to name threaded-comment authors,
    so with the comments gone it is both orphaned and the last place the workbook still
    carries anyone's display name.

    Formatting is untouched: styles.xml, the theme, sharedStrings, the tables and the
    real drawing (xl/drawings/drawing1.xml plus its image) are copied byte-for-byte.
    """
    with zipfile.ZipFile(src) as zin:
        names = set(zin.namelist())
        drop: set[str] = set()
        rewritten: dict[str, bytes] = {}
        removed: list[str] = []

        for sheet, sheet_part in sheet_part_map(zin).items():
            rels = sheet_comment_rels(zin, sheet_part)
            if not rels:
                continue

            # A VML part can also hold form controls. Dropping it would destroy them, so
            # only proceed when every shape in it is a comment note.
            if "vml" in rels:
                vml_text = zin.read(rels["vml"][1]).decode("utf-8")
                shapes = re.findall(r"<v:shape\b.*?</v:shape>", vml_text, re.S)
                notes = [s for s in shapes if 'ObjectType="Note"' in s]
                if len(notes) != len(shapes):
                    sys.exit(f"error: {rels['vml'][1]} holds {len(shapes) - len(notes)} shape(s) "
                             f"that are not comment notes (form controls?). Dropping it would "
                             f"destroy them, so this script stops here.")

            n = 0
            if "threaded" in rels:
                n = len(re.findall(r"<threadedComment\b",
                                   zin.read(rels["threaded"][1]).decode("utf-8")))
            removed.append(f"{sheet}: {n} comment(s)")
            drop.update(target for _, target in rels.values())

            rels_path = sheet_rels_path(sheet_part)
            text = rewritten.get(rels_path, zin.read(rels_path)).decode("utf-8")
            for rid, _ in rels.values():
                text, _n = cut_all(text, rf'<Relationship[^>]*\bId="{rid}"[^>]*/>',
                                   f"relationship {rid}")
            rewritten[rels_path] = text.encode("utf-8")

            if "vml" in rels:
                rid = rels["vml"][0]
                text = rewritten.get(sheet_part, zin.read(sheet_part)).decode("utf-8")
                text, _n = cut_all(text, rf'<legacyDrawing[^>]*\br:id="{rid}"[^>]*/>',
                                   f"legacyDrawing pointing at {rid}")
                rewritten[sheet_part] = text.encode("utf-8")

        if not drop:
            sys.exit("error: this workbook has no comments to remove")

        if "xl/persons/person.xml" in names:
            drop.add("xl/persons/person.xml")
            wb_rels = "xl/_rels/workbook.xml.rels"
            text = zin.read(wb_rels).decode("utf-8")
            text, _n = cut_all(text, r'<Relationship[^>]*persons/person\.xml"[^>]*/>',
                               "person relationship")
            rewritten[wb_rels] = text.encode("utf-8")

        # Only the Overrides go. An unused Default extension is legal, and leaving the vml
        # Default alone keeps the edit to exactly what the removal requires.
        ct = zin.read("[Content_Types].xml").decode("utf-8")
        for part in sorted(drop):
            if f'PartName="/{part}"' in ct:
                ct, _n = cut_all(ct, rf'<Override[^>]*PartName="/{re.escape(part)}"[^>]*/>',
                                 f"content-type override for {part}")
        rewritten["[Content_Types].xml"] = ct.encode("utf-8")

        for path, data in rewritten.items():
            try:
                etree.fromstring(data)
            except etree.XMLSyntaxError as e:
                sys.exit(f"error: rewriting {path} produced invalid XML: {e}")

        dst.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                if info.filename in drop:
                    continue
                zout.writestr(info, rewritten.get(info.filename, zin.read(info.filename)))

    for line in removed:
        print(f"  {line}")
    print("  dropped parts: " + ", ".join(sorted(drop)))
    print(f"wrote {dst}")


def cut_all(text: str, pattern: str, label: str, expect_min: int = 1) -> tuple[str, int]:
    """Remove every match of `pattern` from `text`, byte-exact outside the cuts."""
    out, n = re.subn(pattern, "", text, flags=re.S)
    if n < expect_min:
        sys.exit(f"error: found no {label} to remove")
    return out, n


def delete_comment(src: Path, dst: Path, targets: list[tuple[str, str]]) -> None:
    with zipfile.ZipFile(src) as zin:
        part_map = sheet_part_map(zin)
        rewritten: dict[str, bytes] = {}

        for sheet, cell in targets:
            if sheet not in part_map:
                sys.exit(f"error: no sheet named {sheet!r}; have {list(part_map)}")
            parts = sheet_comment_parts(zin, part_map[sheet])
            if "threaded" not in parts and "comments" not in parts:
                sys.exit(f"error: sheet {sheet!r} carries no comments")
            row, col = cell_to_rowcol(cell)

            # 1. the threaded comment and any replies on the same cell
            path = parts["threaded"]
            text = rewritten.get(path, zin.read(path)).decode("utf-8")
            remaining = len(re.findall(r"<threadedComment\b", text))
            text, n_tc = cut_all(text, rf'<threadedComment\b[^>]*\bref="{cell}"[^>]*>.*?'
                                       r'</threadedComment>', f"threaded comment at {cell}")
            if n_tc >= remaining:
                sys.exit(f"error: {cell} holds the sheet's last comment. Removing it means "
                         f"dropping the comment parts and their relationships, which this "
                         f"script does not do.")
            rewritten[path] = text.encode("utf-8")

            # 2. the legacy shim. Authors are referenced by index, so that list stays.
            if "comments" in parts:
                path = parts["comments"]
                text = rewritten.get(path, zin.read(path)).decode("utf-8")
                text, _ = cut_all(text, rf'<comment\b[^>]*\bref="{cell}"[^>]*>.*?</comment>',
                                  f"legacy comment shim at {cell}")
                rewritten[path] = text.encode("utf-8")

            # 3. the note shape, matched on its 0-based anchor
            if "vml" in parts:
                path = parts["vml"]
                text = rewritten.get(path, zin.read(path)).decode("utf-8")
                shape = (r'<v:shape\b(?:(?!</v:shape>).)*?<x:Row>' + str(row) +
                         r'</x:Row>\s*<x:Column>' + str(col) + r'</x:Column>.*?</v:shape>\s*')
                text, _ = cut_all(text, shape, f"VML note shape at row {row}, col {col}")
                rewritten[path] = text.encode("utf-8")

            print(f"  removed {sheet}!{cell} ({n_tc} threaded element(s), shim, note shape)")

        for path, data in rewritten.items():          # well-formedness gate before writing
            try:
                etree.fromstring(data)
            except etree.XMLSyntaxError as e:
                sys.exit(f"error: rewriting {path} produced invalid XML: {e}")

        dst.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                zout.writestr(info, rewritten.get(info.filename, zin.read(info.filename)))
    print(f"wrote {dst}")


def report(src: Path) -> None:
    with zipfile.ZipFile(src) as z:
        for sheet, sheet_part in sheet_part_map(z).items():
            parts = sheet_comment_parts(z, sheet_part)
            if "threaded" not in parts:
                continue
            root = etree.fromstring(z.read(parts["threaded"]))
            persons = {}
            if "xl/persons/person.xml" in z.namelist():
                persons = {p.get("id"): p.get("displayName")
                           for p in etree.fromstring(z.read("xl/persons/person.xml"))}
            print(f"\n{sheet}  ({parts['threaded']})")
            for c in root:
                ref = c.get("ref")
                who = persons.get(c.get("personId"), "?")
                kind = "reply" if c.get("parentId") else "note "
                body = "".join(c.itertext()).strip().replace("\n", " ")
                print(f"  {ref:6} {kind} [{who}] {body[:96]}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Delete a cell comment from an .xlsx.")
    ap.add_argument("src", type=Path)
    ap.add_argument("dst", type=Path, nargs="?", help="output workbook (omit with --report)")
    ap.add_argument("--delete", action="append", default=[], metavar="SHEET!CELL",
                    help="comment to remove, repeatable")
    ap.add_argument("--all", action="store_true",
                    help="remove every comment in the workbook, dropping the parts that hold "
                         "them (and xl/persons/person.xml, which only they use)")
    ap.add_argument("--report", action="store_true", help="list every comment; write nothing")
    args = ap.parse_args()

    if args.report:
        report(args.src)
        return
    if args.all:
        if not args.dst:
            sys.exit("error: --all needs an output workbook")
        if args.delete:
            sys.exit("error: --all and --delete are mutually exclusive")
        purge_all(args.src, args.dst)
        return
    if not args.dst or not args.delete:
        sys.exit("error: need an output workbook and at least one --delete SHEET!CELL")

    targets = []
    for spec in args.delete:
        if "!" not in spec:
            sys.exit(f"error: --delete wants Sheet!A1, got {spec!r}")
        sheet, cell = spec.rsplit("!", 1)
        targets.append((sheet, cell))
    delete_comment(args.src, args.dst, targets)


if __name__ == "__main__":
    main()
