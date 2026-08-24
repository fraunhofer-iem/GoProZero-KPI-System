# Workbook tooling

Reference for the scripts under `tools/scripts/`. The [README](../README.md) covers the
design and the daily workflow. [AGENTS.md](../AGENTS.md) is the short conventions brief and
the command cheat sheet.

Every script is a self-contained PEP 723 file. `uv run` provisions its dependencies from
the inline metadata block. The repo carries no `requirements.txt` and no virtual
environment to activate by hand.

## Editing the workbook programmatically

A plain openpyxl `load_workbook` and `save` rebuilds the whole file. It silently drops the
parts it does not model. Here that costs the anchored Top-Level diagram, and it rewrites
all 41 package parts, so the tracked binary churns even when one cell changed. Fill
colours, formulas, tables and conditional formatting do survive.

This convention originally protected the workbook's threaded comments. A round-trip left
them *looking* present while they held only the "Your version of Excel allows you to read
this threaded comment..." placeholder. We removed those comments before publication, so
that particular hazard no longer applies to this file. The rewrite behaviour that caused it
still does.

`tools/scripts/xlsx_edit.py` is the safe tool. It treats the `.xlsx` as the zip package it
is, copies every part byte-for-byte, and rewrites only the worksheet XML where a cell
actually changes. A check confirms this. Editing one cell changes exactly one internal part
(`xl/worksheets/sheetN.xml`), and the styles, theme, shared strings, tables, anchored
drawing and hyperlinks all survive bit-for-bit. Reassembled workbooks go to `output/`, so
no script run touches the canonical `data/` copy.

```bash
# CLI: write an edited copy to output/, leaving data/ untouched
uv run tools/scripts/xlsx_edit.py "data/KPI List.xlsx" "output/edited.xlsx" \
    --set "Metrics List!R2=new comment" --set "Top-Level!B3=42"
```

```python
# Library: same thing from Python
from xlsx_edit import set_cells
set_cells("data/KPI List.xlsx", "output/edited.xlsx",
          {"Metrics List": {"R2": "new comment"}})
```

Scope: it sets cell values, either text or number, editing existing cells and inserting
missing ones in order. It does not add or remove rows. `build_company_kpi.py` handles row
pruning for company-specific workbooks separately, editing the master in place. To promote
an edited `output/` file to canonical, copy it over `data/KPI List.xlsx` and commit. The
pre-commit hook re-snapshots.

## Domain sheets are the source of truth

The workbook stores the same raw metric in two places, so the two can drift apart.

Domain sheets hold the full hierarchy: aggregate KPIs (`EN1`, `EN11` and so on) and the raw
level-5 data points (`EN1-1`, `EN1-2` and so on). The five are Environmental Impact,
Economic Viability, Circular Efforts, Resource Efficiency and Social Impact. A row is a raw
data point when its `Data?` column reads `x`.

Metrics List is a flat mirror of the raw data points only. A script generates it, so do not
hand-edit it.

**Edit a raw metric in its domain sheet, then regenerate Metrics List.**

```bash
# dry run: list every cell where Metrics List differs from the domain source of truth
uv run tools/scripts/sync_metrics_list.py "data/KPI List.xlsx" --report

# write a regenerated copy to output/ for review, then promote it to data/
uv run tools/scripts/sync_metrics_list.py "data/KPI List.xlsx" "output/synced.xlsx"
```

`sync_metrics_list.py` copies every data field from the domain row into the matching
Metrics List row, matched by ID. It edits only the cells that differ, and it works through
the surgical editor, so comments, colours and hyperlinks survive. It leaves the navigation
hyperlink column alone. It reports raw metrics missing from Metrics List, and never invents
them.

## Grounding a claim in the literature

`tools/scripts/pdf_search.py` prints page-numbered, quotable snippets from the PDFs in
`data/literature/`. Quote a source from its output instead of recalling it.

```bash
uv run tools/scripts/pdf_search.py "data/literature/ISO 14XXX/ISO 14067.pdf" "carbon footprint" --context 200
```

The `References` sheet is the bibliography. Its `Label` column holds the reference code.
Each PDF filename carries that code as a prefix.
[data/README.md](../data/README.md) catalogs the corpus and explains why git does not
track it.

