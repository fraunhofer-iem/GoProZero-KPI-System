#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Render the interactive HTML visualization of the KPI system.

A self-contained, single-file web page that mirrors docs/USER_MANUAL.md visually: a live,
searchable hierarchy explorer plus designed sections for the five levels, the six calculation
strategies, aggregation, weights/normalization, the workflow, and the glossary.

How it works: a static HTML/CSS/JS *template* (tools/templates/kpi_visualization.html.template)
carries a single `__CATALOG_JSON__` placeholder. This script loads the descriptive KPI catalog,
trims it to the fields the page uses, and injects it into that placeholder. The result has no
external dependencies (no CDN, no fonts, no network) and opens directly in any browser.

The catalog is the same one the frontend consumes, produced by `kpi-engine catalog`. By default
this script reads an already-exported catalog JSON; pass --workbook to (re)export it first.

Usage:
    uv run tools/scripts/build_visualization.py
        # output/kpi-catalog.json  ->  output/kpi-system-visualization.html

    uv run tools/scripts/build_visualization.py --workbook "output/Company KPI List.xlsx"
        # export the catalog from a workbook first, then build

    uv run tools/scripts/build_visualization.py --catalog path/to/catalog.json --out site.html
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

# Repo layout: this file is tools/scripts/build_visualization.py
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TEMPLATE = ROOT / "tools" / "templates" / "kpi_visualization.html.template"
DEFAULT_CATALOG = ROOT / "output" / "kpi-catalog.json"
DEFAULT_OUT = ROOT / "output" / "kpi-system-visualization.html"
ENGINE_DIR = ROOT / "tools" / "kpi-engine"

PLACEHOLDER = "__CATALOG_JSON__"

# Fields the page actually reads. Everything else (per-company inputs, computed scores) is
# dropped so the embedded blob stays small. Empty/"None" values are omitted per KPI; `id`
# and `level` are always kept because the JS indexes on them.
KEEP_FIELDS = (
    "id", "domain", "level", "name", "description", "objective",
    "underlying", "parents", "potentialReferenceValues", "unit", "formula",
    "references", "calculationStrategy", "isRawDataPoint", "dataSource",
    "lifecycleStages", "exampleValue", "comment", "archived",
)
EMPTY = (None, "", [], "None")


def export_catalog(workbook: Path, out_json: Path) -> None:
    """Run `kpi-engine catalog <workbook> --json <out>` via uv inside the engine project.

    Paths are made absolute because the engine subprocess runs with cwd=ENGINE_DIR (needed so
    `uv run kpi-engine` resolves the engine project), not the repo root the caller sees.
    """
    workbook = workbook.resolve()
    out_json = out_json.resolve()
    if not workbook.exists():
        sys.exit(f"error: workbook not found: {workbook}")
    cmd = ["uv", "run", "kpi-engine", "catalog", str(workbook), "--json", str(out_json)]
    print(f"  exporting catalog from {workbook.name} ...", file=sys.stderr)
    # Drop the parent script's ephemeral VIRTUAL_ENV so the nested `uv run` uses the engine's
    # own .venv cleanly (otherwise uv prints a mismatch warning and ignores it).
    env = {k: v for k, v in os.environ.items() if k != "VIRTUAL_ENV"}
    subprocess.run(cmd, cwd=ENGINE_DIR, check=True, env=env)


def trim_catalog(catalog: dict) -> dict:
    """Keep only the fields the page uses; omit empty values to shrink the embedded JSON."""
    out = {
        "meta": catalog.get("meta", {}),
        "domains": catalog.get("domains", []),
        "kpis": {},
        "references": catalog.get("references", {}),
    }
    for kid, k in catalog.get("kpis", {}).items():
        slim = {f: k[f] for f in KEEP_FIELDS if f in k and k[f] not in EMPTY}
        slim["id"] = k["id"]
        slim["level"] = k["level"]
        out["kpis"][kid] = slim
    return out


def build(template: Path, catalog: dict, out: Path) -> None:
    html = template.read_text(encoding="utf-8")
    if html.count(PLACEHOLDER) != 1:
        sys.exit(f"error: template must contain exactly one {PLACEHOLDER} marker: {template}")
    blob = json.dumps(catalog, separators=(",", ":"), ensure_ascii=False)
    # Prevent the embedded data from terminating the <script> tag early. `<\/` is a valid
    # JSON string escape (parses back to `/`), and these sequences only occur inside strings.
    blob = blob.replace("</", "<\\/")
    out.write_text(html.replace(PLACEHOLDER, blob), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the interactive KPI-system HTML visualization.")
    # --catalog defaults to None so we can tell "user picked it" from "use the default". When
    # --workbook is given without an explicit --catalog, we export to a throwaway temp file
    # rather than overwriting the shared master output/kpi-catalog.json.
    ap.add_argument("--catalog", type=Path, default=None,
                    help=f"catalog JSON to embed (default: {DEFAULT_CATALOG.relative_to(ROOT)})")
    ap.add_argument("--workbook", type=Path, default=None,
                    help="if given, export the catalog from this .xlsx first (via kpi-engine)")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE,
                    help="HTML template with the __CATALOG_JSON__ marker")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT,
                    help=f"output HTML path (default: {DEFAULT_OUT.relative_to(ROOT)})")
    args = ap.parse_args()

    if not args.template.exists():
        sys.exit(f"error: template not found: {args.template}")

    tmp_catalog: Path | None = None
    try:
        if args.workbook:
            # Export target: the explicit --catalog if given, else a temp file so the master
            # catalog is never clobbered by a (possibly company-scoped) workbook export.
            if args.catalog is not None:
                catalog_path = args.catalog
            else:
                fd, name = tempfile.mkstemp(suffix=".json", prefix="kpi-catalog-")
                os.close(fd)
                tmp_catalog = catalog_path = Path(name)
            export_catalog(args.workbook, catalog_path)
        else:
            catalog_path = args.catalog if args.catalog is not None else DEFAULT_CATALOG
            if not catalog_path.exists():
                sys.exit(
                    f"error: catalog not found: {catalog_path}\n"
                    f"       generate one with --workbook <file.xlsx>, or run "
                    f"`kpi-engine catalog <workbook> --json {catalog_path}`."
                )

        catalog = trim_catalog(json.loads(catalog_path.read_text(encoding="utf-8")))
    finally:
        if tmp_catalog is not None:
            tmp_catalog.unlink(missing_ok=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    build(args.template, catalog, args.out)

    kpis = catalog["kpis"]
    active = sum(1 for k in kpis.values() if not k.get("archived"))
    size_kb = args.out.stat().st_size / 1024
    print(
        f"wrote {args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out} "
        f"({size_kb:.0f} KB) — {active} active indicators, "
        f"{len(catalog['references'])} references."
    )


if __name__ == "__main__":
    main()
