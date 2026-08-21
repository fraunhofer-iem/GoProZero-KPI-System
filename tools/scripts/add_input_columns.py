#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["lxml>=5"]
# ///
"""Add the company-input columns to the five domain sheets (Tier 1.2 + engine inputs).

The workbook gains a right-hand input block so a company enters everything in Excel and the
KPI engine can read it back:

    ... | Comment | Target Min | Target Max | Value | Reference Value
              R          S            T          U            V

- Target Min / Target Max (S, T): normalization bounds for NORMALIZED_RATIO rows.
- Value (U): the raw measured number for each Data?=x leaf row.
- Reference Value (V): the comparator (previous-version / industry) used by the handful of
  one-child normalized formulas; blank elsewhere.

Appended at the far right via the surgical editor (xlsx_edit), so threaded comments /
colours / hyperlinks are preserved and no existing column shifts. The new columns do not
inherit row fill colour (they are inputs). Metrics List is NOT touched (it mirrors only raw
rows, which never normalize).

Usage:
    uv run tools/scripts/add_input_columns.py --src "output/KPI List.weights.xlsx" \
        --out "output/KPI List.staged.xlsx"
"""
from __future__ import annotations
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xlsx_edit import set_cells  # noqa: E402

DOMAINS = ["Environmental Impact", "Economic Viability", "Circular Efforts",
           "Resource Efficiency", "Social Impact"]
# header row cells -> column S(19) T(20) U(21) V(22)
HEADERS = {"S1": "Target Min", "T1": "Target Max", "U1": "Value", "V1": "Reference Value"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="output/KPI List.weights.xlsx")
    ap.add_argument("--out", default="output/KPI List.staged.xlsx")
    args = ap.parse_args()
    if not os.path.exists(args.src):
        sys.exit(f"source not found: {args.src} (run seed_default_weights.py --write first)")

    edits = {d: dict(HEADERS) for d in DOMAINS}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    set_cells(args.src, args.out, edits)
    print(f"Added input columns {list(HEADERS.values())} (cols S–V) to {len(DOMAINS)} domain sheets.")
    print(f"Wrote {args.out}. Data cells left blank for company input.")


if __name__ == "__main__":
    main()
