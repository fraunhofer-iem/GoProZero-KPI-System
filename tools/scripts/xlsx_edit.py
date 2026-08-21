#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["lxml>=5"]
# ///
"""Surgically edit cell values in an .xlsx WITHOUT going through a full rewrite.

Why this exists
---------------
openpyxl (and most libraries) rebuild the whole workbook on save and silently
DROP parts they don't model -- notably modern *threaded comments*
(`xl/threadedComments/*`, `xl/persons/person.xml`), and potentially charts and
data validation. This module instead treats the .xlsx as the zip package it is:
it copies every part byte-for-byte and rewrites ONLY the worksheet XML parts that
contain a changed cell. Everything else -- threaded comments, fill colours,
hyperlinks, charts, sharedStrings -- is preserved untouched.

Scope: sets cell *values* (text or number). Edits existing cells and inserts
missing cells/rows in the correct order. It does NOT add/remove rows or move
comment anchors -- that (needed for the company-subset feature) is a separate,
harder problem handled elsewhere.

Library use
-----------
    from xlsx_edit import set_cells
    set_cells("data/KPI List.xlsx", "output/edited.xlsx",
              {"Metrics List": {"R2": "new comment", "B5": 42}})

CLI use
-------
    uv run tools/scripts/xlsx_edit.py SRC DST --set "Sheet!A1=hello" --set "Sheet!B2=3.14"
"""
from __future__ import annotations
import argparse
import re
import shutil
import zipfile
from lxml import etree

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
RELS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKGRELS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN}


# ---- column-ref helpers --------------------------------------------------

def col_to_idx(letters: str) -> int:
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch.upper()) - ord("A") + 1)
    return n


def split_ref(ref: str) -> tuple[str, int]:
    m = re.fullmatch(r"([A-Za-z]+)(\d+)", ref)
    if not m:
        raise ValueError(f"bad cell ref: {ref!r}")
    return m.group(1).upper(), int(m.group(2))


# ---- locate worksheet parts ----------------------------------------------

def sheet_part_map(z: zipfile.ZipFile) -> dict[str, str]:
    """Map sheet display name -> worksheet part path (e.g. 'xl/worksheets/sheet8.xml')."""
    wb = etree.fromstring(z.read("xl/workbook.xml"))
    rels = etree.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {
        r.get("Id"): r.get("Target")
        for r in rels.findall(f"{{{PKGRELS}}}Relationship")
    }
    out: dict[str, str] = {}
    for s in wb.findall("m:sheets/m:sheet", NS):
        rid = s.get(f"{{{RELS}}}id")
        tgt = rid_to_target[rid].lstrip("/")  # rels Target may be absolute (/xl/...) or relative
        if not tgt.startswith("xl/"):
            tgt = "xl/" + tgt
        out[s.get("name")] = tgt
    return out


# ---- worksheet cell surgery ----------------------------------------------

def _get_or_make_row(sheet_data, rownum: int):
    rows = sheet_data.findall("m:row", NS)
    for r in rows:
        if int(r.get("r")) == rownum:
            return r
    # insert a new row in ascending order
    new = etree.SubElement(sheet_data, f"{{{MAIN}}}row")
    new.set("r", str(rownum))
    sheet_data.remove(new)
    insert_at = len(rows)
    for i, r in enumerate(rows):
        if int(r.get("r")) > rownum:
            insert_at = i
            break
    sheet_data.insert(list(sheet_data).index(rows[insert_at]) if insert_at < len(rows) else len(sheet_data), new)
    return new


def _get_or_make_cell(row, ref: str):
    letters, _ = split_ref(ref)
    target_col = col_to_idx(letters)
    cells = row.findall("m:c", NS)
    for c in cells:
        if c.get("r") == ref:
            return c
    new = etree.Element(f"{{{MAIN}}}c")
    new.set("r", ref)
    insert_at = len(cells)
    for i, c in enumerate(cells):
        cl, _ = split_ref(c.get("r"))
        if col_to_idx(cl) > target_col:
            insert_at = i
            break
    if insert_at < len(cells):
        cells[insert_at].addprevious(new)
    else:
        row.append(new)
    return new


def _set_cell_value(cell, value):
    """Set value, preserving the cell's coordinate (r) and style (s). Text -> inline
    string; number -> numeric. clear() wipes attributes, so both are restored."""
    ref = cell.get("r")
    style = cell.get("s")
    cell.clear()
    if ref is not None:
        cell.set("r", ref)
    if style is not None:
        cell.set("s", style)
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        cell.attrib.pop("t", None)
        v = etree.SubElement(cell, f"{{{MAIN}}}v")
        v.text = repr(value) if isinstance(value, float) else str(value)
    else:
        cell.set("t", "inlineStr")
        is_ = etree.SubElement(cell, f"{{{MAIN}}}is")
        t = etree.SubElement(is_, f"{{{MAIN}}}t")
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = str(value)


def _edit_worksheet_xml(xml_bytes: bytes, cell_edits: dict[str, object]) -> bytes:
    tree = etree.fromstring(xml_bytes)
    sheet_data = tree.find("m:sheetData", NS)
    for ref, value in cell_edits.items():
        _, rownum = split_ref(ref)
        row = _get_or_make_row(sheet_data, rownum)
        cell = _get_or_make_cell(row, ref)
        cell.set("r", ref)  # ensure ref survives clear()
        _set_cell_value(cell, value)
    return etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)


# ---- package-level driver -------------------------------------------------

def set_cells(src: str, dst: str, edits: dict[str, dict[str, object]]) -> None:
    """Copy src -> dst, rewriting only the worksheet parts touched by `edits`.

    edits: {sheet_name: {cell_ref: value, ...}, ...}
    """
    with zipfile.ZipFile(src) as zin:
        part_map = sheet_part_map(zin)
        rewritten: dict[str, bytes] = {}
        for sheet, cell_edits in edits.items():
            if sheet not in part_map:
                raise KeyError(f"sheet {sheet!r} not found; have {list(part_map)}")
            part = part_map[sheet]
            rewritten[part] = _edit_worksheet_xml(zin.read(part), cell_edits)

        infos = zin.infolist()
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in infos:
                data = rewritten.get(info.filename, zin.read(info.filename))
                # preserve original compression type per entry
                zout.writestr(info, data)


def _parse_set(arg: str):
    m = re.fullmatch(r"(.+?)!([A-Za-z]+\d+)=(.*)", arg, re.S)
    if not m:
        raise argparse.ArgumentTypeError(f"--set must be Sheet!A1=value, got {arg!r}")
    sheet, ref, raw = m.group(1), m.group(2), m.group(3)
    try:
        val: object = int(raw)
    except ValueError:
        try:
            val = float(raw)
        except ValueError:
            val = raw
    return sheet, ref, val


def main():
    ap = argparse.ArgumentParser(description="Surgically set cell values, preserving all other workbook parts.")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--set", dest="sets", action="append", type=_parse_set, required=True,
                    help='Sheet!A1=value (repeatable). Value parsed as int/float if possible, else text.')
    args = ap.parse_args()
    edits: dict[str, dict[str, object]] = {}
    for sheet, ref, val in args.sets:
        edits.setdefault(sheet, {})[ref] = val
    set_cells(args.src, args.dst, edits)
    n = sum(len(v) for v in edits.values())
    print(f"Wrote {args.dst} with {n} cell edit(s) across {len(edits)} sheet(s); all other parts copied verbatim.")


if __name__ == "__main__":
    main()
