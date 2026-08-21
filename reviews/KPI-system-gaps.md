# KPI System — Gap & Inconsistency Audit

*Audit date: 2026-06-23. Source of truth: `data/KPI List.xlsx` via the committed
`snapshot/*.tsv` (266 unique KPI IDs across the five domain sheets; 148 raw `Data?=x`
metrics; 51 reference labels).*

> **Scope & method.** This audit programmatically checked the five domain sheets and the
> Metrics List / References sheets for structural integrity (parent/child link symmetry,
> reachability from each domain root, dangling IDs), run-readiness (weights, normalisation
> reference values), and field completeness (levels, units, calculation strategies,
> citation resolution). Every finding below cites concrete IDs and counts. Findings are
> grouped by **severity for an end user trying to actually run the system**, not by sheet.
>
> **Note on intent.** Some Tier-1 blanks (weights, min/max, raw values) are *intentional*
> — the workbook is a blank master template. They are listed anyway because, intentional or
> not, they are what stops a company from producing a single score, and the fixes are about
> *enabling* the blanks to be filled (defaults, sourcing guidance), not pre-filling them.

## Healthy baseline (no action needed)

- **Metrics List is fully in sync** with the domain sheets: 148/148 raw metrics mirrored,
  **zero field drift** across Indicator Name / Description / Unit / Reference / Source /
  Product Life Cycle Stages. The sync tooling works.
- Environmental, Resource Efficiency, and Social Impact domains have **no orphan rows** —
  every row is reachable from the domain root.

---

## Tier 1 — Hard blockers: the system computes nothing out of the box

These are why a company cannot "run" the system even after supplying all measured data.

### T1.1 — No weights anywhere (0 of 266 rows) — ✅ RESOLVED 2026-06-25
Every `WEIGHTED_AVERAGE_STRATEGY` score (incl. all five domain roots and the top-level
Sustainability composite) requires child weights to produce a value. None were set and there
were no defaults; the "children under one parent sum to 1" rule (USER_MANUAL §A.5) was stated
but unenforced.

