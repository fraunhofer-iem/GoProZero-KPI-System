# Version-controlled KPI workbook

This repository makes **every change to the KPI Excel workbook reviewable like code**. You read
it line by line, in the VS Code Source Control panel and in pull-request diffs. The workbook
keeps the information it encodes in formatting.

## Design

The workbook is *not* plain tabular data. Two things carry meaning beyond cell text:

- **Row fill colour encodes the hierarchy level** (Level 1 = pale green through Level 4 =
  bright green, Level-5 raw metrics = grey).
- The Metrics List sheet uses `=HYPERLINK(...)` formulas (in the *Parent Metrics*
  column) for in-file navigation.

So the model is:

1. **The `.xlsx` is canonical.** It lives at `data/KPI List.xlsx`, and git tracks it as a
   binary file. All edits happen in the workbook.
2. **A deterministic text snapshot sits alongside it:** one tab-separated file per sheet
   under `snapshot/`. A pre-commit hook regenerates it on every commit. Because these are
   normal text files, **VS Code's diff editor and GitHub PRs show line-by-line, cell-level
   changes here.** This is the primary review surface.
3. **A git `textconv` diff driver** covers `*.xlsx`, so `git diff` and `git log -p` on the
   workbook itself render readable text on the command line. (VS Code's built-in diff
   editor does not run textconv drivers. That is exactly why the committed snapshot in
   step 2 exists.)

### Snapshot scope and limitation

The snapshot captures cell values and formulas, so hyperlink-target changes show up. Fill
colours are the exception, and the snapshot does **not** carry them. A change to a row's
hierarchy level still shows, because the `Level` column holds that value as text. If you ever
rely on colour without updating the Level column, that change will not appear in the diff.

## Tooling