Git does not track `data/literature/`. In a fresh clone this script has nothing to search
until you supply your own sources. The three review briefs described in
[AGENTS.md](../AGENTS.md) use it too.

## Building the published site

`tools/scripts/build_site.py` builds the public GitHub Pages site: the branded manual as
`index.html`, plus the catalog JSON the page embeds. Pass `--with-explorer` to add the
unbranded hierarchy explorer.

```bash
uv run tools/scripts/build_site.py
```

`.github/workflows/pages.yml` runs this on every push to `main`, so the live page at
https://fraunhofer-iem.github.io/GoProZero-KPI-System/ cannot drift from
`data/KPI List.xlsx`. The workflow needs Settings -> Pages -> Source set to "GitHub
Actions". Git tracks nothing built here: `output/` and `site/` are both gitignored.

## Building the standalone visualization

`output/kpi-system-visualization.html` is a self-contained interactive view of the KPI
system, meant as a visual companion to the user manual. Its hierarchy explorer is
searchable and builds from the live catalog. Further sections cover the five levels, the
calculation strategies, bottom-up aggregation, weights and normalization, the workflow, and
the glossary. The page has no external dependencies and opens directly in a browser.

The source is split in two. `tools/templates/kpi_visualization.html.template` is the
authored HTML/CSS/JS shell. It holds the prose, the layout and the styling, with a single
catalog-data marker. A header comment in the template records which parts auto-sync from
the catalog and which prose is hand-authored.

**Edit the design in the template, not in the generated HTML.**

`tools/scripts/build_visualization.py` injects the KPI catalog into the template.

```bash
uv run tools/scripts/build_visualization.py
```

It reads `output/kpi-catalog.json` and writes `output/kpi-system-visualization.html`. Pass
`--workbook "<file.xlsx>"` to re-export the catalog first, which the engine writes to a
temp file so the master catalog stays untouched. Pass `--out <path>` for a different
target. The engine produces the catalog JSON it consumes:

```bash
uv run kpi-engine catalog "data/KPI List.xlsx" --json output/kpi-catalog.json
```

> The page does not come from `docs/USER_MANUAL.md`. The two are independent renderings, so
> you must mirror prose changes by hand. The committed
> `output/kpi-system-visualization.html` is the generic master example with no company
> data, and per-company or scoped builds stay local. A script generates it, so it shows as
> modified after a rebuild. Re-commit it when the catalog or the template changes.

## Company-specific workbooks

The master `data/KPI List.xlsx` holds the full KPI tree. A workshop decides which KPIs are
out of scope for a given product or company. `tools/scripts/build_company_kpi.py` prunes
those KPIs and their now-orphaned descendants. It writes a derived workbook to `output/`.

```bash
# reads data/others/acme.scope.json -> output/<label> KPI List.xlsx
uv run tools/scripts/build_company_kpi.py acme
```

The per-company scope file lives outside the code in `data/others/`, gitignored and kept
local, as `<company>.scope.json`. It holds a `remove` map of out-of-scope KPI IDs, plus
optional `review` and `annotate` entries.

Removal cascades by reachability. A KPI survives only if it is still reachable from its
domain root (`EN0`, `EC0`, `C0`, `R0` or `S0`) through non-removed nodes. The script then
rewrites each kept aggregate's *Underlying Metrics* to list only the surviving children, so
the derived tree stays internally consistent.

The derived file is the master edited in place, not a fresh rebuild. The script deletes the
out-of-scope rows from a loaded copy and saves the result to `output/`. The sheets that do
not change (Overview, Top-Level, References) therefore come across verbatim. The
load-then-save cycle in openpyxl preserves the theme, fill colours, merged cells, row
heights, fonts and hyperlinks across the whole workbook. The palette does not drift.
Theme-indexed fills like the Resource Efficiency sheet stay their intended colour instead
of turning purple.

One thing openpyxl cannot round-trip needs special handling. Anchored images such as the
Top-Level diagram get grafted back after the save. The master no longer carries cell
comments, and nothing here touches the textual *Comment* column. The script opens the
canonical `data/` workbook read-only.
