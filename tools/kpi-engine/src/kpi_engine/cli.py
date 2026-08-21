"""Command-line interface for the KPI engine.

    kpi-engine compute "data/KPI List.xlsx" [--json out.json]
    kpi-engine validate "data/KPI List.xlsx"
    kpi-engine catalog "data/KPI List.xlsx" --json catalog.json
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from kpi_engine.catalog import load_catalog
from kpi_engine.engine import evaluate_all
from kpi_engine.loader import load_workbook_model
from kpi_engine.report import (
    catalog_to_json,
    render_catalog_summary,
    render_issues,
    render_results,
    results_to_json,
)
from kpi_engine.validate import validate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kpi-engine", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_compute = sub.add_parser("compute", help="compute all KPI scores from the workbook")
    p_compute.add_argument("workbook", type=Path)
    p_compute.add_argument("--json", type=Path, default=None,
                           help="also write machine-readable results to this path")

    p_validate = sub.add_parser("validate", help="report structural integrity issues")
    p_validate.add_argument("workbook", type=Path)

    p_catalog = sub.add_parser(
        "catalog", help="export the descriptive KPI catalog as JSON (for a frontend)")
    p_catalog.add_argument("workbook", type=Path)
    p_catalog.add_argument("--json", type=Path, default=None,
                           help="write the catalog JSON to this path (else stdout)")

    args = parser.parse_args(argv)

    if not args.workbook.exists():
        print(f"error: workbook not found: {args.workbook}", file=sys.stderr)
        return 2

    if args.command == "catalog":
        catalog = load_catalog(args.workbook)
        payload = catalog_to_json(catalog)
        if args.json is not None:
            args.json.write_text(payload, encoding="utf-8")
            print(render_catalog_summary(catalog))
            print(f"Wrote catalog JSON to {args.json}")
        else:
            print(payload)
        return 0

    kpis = load_workbook_model(args.workbook)

    if args.command == "validate":
        print(render_issues(validate(kpis)))
        return 0

    # compute
    results = evaluate_all(kpis)
    print(render_results(kpis, results))
    if args.json is not None:
        args.json.write_text(results_to_json(results), encoding="utf-8")
        print(f"\nWrote JSON results to {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
