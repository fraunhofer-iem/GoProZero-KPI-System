# Working in this repository

This repo makes a **KPI Excel workbook reviewable like code**. The workbook is canonical;
everything else (text snapshots, catalog JSON, HTML/PDF, per-company builds) is derived
from it. Read the [README](README.md) for the full design; this file is the short list of
things to get right.

## Critical conventions — get these wrong and you cause silent data loss

1. **Never edit the workbook with a plain `openpyxl` `load_workbook(...)` → `save(...)`.**
   That round-trip silently destroys the workbook's **62 threaded comments** (text +
   authors) and can drop charts/validation. Fill colours and formulas survive; the comment
   loss is silent and irreversible.
   → To change cell **values**, use the surgical editor: `tools/scripts/xlsx_edit.py`
   (it rewrites only the changed worksheet XML, byte-preserving everything else). It writes
   to `output/`; promote to `data/` by copying over `data/KPI List.xlsx`.

2. **`Metrics List` is a generated mirror — do not hand-edit it.** Raw (level-5) metrics
   live in both their **domain sheet** (the source of truth) and the flat `Metrics List`.
   Edit the domain sheet, then regenerate with `tools/scripts/sync_metrics_list.py`.

3. **`snapshot/*.tsv` is auto-generated** by the `.githooks/pre-commit` hook on every commit
   that stages `data/*.xlsx`. Never hand-edit it. It captures cell **values and formulas**,
   **not fill colours** (hierarchy level is tracked by the `Level` column instead).

4. **Scripts are self-contained UV / PEP-723 files.** Run everything with `uv run` — it
   provisions deps from the inline metadata block. There is no `requirements.txt` or venv to
   activate. Dependencies for a script live in the `# /// script` header at its top.

## Layout

- `data/KPI List.xlsx` — the canonical workbook (tracked as binary). See [data/README.md](data/README.md).
- `snapshot/` — one `.tsv` per sheet; the primary review surface (generated, committed).
- `tools/kpi-engine/` — Python package that reads the workbook into a model and
  computes/validates/exports it. Has its own tests (`pytest` under `tools/kpi-engine/`).
- `tools/scripts/` — standalone `uv run` utilities (see below).
- `tools/templates/` — HTML templates for the manual and visualization (edit design here,
  not the generated HTML).
- `reviews/` — domain-level audits of KPI descriptions & references (see the auditor agent).
- `docs/` — `USER_MANUAL.md` and `KPI_System_Understanding.md`.
- `output/` — generated artifacts (workbooks, catalog JSON, HTML, PDF); gitignored except
  the committed generic-master `kpi-system-visualization.html`.
- `data/literature/`, `data/others/` — **local only, gitignored** (large + copyrighted /
  company-specific). Absent in a fresh clone.

## The workbook model (for reading `snapshot/*.tsv`)

- Sheets: `Overview`, `Top-Level`, the five **domain sheets** (`Environmental Impact`,
  `Economic Viability`, `Circular Efforts`, `Resource Efficiency`, `Social Impact`),
  `Metrics List`, `References`.
- A row is a **raw/leaf metric** when its **`Data?` column = `x`**; otherwise it's a
  composite/aggregate KPI. `Level` encodes hierarchy depth (0 = top score … 5 = raw metric).
- IDs: domain prefix + number, e.g. `EN1` (aggregate) → `EN1-1` (raw child). `Underlying
  Metrics` lists children; `Parent Metrics` lists parents (via `=HYPERLINK` for navigation).
- Multi-valued cells are newline-separated (encoded as `\n` in the snapshot).
- `References` sheet columns: `Title | Description | Label | Type | Link | Comment`. The
  **`Label`** is the reference code (`EN 15804`, `GRI 302-3`, `RM+23`, …) that a metric's
  `Reference` field points to.

## Common commands

```bash
# Compute / validate / export the workbook
uv run kpi-engine compute  "data/KPI List.xlsx"
uv run kpi-engine validate "data/KPI List.xlsx"                 # structural integrity issues
uv run kpi-engine catalog  "data/KPI List.xlsx" --json output/kpi-catalog.json

# Safe editing & regeneration
uv run tools/scripts/xlsx_edit.py "data/KPI List.xlsx" "output/edited.xlsx" --set "Sheet!A1=value"
uv run tools/scripts/sync_metrics_list.py "data/KPI List.xlsx" --report   # dry-run diff
uv run tools/scripts/export_snapshot.py                                   # workbook -> snapshot/

# Build artifacts
uv run tools/scripts/build_visualization.py
uv run tools/scripts/build_manual_pdf.py

# Ground a claim in the literature (local corpus only)
uv run tools/scripts/pdf_search.py "data/literature/<path>.pdf" "term" --context 200

# Engine tests
cd tools/kpi-engine && uv run pytest
```

## When editing KPI definitions

Prefer letting the tools enforce invariants: after any change to a raw metric, run
`sync_metrics_list.py` and `kpi-engine validate`, then commit so the pre-commit hook
re-snapshots. Recommend fixes from reviews to the human; don't silently rewrite definitions.