> **Fix.** Equal-weight defaults were seeded (`seed_default_weights.py`; 117 child cells, each
> parent's children sum to 1.0). The rule is now **enforced** by the engine's `validate`: a
> `weight_sum` issue fires when an aggregate parent's child weights ≠ 1.0 (±1e-6), and a
> `weight_missing` issue fires when a child of a weighted parent has no weight (it would
> silently default to 1.0 and distort the average). DAG-shared standalones (`EN9`, whose impact
> children are weighted by `EN0`) are exempt from the sum check. The seeded master passes both
> checks. (`validate.py`, `tests/test_validate.py`.)

### T1.2 — `NORMALIZED_RATIO` rows need Min/Max — ✅ RESOLVED 2026-06-25 (defaults + sourcing guide)
Every normalised score depends on Target Min/Max. The **Potential Reference Values** column
held only *labels* (e.g. "Target Value: Min, Max"), never numbers, and the workbook gave **no
guidance on where to obtain the benchmarks** — the deepest usability gap. (Now 81 normalized
rows after the round 2–6 re-tags, up from the original 67.)

> **Fix (`apply_review_round7.py` + `reviews/min-max-sourcing.md`).** Split the 81 rows:
> - **35 bounded-ratio rows** (a share `x/total`, or a complement `1 − bad/total`, higher =
>   better) were **seeded `Min=0, Max=1`** — the identity default, since the ratio already *is*
>   a 0–1 score. Verified: all 35 compute out of the box on example inputs.
> - **46 benchmark rows** (LCIA/PEF factors, intensities, financial ratios, rating scales,
>   company targets, prior-period) stay blank — there is no safe universal default — and are
>   each documented in **`reviews/min-max-sourcing.md`**: what Min/Max mean and **where the
>   number comes from**, grouped by source category. The classification lives in
>   `apply_review_round7.py` (`SEED_01` / `BENCHMARK`) so the seeder and guide cannot drift.
>
> The engine still reports `Target Min/Max not set` for any benchmark row a company hasn't
> filled (it never fabricates a benchmark).

### T1.3 — No calculation engine — ✅ RESOLVED (engine in `tools/kpi-engine/`)
The aggregation was originally out of scope. **A calculation engine now exists** under
`tools/kpi-engine/` and implements all three pieces the spec described: bottom-up rollup with
memoization/cycle-protection (`engine.evaluate_all` / `_aggregate`), min-max **normalization**
(`_normalized` / `strategies.normalize`), and **missing-data reweighting** (absent children are
dropped and present weights renormalized, `weighted_average`). It also adds `SUM_AGGREGATE`,
`FORMULA_VALUE`, encoded ratio formulas, an out-of-range hard error (T3.6) and structural
`validate`. CLI: `kpi-engine compute|validate "data/KPI List.xlsx"`. 26 tests, mypy strict.

> **Loader robustness (2026-06-25).** The loader previously read the workbook `read_only`, which
> trusts the stored worksheet `<dimension>`; the surgical editor (`xlsx_edit.py`) appends the
> input-block columns without rewriting that dimension, so `read_only` silently dropped the
> seeded Target Min/Max. Switched the loader to normal mode (negligible cost at 266 rows) so the
> engine reliably reads workbooks its own tooling produces. (`loader.py`.)

**Net effect of Tier 1:** the system now computes scores out of the box — weights are seeded and
enforced, 35 normalized rows carry working defaults, the remaining 46 have explicit sourcing
guidance, and an engine turns inputs into scores.

---

## Tier 2 — Wiring defects: parts compute wrong or silently drop out

### T2.1 — 8 rows orphaned from their domain root (never roll up) — ✅ RESOLVED 2026-06-23
Each names its parent, but the parent's **Underlying Metrics** never lists the child back,
so the row is disconnected from aggregation:

| Domain | Orphaned IDs | Branch |
|---|---|---|
| Economic Viability | `EC5`, `EC5-1` | CO2 Cost Performance (EC0 does not list EC5) |
| Economic Viability | `EC46`, `EC4-24`, `EC47` | Remanufacturing/Circular-Material Viability (EC4 lists neither EC46 nor EC47) |
| Circular Efforts | `C233`, `C2-14` | Remanufacture Success Rate (C23 lists only C231, C232) |
| Circular Efforts | `C5-5` | Discarded component weight (C5 does not list C5-5) |

A company would fill these in and they would contribute nothing to any score.

> **Fix:** added each orphan to its parent's Underlying Metrics (`EC0 += EC5`, `EC4 += EC46,
> EC47`, `C23 += C233`, `C5 += C5-5`), completing the back-link so the sub-orphans (`EC5-1`,
> `EC4-24`, `C2-14`) become reachable transitively. Weights re-seeded. Engine `validate` now
> reports 0 orphans. (`tools/scripts/fix_tier2_wiring.py`)

### T2.2 — 2 formulas reference IDs that do not exist — ✅ RESOLVED 2026-06-23
- **`R2`** (Energy Efficiency Score) aggregated `R21, R22, R23` — **`R23` did not exist.**
- **`EN3-2`** and **`EN3-3`** both declared parent **`EN33`** — which did not exist. Their
  real parent is **`EN32`** (which lists them).

> **Fix:** dropped the dangling `R23` from `R2`'s Underlying Metrics (R2 now aggregates the
> two metrics that exist, R21 + R22, and re-sums to 1.0); corrected `EN3-2`/`EN3-3` parent
> `EN33 → EN32`. Engine `validate` now reports 0 dangling references.

### T2.3 — asymmetric parent/child links — ✅ RESOLVED 2026-06-24
The tree built from **Underlying Metrics** disagreed with the tree built from **Parent
Metrics** (53 cases at audit; 38 after the Tier-2/re-model work).

> **Fix:** since the engine drives aggregation from **Underlying Metrics**, Parent Metrics is
> now treated as a generated mirror — regenerated as the exact **global inverse of Underlying
> Metrics** (across domains, so cross-domain parents like `EN1-4 → EC5` are preserved). 33
> rows updated; asymmetry is now **0** by construction. (`tools/scripts/apply_review_round3.py`)
> Maintainers editing in Excel should still keep both columns consistent, or re-run the
> regeneration.

### T2.4 — 3 cross-domain edges — ✅ ACCEPTED AS INTENTIONAL 2026-06-23
`EN1-4 ↔ EC5`, `EN41 ↔ R2-7`, `EC5 ↔ R2-7`. Economic's CO2 Cost Performance draws on the
product carbon footprint (`EN1-4`) and produced units (`R2-7`); water-footprint intensity
(`EN41`) draws on produced units. These are **semantically correct reuse**, not defects.

> **Decision:** the system is a **directed acyclic graph, not five independent trees** —
> domains cover different aspects but legitimately share KPIs. The edges are kept; the
> engine resolves them via a global id map. (Earlier framing of this as a "broken model" is
> withdrawn.) Consequence to remember: a shared leaf contributes to more than one domain
> score, and company-subset pruning must follow edges across domains
> (`tools/scripts/build_company_kpi.py` already merges both link directions).

### T2.5 — rows simultaneously "raw input" and "aggregate" — ✅ RESOLVED 2026-06-24
**`EN1-4`** (Absolute PCF), **`EN4-4`** (Absolute Water Footprint) and **`EC1-5`** (Material
Costs) were tagged `Data?=x` *and* carried children — contradictory (supply the total, or
compute it?) and a double-counting trap.

> **Fix:** made them computed totals — `EN1-4`/`EN4-4` re-tagged `RAW_VALUE → SUM_AGGREGATE`
> (= sum of their scopes / water-types); `EC1-5` was already SUM. The `Data?=x` input flag was
> cleared on all three (the children are the supplied inputs). Verified: `EN1-4 = 54+61+68 =
> 183`. (`tools/scripts/apply_review_round3.py`)
>
> **Follow-up 2026-06-25:** clearing `Data?=x` left the three rows *stranded* in the Metrics List
> — the sync tool mirrors values but cannot delete rows, so they lingered as computed totals
> masquerading as raw inputs. They were removed from the Metrics List (149 → 146 rows) by a
> zip/XML row-delete that preserves the sheet's table, threaded comments and VML drawing
> (`tools/scripts/delete_metrics_list_rows.py`); the comments below shifted up in lockstep and
> the domain sheets were byte-copied untouched. The sync report now shows 0 orphans.

---

## Tier 3 — Data-integrity gaps that mislead users

### T3.1 — "Raw data = Level 5" is false in the data — ✅ RESOLVED 2026-06-25
74 of 148 `Data?=x` rows were **not** Level 5 (they sat at Level 3/4) and 6 had a blank Level
(`R2-4, R2-5, R2-6, S3-5, S3-6, S3-7`). Because the snapshot cannot capture fill colour, Level
is the only machine-readable hierarchy signal, so this conflicted with USER_MANUAL §A.2.

> **Fix.** Every `Data?=x` row was set to **Level 5** (`apply_review_round8.py`; 74 rows), so
> the data now matches the manual's rule. Verified: 0 `Data?=x` rows off Level 5. The new
> levels were mirrored into the Metrics List via `sync_metrics_list.py`.

### T3.2 — citation codes do not resolve to the References sheet — ✅ RESOLVED 2026-06-25
The manual's "look the code up in the References **Label** column" flow dead-ended for many
codes (49 distinct once sub-clauses are counted, not the 22 first sampled).

> **Fix (`apply_review_round8.py`).** Added a References row for each of the **45** codes that
> map to a standard / paper already in `data/literature/` (GRI, ESRS, SASB, ISO 14021,
> EN 15804+A2 Module D, Cradle to Cradle, `MM+17`, `TF+25`), with the `Label` = the exact code,
> a proper Title/Description and the **public URL** for each source (`apply_review_round9.py`
> reformatted these to match the sheet's existing entries — no local paths). Unresolved now:
> **4**, which have **no local
> source** — `MCI+15`, `MCI+16` (Ellen MacArthur MCI — the missing PDF also behind `C4`'s
> `needs_review`), `WBCSD`, and `waterfootprintnetwork` (a website). These are reported, not
> invented; add the sources to `data/literature/` to close them.

### T3.3 — A raw input with no unit — ✅ RESOLVED 2026-06-25
`R2-4` (Stored energy derived from outflow) had no Unit and no Level.

> **Fix.** Unit set to **kWh** (matching the other energy KPIs) and Level set to 5 (T3.1).
> (`apply_review_round8.py`.)

### T3.4 — ~~One normalised row with no reference values~~ — ✅ WITHDRAWN (stale) 2026-06-25
The finding named `EN44` (Lifecycle Water Footprint Ratio) as a `NORMALIZED_RATIO` row with no
reference values. `EN44` was re-tagged **`WEIGHTED_AVERAGE`** during the literature round (it
aggregates already-normalized child scores), so it no longer needs reference values. No action
required.

### T3.5 — Strategy mistags (surfaced by the engine) — ⚙️ PARTIALLY RESOLVED 2026-06-23
Rows whose declared strategy combines raw-unit leaves wrongly. Three groups:

- **Cost/total roll-ups — ✅ FIXED:** `EC121` (COGS), `EC1-5`, `EC411`, `EC421`, `EC431`,
  `EC441`, `EC451`, `EC461` were `WEIGHTED_AVERAGE` (a total came out as a *mean*) though
  their formula text is literally a sum. Introduced a **`SUM_AGGREGATE_STRATEGY`** (engine +
  workbook) and re-tagged them. Verified: e.g. `EC411` Repair Costs = 78+85+32+39 = **234**
  (was the mean), and the downstream `Profits/Costs` ratios now use the real total.
- **Clear single re-tags — ✅ FIXED:** `EN14`/`EN44` (`NORMALIZED_RATIO` → `WEIGHTED_AVERAGE`;
  their children are already normalized % scores) and `EN32` "Hazardous Material Share"
  (`WEIGHTED_RATIO` → `NORMALIZED_RATIO`, formula `1 − hazardous/total` encoded). Verified:
  `EN32` = 1 − 46/53 = **0.132** (was 49.5).
- **Impact/index scores needing real normalisation — ⏳ DEFERRED to the formula review:**
  `EN6`, `EN7`, `EN8`, `EN9`, `C4`, `C5`, `S34`. These average raw quantities in *mixed
  units* (kg CFC-11, CTUh, €, …); each needs designed per-row normalisation, and several
  need the literature (EN9 = PEF single score, C4 = MCI-style index). Folded into the
  `needs_review` formula-encoding pass.
- **`C34` Ease of Disassembly — ✅ RESOLVED 2026-06-24 (round 4).** *(An earlier draft of this
  note wrongly said "C34 is fine — its children are already %." It was not.)* `C34`
  weight-averaged two raw-unit leaves — `C3-5` Instructions Availability (raw %) and `C3-6`
  Disassembly Time (raw **minutes**) — so it returned **69.5**, dragging `C3` to **17.385** and
  the Circular Efforts root `C0` to **3.533**, far outside [0,1]. Fixed exactly like the S34
  re-model: `C3-5`/`C3-6` re-tagged `RAW_VALUE → NORMALIZED_RATIO`, each self-normalizing
  against company Target Min/Max (engine formulas `C3-5`/`C3-6` = `_self()`); `C34` now
  weight-averages two 0–1 scores. Min/Max stay company-supplied (for `C3-6` lower time is
  better → set Max = worst-acceptable time). Verified on the example: `C34` 69.5 → **0.695**,
  `C3` → **0.184**, `C0` → **0.093** (in range; `C0`'s remaining `(unverified)` flag now comes
  solely from `C4`'s MCI index). 19 engine tests pass. (`tools/scripts/apply_review_round4.py`)

Applied via `tools/scripts/fix_strategy_mistags.py` (surgical; comments preserved), weights
re-seeded. The engine computes faithfully per declared strategy, so it exposes such issues
rather than hiding them.

### T3.6 — more out-of-range aggregates: Economic + Resource roots — ✅ RESOLVED 2026-06-25
Computing the workbook with a full set of inputs shows **14 score-type nodes (WEIGHTED_AVERAGE
/ WEIGHTED_RATIO / NORMALIZED_RATIO) landing outside [0,1]** — i.e. the same mistag class as
T3.5/C34, but in branches the earlier pass did not touch. The engine did **not** flag these
`(unverified)`, so they failed silently: with example inputs the **Economic Viability root `EC0`
≈ 74** and the **Resource Efficiency root `R0` ≈ 11**, instead of a 0–1 score. Root causes (the
other nodes are pure propagation):

**Economic Viability — monetary subtree.** T3.5 fixed the leaf cost roll-ups (`EC121` COGS,
`EC4xx`) to `SUM_AGGREGATE` but left their parents as `WEIGHTED_AVERAGE`, so € totals get
*averaged*:

| Row | Strategy now | Should be | Reason |
|---|---|---|---|
| `EC111` Lifecycle Mgmt Costs | WEIGHTED_AVERAGE | `SUM_AGGREGATE` | € total of cost lines |
| `EC112` EOL Costs | WEIGHTED_AVERAGE | `SUM_AGGREGATE` | € total of cost lines |
| `EC11` Total Investment Cost | WEIGHTED_AVERAGE | `SUM_AGGREGATE` | € total (incl. EC111/EC112) |
| `EC12` Net Profit | WEIGHTED_AVERAGE | **difference** (Revenue − costs) | not a mean of euros; SUM only adds, so needs a formula or a small engine addition |
| `EC1` ROI | WEIGHTED_AVERAGE | `NORMALIZED_RATIO` | = Net Profit ÷ Investment Cost |
| `EC2` Gross Margin | WEIGHTED_AVERAGE | `NORMALIZED_RATIO` | = (Revenue − COGS) ÷ Revenue |

**Resource Efficiency — `WEIGHTED_RATIO` does not divide.** The engine implements
`weighted_ratio = weighted_average` (`strategies.py`), so rows whose own formula text is a
division silently *average* their two raw inputs:

| Row | Formula text | Strategy now | Should be |
|---|---|---|---|
| `R121` Product Waste Share | `R1-4 / R1-6` | WEIGHTED_RATIO (→ avg) | `NORMALIZED_RATIO` (real ratio) |
| `R221` End User Energy Efficiency | `R2-5 / R2-6` | WEIGHTED_RATIO (→ avg) | `NORMALIZED_RATIO` (output/input) |

(`R12` then mixes the broken `R121` with a raw mass `R1-5`; `EC0/EC1`, `R0/R1/R2/R22` are
propagation.) Fix is the same medicine as C34 (re-tag + encode the division/ratio in
`formulas.py`, leave Min/Max company-supplied) plus a `SUM_AGGREGATE`/difference decision for
the four monetary rows.

> **Fix (`tools/scripts/apply_review_round5.py`).** Re-tagged **nine** rows (the audit's eight
> + `R12`, see below) and encoded their formulas in the engine:
>
> | Row | Was | Now | Engine handling |
> |---|---|---|---|
> | `EC111`, `EC112`, `EC11` | WEIGHTED_AVERAGE | `SUM_AGGREGATE` | € totals summed, not averaged |
> | `EC12` Net Profit | WEIGHTED_AVERAGE | **`FORMULA_VALUE`** (new) | `Revenue − (COGS+Operating+Lifecycle+EOL)` — a raw € difference |
> | `EC1` ROI | WEIGHTED_AVERAGE | NORMALIZED_RATIO | `EC12 / EC11`, normalized vs company Min/Max |
> | `EC2` Gross Margin | WEIGHTED_AVERAGE | NORMALIZED_RATIO | `(EC1-4 − EC121) / EC1-4` |
> | `R12` End-of-Life Waste | WEIGHTED_AVERAGE | NORMALIZED_RATIO | `(R1-4 − R1-6) / R1-4` — see round-6 note |
> | `R121` Product Waste Share | WEIGHTED_RATIO | *(archived — folded into `R12`)* | round 6 |
> | `R221` End User Energy Eff. | WEIGHTED_RATIO | NORMALIZED_RATIO | `R2-5 / R2-6` |
>
> **New strategy `FORMULA_VALUE_STRATEGY`** (mirrors how `SUM_AGGREGATE` was introduced in
> T3.5): a raw value computed from an encoded formula over children (e.g. a difference); not
> normalized and **not** range-checked, since it legitimately falls outside [0,1] and feeds a
> downstream ratio (`EC12` → `EC1`).
>
> **The 9th mistag (`R12`) was surfaced by the new hard error, not the structural audit.** The
> audit assumed `R12` was pure propagation; in fact it weight-averaged a 0–1 share (`R121`)
> with a raw kg mass (`R1-5`) → ~27. Round 5 first re-tagged it NORMALIZED_RATIO over the
> declared division `R121 / R1-5` but had to flag it `needs_review` (kg vs share mismatch).
>
> **Round 6 (2026-06-25, user decision) — `R12` simplified, `R121`/`R1-5` archived.** `R121`
> (`(Mass − Cyclable)/Mass`) already **is** the end-of-life-waste figure; the comparison to a
> reference product (`R1-5`) added the dimensional mismatch for no real benefit — the
> NORMALIZED Target Min/Max band already encodes the reference level. So `R121`'s computation
> was folded up into `R12` (now `(R1-4 − R1-6)/R1-4` over the two raw leaves directly), and
> `R121` + `R1-5` were **archived** (unwired, reversible; `R1-5` stays a recordable `Data?=x`
> figure that now feeds nothing). This removed the `needs_review`/`(unverified)` flag — `R12`,
> `R1` and `R0` now compute cleanly in range. (`tools/scripts/apply_review_round6.py`.)
>
> **Design decision — out-of-range is now a hard error.** Per the open question below, the
> engine treats any `WEIGHTED_AVERAGE` / `WEIGHTED_RATIO` result outside `[0,1]` (±1e-9) as a
> `Status.ERROR` (`engine.py`, `_aggregate`), with a message naming the likely mis-tag. This
> is what caught `R12`. `SUM_AGGREGATE` / `FORMULA_VALUE` (raw €) and `NORMALIZED_RATIO` (always
> clamped) are exempt by construction. Verified end-to-end on a current-structure example
> workbook: all five roots land in `[0,1]` (`EN0` 0.354, `EC0` 0.202 *(was ≈74)*, `C0` 0.093
> *(unverified, from C4's MCI index)*, `R0` 0.005 *(was ≈11; no longer unverified)*, `S0`
> 0.059), **zero** out-of-range errors remain, and a structural sweep confirms no other
> score-aggregate has a non-score child. 22 engine tests pass, mypy clean. (`formulas.py`,
> `engine.py`, `model.py`; re-tags via `apply_review_round5.py` + `apply_review_round6.py`.)

> **Open design question — resolved.** *Should the engine treat any aggregate that resolves > 1
> as a hard validation error so this class can't reappear silently?* **Yes — implemented** (see
> the design decision above). A mis-tagged aggregate now fails loudly instead of emitting a
> plausible-looking bad score.

---

## Literature review (2026-06-23)

Five bounded `kpi-literature-crosschecker` runs grounded the `needs_review` formulas and the
deferred Group-3 impact scores against `data/literature/` (page-cited reports in this folder:
`EN1-carbon-phases.md`, `EN4-water-phases.md`, `EN-impact-pef.md`, `C-circular-indices.md`,
`S-social-economic.md`).

**✅ Applied (grounded, low-risk):**
- **C231** → formula `C2-13 / C2-11` (remanufactured / total inflow), `needs_review` cleared
  — DIN SPEC 91472 p.24–25.
- **C5** → re-tagged NORMALIZED_RATIO, formula `(C5-1+C5-2+C5-3+C5-4) / C1-5` — ISO 59020 §A.3.3.
- **C4** → re-tagged NORMALIZED_RATIO, formula `1 − (C4-1+C4-2)/(2·C4-3)` (was dimensionally
  invalid); kept `needs_review` — the MCI source PDF is missing from the corpus.
- **Reference cleanup:** added missing standard Labels (ISO 14044, ISO 14046, ISO 59020,
  PSILCA, ESRS S1); fixed mis-cites `EN4 ESRS E2-4→E3-4`, `S3-6 GRI 202-1→GRI 201-1`,
  `EN7-2/3 USEtox2.1/2.2→USEtox2.0`, dropped redundant orphan `WBCSD` on EN1.

**✅ Re-models resolved (round 2, 2026-06-24) — `tools/scripts/apply_review_round2.py`:**
- **Carbon phases EN131–135 + EN14** and **water phases EN441–445 + EN44**: **ARCHIVED** —
  unwired from EN1/EN4 (which still score from their benchmark ratios) and marked optional in
  their Comment. They conflated org/type with life-cycle-stage axes and needed bespoke
  per-stage LCA data; rows remain (reversible) but are dormant. Engine `validate` treats
  ARCHIVED rows as intentional, not orphans.
- **PEF impacts EN6/EN7/EN8 + leaves**: each impact leaf (EN6-1..8, EN7-1..3, EN8-1..3) is now
  **self-normalizing** (NORMALIZED_RATIO over its own characterised result ÷ EF normalisation
  factor as Target Max); EN6/EN7/EN8 weight-average them. **EN9** is now a genuine PEF single
  score over EN1/EN5/EN6/EN7/EN8, **unwired from EN0** (standalone reference — resolves the
  T2.3 double-count). The EF normalisation/weighting factor *values* are not in the PEF PDF
  (Rec. (EU) 2021/2279 delegates them to the JRC EF reference package); they stay company-
  supplied with an in-workbook guidance note (see `reviews/PEF-factors.md`). Unit notes:
  EN5-2 land use uses the EF "pt" indicator (not m²a/FU); EN8-1 water should be AWARE-weighted.
- **Social S34**: children S3-5/S3-6/S3-7 now self-normalize against company targets; S34
  weight-averages the 0–1 scores.

Verified: with example inputs the Environmental, Circular and Social roots land in 0–1
(EN0≈0.35, EN6/7/8 in range, EN9 a PEF single score, C0≈0.06, S0/S34 in range); engine 19
tests pass, mypy clean. The Economic Viability and Resource Efficiency roots were **not** yet
in range at that point (EC0≈74, R0≈11) — ✅ **now resolved** by the round-5 re-tags (nine rows
incl. `R12`) and the out-of-range hard error; see **T3.6** above. All five roots land in 0–1;
22 engine tests pass.

## Summary counts

| Finding | Count |
|---|---|
| Rows with a weight set | ✅ seeded + sum-to-1 enforced in `validate` (T1.1) |
| `NORMALIZED_RATIO` rows needing Min/Max | ✅ 35 seeded 0/1 + 46 with sourcing guide (of 81; T1.2) |
| Calculation engine | ✅ `tools/kpi-engine/` (rollup + normalize + reweight; T1.3) |
| Orphan rows (unreachable from domain root) | ✅ 0 (was 8, T2.1) |
| Formulas citing non-existent IDs | ✅ 0 (was 2: R23, EN33, T2.2) |
| Asymmetric parent/child links | ✅ 0 (was 53; Parent Metrics regenerated, T2.3) |
| Cross-domain edges | 3 (intentional — kept, T2.4) |
| Raw rows also tagged as aggregates | ✅ 0 (was 2→3; now computed SUMs, T2.5) |
| `C34` Ease of Disassembly out of range | ✅ fixed (round 4, T3.5) |
| Score-type aggregates computing outside [0,1] | ✅ 0 (was 14 nodes / 9 root mistags incl. R12; T3.6) |
| `Data?=x` rows not at Level 5 | ✅ 0 (was 74 + 6 blank; T3.1) |
| Citation codes unresolved against References | ✅ 4 (was 49; 45 linked to literature, T3.2 — 4 have no local source) |
| Raw rows with no unit | ✅ 0 (R2-4 → kWh, T3.3) |
| Metrics List drift | 0 ✅ |

---

*Audit produced by automated structural checks over `snapshot/*.tsv`. Re-run after any
workbook change to confirm fixes.*