[UV](https://docs.astral.sh/uv/) runs the Python. The scripts under `tools/scripts/` are
*self-contained*. Each one declares its dependencies in a PEP 723 metadata block at the top of
the file, so `uv run` provisions them automatically. Most need only `openpyxl`. The manual PDF
builder also pulls `markdown` and `weasyprint`, and `pdf_search.py` uses `pymupdf`. The repo
carries no `requirements.txt` and no virtual environment to activate by hand.

## Setup (one time)

Already done in this repo, but to reproduce on a fresh clone (Windows / PowerShell):

```powershell
# Point git at the versioned hook and register the textconv diff driver.
git config core.hooksPath .githooks
git config diff.xlsx.textconv "uv run tools/scripts/xlsx_to_text.py"
git config diff.xlsx.binary true

# Generate the snapshot (uv fetches openpyxl on first run).
uv run tools/scripts/export_snapshot.py
```

> `.git/config` holds `core.hooksPath`, `diff.xlsx.textconv`, and `diff.xlsx.binary`. Git does
> **not** commit that file, so each clone must run the `git config` lines above once.

## Daily workflow

1. Edit `data/KPI List.xlsx`, either in Excel or programmatically via
   `tools/scripts/xlsx_edit.py` (see "Editing programmatically" below). Do *not* edit the
   workbook with a plain openpyxl `load`/`save`: it destroys threaded comments.
2. Stage and commit. The pre-commit hook regenerates `snapshot/` automatically and adds
   it to the commit, so the review surface never drifts from the workbook.
3. Review changes in the VS Code Source Control panel. The `snapshot/*.tsv` diffs show
   exactly which cells changed. Install the recommended extensions (`rainbow-csv`,
   `gc-excelviewer`) when VS Code prompts.
4. For a quick terminal view of the workbook itself:
   `git diff -- "data/KPI List.xlsx"` (rendered via the textconv driver).

## Editing programmatically (preserves everything)

**Why not just use openpyxl?** A plain openpyxl `load_workbook` and `save` rebuilds the whole
file. It silently drops the parts it does not model. The costly loss is this workbook's **62
modern *threaded comments***, along with their text and authors. Charts and data validation may
go the same way. After such a round-trip the comments *look* present but contain only the "Your
version of Excel allows you to read this threaded comment…" placeholder. Fill colours and
formulas do survive, but the comment loss is silent and irreversible.

**The safe tool: `tools/scripts/xlsx_edit.py`.** It treats the `.xlsx` as the zip package it is.
It copies every part byte-for-byte and rewrites *only* the worksheet XML where a cell actually
changes. A check confirms this: editing one cell changes exactly one internal part
(`xl/worksheets/sheetN.xml`), and all threaded comments, persons, colours and hyperlinks survive
bit-for-bit. Reassembled workbooks go to `output/`, so no script run touches the canonical
`data/` copy.

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

Scope: it sets cell values (text or number), editing existing cells and inserting missing ones
in order. It does **not** add or remove rows. `build_company_kpi.py` handles row pruning for
company-specific workbooks separately, editing the master in place (see [Company-specific
workbooks](#company-specific-workbooks)). To promote an edited `output/` file to canonical, copy
it over `data/KPI List.xlsx` and commit (the hook re-snapshots).

## Data model: domain sheets are the source of truth

The workbook stores the same raw metric in two places, so the two can drift apart:

- **Domain sheets** hold the full hierarchy: aggregate KPIs (`EN1`, `EN11` and so on) *and* the
  raw level-5 data points (`EN1-1`, `EN1-2` and so on). The five are Environmental Impact,
  Economic Viability, Circular Efforts, Resource Efficiency and Social Impact. A row is a raw
  data point when its `Data?` column reads `x`.
- **Metrics List** is a flat mirror of only the raw data points. It is a *generated artifact*,
  so do not hand-edit it.

**Rule: edit a raw metric only in its domain sheet, then regenerate Metrics List.**

```bash
# dry run — list every cell where Metrics List differs from the domain source of truth
uv run tools/scripts/sync_metrics_list.py "data/KPI List.xlsx" --report

# write a regenerated copy to output/ for review, then promote it to data/
uv run tools/scripts/sync_metrics_list.py "data/KPI List.xlsx" "output/synced.xlsx"
```

`sync_metrics_list.py` copies every data field from the domain row into the matching Metrics
List row, matched by ID. It edits only the cells that differ, and it works through the surgical
editor so comments, colours and hyperlinks survive. The script leaves the navigation hyperlink
column alone, and it *reports* (never invents) raw metrics missing from Metrics List.

## Reviewing KPIs against the literature

The literature cross-check compares the KPIs against the curated sources in `data/literature/`,
which holds PDFs in per-standard subfolders. The `References` sheet is the bibliography. Its
`Label` column holds the reference code, and each paper's filename carries that code as a
prefix.

- `tools/scripts/pdf_search.py` is the grounding tool: it prints page-numbered, quotable
  snippets, so you can quote any claim about a source verbatim instead of recalling it.
  ```bash
  uv run tools/scripts/pdf_search.py "data/literature/ISO 14XXX/ISO 14067.pdf" "carbon footprint" --context 200
  ```
- `.claude/agents/kpi-literature-crosschecker.md` is a Claude Code subagent that audits a
  *bounded batch* of KPIs (one sheet, or an ID prefix like `EN1`) against the cited sources. It
  checks the indicator name, the description and the reference code against the source text,
  while tolerating intentional product-specific adaptations. It asserts nothing without a
  page-cited quote, and it writes a findings report to `reviews/`. The agent never edits the
  workbook. You apply approved fixes via Excel or `tools/scripts/xlsx_edit.py`. Invoke it per
  batch to keep accuracy high, e.g. *"cross-check the EN1 metrics against the literature."*

## Documentation

- `docs/USER_MANUAL.md` is the user manual. Part A is for practitioners filling the system
  in for a product, Part B for editors changing KPI definitions in Excel.
- `tools/scripts/build_manual_pdf.py` renders it to `output/USER_MANUAL.pdf`, the
  distribution format: `uv run tools/scripts/build_manual_pdf.py`.
- `docs/KPI_System_Understanding.md` holds the system-understanding notes: the model, the
  conventions and the known issues.

## Visualization

A self-contained, interactive HTML visualization of the KPI system, meant as a visual companion
to the user manual. Its hierarchy explorer is searchable and builds from the live catalog.
Further sections cover the five levels, the calculation strategies, bottom-up aggregation,
weights and normalization, the workflow, and the glossary. The page has no external dependencies
and opens directly in a browser.

The source is split into a static template and a build script:

- `tools/templates/kpi_visualization.html.template` is the authored HTML/CSS/JS shell:
  the prose, the layout and the styling, with a single catalog-data marker. **Edit the design
  here**, not the generated HTML. A header comment in the file records which parts auto-sync
  from the catalog and which prose is hand-authored.
- `tools/scripts/build_visualization.py` injects the KPI catalog into the template:

  ```bash
  uv run tools/scripts/build_visualization.py
  ```

  Reads `output/kpi-catalog.json` and writes `output/kpi-system-visualization.html`. Pass
  `--workbook "<file.xlsx>"` to re-export the catalog first, which the engine writes to a temp
  file so it leaves the master catalog alone. Pass `--out <path>` for a different target.

The engine produces the catalog JSON it consumes: `uv run kpi-engine catalog "data/KPI
List.xlsx" --json output/kpi-catalog.json`.

> The page does **not** come from `docs/USER_MANUAL.md`. The two are independent renderings,
> so you must mirror prose changes by hand. The committed
> `output/kpi-system-visualization.html` is the generic master example with no company
> data, and per-company or scoped builds stay local. Because a script generates it, it shows
> as modified after a rebuild. Re-commit it when the catalog or template changes.

## Layout

```
.
├── data/
│   ├── KPI List.xlsx        # canonical workbook
│   └── literature/          # curated source PDFs, per-standard subfolders
├── snapshot/                # generated, committed — the review surface
│   ├── _sheets.txt
│   └── <one .tsv per sheet>
├── output/                  # derived workbooks, catalog JSON, manual PDF (gitignored);
│                            #   the master visualization HTML is committed as an example
├── reviews/                 # literature cross-check + description-audit reports
├── docs/                    # user manual (+ PDF source) + system-understanding notes
├── .claude/agents/          # kpi-literature-crosschecker subagent
├── tools/
│   ├── scripts/             # workbook & build utilities (self-contained uv run scripts)
│   ├── templates/           # HTML template for the visualization
│   └── kpi-engine/          # KPI calculation engine (Python package)
├── .githooks/pre-commit
├── .vscode/extensions.json
├── .gitattributes
└── .gitignore
```

## Do not

- Do not convert the workbook to CSV as the source of truth, and do not regenerate the `.xlsx`
  from text. Either one would drop the level colours and hyperlinks.
- Do not edit files under `snapshot/` by hand. The tooling generates them.
- Do not commit the virtual environment (`.venv/`).

## Company-specific workbooks

The master `data/KPI List.xlsx` holds the full KPI tree. A workshop decides which KPIs are out
of scope for a given product or company. `tools/scripts/build_company_kpi.py` then prunes those
KPIs and their now-orphaned descendants. It writes a derived workbook to `output/`.

- The per-company scope file lives outside the code in `data/others/`, git-ignored and kept
  local, as `<company>.scope.json`. It holds a `remove` map of out-of-scope KPI IDs, plus
  optional `review` and `annotate` entries.
- Removal cascades by reachability. A KPI survives only if it is still reachable from its
  domain root (`EN0`, `EC0`, `C0`, `R0` or `S0`) through non-removed nodes. The script then
  rewrites each kept aggregate's *Underlying Metrics* to list only the surviving children, so
  the derived tree stays internally consistent.
- The derived file is the master edited in place, not a fresh rebuild. The script deletes
  the out-of-scope rows from a loaded copy and saves the result to `output/`. So the sheets
  that do not change (Overview, Top-Level, References) come across verbatim. The
  load-then-save cycle in openpyxl keeps the theme, fill colours, merged cells, row heights,
  fonts and hyperlinks across the whole workbook, with no palette drift. Theme-indexed fills
  like the Resource Efficiency sheet stay their intended colour instead of turning purple.
  Two things openpyxl cannot round-trip need special handling. Anchored images such as the
  Top-Level diagram get grafted back after save. The master's threaded comments do not
  survive, though the textual *Comment* column does. The canonical `data/` workbook is only
  ever opened read-only.

```bash
# reads data/others/acme.scope.json -> output/<label> KPI List.xlsx
uv run tools/scripts/build_company_kpi.py acme
```
