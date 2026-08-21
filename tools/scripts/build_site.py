#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Build the public GitHub Pages site from the canonical workbook.

Why this exists
---------------
`output/` is gitignored, so a fresh clone -- including the one the GitHub Actions
runner makes on every push -- contains no HTML at all. Rather than commit a built
page that can silently drift from `data/KPI List.xlsx`, this script regenerates the
site during the deploy. The published page is therefore always the current workbook,
and the repository keeps its rule that derived artifacts are generated, not tracked.

What it produces (default `site/`, the directory the Pages workflow uploads):

    site/index.html         the it's OWL-branded manual -- the landing page
    site/kpi-catalog.json   the machine-readable catalog the page embeds
    site/explorer.html      the unbranded hierarchy explorer (only with --with-explorer)

The heavy lifting belongs to build_visualization.py, which exports the catalog via
`kpi-engine catalog` and injects it into an HTML template at the `__CATALOG_JSON__`
marker. This script only decides which templates make up the site and where they go.
Both pages come out as single self-contained files.

The landing page already embeds the hierarchy explorer as its `#explorer` section, so
`explorer.html` is opt-in: pass --with-explorer to publish the unbranded build too.

Usage:
    uv run tools/scripts/build_site.py                      # -> site/
    uv run tools/scripts/build_site.py --out-dir public     # somewhere else
    uv run tools/scripts/build_site.py --with-explorer       # + explorer.html
    uv run tools/scripts/build_site.py --no-catalog          # do not publish the JSON
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# Repo layout: this file is tools/scripts/build_site.py
ROOT = Path(__file__).resolve().parents[2]
BUILD_VIZ = ROOT / "tools" / "scripts" / "build_visualization.py"
MANUAL_TEMPLATE = ROOT / "tools" / "templates" / "kpi_manual_itsowl.html.template"
EXPLORER_TEMPLATE = ROOT / "tools" / "templates" / "kpi_visualization.html.template"
DEFAULT_WORKBOOK = ROOT / "data" / "KPI List.xlsx"
DEFAULT_OUT = ROOT / "site"


def build_page(*args: str) -> None:
    """Run build_visualization.py as its own uv script so it provisions its own deps."""
    subprocess.run(["uv", "run", str(BUILD_VIZ), *args], cwd=ROOT, check=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the public Pages site.")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT,
                    help=f"directory to write the site into (default: {DEFAULT_OUT.name}/)")
    ap.add_argument("--workbook", type=Path, default=DEFAULT_WORKBOOK,
                    help="workbook the catalog is exported from")
    ap.add_argument("--template", type=Path, default=MANUAL_TEMPLATE,
                    help="template for index.html (default: the it's OWL manual)")
    ap.add_argument("--with-explorer", action="store_true",
                    help="also build explorer.html from the unbranded visualization template")
    ap.add_argument("--no-catalog", action="store_true",
                    help="delete kpi-catalog.json after the build instead of publishing it")
    args = ap.parse_args()

    for label, path in (("workbook", args.workbook), ("template", args.template)):
        if not path.exists():
            sys.exit(f"error: {label} not found: {path}")

    # `kpi-engine catalog --json` will not create missing parent directories, and the
    # catalog is the first thing written, so the output directory has to exist first.
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    catalog = out / "kpi-catalog.json"

    # Clear last run's output so a page this build no longer produces cannot linger and
    # get deployed. Only the names this script writes are removed: --out-dir may point
    # anywhere, so emptying the directory wholesale would be a foot-gun.
    produced = {catalog, out / "index.html", out / "explorer.html"}
    for stale in produced:
        stale.unlink(missing_ok=True)
    leftover = [f.name for f in out.iterdir() if f.is_file()]
    if leftover:
        print(f"note: {out}/ also holds {', '.join(sorted(leftover))}, "
              f"which this script did not write and will not remove")

    # One catalog export, reused by every page, so all pages show the same workbook state.
    build_page("--workbook", str(args.workbook), "--catalog", str(catalog),
               "--template", str(args.template), "--out", str(out / "index.html"))

    if args.with_explorer:
        build_page("--catalog", str(catalog),
                   "--template", str(EXPLORER_TEMPLATE), "--out", str(out / "explorer.html"))

    if args.no_catalog:
        catalog.unlink(missing_ok=True)

    print(f"\nsite ready in {out if not out.is_relative_to(ROOT) else out.relative_to(ROOT)}/")
    for f in sorted(out.iterdir()):
        print(f"  {f.name:24} {f.stat().st_size / 1024:6.0f} KB")


if __name__ == "__main__":
    main()
