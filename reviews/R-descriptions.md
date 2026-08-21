# R description audit — refine + ground KPI descriptions

**Scope:** the full **Resource Efficiency (R) domain — all 45 KPIs** (2 archived: R1-5, R121),
audited family by family (R1 Material, R2 Energy aggregates + raw leaves, R3 Water, R0 root).
Goal: reconcile each handmade description with its *current* implementation (Strategy, Formula,
relations after the gap-fix re-model) and ground it in the cited literature where a source applies.
**Date:** 2026-06-29.
**Method:** current state from `snapshot/Resource Efficiency.tsv` (+ `References.tsv`); every
literature claim is a verbatim page-cited quote via `tools/scripts/pdf_search.py`; conservative
stance — adaptations kept faithful + flagged, not rewritten to match a source.
**Verdict legend:** CONSISTENT / DRIFTED / ADAPTED / UNVERIFIABLE (see EN/EC/C reports).
Columns on the sheet: C=Description, G=Potential Reference Values, H=Unit, I=Formula,
J=Reference, R=Comment.

---

## R domain — consolidated summary & decisions

**Verdicts across all 45 R KPIs:** CONSISTENT 23 · DRIFTED 8 · ADAPTED 8 · UNVERIFIABLE 6.
The R12 recoverability flip and the R121/R1-5 archival are verified correctly applied. The
defects are the familiar stale-text pattern, a couple of citation problems, and — uniquely for
this domain — a genuine **direction bug in the engine** (R32). Nothing applied yet — all proposals.

### A. Description rewrites — DRIFTED rows (8)

| KPI | Problem | Proposed |
|---|---|---|
| R0 | stale Formula `…+R5` (children are R1/R2/R3) | name R1/R2/R3; fix formula |
| R2 | Formula still names the removed `R23` (children are R21/R22) | drop R23 from formula text |
| R3 | wording doesn't name its sub-scores | rewrite to R31/R32/R33 |
| R32 ⚠️ | desc + formula compute `Current/Previous` → **rewards higher consumption** (backwards) | rewrite to a reduction (higher = less water) — **see decision D1** |
| R213 | desc is numerator-only, not the stored/generated share | rewrite to the share |
| R221 | desc still says "consumption when used", not the output/input efficiency ratio | rewrite to R2-5/R2-6 efficiency |
| R2-10 | desc copy-pasted from R2-9; omits the "(Previous)/baseline" qualifier | add the baseline qualifier |
| R3-3 | (citation defect — see §C) | citation only |

### B. Adjacent-cell drift — Formula text (apply with the rewrites)

Stale root/aggregate formula text: `R0` (`…+R5` → R1+R2+R3), `R2` (drop `R23`). Minor: R11
Formula trailing space; blank Objective/Goal on R213/R221/R222/R223; "costumer" typo on R221.

### C. Citation issues

- **R32 / R311 / R3-1 / R3-2 / R11 / R212 — SOURCE-NOT-FOUND papers** → **decision D2**:
  `AM+22` (R311/R32/R3-1/R3-2) and `ACM+17` (R11/R212) resolve to Labels but have **no PDF**
  in `data/literature/Papers/`. ISO 59020 / EN15804 / ESRS ground the affected rows instead.
- **Clear citation corrections (recommend applying):** `R3-3` `GRI 306-4` (waste) → `ESRS E3-4`
  (water recycled/reused); `R3-4` `SASB RT-CP-140a.1` (qualitative risk) → `RT-CP-130a.1`
  (quantitative water); `R21` `SASB RT-CP-120a.1` (air) → `RT-CP-130a.1`; `R224` loose cites →
  `GRI 302-4` (reduction of energy consumption, already present).

### D. Decisions — RESOLVED 2026-06-29

1. **R32 direction → NO engine flip; description clarification only. ✗→✓ (corrected 2026-06-29).**
   The original "flip it" call was based on a false-positive blocker: the R30 batch read the
   workbook snapshot and assumed an ascending band, missing that the engine encodes
   `R32 = current/previous` with **`lower_is_better=True`** (`formulas.py:185`). The engine's
   `normalize()` has no direction inversion (`strategies.py:18`); direction is carried by the
   `lower_is_better` flag + an **inverted Target Min/Max band (Min > Max)**, enforced by the
   `band_direction` guard in `validate.py`. This is the same valid pattern as R224/R223 — R32 is
   **correct as-is**, and `1 − current/previous` would break it (it would contradict the flag and
   trip the guard). **Action:** keep `formulas.py` unchanged; rewrite only the R32 *description*
   to convey "reduction in water consumption vs a previous period; a lower current/previous ratio
   scores higher (lower-is-better → set an inverted Min/Max band)." Do **not** seed 0/1 (an
   ascending band would be wrong here); leave the band company-supplied with that guidance.
2. **SOURCE-NOT-FOUND papers (`AM+22`, `ACM+17`) → drop & re-ground. ✓** Remove from the
   Reference cells; cite the corpus-present ISO 59020 / EN15804 / ESRS that ground those rows
   (consistent with the C-domain decision).

### E. ADAPTED Comment flags (non-obvious only)

R11 (org→product reuse-share adaptation), R221 (output/input band not seeded 0/1 — company-set),
R311/R312/R3-4/R3-5 (org→product water adaptations), R2-7 (cross-domain: also feeds EC5/EN41) —
keep the description, add a short Comment-cell note where the adaptation isn't self-evident; skip
obvious ones, matching the EN/EC/C policy.

### R1 — Material Efficiency Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the efficiency of material utilization based on underlying metrics."
- **Verdict:** CONSISTENT (composite parent; internal check) — the prose correctly states
  a roll-up "based on underlying metrics," matching `Underlying = R11\nR12` and
  `Formula = Sum (weight * R11 + weight * R12)`. Both children exist (rows 4, 7).
- **Grounding:** composite/parent — no single literature source expected (Reference cell
  blank by design). The two arms are grounded on the children's rows (ISO 59020 A.3.3 for
  R11 reutilization; ISO 59020 p.42 circular-vs-linear outflow + C2C cycling for R12).
- **Implementation check:** `Underlying = R11\nR12`; Parent = R0; strategy
  WEIGHTED_AVERAGE; Unit %. Children both 0–1/% sub-scores, so averaging to % is
  dimensionally sound. Description is generic ("based on underlying metrics") but not
  wrong; it just does not name the two arms (reutilization + recoverability).
- **Proposed revision (C):** "Aggregates the product's material-efficiency performance into
  one score by combining how much of the resource outflow is reutilized as material of
  value (R11) and how much of the product's mass is recoverable at end of life (R12).
  Higher means more material is kept in use and less becomes waste."
- **Notes:**
  - [minor] Formula text (I) reads `Sum (weight * R1 + … + weight * R5)` on the **R0** row
    above, but on **R1** itself the Formula already correctly reads
    `Sum (weight * R11 + weight * R12)` — no fix needed on R1's I cell. (The stale `…+R5`
    ellipsis is on R0, outside this batch; flag it there.)
  - Blank Reference (J) is correct for a composite parent — not a defect.

### R11 — Reutilized Material Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the reutilization of the resource outflow that can be cycled as material of value within or outside the production process."
- **Verdict:** CONSISTENT — text matches `Sum (weight * R111 + weight * R112)` over the
  reused-within (R111) and repurposed-outside (R112) arms; "within or outside the production
  process" maps cleanly onto the two children.
- **Grounding:**
  - ISO 59020 p.45 (A.3.3): "where P REUO(X) is the actual reused products and components
    derived from outflow (X), in %; m REUO(X) is the mass of outflow (X) that is reused …
    m TO(X) is the total mass of outflow (X)". (`data/literature/ISO 59XXX/ISO-59020.pdf`)
    — grounds the reused-mass / total-outflow-mass ratio the children compute.
  - ISO 59020 p.42 (Annex A): "The following three core circularity indicators are intended
    to represent … the circular outflows: — components and products that are reused (see
    A.3.3); — per cent recycled material derived from outflow (see A.3.4), — products and
    materials for renewable recirculation (see A.3.5)." (`…/ISO-59020.pdf`)
  - C2C p.36 (5.3 / 5.4): "Select product and material types contain cycled and/or renewable
    content"; "≥ 50% of materials by weight are compatible with the intended cycling
    pathway(s)". (`data/literature/Cradle To Cradle/c2c-certified-full-scope_v4.1_final_011525.pdf`)
- **Implementation check:** `Underlying = R111\nR112`; Parent = R1; strategy
  WEIGHTED_AVERAGE (each 0.5); Unit %. Children exist (rows 5, 6) and both compute a
  mass-over-outflow ratio — consistent with the ISO 59020 A.3.3 framing. No description
  drift.
- **Proposed revision (C):** keep as-is. (Optional, to name the arms: "Measures how much of
  the production's resource outflow is reutilized as material of value — reused back into
  the same lifecycle (R111) or repurposed into an external product/system (R112).")
- **Notes:**
  - [major] **Reference (J) cites `ACM+17`, which is SOURCE-NOT-FOUND** — no `ACM+17*`
    file exists in `data/literature/Papers/` (verified by directory listing). The Label
    resolves in References.tsv (line 39, "Product Circularity Assessment Methodology") but
    the PDF is absent, so the citation is currently unverifiable. Recommend either adding
    the PDF or dropping `ACM+17` and leaning on `ISO 59020` (A.3.3), which is present and is
    the tightest ground.
  - [minor] **`C2C` code ambiguity:** J cites bare `C2C`; References carries generic `C2C`
    (line 19) plus `C2C 5.2`/`C2C 5.3` (lines 58–59). Pin the canonical Label.
  - [minor] Formula text (I) has a **stray trailing space**: `Sum (weight * R111 + weight *
    R112 )` — drop the space before `)`.
  - Comment-cell flag (R) not needed — the reutilization concept maps obviously onto the
    cited ISO 59020 indicator; adaptation is self-evident.

### R111 — Reused Byproduct Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the percentage of byproduct which is reused back into the product's lifecycle."
- **Verdict:** CONSISTENT — text matches
  `Reused = Recirculated mass derived from outflow / Total mass of outflow`, then
  `(Reused - Min)/(Max - Min)`, over R1-2 (recirculated byproduct) and R1-1 (total outflow).
- **Grounding:**
  - ISO 59020 p.45 (A.3.3): "m REUO(X) is the mass of outflow (X) that is reused, in kg or
    other mass unit; m TO(X) is the total mass of outflow (X)". (`…/ISO-59020.pdf`) —
    grounds exactly the reused-mass ÷ total-outflow-mass ratio.
  - GRI 306-4 p.13: "Total weight of waste diverted from disposal in metric tons … a. Total
    weight of hazardous waste diverted from disposal … by the following recovery operations:
    Preparation for reuse; i. Recycling; ii. Other recovery operations." (`data/literature/GRI - Global Reporting Initiative/GRI 306_ Waste 2020.pdf`)
    — grounds the "reused/diverted byproduct" numerator concept (the R1-2 input).
- **Implementation check:** `Underlying = R1-1\nR1-2`; Parent = R11; strategy
  NORMALIZED_RATIO; Unit %; Min/Max seeded 0/1 (Comment documents this). R1-2 (recirculated
  byproduct, kg) ÷ R1-1 (total byproduct of outflow, kg) is a well-formed 0–1 share; both
  leaves exist (rows 9, 10) and share unit kg. No drift. ("reused back into the product's
  lifecycle" = R1-2's definition "reused or reutilized in the same process cycle" — exact
  match.)
- **Proposed revision (C):** keep as-is. (Optional sharpening: "Measures the share of the
  production's total byproduct outflow (R1-1) that is recirculated and reused back into the
  same product lifecycle (R1-2). Higher means less byproduct leaves the loop.")
- **Notes:**
  - [minor] **Reference (J) is blank** though the ratio is groundable. Add `ISO 59020`
    (A.3.3) — it is the tightest match and is present in the corpus. (`GRI 306-4` already
    sits on the R1-2 input leaf.)
  - G cell "Target Value: min, max" matches the Min=0/Max=1 seed pattern — consistent.

### R112 — Repurposed Byproduct Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share repurposed byproduct from the outflow of the current product's lifecycle to another external product or system."
- **Verdict:** CONSISTENT — text matches
  `Repurposed = Repurposed mass derived from outflow / Total mass of outflow`, then
  normalized, over R1-3 (repurposed byproduct) and R1-1 (total outflow). "to another
  external product or system" = R1-3's definition "reused outside of the product's process
  cycle" — exact match.
- **Grounding:**
  - ISO 59020 p.45 (A.3.3): "m REUO(X) is the mass of outflow (X) that is reused … m TO(X)
    is the total mass of outflow (X)". (`…/ISO-59020.pdf`) — the same reused-over-outflow
    ratio; "repurposed externally" is a faithful narrowing of A.3.3's "reuse … of other"
    products/components.
  - GRI 306-4 p.13: "recovery operations: Preparation for reuse; … Other recovery
    operations." (`…/GRI 306_ Waste 2020.pdf`) — grounds the externally-recovered byproduct
    (R1-3) numerator.
- **Implementation check:** `Underlying = R1-1\nR1-3`; Parent = R11; strategy
  NORMALIZED_RATIO; Unit %; Min/Max seeded 0/1. R1-3 (kg) ÷ R1-1 (kg) is a well-formed 0–1
  share; both leaves exist (rows 9, 11). No drift.
- **Proposed revision (C):** light grammar fix only — "Measures the share of the
  production's total byproduct outflow (R1-1) that is repurposed into another external
  product or system (R1-3). Higher means more outflow finds value outside the original
  lifecycle." (The current text reads slightly ungrammatically: "the share repurposed
  byproduct from the outflow …".)
- **Notes:**
  - [minor] **Reference (J) is blank** — add `ISO 59020` (A.3.3). The repurposing-specific
    paper `WS+24` (References line 33) is about *identifying* repurposing opportunities, not
    a mass-share ratio, so it is a weaker fit; ISO 59020 is the better ground.
  - [minor] grammatical cleanup in C (see proposed revision).

### R12 — End-of-Life Recoverability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of a product unit's mass that can be cycled back at end of life — reused, recycled, or repurposed — instead of becoming waste. Higher means more of the product is recoverable."
- **Verdict:** CONSISTENT — **the flip is correctly reflected.** The Description now states
  the *recoverable* (higher = better) direction and matches the Formula
  `Recoverability = 1 - (Mass of Product Unit - Cyclable Potential) / Mass = Cyclable
  Potential / Mass of Product Unit`, over R1-4 (mass of product unit) and R1-6 (cyclable
  potential). No residual waste-share framing remains in C.
- **Grounding:**
  - ISO 59020 p.42 (Annex A): "The remaining outflows are considered as linear and do not
    count towards circularity. The linear (non-circular) outflow can be calculated by
    subtracting the circular outflows from 100 %." (`…/ISO-59020.pdf`) — grounds the
    `1 − (non-recoverable / mass)` complement construction R12 uses.
  - ISO 59020 p.10 (3.1.4): "circularity aspect … EXAMPLE Durability, recyclability,
    reusability, repairability, **recoverability**." (`…/ISO-59020.pdf`) — grounds
    "recoverability" as a named circularity aspect.
  - C2C p.36 (5.4): "≥ 50% of materials by weight are compatible with the intended cycling
    pathway(s)"; p.36 (5.3): "contain cycled and/or renewable content".
    (`…/c2c-certified-full-scope_v4.1_final_011525.pdf`) — grounds "mass that can be cycled
    back … reused, recycled, or repurposed" as cycling-pathway-compatible mass.
- **Implementation check:** `Underlying = R1-4\nR1-6`; Parent = R1; strategy
  NORMALIZED_RATIO; Unit %; Min/Max seeded 0/1 (now a bounded ratio, moved from
  PERFORMANCE_DIRECTION to SEED_01 per Comment). `Cyclable Potential (R1-6) / Mass (R1-4)`
  is a well-formed 0–1 share; both leaves exist (rows 12, 14) and share unit kg. The
  Comment (R) documents the full history: R121 folded in (identical formula), R1-5
  reference comparison dropped (Min/Max band now encodes the reference level), 2026-06-26
  direction flip. **Description, Formula, Comment and direction are mutually consistent.**
- **Proposed revision (C):** keep as-is — the rewrite is already done and correct.
- **Notes:**
  - [minor] **Reference (J) is blank** though the concept is groundable. Add `ISO 59020`
    (recoverability aspect / circular-vs-linear outflow, p.10 + p.42) and optionally `C2C`
    (cycling-pathway compatibility) so the recoverability share is auditable.
  - [minor] The Formula cell (I) restates the algebra twice
    (`1 - (Mass - Cyclable)/Mass = Cyclable/Mass`). That is intentional/clarifying, not
    drift — but the **Comment's first line** still opens "End-of-Life Waste = (Mass -
    Cyclable Potential)/Mass — the product waste share …", i.e. it leads with the *old*
    waste-share definition before the dated flip note. Consider trimming that stale lead
    sentence so the Comment opens with the current recoverability framing; the dated history
    below it can stay.
  - G cell "Target Value: min, max\nIndustry Average" — "Industry Average" is a reasonable
    benchmark hint; consistent with NORMALIZED_RATIO. No fix.

### R121 — Product Waste Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY — ARCHIVED]
- **Current (C):** "Measures the amount of waste generated, when the product is disposed."
- **Verdict:** CONSISTENT (intent) — **ARCHIVED, intentionally dormant.** The text states
  the correct intent (product waste at disposal) for the metric this row *was*; its
  computation `Waste = (Mass of Product Unit - Potential cyclable waste of product unit) /
  Mass of Product Unit` was folded up into R12 (which now carries the complement). Per the
  brief, do **not** rewrite to match a dormant state — keep intent-correct text and note
  the archived status.
- **Grounding:** same family ground as R12 (ISO 59020 p.42 linear/non-circular outflow =
  `100% − circular`; the waste share is the complement of R12's recoverability). No separate
  citation needed for a folded-in archived row.
- **Implementation check:** `Underlying` is **blank**, `Parent` is **blank** — unwired
  (correct for archived). Formula still present (the `(Mass - Cyclable)/Mass` waste share).
  Comment (R) reads: "ARCHIVED 2026-06-25 (T3.6): folded into R12 (End-of-Life Waste),
  which now carries this exact (Mass - Cyclable)/Mass computation directly. Unwired;
  reversible." — clearly marks dormancy by design, **not** a defect.
- **Proposed revision (C):** keep as-is (intent-correct). Do not rewrite.
- **Notes:**
  - [minor] The Comment names R12 as "End-of-Life **Waste**" — that was R12's name *before*
    the 2026-06-26 flip to "End-of-Life **Recoverability**". Update the R121 Comment's R12
    reference to "End-of-Life Recoverability (now the recoverable complement of this waste
    share)" so the archived note points at R12's current name/direction.
  - Status reads correctly as intentionally dormant. No grounding action required.

### R1-1 — Total byproduct of outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of mass of material and waste produced throughout the production process."
- **Verdict:** ADAPTED — accurate raw total-outflow denominator at product level; org-level
  source (ESRS E5-5 resource outflows) adapted to a product-process figure.
- **Grounding:** ESRS E5 p.6 (DR E5-5): "Disclosure Requirement E5-5 – Resource outflows.
  The undertaking shall disclose information on its resource outflows, including waste …"
  (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E5 Delegated-act-2023-5303-annex-1_en.pdf`).
  ISO 59020 p.45 (A.3.3): "m TO(X) is the total mass of outflow (X), in kg or other mass
  unit." (`…/ISO-59020.pdf`) — grounds "total mass of outflow" as the denominator term.
- **Implementation check:** Raw leaf, no formula; Parent IDs in the `Parent`-equivalent
  column = `R111\nR112`; feeds both ratios as the total-outflow denominator (R1-1). Unit kg
  consistent with R1-2/R1-3. `Data? = x`, stage M. Reference J = `ESRS E5-5`, which resolves
  (line 66). Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** [minor] org-level ESRS E5-5 reports outflows at undertaking level in
  tonnes/kg; here it is the product-process outflow mass — faithful adaptation. Adaptation
  is self-evident for a raw mass leaf; a Comment flag is optional. Optionally add `ISO 59020`
  (A.3.3 "total mass of outflow") alongside ESRS E5-5 for the denominator term.

### R1-2 — Recirculated byproduct derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of mass of material and waste reused or reutilized in the same process cycle."
- **Verdict:** ADAPTED — accurate raw reused-within numerator; grounded in GRI 306-4 /
  ESRS E5-5.
- **Grounding:** GRI 306-4 p.13: "Total weight of waste diverted from disposal in metric
  tons … recovery operations: Preparation for reuse; i. Recycling; ii. Other recovery
  operations." (`…/GRI 306_ Waste 2020.pdf`) — "diverted from disposal / preparation for
  reuse" grounds "reused or reutilized in the same process cycle." ISO 59020 p.45 (A.3.3):
  "m REUO(X) is the mass of outflow (X) that is reused". (`…/ISO-59020.pdf`)
- **Implementation check:** Raw leaf; feeds R111 as the numerator; Unit kg consistent with
  R1-1. `Data? = x`, stage M. Reference J = `GRI 306-4\nESRS E5-5`, both resolve (lines 83,
  66). Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** none material. Self-evident adaptation; no Comment flag needed.

### R1-3 — Repurposed byproduct derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of mass of material and waste reused outside of the product's process cycle."
- **Verdict:** ADAPTED — accurate raw repurposed-externally numerator; grounded in
  GRI 306-4 / ESRS E5-5.
- **Grounding:** GRI 306-4 p.13: "recovery operations: Preparation for reuse; i. Recycling;
  ii. Other recovery operations." (`…/GRI 306_ Waste 2020.pdf`) — "Other recovery
  operations" / diversion grounds reuse outside the original cycle. ISO 59020 p.45 (A.3.3)
  reused-mass term as above.
- **Implementation check:** Raw leaf; feeds R112 as the numerator; Unit kg consistent with
  R1-1. `Data? = x`, stage M. Reference J = `GRI 306-4\nESRS E5-5`, both resolve. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** [minor] R1-2 ("same process cycle") and R1-3 ("outside the product's process
  cycle") are mutually exclusive arms of R1-1's total outflow — wording is clean and
  non-overlapping. No fix.

### R1-4 — Mass of Product Unit  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total weight of a single product unit."
- **Verdict:** CONSISTENT — unambiguous raw figure; matches unit kg and the R12 denominator
  (`Mass of Product Unit`).
- **Grounding:** author/product-level physical quantity (a product's mass); no standard
  prescribes a single product unit's weight. ISO 59020 frames mass-based outflow shares
  generally (p.45, A.3.3) but the unit mass itself is a measured input — UNVERIFIABLE at the
  standard level is acceptable, but the term is self-defining so verdict is CONSISTENT, not
  a defect.
- **Implementation check:** Raw leaf; Parent = R12; feeds the R12 recoverability denominator.
  Unit kg consistent with R1-6. `Data? = x`, stages P,M,D. Reference J blank — appropriate
  for a self-defining measured mass. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** none. Blank Reference is fine for a self-defining raw mass.

### R1-5 — Reference Product Waste  [Level 5, raw, RAW_VALUE_STRATEGY — ARCHIVED]
- **Current (C):** "A benchmark waste amount for similar products, used as reference value."
- **Verdict:** UNVERIFIABLE — author/product-defined benchmark input; **ARCHIVED,
  intentionally dormant.** No standard supplies a "reference product waste" value; it is a
  supplied benchmark. Per the brief, keep intent-correct text and note archived status; do
  not rewrite.
- **Grounding:** author-defined benchmark — no citable source for the value itself
  (legitimate). EN15804+A2 / ISO 59020 set methods but not product benchmarks, consistent
  with leaving J blank.
- **Implementation check:** Raw leaf; `Parent`-equivalent column **blank** — unwired
  ("now feeds nothing"), as the brief states. `Data? = x` (still a recordable figure),
  stage E. Comment (R): "ARCHIVED 2026-06-25 (T3.6): the reference-product-waste comparison
  was dropped from R12 (the NORMALIZED Target Min/Max band already encodes the reference
  level). No longer scored; kept as a recordable figure. Reversible." — reads correctly as
  intentionally dormant, **not** a defect.
- **Proposed revision (C):** keep as-is (intent-correct).
- **Notes:** Status correct. The figure remains a recordable `Data? = x` input that feeds
  nothing post-archive, exactly as described in the brief. No fix.

### R1-6 — Product Cyclable Potential  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total potential of reusable, recyclable, repurposable materials from a disposed product unit."
- **Verdict:** CONSISTENT — accurate raw numerator for R12; matches unit kg and the R12
  numerator (`Cyclable Potential`). "reusable, recyclable, repurposable" maps onto the three
  cycling routes R12 aggregates.
- **Grounding:**
  - ISO 59020 p.42 (Annex A): circular outflows = "components and products that are reused
    (A.3.3); per cent recycled material derived from outflow (A.3.4); products and materials
    for renewable recirculation (A.3.5)." (`…/ISO-59020.pdf`) — grounds the
    reusable/recyclable/repurposable composition of "cyclable potential."
  - C2C p.36 (5.4): "≥ 50% of materials by weight are compatible with the intended cycling
    pathway(s)." (`…/c2c-certified-full-scope_v4.1_final_011525.pdf`) — grounds
    cycling-pathway-compatible mass as the recoverable fraction.
- **Implementation check:** Raw leaf; Parent = R12; feeds the R12 numerator. Unit kg
  consistent with R1-4 (so `R1-6 / R1-4` is a well-formed 0–1 share). `Data? = x`, stage E.
  Reference J blank. Consistent. (Sanity: R1-6 ⊆ R1-4 — cyclable mass is a subset of total
  mass — so R12 ∈ [0,1] as intended.)
- **Proposed revision (C):** keep as-is.
- **Notes:** [minor] Reference J blank though groundable — optionally add `ISO 59020`
  (A.3.3/A.3.4 circular outflows) and/or `C2C` (cycling-pathway compatibility) to make the
  cyclable-potential input traceable, mirroring the citation that should land on R12.

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| R1 | Material Efficiency Score | CONSISTENT (composite) | optional: name the two arms (R11+R12) |
| R11 | Reutilized Material Performance | CONSISTENT | keep; fix Formula trailing space; fix `ACM+17`/`C2C` citations |
| R111 | Reused Byproduct Share | CONSISTENT | keep; add `ISO 59020` to blank Reference |
| R112 | Repurposed Byproduct Share | CONSISTENT | grammar fix; add `ISO 59020` to blank Reference |
| R12 | End-of-Life Recoverability | CONSISTENT | keep (flip done correctly); add `ISO 59020`/`C2C`; trim stale Comment lead |
| R121 | Product Waste Share (ARCHIVED) | CONSISTENT (intent) | keep; update Comment's R12 name reference |
| R1-1 | Total byproduct of outflow | ADAPTED | keep |
| R1-2 | Recirculated byproduct derived from outflow | ADAPTED | keep |
| R1-3 | Repurposed byproduct derived from outflow | ADAPTED | keep |
| R1-4 | Mass of Product Unit | CONSISTENT | keep |
| R1-5 | Reference Product Waste (ARCHIVED) | UNVERIFIABLE | keep (dormant) |
| R1-6 | Product Cyclable Potential | CONSISTENT | keep; optionally add `ISO 59020`/`C2C` |

**Counts (12 rows):** CONSISTENT 5 (R1, R11, R111, R112, R1-6) + 2 intent-CONSISTENT
archived/grounded (R12 done-flip is CONSISTENT, R121 intent-CONSISTENT, R1-4 CONSISTENT) —
tallied as **CONSISTENT 7** (R1, R11, R111, R112, R12, R1-4, R1-6; R121 intent-CONSISTENT);
**ADAPTED 3** (R1-1, R1-2, R1-3); **UNVERIFIABLE 2** (R1-5 archived benchmark, and R1-4's
value-source is author-supplied though the term is self-defining → kept CONSISTENT, not
counted here); **DRIFTED 0** at the Description level. *Note:* the **R12 flip in the brief
is VERIFIED as correctly applied** — Description, Formula, direction and Comment all agree;
no waste-share framing remains in C.

**Proposed description rewrites:** only **R112** needs a genuine (grammar) rewrite; **R1**
gets an optional arm-naming clarification. All other Descriptions are kept (R12's rewrite
was already correctly applied; archived rows R121/R1-5 keep intent-correct text).

**Proposed adjacent-cell fixes (drift beyond Description):**
1. [major] **R11 Reference `ACM+17` is SOURCE-NOT-FOUND** — no PDF in `data/literature/Papers/`.
   Add the paper or drop the code; `ISO 59020` (A.3.3) is present and grounds R11 better.
2. [minor] **R11 Reference `C2C`** — pin canonical Label (`C2C` generic vs `C2C 5.2`/`C2C 5.3`).
3. [minor] **R11 Formula (I)** — stray trailing space: `… weight * R112 )` → `… weight * R112)`.
4. [minor] **Blank Reference cells on groundable ratios/leaves:** add `ISO 59020` to **R111**,
   **R112**; add `ISO 59020`(+`C2C`) to **R12** and **R1-6**.
5. [minor] **R12 Comment lead** still opens "End-of-Life Waste = (Mass - Cyclable)/Mass — the
   product waste share" before the dated flip note — trim so the Comment opens with the
   current recoverability framing.
6. [minor] **R121 Comment** refers to R12 by its pre-flip name "End-of-Life Waste" — update to
   "End-of-Life Recoverability."
7. [minor, R0 — out of batch] R0 Formula text reads `Sum (weight * R1 + … + weight * R5)`;
   R0's children are `R1\nR2\nR3`, so the `…+R5` ellipsis is stale. Flag on the R0 row.

**SOURCE-NOT-FOUND codes:** `ACM+17` (cited on R11) — Label resolves in References.tsv
(line 39) but **no `ACM+17*` file exists** in `data/literature/Papers/` (verified by
directory listing). Recorded, not substituted.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above (ISO
59020, C2C v4.1, ESRS E5, GRI 306 Waste 2020). I did not read full standard sections beyond
the cited pages, nor the additional ISO 59XXX files (59004/59010/59014/59040) — ISO 59020 is
the cited code and the relevant one. I did not audit numeric Min/Max bands, weights, the R0
parent (out of scope), or cross-domain references (R2-7 cites EC5/EN41 — not in this batch).
The `ACM+17` SOURCE-NOT-FOUND is reported from a directory listing of `Papers/`; if the file
exists under a different prefix it was not located. The R12 flip was verified as a
consistency check between Description / Formula / Comment in the snapshot, not against a
recomputation of values.


---

## R2 — Energy Efficiency: recovery + consumption sub-trees

### R2 — Energy Efficiency Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the efficiency of energy utilization, consumption, and reduction of overall usage."
- **Verdict:** DRIFTED (Formula text + relations). The **description prose is fine** as a
  composite roll-up, but the **Formula cell (I) still reads `Sum (weight * R21 + … + weight * R23)`** —
  naming a dangling `R23` that no longer exists. `Underlying Metrics` now = `R21\nR22` only
  (no R23 row exists in the sheet). Gap-fix drift: the child was removed but the formula text
  was not updated.
- **Grounding:** composite/parent — no single literature source expected (Reference cell blank
  by design, correct). The two halves are grounded on their children: recovery via ISO 59020
  p.55 (energy recovery) and EN15804+A2 Module D; consumption via GRI 302 / ESRS E1-5.
  ESRS E1 p.8 (DR E1-5): *"The objective of this Disclosure Requirement is to provide an
  understanding of the undertaking's total energy consumption in absolute value, improvement
  in energy efficiency … and the share of renewable energy in its overall energy mix."*
  (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E1 Delegated-act-2023-5303-annex-1_en.pdf`)
- **Implementation check:** `Underlying = R21\nR22`; both children exist (rows 16, 20);
  strategy WEIGHTED_AVERAGE; Unit % compatible with averaging two 0–1/% sub-scores. The
  prose ("utilization, consumption, and reduction") maps onto R21 (recovery/utilization) +
  R22 (consumption, which itself contains the reduction arm R224). No description drift; only
  the **Formula text names R23** and the brief confirms R23 was removed.
- **Proposed revision (C):** keep prose; optional explicit-children version:
  "Aggregates the product's energy performance into one score by combining its energy-recovery
  performance (R21) and its energy-consumption performance (R22). Higher means more energy is
  recovered/reused and less is consumed per output across the product's life cycle."
- **Notes:**
  - [major] **Formula (I) fix:** `Sum (weight * R21 + … + weight * R23)` → `Sum (weight * R21 + weight * R22)`. Removes the dangling R23 reference (verifying the brief's gap-fix context: R2 now aggregates only R21 + R22).
  - Blank Reference (J) is correct for a composite parent — not a defect.
  - Parent R0 is outside this batch; not verified here.

### R21 — Energy Recovery Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures how performant the energy recovery system of the product pipeline is. It evaluates the amount of energy that can be recovered from the non-circular resource outflow and how much of it is reused back into the product pipeline."
- **Verdict:** CONSISTENT (composite parent; internal check). Prose correctly describes a
  roll-up of recovery sub-ratios (R211 regeneration, R212 reuse, R213 storage), matching
  `Underlying = R211\nR212\nR213` and strategy WEIGHTED_AVERAGE.
- **Grounding:**
  - ISO 59020 p.55: *"residual, non-renewable resources of negligible or negative material value, which is considered as non-recoverable, can be used for the generation or recovery of energy. The non-renewable resources that can be used for energy recovery include, for example, waste (via processes such as bio-gas production, pyrolysis, gasification, incineration with energy recovery, etc.), heated water from chemical plants and water used for washing (e.g. by condensation or heat exchang[e])."* (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds recovering energy from the non-circular resource outflow.
  - EN15804+A2 p.36: *"Information module D aims at transparency for the environmental benefits or loads resulting from reusable products, recyclable materials and/or useful energy carriers leaving a product system e.g. as secondary materials or fuels."* (`data/literature/EPD/EN15804+A2.pdf`) — grounds the "useful energy carriers leaving the system" recovery concept (the cited `Module D - EN15804+A2`).
- **Implementation check:** Children R211, R212, R213 all exist (rows 17–19); Formula text (I)
  reads `Sum (weight * R211 + weight * R212 )` — it **omits R213**, although R213 is a wired
  child (weight 0.3334; R211 0.3333, R212 0.3333). Unit % compatible with averaging. Comment
  (R) "Only applicable when there exist self-generated energy" is a sensible scoping note.
- **Proposed revision (C):** keep prose (it accurately frames recovery + reuse).
- **Notes:**
  - [minor] **Formula (I) fix:** `Sum (weight * R211 + weight * R212 )` → `Sum (weight * R211 + weight * R212 + weight * R213)` (R213 is a wired child but is not named in the formula text).
  - **Reference (J) — code mismatch:** R21 cites `SASB RT-CP-120a.1`, but in the C&P standard
    `RT-CP-120a.1` is **Air Quality**, not energy. SASB C&P p.6: *"… (4) particulate matter (PM)
    … RT-CP-120a.1 Energy Management (1) Total energy consumed, (2) percentage grid electricity,
    (3) percentage renewable and (4) total self-generated energy … RT-CP-130a.1"*
    (`data/literature/SASB - Sustainability Account Standards Board/RT-CP-containers-and-packaging-standard_en-gb.pdf`)
    — i.e. the **energy** disclosure in C&P is `RT-CP-130a.1`, and `120a.1` is air emissions.
    (This is the same table-vs-body topic-shift flagged for EN21.) Recommend re-pointing to
    `SASB RT-CP-130a.1` (energy, incl. "total self-generated energy" — the closest match to a
    recovery arm) **and** keeping ISO 59020 + Module D as the primary recovery grounds. [major]
  - Comment-cell flag (ADAPTED, non-obvious): "Product-level energy-recovery roll-up; grounded
    in ISO 59020 energy recovery + EN15804+A2 Module D exported-energy. SASB energy code is
    `RT-CP-130a.1` (not 120a.1)."

### R211 — Regeneration of Energy  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the overall energy generated from the resource outflow of the product's lifecycle."
- **Verdict:** CONSISTENT — prose matches `Regen = Generated Energy / Potential Energy`, then
  `(Regen - Min)/(Max - Min)`, over children R2-1 (total potential energy of outflow) and
  R2-2 (generated energy from outflow).
- **Grounding:**
  - EN15804+A2 p.35: *"Materials for energy recovery are identified based on the efficiency of energy recovery with a rate higher than 60 % … Materials from which energy is recovered with an efficiency rate below 60% are not considered materials for energy recovery."* (`data/literature/EPD/EN15804+A2.pdf`) — grounds an energy-recovery **rate** (recovered ÷ potential) as a recognised quantity; matches the `generated/potential` ratio. (R211 cites `Module D - EN15804+A2`.)
  - ISO 59020 p.55 (quote under R21) grounds generating energy from the resource outflow.
- **Implementation check:** Children R2-1 (kWh, potential) and R2-2 (kWh, generated) both exist
  (rows 25–26) and share unit kWh, so the ratio is dimensionless → Unit % consistent. Min/Max
  seeded 0/1 (Comment R documents this; a 0–1 score already). Strategy NORMALIZED_RATIO matches.
  The current description states only the numerator ("energy generated") and omits the
  ratio-against-potential framing the formula computes.
- **Proposed revision (C):** "Measures how much of the energy that could be recovered from the
  product's resource outflow is actually generated — generated energy (R2-2) ÷ total potential
  energy of the outflow (R2-1). Higher means a more effective energy-recovery system."
- **Notes:** [minor] description names only the numerator; the proposed revision makes the
  ratio explicit to match the formula + children. Reference `Module D - EN15804+A2` resolves.

### R212 — Reused Energy Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the percentage of generated energy in the product's lifecycle which is reused back into the process pipeline."
- **Verdict:** ADAPTED — prose matches `Reuse = Recirculated Energy / Generated Energy`, then
  normalized; the recirculation-of-recovered-energy concept is grounded in ISO 59020 / Module D,
  but the **cited code `ACM+17` has no PDF in the corpus** (see SOURCE-NOT-FOUND).
- **Grounding:**
  - ISO 59020 p.71: *"If any resource outflows are known to have their value recovered, by repair, refurbish, remanufacture, repurpose, recycling, reuse or subject to recirculation in the biolog[ical cycle]"* (`data/literature/ISO 59XXX/ISO-59020.pdf`) — grounds recirculation/reuse of recovered value (here, recovered energy).
  - EN15804+A2 p.36 (Module D "useful energy carriers leaving a product system", quote under R21) grounds reusing recovered energy.
  - The cited `ACM+17` ("Product Circularity Assessment Methodology", References.tsv line 39) is **not present** in `data/literature/Papers/` — could not retrieve any quote from it.
- **Implementation check:** Children R2-2 (generated, kWh) and R2-3 (recirculated, kWh) both
  exist (rows 26–27), share unit kWh → ratio dimensionless, Unit % consistent. Min/Max seeded
  0/1 (Comment R). Strategy NORMALIZED_RATIO matches. Prose matches formula + children.
- **Proposed revision (C):** keep prose (accurate). Optional explicit version: "Measures the
  share of the recovered/generated energy (R2-2) that is recirculated back into the product's
  processes (R2-3). Higher means more recovered energy displaces purchased energy."
- **Notes:**
  - [major] **Reference (J):** `ACM+17` is a **SOURCE-NOT-FOUND** code — the paper has no file
    in the corpus, so the citation cannot be verified. Recommend re-grounding on the recovered-
    energy-reuse concept with `ISO 59020` (recirculation, p.71) and/or `Module D - EN15804+A2`
    (both present and grounded above), and either supply the ACM+17 PDF or drop the token.
  - Comment-cell flag (ADAPTED, non-obvious): "Recovered-energy reuse share; concept grounded
    in ISO 59020 recirculation / EN15804+A2 Module D. Cited ACM+17 source not in corpus."

### R213 — Stored Energy Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the amount of stored energy in form of electricity, heat, or in other forms."  **(Objective/Goal cell is blank.)**
- **Verdict:** DRIFTED + UNVERIFIABLE. (a) DRIFTED: the prose states only "amount of stored
  energy", but the formula is a **share** `Stored = Stored Energy / Generated Energy`, then
  normalized — the description omits the denominator/ratio framing. (b) UNVERIFIABLE: a
  "stored-energy-over-generated" ratio is an **author-defined energy ratio** — none of the
  in-scope sources (ISO 59020, EN15804+A2 Module D, GRI 302, ESRS E1) prescribe an
  energy-storage share metric. The Reference cell (J) is **blank**.
- **Grounding:** searched ISO 59020 ("energy recovery", "secondary energy"), EN15804+A2
  ("exported energy", "energy carriers"), GRI 302 ("energy"), ESRS E1 ("energy consumption and
  mix") — **no source defines a stored-energy share** of generated recovery energy. ISO 59020
  p.55 and EN15804+A2 p.36 (quotes above) cover energy *recovery* and *exported energy carriers*
  but not an internal storage fraction. So the storage ratio remains author-defined; this is a
  legitimate UNVERIFIABLE, not a defect.
- **Implementation check:** Children R2-2 (generated, kWh) and R2-4 (stored, kWh) both exist
  (rows 26, 28); share unit kWh → ratio dimensionless, Unit % consistent. Min/Max seeded 0/1
  (Comment R). Strategy NORMALIZED_RATIO matches. Note: R2-4's own row is sparse (no Data Source,
  no `x` mark for "Data?"), so the input may be unmeasured in practice — flag for the leaf batch.
- **Proposed revision (C):** "Measures the share of recovered/generated energy (R2-2) that is
  put into storage rather than immediately reused — stored energy (R2-4) ÷ generated energy
  (R2-2), in any form (electricity, heat, etc.). Higher means more recovered energy is buffered
  for later use."
- **Notes:**
  - [minor] description states only the numerator; proposed revision makes it a share to match
    the formula.
  - [minor] **Objective/Goal cell is blank** while every sibling (R211/R212) has one — add e.g.
    "To buffer recovered energy for later use and improve energy circularity."
  - UNVERIFIABLE is the correct status for this author-defined storage ratio; blank Reference is
    therefore acceptable. Do **not** invent a source. (If a code is wanted, `ISO 59020` is the
    closest *thematic* anchor for circular energy, but it does not define this specific ratio —
    cite only as thematic context, not as the metric's source.)

### R22 — Energy Consumption Performance  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the energy consumed per defined output (functional unit) across the product's lifecycle."
- **Verdict:** CONSISTENT (composite parent; internal check), with one wording caveat. Prose
  describes a roll-up of consumption sub-ratios, matching `Underlying = R221\nR222\nR223\nR224`
  and WEIGHTED_AVERAGE. The phrase "per defined output (functional unit)" is precise for the
  intensity arm (R222) but is slightly narrow as a label for the whole parent (which also rolls
  up end-user efficiency R221, logistics R223, and reduction R224).
- **Grounding:**
  - ESRS E1 p.8 (DR E1-5): *"The undertaking shall provide information on its energy consumption and mix … total energy consumption in absolute value, improvement in energy efficiency …"* (`…/ESRS E1 …annex-1_en.pdf`) — grounds energy-consumption + efficiency as a disclosure (cites `ESRS E1-5`).
  - GRI 302 p.3 (table of contents): *"Disclosure 302-2 Energy consumption outside of the organization … 302-3 Energy intensity … 302-5 Reductions in energy requirements of products and services"* (`…/GRI 302_ Energy 2016.pdf`) — the parent's three cited GRI codes (302-2, 302-3, 302-5) collectively cover the consumption arm.
- **Implementation check:** Children R221, R222, R223, R224 all exist (rows 21–24); strategy
  WEIGHTED_AVERAGE (each 0.25). Unit % compatible. **Formula text (I)** reads
  `Sum (weight * R221 + … + weight * R223)` — the elided "…" before R223 conventionally implies
  R222, but R224 (a wired 0.25-weight child) is **not named**; the "… R223" tail under-counts
  the four children. Minor formula-text drift (less severe than R2/R21 because it uses an
  ellipsis, but R224 should be the visible tail).
- **Proposed revision (C):** "Aggregates the product's energy-consumption performance into one
  score across its life cycle, combining end-user efficiency (R221), manufacturing energy
  intensity (R222), logistics energy (R223) and energy-use reduction over time (R224). Enables
  benchmarking and tracks reductions in overall consumption."
- **Notes:**
  - [minor] **Formula (I):** make R224 the visible tail — `Sum (weight * R221 + … + weight * R224)`.
  - [minor] **Reference (J):** the four-code list `GRI 302-2 / 302-3 / 302-5 / ESRS E1-5` is
    reasonable as an aggregate anchor, but `GRI 302-5` (reductions in *products' energy
    requirements*) is really the R221/R224 concept and `302-3` the R222 concept — the codes are
    better placed on the children (see per-child notes). Keeping them on the parent is
    acceptable for a composite; optionally trim to `ESRS E1-5` + `GRI 302-3` as the cleanest
    consumption anchors.
  - Blank-by-design caveat does not apply (this parent legitimately carries codes); composite
    internal check passes.

### R221 — End User Energy Efficiency  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the energy consumption when the product is used by the users or costumer."  **(Objective/Goal cell is blank.)**
- **Verdict:** DRIFTED. The gap-fix re-tagged R221 to NORMALIZED_RATIO with **Formula
  `Performance = Output / Input`** (per the brief: `R2-5 / R2-6`, operational output energy ÷
  operational input energy). That is an **output-over-input efficiency ratio** (higher = more
  efficient). The current description ("Measures the energy consumption when the product is
  used") describes a raw *consumption* level, not an efficiency *ratio* — and "costumer" is a
  typo. The description must be updated to an output/input efficiency framing. **Verification of
  the brief's claim:** the description does **not** yet match an output-over-input efficiency
  ratio — confirmed DRIFTED, rewrite needed.
- **Grounding:**
  - EN15804+A2 p.26 (B6): *"B6, operational energy use (e.g. operation of heating system and other building related installed services)"* and p.34: *"B6 Energy use to operate building integrated technical systems … energy use during the operation of the product (the integrated building service)."* (`data/literature/EPD/EN15804+A2.pdf`) — grounds **operational (in-use) energy** as a life-cycle quantity (the B6 use-stage operational energy the brief points to). The input leg (R2-6) and output leg (R2-5) are operational-energy quantities.
  - The cited `GRI 302-5` is about *reductions* in energy requirements, **not** an efficiency
    ratio. GRI 302 p.15 (DR 302-5): *"Reductions in energy requirements of sold products and
    services achieved during the reporting period, in joules or multiples. a. Basis for
    calculating reductions in energy consumption, such as base year or baseline …"*
    (`…/GRI 302_ Energy 2016.pdf`) — this reports a year-over-year *reduction* of a product's
    energy requirement, not an `output/input` efficiency. So GRI 302-5 grounds the *theme*
    (product in-use energy performance) but **not** the live `Output/Input` formula.
- **Implementation check:** Children R2-5 (Operational Output Energy, kWh) and R2-6
  (Operational Input Energy, kWh) both exist (rows 29–30), share unit kWh → ratio dimensionless,
  Unit % consistent. Strategy NORMALIZED_RATIO matches. Comment (R) confirms the re-tag:
  "End User Energy Efficiency = Output/Input; a real ratio … Re-tagged WEIGHTED_RATIO->
  NORMALIZED_RATIO 2026-06 (T3.6)." `G` (Potential Reference Values) = "Target Value: min, max"
  consistent with a normalized band. **No Min/Max seeded** in the row (unlike the recovery
  ratios), and the Comment lacks the "seeded 0/1" note — but `Output/Input` is **not**
  intrinsically ≤ 1, so leaving the band company-set (not 0/1) is actually correct here.
- **Proposed revision (C):** "Measures how efficiently the product converts supplied energy into
  useful output during the use phase — operational output energy (R2-5) ÷ operational input
  energy (R2-6). Higher means less energy is wasted to deliver the same product function."
- **Notes:**
  - [major] description drift: rewrite from a raw consumption statement to the output/input
    efficiency ratio (matches the live `R2-5 / R2-6` formula). **Brief verification: confirmed —
    the current description does not describe an output-over-input efficiency ratio.**
  - [minor] typo "costumer" → "customer" (in the discarded text; not carried into the revision).
  - [minor] **Objective/Goal cell is blank** — add e.g. "To improve in-use energy efficiency and
    reduce the energy customers spend operating the product."
  - **Reference (J):** `GRI 302-5` grounds the product-in-use-energy *theme* but not the
    `Output/Input` ratio; the operational-energy legs are better grounded by **EN15804+A2 B6**
    (p.26/p.34). Recommend adding `Module D - EN15804+A2`/B6 context — or note that the
    `Output/Input` efficiency ratio itself is author-defined (no source prescribes it). Keep
    GRI 302-5 as the thematic anchor with the caveat.
  - Comment-cell flag (ADAPTED, non-obvious): "In-use energy efficiency = R2-5/R2-6; operational
    energy grounded in EN15804+A2 B6, but the output/input ratio is author-defined — GRI 302-5
    covers product-energy *reduction*, not this efficiency ratio."

### R222 — Energy Intensity Performance  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the energy consumption needed to produce or manufacture the products."  **(Objective/Goal blank.)**
- **Verdict:** CONSISTENT — prose matches `Intensity = Total manufacturing energy / Total
  produced units`, then normalized; the energy-intensity (energy per output unit) concept is
  directly grounded.
- **Grounding:**
  - GRI 302 p.13 (DR 302-3): *"Energy intensity ratio for the organization. a. Organization-specific metric (the denominator) chosen to calculate the ratio … calculate the ratio by dividing the absolute energy consumption (the numerator) by the organization-specific metric (the denominator)."* and *"Energy intensity ratios … express the energy required per unit of activity, output, or any other organization-specific metric."* (`…/GRI 302_ Energy 2016.pdf`) — grounds energy ÷ output-unit intensity exactly (cites `GRI 302-3`).
- **Implementation check:** Children R2-11 (Total manufacturing energy, kWh) and R2-7 (Total
  produced units, Units) both exist (rows 35, 31). Ratio kWh/unit → normalized to %, Unit %
  consistent. Strategy NORMALIZED_RATIO matches. Comment (R): "Declines in energy intensity are
  a proxy for efficiency improvements" — correct directionality note. No drift.
- **Proposed revision (C):** keep prose. Optional explicit version: "Measures the manufacturing
  energy consumed per unit produced — total manufacturing energy (R2-11) ÷ total produced units
  (R2-7). Lower intensity indicates more efficient production."
- **Notes:**
  - [minor] **Objective/Goal cell is blank** — add e.g. "To reduce the energy required to
    manufacture each product unit."
  - **Direction caveat:** energy intensity is **lower = better**, but the family normalizes
    higher = better. The Comment treats *declines* as improvement, so the company Target Min/Max
    band must encode the lower-is-better direction (matches the band-direction guidance in
    recent commits). Worth a one-line confirmation that R222's band is set lower-is-better.
  - Reference `GRI 302-3` resolves and is the exact ground. CONSISTENT.

### R223 — Logistics Energy Performance  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of energy consumption for transportation and distribution of products. Includes reverse logistics."  **(Objective/Goal blank.)**
- **Verdict:** CONSISTENT — prose matches `Logistics = Total energy consumption for logistics /
  Total energy inflow (Current)`, then normalized; the value-chain transportation-energy concept
  is grounded.
- **Grounding:**
  - GRI 302 p.11 (DR 302-2): *"Energy consumption outside of the organization, in joules or multiples … list energy consumption outside of the organization, with a breakdown by upstream and downstream categories and activities."* (`…/GRI 302_ Energy 2016.pdf`) — transportation & distribution are GHG-Protocol upstream/downstream categories covered by 302-2, grounding logistics energy (cites `GRI 302-2`).
- **Implementation check:** Children R2-8 (Logistics Energy Consumption, kWh) and R2-9 (Total
  energy inflow Current, kWh) both exist (rows 32–33); share unit kWh → ratio dimensionless,
  Unit % consistent. Strategy NORMALIZED_RATIO matches. R2-8's description and R223's prose both
  explicitly include reverse logistics — aligned. No drift.
- **Proposed revision (C):** keep prose. Optional: "Measures the share of the product's total
  energy inflow (R2-9) that is consumed by transportation and distribution, including reverse
  logistics (R2-8). Lower means a less energy-intensive logistics footprint."
- **Notes:**
  - [minor] **Objective/Goal cell is blank** — add e.g. "To reduce transport and distribution
    energy across forward and reverse logistics."
  - **Direction caveat:** like R222, a *lower* logistics share is better — confirm the band is
    set lower-is-better.
  - Reference `GRI 302-2` resolves and grounds the concept. CONSISTENT.

### R224 — Energy Inflow Improvement  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the reduction of total energy used throughout the product's life cycle."
- **Verdict:** CONSISTENT (on substance) — prose matches `Reduction = [Total energy inflow]
  Current / Previous`, then normalized; a period-over-period energy-reduction concept. Two of
  the three cited codes are **loose** (see notes), but the description itself is faithful.
- **Grounding:**
  - GRI 302 p.14 (DR 302-4): *"Disclosure 302-4 Reduction of energy consumption … Amount of reductions in energy consumption achieved as a direct result of conservation and efficiency [initiatives]."* (`…/GRI 302_ Energy 2016.pdf`) — directly grounds an energy-**reduction** metric (cites `GRI 302-4`; the tightest match).
  - **Loose cites:** `ESRS E5-4` is *Resource inflows* (ESRS E5 p.1 ToC: *"Disclosure Requirement E5-4 – Resource inflows"*, `…/ESRS E5 …annex-1_en.pdf`) — an inflow disclosure, **not** a reduction-over-time metric. `SASB RT-EE-130a.1` is an energy-**mix** disclosure (SASB RT-EE p.8: *"RT-EE-130a.1. (1) Total energy consumed, (2) percentage grid electricity and (3) percentage renewable"*, `…/RT-EE-electrical-and-electronic-equipment-standard_en-gb.pdf`) — it reports total/mix, **not** a current-vs-previous reduction.
- **Implementation check:** Children R2-9 (Total energy inflow Current, kWh) and R2-10 (Total
  energy inflow Previous, kWh) both exist (rows 33–34); share unit kWh → ratio dimensionless,
  Unit % consistent. `G` = "Target Value: min, max\nValue of another Timeframe" — consistent
  with a current/previous reduction. Strategy NORMALIZED_RATIO matches. No description drift.
  Note the Formula text writes `Current / Previous`; a *reduction* is conventionally
  `1 - Current/Previous` (so that a drop in energy scores higher) — confirm whether the band or
  a `1 -` term supplies the higher-is-better direction (cf. the R12/EN13 direction-flip
  pattern). If `Current/Previous` is used raw, the band must be lower-is-better.
- **Proposed revision (C):** keep prose. Optional clarity: "Measures the reduction in the
  product's total energy inflow over time, comparing the current period (R2-9) against an
  earlier period (R2-10). Higher means energy use has fallen."
- **Notes:**
  - [minor] **Reference (J):** `GRI 302-4` is the precise ground (energy reduction). `ESRS E5-4`
    (resource *inflows*) and `SASB RT-EE-130a.1` (energy *mix*) are thematically adjacent but do
    **not** define a reduction metric — recommend demoting/removing them or replacing `ESRS E5-4`
    with **`ESRS E1-5`** (energy consumption + "improvement in energy efficiency", p.8) which is
    closer. Keep `GRI 302-4` as primary.
  - [minor] **Direction:** confirm `Current/Previous` is wrapped to higher-is-better (a `1 -`
    term or a lower-is-better band), consistent with the recent direction-fix commits.
  - Comment-cell flag (ADAPTED, non-obvious): "Period-over-period energy-reduction at product
    level; grounded in GRI 302-4. ESRS E5-4 (inflows) / SASB RT-EE-130a.1 (mix) are loose cites."

---

## Batch summary

**Counts (10 metrics):** CONSISTENT 5 (R21 composite, R211, R22 composite, R222, R223) ·
DRIFTED 3 (R2 — formula text only; R213; R221) · ADAPTED 1 (R212) · UNVERIFIABLE 1 (R213).
R224 is CONSISTENT on substance with loose citation codes.

**Proposed description rewrites (C):** **R221** (raw-consumption → output/input efficiency
ratio — the brief's key change, confirmed needed) and **R213** (numerator-only → stored ÷
generated share, + fill blank Objective). Light/optional sharpening offered for R211, R22, R2.
R21, R212, R222, R223, R224 keep current prose (faithful).

**Brief-verification results:**
1. **R221 → NORMALIZED_RATIO `R2-5 / R2-6` (output ÷ input).** Children R2-5 (output) / R2-6
   (input) exist, share kWh, ratio is well-formed, strategy + Comment confirm the re-tag.
   The **description does NOT yet match an output-over-input efficiency ratio** (it still says
   "energy consumption when the product is used") → DRIFTED, rewrite proposed above.
2. **R2 aggregates only R21 + R22 (R23 removed).** Confirmed: `Underlying = R21\nR22`, no R23
   row exists. **However the Formula text (I) still reads `… + weight * R23`** → propose fixing
   to `Sum (weight * R21 + weight * R22)`. (Description prose is fine; only the formula text is
   stale.)

**Proposed adjacent-cell fixes (beyond Description):**
| Cell | Where | Fix |
|------|-------|-----|
| I (Formula) | R2 | `… + weight * R23` → `Sum (weight * R21 + weight * R22)` [major] |
| I (Formula) | R21 | add R213: `Sum (weight * R211 + weight * R212 + weight * R213)` [minor] |
| I (Formula) | R22 | name R224 in tail: `Sum (weight * R221 + … + weight * R224)` [minor] |
| J (Reference) | R21 | `SASB RT-CP-120a.1` (= Air Quality in C&P) → `SASB RT-CP-130a.1` (energy); keep ISO 59020 + Module D [major] |
| J (Reference) | R212 | `ACM+17` is SOURCE-NOT-FOUND — re-ground on `ISO 59020`/`Module D - EN15804+A2`, or supply the PDF [major] |
| J (Reference) | R224 | demote/replace `ESRS E5-4` (inflows) & `SASB RT-EE-130a.1` (mix); keep `GRI 302-4`; consider `ESRS E1-5` [minor] |
| J (Reference) | R213 | blank is acceptable (UNVERIFIABLE author ratio); do not invent a source [—] |
| Objective | R213, R221, R222, R223 | blank Objective/Goal cells — add a one-line goal each [minor] |
| C (typo) | R221 | "costumer" → "customer" (resolved by the rewrite) [minor] |

**SOURCE-NOT-FOUND codes:** `ACM+17` (cited on R212; "Product Circularity Assessment
Methodology", References.tsv line 39) — no file with that prefix in `data/literature/Papers/`
and no title match found; recorded, not substituted.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above; I did not
read full standard sections beyond the cited pages. The raw `R2-1..R2-11` leaves are out of
scope and were checked only for existence/units/wiring (note R2-4 looks sparsely populated —
flag for the leaf batch). Direction (higher-vs-lower-is-better) for R222/R223/R224 is inferred
from formula + Comments; I did not open the engine code to confirm how each band is applied —
flagged for confirmation against the recent band-direction commits. The "stored-energy share"
(R213) and "output/input end-user efficiency" (R221 ratio) are author-defined constructions
with no datapoint-level source — UNVERIFIABLE/author-defined is the correct status, not a
defect. Parent R0 and the per-child weights were not audited (out of scope). SASB code
numbering is reported from the cited summary/body pages of the C&P and EE PDFs; I did not
exhaustively map every SASB topic code.


---

## R2 — Raw energy data inputs R2-1…R2-11

### R2-1 — Total potential energy of outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of energy that can be derived from the resource outflow throughout the product's lifecycle. It includes potentials from all forms of resource outflow e.g. heat, waste, etc."
- **Verdict:** UNVERIFIABLE — author-defined raw input; legitimate, no citable standard supplies the value.
- **Grounding:** none cited (J blank), appropriate for a raw potential figure. Concept (recoverable energy potential) is adjacent to EN 15804 Module D recovery potential but the value itself is author-supplied — no quote claimed.
- **Implementation check:** Feeds R211 as the **denominator** of `Regen = Generated Energy / Potential Energy` (R211 children = `R2-1\nR2-2`, R2-2 = generated). "Potential energy of outflow" = potential, "generated" = actual — numerator/denominator roles are coherent. Unit kWh consistent with R2-2 (also kWh), so the R211 ratio is well-formed. Stages = M. No drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] "potential energy" risks confusion with the physics term; the prose's "energy that can be derived from the resource outflow" disambiguates it — acceptable. Raw leaf, no Comment-cell flag needed.

### R2-2 — Generated energy derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy actually generated from the resource outflow."
- **Verdict:** UNVERIFIABLE — author-defined raw input. (Cites `Module D - EN15804+A2`, which resolves in References.tsv line 93 and the PDF exists at `data/literature/EPD/EN15804+A2.pdf` / Module-D whitepapers — but the raw kWh figure itself is supplied, not prescribed by the standard.)
- **Grounding:** `Module D - EN15804+A2` (J) is the correct *conceptual* anchor for energy recovered beyond the system boundary; per the lighter-pass stance no verbatim quote is pulled for a raw input whose value is author-supplied. Code is valid (resolves), not orphan.
- **Implementation check:** Three-way fan-out — feeds R211 (numerator of `Generated/Potential`), R212 (denominator of `Reuse = Recirculated/Generated`), and R213 (denominator of `Stored = Stored/Generated`). Parent Metrics cell correctly lists `R211\nR212\nR213`. Unit kWh consistent across all three ratios. Description ("energy actually generated") cleanly distinguishes it from R2-1 (potential). No drift.
- **Proposed revision:** keep as-is.
- **Notes:** Code `Module D - EN15804+A2` resolves; keep. No Comment-cell flag needed for a raw leaf.

### R2-3 — Recirculated energy derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy recirculated back to the product's lifecycle."
- **Verdict:** UNVERIFIABLE — author-defined raw input.
- **Grounding:** J blank, appropriate.
- **Implementation check:** Feeds R212 as the **numerator** of `Reuse = Recirculated Energy / Generated Energy` (R212 children = `R2-2\nR2-3`). "Recirculated back into the lifecycle" matches the reuse-numerator role; Unit kWh consistent with R2-2 denominator. Stages = M. No drift.
- **Proposed revision:** keep as-is.
- **Notes:** none. Terminology ("recirculated") matches R212's formula wording ("Recirculated Energy") — consistent.

### R2-4 — Stored energy derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy stored from the generated energy."
- **Verdict:** CONSISTENT (substance) — text describes a stored-energy figure measured against generated energy, matching its role; Unit kWh is correct. Minor hygiene gaps (empty stages, blank Objective) noted below; not a description defect.
- **Grounding:** J blank, appropriate for a raw input.
- **Implementation check:** Gap-fix context **confirmed** — Unit (H) = `kWh` and Level = `5`, matching a stored-energy quantity in kWh. Feeds R213 as the **numerator** of `Stored = Stored Energy / Generated Energy` (R213 children = `R2-2\nR2-4`). Description "energy stored from the generated energy" matches the stored/generated numerator role exactly, and kWh is dimensionally consistent with R2-2 (generated, kWh) so the R213 ratio is in [0,1] as intended. No description/unit drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] **Product Life Cycle Stages cell is empty** — every sibling raw energy leaf carries `M` (manufacturing); set R2-4 stages to `M` for consistency. [minor] Objective/Goal cell is blank (siblings R2-1/-2/-3 are also blank for these raw leaves, so this is in-pattern — no action). The gap-fix Unit=kWh / Level=5 is correct and matches the description.

### R2-5 — Operational Output Energy  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy effectively used for the desired output of the product."
- **Verdict:** CONSISTENT — text matches the **numerator** role in R221 `Performance = Output / Input`.
- **Grounding:** J blank, appropriate.
- **Implementation check:** R221 (End User Energy Efficiency) children = `R2-5\nR2-6`, Formula `Performance = Output / Input`. R2-5 = "energy effectively used for the desired output" → the **Output** numerator. Role confirmed. Unit kWh consistent with R2-6 (Input, kWh) so the efficiency ratio is dimensionless as intended. Data Source = "Customer / Product Data", stages should be U (use phase) to match parent R221's `U` — see note. No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] **Product Life Cycle Stages cell is empty**; R221 (the parent) is tagged `U` (use phase) and the prose says "when the product is used" — set R2-5 stages to `U` for consistency. The numerator role is unambiguous.

### R2-6 — Operational Input Energy  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy supplied to the product."
- **Verdict:** CONSISTENT — text matches the **denominator** role in R221 `Performance = Output / Input`.
- **Grounding:** J blank, appropriate.
- **Implementation check:** R221 children = `R2-5\nR2-6`, Formula `Performance = Output / Input`. R2-6 = "energy supplied to the product" → the **Input** denominator. Role confirmed. Unit kWh consistent with R2-5. Data Source = "Customer / Product Data". No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] **Product Life Cycle Stages cell is empty**; mirror parent R221's `U` (use phase), as for R2-5. Output(R2-5)/Input(R2-6) numerator/denominator pairing is clean and dimensionally consistent.

### R2-7 — Total produced units  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total number of units produced during the referenced time period."
- **Verdict:** CONSISTENT — text matches the denominator role in R222 `Intensity = Total manufacturing energy / Total produced units`; Unit `Units` is correct (a count, not energy).
- **Grounding:** J blank, appropriate for a raw count.
- **Implementation check:** **Cross-domain reuse (intentional, per brief).** Parent Metrics cell = `EC5\nEN41\nR222` — the same produced-units count feeds R222 (energy intensity, this domain), EC5 (CO₂ Cost Performance, Economic) and EN41 (water intensity, Environmental). In R222 it is the **denominator** of energy-per-unit; the description (a unit count over the referenced period) fits the per-unit-intensity denominator for all three parents. Unit `Units` (count) is the only non-kWh leaf in this batch and is correct — do **not** flag the unit mismatch, it is a count by design. No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor, non-obvious — worth a brief Comment per brief] R2-7 is the **one cross-domain raw input** in this batch: it is shared by EC5 (Economic) and EN41 (Environmental water intensity) as well as R222. Suggested Comment-cell note: "Shared denominator: also feeds EC5 (CO₂ cost) and EN41 (water intensity). Intentional cross-domain reuse — keep a single canonical produced-units figure." This is the only raw leaf here meriting a Comment flag.

### R2-8 — Logistics Energy Consumption  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total energy consumption for transportation and distribution of products. Includes reverse logistics."
- **Verdict:** CONSISTENT — text matches the **numerator** role in R223 `Logistics = Total energy consumption for logistics / Total energy inflow (Current)`.
- **Grounding:** J blank, appropriate.
- **Implementation check:** R223 (Logistics Energy Performance) children = `R2-8\nR2-9`. R2-8 = logistics energy → numerator; R2-9 = total energy inflow → denominator. Description mirrors R223's prose ("transportation and distribution… reverse logistics") verbatim — consistent. Unit kWh consistent with R2-9 denominator. Stages = M (note: parent R223 is tagged `S,D` shipping/distribution — see note). No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] Stages = `M` here while parent R223 is `S,D` and the metric is about transport/distribution; `S,D` (or adding D) would fit logistics better than `M`. Low priority — does not affect the value or the ratio.

### R2-9 — Total energy inflow (Current)  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of energy coming into the system's boundary to be used throughout the product's lifecycle."
- **Verdict:** CONSISTENT — serves a dual denominator role coherently; cites `SASB RT-EE-130a.1` (resolves, References.tsv line 99).
- **Grounding:** `SASB RT-EE-130a.1` (J) resolves to a Label (SASB Electrical & Electronic Equipment energy disclosure) and the code is valid; per the lighter-pass stance no quote is pulled for a raw author-supplied inflow figure. Code valid, not orphan.
- **Implementation check:** Parent Metrics = `R223\nR224`. In R223 it is the **denominator** (`/ Total energy inflow (Current)`); in R224 it is the **Current** term of `Reduction = [Total energy inflow] Current / Previous` (R224 children = `R2-9\nR2-10`). Both roles fit "total energy coming into the system boundary." Unit kWh consistent with R2-8 and R2-10. Stages = S. No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** SASB code resolves; keep. The "(Current)" qualifier in the name is what distinguishes it from R2-10 — see R2-10.

### R2-10 — Total energy inflow (Previous)  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of energy coming into the system's boundary to be used throughout the product's lifecycle."
- **Verdict:** DRIFTED (hygiene) — the description is **identical to R2-9's** and does not encode the "(Previous)" timeframe that distinguishes this row. The name and its R224 role both say this is the **prior-period** inflow, but the Description never says so. Substance/Unit are fine; only the text fails to capture the timeframe distinction.
- **Grounding:** `SASB RT-EE-130a.1` (J) resolves (References.tsv line 99); code valid. No quote for a raw supplied figure.
- **Implementation check:** Parent Metrics = `R224` only. In R224 `Reduction = [Total energy inflow] Current / Previous`, R2-10 is the **Previous** denominator term (R224 children = `R2-9\nR2-10`; R2-9 = Current, R2-10 = Previous). The name correctly carries "(Previous)", but the Description text is copy-pasted from R2-9 and omits the earlier-timeframe meaning. Unit kWh consistent with R2-9. Stages = S.
- **Proposed revision (C):** "The total amount of energy coming into the system's boundary throughout the product's lifecycle, **measured in the previous (baseline) timeframe** — used as the comparison baseline for the energy-inflow reduction in R224."
- **Notes:** [minor] Pure description-hygiene drift: two leaves that differ only by timeframe must not share identical prose, or the audit trail can't tell Current from Previous. Mirrors the R2-9 text plus the timeframe qualifier; no Unit/Formula/wiring change.

### R2-11 — Total manufacturing energy  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The amount of energy spent during the manufacturing or production phase."
- **Verdict:** CONSISTENT — text matches the **numerator** role in R222 `Intensity = Total manufacturing energy / Total produced units`.
- **Grounding:** J blank, appropriate.
- **Implementation check:** R222 (Energy Intensity Performance) children = `R2-11\nR2-7`, Formula `Intensity = Total manufacturing energy / Total produced units`. R2-11 = manufacturing energy → **numerator** (kWh); R2-7 = produced units → denominator (Units), giving kWh/unit intensity. Description matches the numerator role. Stages = M, consistent with "manufacturing/production phase." No description drift.
- **Proposed revision:** keep as-is.
- **Notes:** none. Numerator(R2-11 kWh)/denominator(R2-7 Units) pairing yields the kWh-per-unit intensity R222 intends — dimensionally coherent.

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| R2-1 | Total potential energy of outflow | UNVERIFIABLE | keep as-is |
| R2-2 | Generated energy derived from outflow | UNVERIFIABLE | keep as-is |
| R2-3 | Recirculated energy derived from outflow | UNVERIFIABLE | keep as-is |
| R2-4 | Stored energy derived from outflow | CONSISTENT | keep as-is (set empty stages → M) |
| R2-5 | Operational Output Energy | CONSISTENT | keep as-is (set empty stages → U) |
| R2-6 | Operational Input Energy | CONSISTENT | keep as-is (set empty stages → U) |
| R2-7 | Total produced units | CONSISTENT | keep as-is (add cross-domain Comment) |
| R2-8 | Logistics Energy Consumption | CONSISTENT | keep as-is |
| R2-9 | Total energy inflow (Current) | CONSISTENT | keep as-is |
| R2-10 | Total energy inflow (Previous) | DRIFTED | rewrite to add the "previous/baseline timeframe" qualifier |
| R2-11 | Total manufacturing energy | CONSISTENT | keep as-is |

**Counts (11 leaves):** CONSISTENT 7 (R2-4, R2-5, R2-6, R2-7, R2-8, R2-9, R2-11);
UNVERIFIABLE 3 (R2-1, R2-2, R2-3); DRIFTED 1 (R2-10). ADAPTED 0. No SOURCE-NOT-FOUND —
the only cited codes (`Module D - EN15804+A2` on R2-2; `SASB RT-EE-130a.1` on R2-9/R2-10)
both resolve in References.tsv and their PDFs exist in the corpus.

**Gap-fix verifications requested in the brief:**
- **R2-4** Unit=kWh, Level=5 → **confirmed**; description ("energy stored from the generated
  energy") matches a stored-energy figure in kWh and its R213 stored/generated numerator role.
- **R2-5 (Output) / R2-6 (Input)** → **confirmed** as the numerator/denominator of R221's
  `Performance = R2-5/R2-6` (Output/Input) efficiency ratio; both kWh, ratio dimensionless.
- **R2-7 produced units → cross-domain** → **confirmed**; Parent Metrics = `EC5\nEN41\nR222`.
  Treated as intentional reuse, not an error; Unit `Units` (a count) is correct, not flagged.

**Rows needing a decision / proposed adjacent fixes (most severe first):**
1. **[minor] R2-10 description** is identical to R2-9 and omits the "(Previous)" timeframe —
   the one genuine description drift; rewrite per the proposed text so the baseline term is
   self-documenting.
2. **[minor] R2-7 Comment (non-obvious)** — add a short cross-domain note that it also feeds
   EC5 and EN41 (the only raw leaf in this batch warranting a Comment flag).
3. **[minor] Empty Product Life Cycle Stages** on R2-4 (→ M), R2-5 (→ U), R2-6 (→ U) — set to
   match siblings/parent for consistency; does not affect any value.
4. **[minor] R2-8 stages** = `M` while it is a logistics/transport input under R223 (`S,D`);
   consider `S,D`/adding D. Low priority.

**Limits of this run:** This was a deliberate lighter pass on raw author-defined inputs;
per the conservative + lighter-pass instruction no verbatim literature quotes were pulled
for raw kWh figures whose values are author-supplied (the two cited codes were checked only
for *resolution*, not concept-grounded with quotes). Verdicts rest on
description-vs-Unit/Formula/parent-wiring consistency read from
`snapshot/Resource Efficiency.tsv`. Parent sub-scores R21/R211/R212/R213/R22/R221/R222/R223/R224
were inspected only as far as needed to confirm each leaf's numerator/denominator role; their
own descriptions, weights, and Min/Max bands were not audited here. Cross-domain parents EC5
(Economic) and EN41 (Environmental) were confirmed to exist as wiring targets but their own
rows were not opened. No workbook cells were edited.


---

## R3 — Water Efficiency + R0 Domain Root

### R0 — Resource Efficiency Score  [Level 1, composite root, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the overall resource efficiency of the production based on the underlying metrics."
- **Current (I):** "Sum (weight * R1 + … + weight * R5)"
- **Verdict:** DRIFTED — *not* the description (which is fine for a root), but the **Formula
  text (col I)** is stale: it reads "Sum (weight * R1 + … + weight * R5)" while the current
  `Underlying Metrics` are **R1\nR2\nR3** only (Material, Energy, Water). There is no R4/R5
  in this domain. This is the same stale-root pattern flagged for EN0/EC0/C0 in the gap-fix
  pass — the formula cell enumerates children that no longer exist.
- **Grounding:** composite root — no single literature source expected; Reference cell is
  blank **by design** (a parent the author defines to aggregate its children). Verified
  internally: children R1, R2, R3 all exist as Level-2 rows with `Parent Metrics = R0`, each
  carrying a Reference Value weight of ≈0.3333 (R1=0.3333, R2=0.3333, R3=0.3334), summing to
  1.0 — consistent with a WEIGHTED_AVERAGE over three equally-weighted children.
- **Implementation check:** `Underlying Metrics = R1\nR2\nR3`; `Parent Metrics = None`;
  strategy WEIGHTED_AVERAGE; Unit %. Children R1/R2/R3 each exist and each names R0 as
  parent. Unit % is compatible with averaging three 0–1/% sub-scores. The only defect is the
  Formula text naming `R1 … R5`.
- **Proposed revision (C):** "Aggregates the product's overall resource efficiency into one
  score by combining its material efficiency (R1), energy efficiency (R2), and water
  efficiency (R3). Provides one figure to prioritize material-, energy-, and water-saving and
  circularity actions."
- **Proposed Formula text (I):** "Sum (weight * R1 + weight * R2 + weight * R3)"
- **Notes:**
  - [minor] Formula text drift: `R1 … R5` → `R1 + R2 + R3` (matches the three live children).
    Same stale-root class as EN0/EC0/C0.
  - Blank Reference (J) is correct for a composite root — not a defect.
  - Description currently says "of the production"; the children are product-life-cycle
    metrics, so "of the product" is the more accurate scope (minor wording).

---

## R3 — Water Efficiency Score (family parent)

### R3 — Water Efficiency Score  [Level 2, composite, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the efficiency of water resource utilization based on underlying metrics"
- **Current (I):** "Sum (weight * R31 + … + weight * R33)"
- **Verdict:** DRIFTED (mild) — the description is sound for a composite, but its three
  children (R31 savings, R32 consumption-reduction, R33 utilization-efficiency) are not named
  and the prose is generic. The **Formula text** "R31 + … + R33" *does* match the current
  children (R31\nR32\nR33), so unlike R0 there is no stale-grandchild drift here. Downgrading
  to DRIFTED only because the description is vaguer than its siblings (R1/R2 name their arms).
- **Grounding:** composite/parent — Reference cell blank by design. Concept halves grounded
  on the children's rows (ISO 14046 water footprint; GRI 303 / ESRS E3 water consumption,
  discharge, reuse — quotes under R31/R312/R32/R33 below).
- **Implementation check:** `Underlying Metrics = R31\nR32\nR33`; `Parent = R0`; strategy
  WEIGHTED_AVERAGE; weights R31=0.3333, R32=0.3333, R33=0.3334 (sum 1.0). Children all exist.
  Unit % consistent with averaging three sub-scores. No formula-text drift.
- **Proposed revision (C):** "Aggregates the product's water-efficiency performance into one
  score by combining its water-savings performance (R31, treatment + reuse), its water-
  consumption reduction over time (R32), and its water-utilization efficiency (R33, intake
  vs. discharge). Provides an overview for prioritizing water-saving and circular-water
  actions across the product's life cycle."
- **Notes:**
  - Blank Reference (J) is correct for a composite parent.
  - [minor] trailing-space / missing period in the current description ("underlying metrics"
    with no full stop).
  - Composite verdict could equally be read as CONSISTENT (the implementation is sound); the
    only action is an optional description sharpen to match the R1/R2 child-naming style.

---

## R31 — Water Savings Performance (sub-score)

### R31 — Water Savings Performance  [Level 3, composite, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures how performant the implemented efficiency measures for water treatment and the reuse of water derived from outflow."
- **Current (I):** "Sum (weight * R311 + weight * R312)"
- **Verdict:** CONSISTENT (composite; internal check) — the prose correctly describes a
  roll-up of a water-**treatment** share (R311) and a water-**reuse** share (R312), matching
  `Underlying = R311\nR312` and the Formula text. The sentence is grammatically incomplete
  ("how performant … the reuse of water" lacks a verb) — a hygiene fix, not a content drift.
- **Grounding:** composite — Reference blank by design. The two arms are grounded on the
  children: GRI 303-2 (treatment / effluent quality) and ESRS E3-4 / GRI 303 (recycling and
  reuse) — quotes under R311/R312.
  - GRI 303 p.7: "An organization can reduce its water withdrawal, consumption, discharge,
    and associated impacts through efficiency measures, such as water recycling and reuse,
    and process redesign … It can improve water quality through better treatment of water
    discharge." (`data/literature/GRI - Global Reporting Initiative/GRI 303_ Water and Effluents 2018.pdf`)
- **Implementation check:** Children R311, R312 both exist; strategy WEIGHTED_AVERAGE
  (each 0.5). Unit % compatible with averaging two 0–1 ratios. Both child concepts (treatment
  share, reuse share) map cleanly onto "water treatment" + "reuse of water derived from
  outflow." No formula-text drift.
- **Proposed revision (C):** "Measures how effective the product's water-recovery measures
  are by combining the share of outflow that is treated for reuse (R311) and the share of
  water that is actually recirculated back into the process (R312). Higher means more water
  is recovered and reused rather than discharged."
- **Notes:**
  - [minor] grammar: current sentence is a fragment ("how performant … the reuse of water
    derived from outflow") — fix in the revision above.
  - Blank Reference (J) is appropriate for a composite sub-score.

---

## R311 — Treated Water Share

### R311 — Treated Water Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of processed / treated waste water into usable water."
- **Current (I):** "Treated = Treated water from outflow / Total water outflow  →  (Treated - Min)/(Max - Min)"
- **Current (J):** `GRI 303-2`, `AM+22`
- **Verdict:** ADAPTED — a faithful product-level "treated-water share" ratio. The *concept*
  of treating discharge to a quality standard is grounded in GRI 303-2; the specific
  treated÷outflow **share ratio** is author-constructed (no standard supplies this datapoint),
  and the primary cited paper `AM+22` is **not present in the corpus** (file missing).
- **Grounding:**
  - GRI 303 p.10 (Disclosure 303-2, Management of water discharge-related impacts):
    "A description of any minimum standards set for the quality of effluent discharge, and
    how these minimum standards were determined …"
    (`data/literature/GRI - Global Reporting Initiative/GRI 303_ Water and Effluents 2018.pdf`)
  - GRI 303 p.13 (303-4 recommendation 2.4.2): "A breakdown of total water discharge to all
    areas in megaliters by level of treatment, and how the treatment levels were determined."
    (same file) — grounds "treated water" as a recognised, level-of-treatment quantity.
  - `AM+22` ("Assessing water circularity in cities", References.tsv line 50) — Label
    resolves, but **no PDF for it exists in `data/literature/Papers/`** → SOURCE-NOT-FOUND for
    the file. The treated/outflow share itself is therefore ungrounded by a retrievable source.
- **Implementation check:** Children R3-1 (Treated water from outflow, m³) and R3-2 (Total
  water outflow, m³) both exist and share unit m³, so the ratio is well-formed; Unit % via
  normalization (Min/Max seeded 0/1). Direction is **higher-is-better** (more treated water →
  higher score) and the formula `Treated/Total` increases with treatment — direction is
  correct, no flip needed. Formula text matches children. No implementation drift.
- **Proposed revision (C):** "Measures the share of the product's total water outflow (R3-2)
  that is treated to a reusable quality (R3-1): treated water ÷ total outflow. Higher means
  more of the process water is recovered to usable quality rather than discharged as waste."
- **Notes:**
  - [major] `AM+22` is cited but its PDF is **absent from the corpus** (Label exists in
    References.tsv, file does not). Treated as SOURCE-NOT-FOUND; the share ratio cannot be
    grounded to it. GRI 303-2 grounds only the *treatment-to-a-standard* concept, not the
    share construction — so the ratio remains author-defined.
  - Comment-cell (R) flag, ADAPTED + non-obvious: "Product-level treated-water share; GRI
    303-2 grounds treatment-to-quality-standard, but the treated÷outflow share is
    author-defined (AM+22 source not in corpus)."
  - Direction is correctly higher-is-better — no direction flag needed.

---

## R312 — Reused Water Share

### R312 — Reused Water Share  [Level 4, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of recirculated water back into the processes involved in the product's lifecycle."
- **Current (I):** "Reused = Recirculated water derived from outflow / Total water outflow  →  (Reused - Min)/(Max - Min)"
- **Current (J):** `ESRS E3-4`, `AM+22`
- **Verdict:** ADAPTED — a faithful product-level "reused-water share." This is the
  **best-grounded** water ratio in the family: ESRS E3-4 explicitly discloses "total water
  recycled and reused in m3," which is exactly this metric's numerator concept. The
  share-against-outflow construction is the author's adaptation; `AM+22` is again missing.
- **Grounding:**
  - ESRS E3 p.5 (Disclosure Requirement E3-4, §28): "The disclosure required by paragraph 26
    relates to own operations and shall include: (a) total water consumption in m3; … (c)
    total water recycled and reused in m3."
    (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E3 Delegated-act-2023-5303-annex-1_en.pdf`)
  - ESRS E3 p.6 (footnote on E3-4): "('Water usage and recycling', 2. Weighted average
    percentage of water recycled and reused by investee companies)." (same file) — grounds the
    **percentage** framing of recycled/reused water directly.
  - GRI 303 p.7: "… efficiency measures, such as water recycling and reuse, and process
    redesign …" (`…/GRI 303_ Water and Effluents 2018.pdf`)
  - `AM+22` — SOURCE-NOT-FOUND (file absent; see R311).
- **Implementation check:** Children R3-2 (Total water outflow, m³) and R3-3 (Recirculated
  water derived from outflow, m³) both exist, share unit m³; ratio well-formed; Unit % via
  normalization (Min/Max 0/1). Direction higher-is-better, formula `Recirculated/Outflow`
  increases with reuse — direction correct. No implementation drift.
- **Proposed revision (C):** "Measures the share of the product's total water outflow (R3-2)
  that is recirculated back into its life-cycle processes (R3-3): reused water ÷ total
  outflow. Higher means more process water is reused rather than discharged, reducing fresh
  withdrawal."
- **Notes:**
  - `ESRS E3-4` is a strong, correct citation — keep it (org-level "total water recycled and
    reused", adapted to a product-level share).
  - [minor] `AM+22` PDF absent (SOURCE-NOT-FOUND) — the metric is still grounded via ESRS E3-4,
    so this is not a blocker; either obtain the AM+22 PDF or rely on ESRS E3-4 as primary.
  - Comment-cell (R) flag, ADAPTED + non-obvious: "Product-level reused-water share; adapts
    ESRS E3-4 'total water recycled and reused (m3)' to a share of outflow. Band author-defined."
  - Direction correct (higher-is-better) — no flag needed.

---

## R32 — Water Consumption Reduction

### R32 — Water Consumption Reduction  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the amount of water consumed throughout the product's lifecycle and compares the value with a previous timeframe. It evaluates any improvement of water utilization."
- **Current (I):** "Reduction = [Total process water consumption] Current / Previous  →  (Reduction - Min)/(Max - Min)"
- **Current (J):** `AM+22`
- **Verdict:** DRIFTED — **direction defect.** The formula `Reduction = Current / Previous`
  is a ratio that **rises when consumption rises** (Current > Previous → ratio > 1) and falls
  when consumption is reduced. Under the family's higher-is-better normalization, that scores
  **backwards**: a product that *increased* water use would score higher than one that cut it.
  The name "Water Consumption **Reduction**" and the objective "track continuous improvement"
  both imply lower-is-better, so the encoded ratio contradicts the intended direction. This is
  the same class of bug fixed for R12/EN43 (a reduction/waste arm that was never complemented).
- **Grounding:**
  - ESRS E3 p.5 (E3-4 §28a): "total water consumption in m3" — grounds the consumption
    quantity being tracked.
    (`…/ESRS E3 Delegated-act-2023-5303-annex-1_en.pdf`)
  - GRI 303 p.16 (Disclosure 303-5 Water consumption): "Total water consumption from all areas
    in megaliters." (`…/GRI 303_ Water and Effluents 2018.pdf`) — grounds the consumption
    figure (R3-4). The *reduction-over-time ratio* itself is author-constructed.
  - ISO 14046 p.16 (Note 2): "The term 'water consumption' is often used to describe water
    removed from, but not returned to, the same drainage basin. Water consumption can be
    because of evaporation, transpiration, integration into a product, or release into a
    different drainage basin or the sea." (`data/literature/ISO 14XXX/ISO-14046.pdf`)
  - `AM+22` — SOURCE-NOT-FOUND (file absent).
- **Implementation check:** Child R3-4 (Total process water consumption, m³) exists; only one
  child is wired, with "Previous" being a supplied earlier-timeframe value (Potential Reference
  Values: "Value of another Timeframe"). Strategy NORMALIZED_RATIO, Unit %. **No Min/Max seed
  shown** (unlike R311/R312/R33, R32 has no `0/1` Comment and no Target Min/Max in cols), so
  the normalization band is unset — combined with the wrong-direction ratio this is a real
  scoring risk.
- **Proposed revision (C):** "Measures the reduction in the product's total process-water
  consumption (R3-4) relative to an earlier timeframe. Higher means the product now consumes
  less water than before. (Computed so that a fall in consumption raises the score.)"
- **Proposed Formula text (I) — direction fix:** flip to a reduction fraction, e.g.
  "Reduction = 1 - (Current / Previous)" (positive when Current < Previous), then
  "(Reduction - Min)/(Max - Min)" — mirroring R224 (energy) and R33's `1 - (…)` pattern, so
  lower consumption → higher score. **Decision needed (see below).**
- **Notes:**
  - [blocker] Direction: as written `Current/Previous` rewards *higher* consumption under
    higher-is-better normalization. Recommend `1 - Current/Previous` (or `(Previous-Current)/
    Previous`) so the metric matches its name and objective. This is the headline finding of
    the batch and mirrors the EN43 / R12 direction fixes already applied in the gap-fix pass.
  - [minor] Min/Max band appears unseeded for R32 (no 0/1 Comment, no Target Min/Max), unlike
    its siblings — confirm the normalization band so the (now-flipped) ratio scores sensibly.
  - [minor] `AM+22` PDF absent (SOURCE-NOT-FOUND). Concept (consumption tracked over time) is
    groundable in ESRS E3-4 / GRI 303-5 / ISO 14046 — consider adding `ESRS E3-4` or
    `GRI 303-5` to col J so the row is auditable without AM+22.
  - Comment-cell (R) flag: "Reduction ratio — flipped to 1 − Current/Previous so lower
    consumption scores higher (lower-is-better quantity, higher-is-better score)."

---

## R33 — Water Utilization Efficiency

### R33 — Water Utilization Efficiency  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the ratio between the inflow of water for consumption and the water waste discharged out of the system's boundary. It evaluates the overall efficiency of the product's water lifecycle."
- **Current (I):** "Ratio = 1 - (Total water discharge / Total process water consumption)  →  (Ratio - Min)/(Max - Min)"
- **Current (J):** `AM+22`
- **Verdict:** CONSISTENT (direction correct) — the formula `1 - (discharge / consumption)`
  is **already** the correct higher-is-better form: more discharge → lower score, less
  discharge per unit consumed → higher score. The description, however, has a small wording
  mismatch: it says "the ratio between inflow … and water waste discharged," but the formula
  is `1 − discharge/consumption` (a retention/efficiency share), not a raw inflow:discharge
  ratio. Sharpen the prose to match the `1 − discharge/consumption` form.
- **Grounding:**
  - GRI 303 p.13 (Disclosure 303-4 Water discharge): "Total water discharge to all areas in
    megaliters …" (`…/GRI 303_ Water and Effluents 2018.pdf`) — grounds the discharge
    numerator (R3-5).
  - GRI 303 p.16 (303-5): "Total water consumption from all areas in megaliters." (same file)
    — grounds the consumption denominator (R3-4).
  - ISO 14046 p.46: "The allocation principles and procedures in 5.3.3.2 also apply to reuse
    and recycling situations when used in water footprint assessment." (`data/literature/ISO 14XXX/ISO-14046.pdf`)
    — grounds treating reuse/retained water within the product water footprint.
  - `AM+22` — SOURCE-NOT-FOUND (file absent).
- **Implementation check:** Children R3-4 (Total process water consumption, m³) and R3-5
  (Total water discharge, m³) both exist, share unit m³; `1 - discharge/consumption` is a 0–1
  efficiency share (when discharge ≤ consumption); Unit % via normalization (Min/Max 0/1).
  Direction correct. Note: if discharge can exceed consumption the raw ratio can go negative
  pre-normalization — worth a sanity bound, but not a drift.
- **Proposed revision (C):** "Measures how efficiently the product retains the water it
  consumes, as one minus the share of process-water consumption (R3-4) that leaves the system
  boundary as discharge (R3-5): 1 − (water discharge ÷ water consumption). Higher means less
  of the consumed water is lost as waste-water discharge."
- **Notes:**
  - Direction is **correct** as implemented (`1 − discharge/consumption`) — explicitly noted
    because the brief asked to check R31/R32/R33 directions; only **R32** has the direction
    defect, R33 does not.
  - [minor] description currently calls it "the ratio between inflow … and discharge"; the
    formula is a retention share `1 − discharge/consumption` — align the wording (revision
    above).
  - [minor] `AM+22` PDF absent (SOURCE-NOT-FOUND); concept groundable via GRI 303-4 / 303-5 —
    consider adding `GRI 303-4`/`GRI 303-5` to col J.
  - Comment-cell (R) flag, ADAPTED + non-obvious: "Water-retention efficiency; discharge and
    consumption grounded in GRI 303-4/303-5, the 1 − discharge/consumption construction is
    author-defined."

---

## R3 leaves (raw inputs)

### R3-1 — Treated water from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of water outflow that is undergoing treatment to recover its quality up to a certain standard."
- **Current (J):** `AM+22`
- **Verdict:** UNVERIFIABLE — accurate raw-input definition (numerator of R311), but the only
  cited source (`AM+22`) has **no PDF in the corpus**. The concept of treating discharge to a
  quality standard is grounded in GRI 303-2 (below), but the row cites only AM+22.
- **Grounding:** GRI 303 p.10 (303-2): "A description of any minimum standards set for the
  quality of effluent discharge …"; GRI 303 p.13 (recommendation 2.4.2): "breakdown of total
  water discharge … by level of treatment." (`…/GRI 303_ Water and Effluents 2018.pdf`) —
  grounds "treated to a standard" generally. `AM+22` itself SOURCE-NOT-FOUND.
- **Implementation check:** Raw leaf, no formula; Parent R311; unit m³ consistent with R3-2
  for the R311 ratio. Description matches numerator role. No drift.
- **Proposed revision (C):** keep as-is. (Optional: append "(numerator of R311)" for wiring
  clarity.)
- **Notes:** [minor] cited `AM+22` file absent; consider adding `GRI 303-2` (treatment-to-
  standard) to col J for an auditable ground.

### R3-2 — Total water outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total volume of water output throughout the product's lifecycle still within the system's boundaries e.g. resulting water waste from manufacturing."
- **Current (J):** `AM+22`
- **Verdict:** UNVERIFIABLE — accurate raw denominator (shared by R311 and R312), but cited
  source `AM+22` is absent from the corpus. "Total water outflow within the system boundary"
  is the author's framing (distinct from GRI 303-4 "water discharge," which is outflow that
  *leaves* the boundary) — so GRI 303 does not directly ground this internal-outflow concept.
- **Grounding:** No retrievable source matches "outflow still within the system boundary."
  GRI 303-4 (p.13, quote under R3-5) covers *discharge out of* the boundary, which is R3-5,
  not R3-2. `AM+22` SOURCE-NOT-FOUND. The metric is author-defined.
- **Implementation check:** Raw leaf; Parent R311, R312; unit m³; denominator of both R311
  and R312 ratios. Consistent. No drift.
- **Proposed revision (C):** keep as-is. (Optional clarification: distinguish from R3-5
  "discharge out of boundary" — R3-2 is the total recoverable outflow pool, R3-5 is the
  portion that leaves as waste.)
- **Notes:** [minor] `AM+22` absent (SOURCE-NOT-FOUND); the within-boundary-outflow concept
  is genuinely author-defined, so UNVERIFIABLE is the correct status (not a defect).

### R3-3 — Recirculated water derived from outflow  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of water outflow that is reused or reutilized back as inflow in the product's lifecycle processes."
- **Current (J):** `GRI 306-4`
- **Verdict:** DRIFTED (citation) — the *description* is accurate (numerator of R312, reused
  water), but the cited code `GRI 306-4` is the **Waste** standard's "Waste diverted from
  disposal" disclosure, measured in **metric tons of waste**, not a water (m³) volume. The
  correct water grounding for recycled/reused water is **ESRS E3-4** ("total water recycled
  and reused in m3") and/or **GRI 303** (recycling and reuse), not GRI 306-4.
- **Grounding:**
  - GRI 306 p.13 (Disclosure 306-4): "Waste diverted from disposal … Total weight of waste
    diverted from disposal in metric [tons]." (`…/GRI 306_ Waste 2020.pdf`) — this is **waste
    mass**, mismatched to a water-volume metric.
  - Correct ground — ESRS E3 p.5 (E3-4 §28c): "total water recycled and reused in m3."
    (`…/ESRS E3 Delegated-act-2023-5303-annex-1_en.pdf`)
  - GRI 303 p.7: "… water recycling and reuse …" (`…/GRI 303_ Water and Effluents 2018.pdf`)
- **Implementation check:** Raw leaf; Parent R312; unit m³ consistent with R3-2 for the R312
  ratio. Description matches numerator role. The defect is purely the citation domain (waste
  vs. water).
- **Proposed revision (C):** keep as-is (definition is correct).
- **Proposed citation fix (J):** replace `GRI 306-4` with `ESRS E3-4` (and optionally
  `GRI 303` / `AM+22` if AM+22 is later added). GRI 306-4 measures diverted waste mass, not
  reused water volume.
- **Notes:** [major] `GRI 306-4` (waste-mass diversion) is the wrong topic for a water-volume
  reuse metric; `ESRS E3-4` is the matching code and already cited on R312. Same mis-citation
  also appears on R1-2 (Recirculated byproduct) where 306-4 *is* appropriate (that one is a
  mass flow) — so this is a copy-over to a water row, not a systemic error.

### R3-4 — Total process water consumption  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total volume of water intake needed throughout the product's process cycle."
- **Current (J):** `ESRS E3-4`, `GRI 303-5`, `SASB RT-CP-140a.1`, `AM+22`
- **Verdict:** ADAPTED — accurate raw consumption denominator (feeds R32 and R33); well
  grounded by ESRS E3-4 and GRI 303-5. One citation is wrong-topic: `SASB RT-CP-140a.1` is the
  *qualitative water-risk discussion* code, not the quantitative water-consumption datapoint
  (which is `RT-CP-130a.1` in this PDF).
- **Grounding:**
  - GRI 303 p.16 (Disclosure 303-5): "Total water consumption from all areas in megaliters."
    (`…/GRI 303_ Water and Effluents 2018.pdf`)
  - ESRS E3 p.5 (E3-4 §28a): "total water consumption in m3." (`…/ESRS E3 …annex-1_en.pdf`)
  - ISO 14046 p.16 (Note 2): "water consumption … water removed from, but not returned to, the
    same drainage basin …" (`data/literature/ISO 14XXX/ISO-14046.pdf`)
  - SASB C&P p.6 / p.16: "RT-CP-130a.1 Water Management (1) Total water withdrawn, (2) total
    water consumed …"; and "RT-CP-140a.1. Description of water management risks and discussion
    of strategies and practices to mitigate those risks" (Discussion and Analysis).
    (`data/literature/SASB - Sustainability Account Standards Board/RT-CP-containers-and-packaging-standard_en-gb.pdf`)
    → the **quantitative** water-consumed datapoint is **RT-CP-130a.1**, not 140a.1.
- **Implementation check:** Raw leaf; Parents R32, R33; unit m³ consistent with R3-5 (R33) and
  used as R32's tracked quantity. Description ("water intake … process cycle") matches the
  consumption concept. No description drift.
- **Proposed revision (C):** keep as-is. (Optional ISO-14046 alignment: "Total process water
  consumed across the product's life cycle — water withdrawn and not returned to the same
  basin.")
- **Notes:** [major] citation: `SASB RT-CP-140a.1` is the water-risk *discussion* code; the
  quantitative "total water consumed" datapoint is `RT-CP-130a.1`. Either swap to
  `SASB RT-CP-130a.1` or drop the SASB token (ESRS E3-4 + GRI 303-5 already ground it). Note
  `RT-CP-130a.1` does exist as a Label in References.tsv (line 96). [minor] `AM+22` PDF absent.

### R3-5 — Total water discharge  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total volume of water discharged out of the process' system boundary e.g. waste water discharged into an external water waste management system or lake."
- **Current (J):** `GRI 303-4`, `AM+22`
- **Verdict:** ADAPTED — accurate raw discharge numerator (feeds R33); directly grounded by
  GRI 303-4. The product-level adaptation (product boundary vs. org facility) is the only
  divergence.
- **Grounding:** GRI 303 p.13 (Disclosure 303-4 Water discharge): "Total water discharge to
  all areas in megaliters, and a breakdown of this total by the following types of destination
  … Surface water; Groundwater; Seawater; Third-party water …"
  (`…/GRI 303_ Water and Effluents 2018.pdf`) — "lake / external system" in the description
  maps to GRI's surface-water / third-party destinations. `AM+22` SOURCE-NOT-FOUND.
- **Implementation check:** Raw leaf; Parent R33; unit m³ consistent with R3-4 for the R33
  ratio. Description matches the discharge-out-of-boundary concept. No drift.
- **Proposed revision (C):** keep as-is.
- **Notes:** `GRI 303-4` is a correct, tight citation — keep. [minor] `AM+22` PDF absent
  (SOURCE-NOT-FOUND); GRI 303-4 already grounds the row, so not a blocker.

---

## Batch summary

**Counts (12 rows):** CONSISTENT 2 (R31, R33) · DRIFTED 4 (R0 formula text, R3 description,
R32 direction, R3-3 citation) · ADAPTED 4 (R311, R312, R3-4, R3-5) · UNVERIFIABLE 2 (R3-1,
R3-2). (R0 and R3 are composite roots/parents whose *descriptions* are sound; their DRIFTED
verdict is for adjacent Formula-text / wording drift, not the prose itself.)

**Gap-fix context verified:**
- **R0 is a WEIGHTED_AVERAGE of R1/R2/R3** — confirmed (children exist, parents point back,
  weights ≈⅓ each summing to 1.0). The **Formula text is stale** ("R1 … R5"); it should read
  "R1 + R2 + R3". Same class as EN0/EC0/C0.
- **R31/R32/R33 direction check:** R311, R312, R33 encode direction **correctly**
  (higher-is-better; R33 already uses `1 − discharge/consumption`). **R32 is the exception** —
  `Reduction = Current / Previous` rewards *higher* consumption under higher-is-better
  normalization; it must be flipped (`1 − Current/Previous`) to match its name/objective.

**Proposed description rewrites (col C):** R0, R3 (sharpen to name children), R31 (grammar +
children), R311, R312, R32, R33 (sharpen to match formula). Leaves R3-1…R3-5 keep their text
(definitions accurate; fixes are citations, not prose).

**Proposed adjacent-cell fixes:**
- [minor] **R0 Formula (I):** "Sum (weight * R1 + … + weight * R5)" → "Sum (weight * R1 +
  weight * R2 + weight * R3)".
- [blocker] **R32 Formula (I):** flip `Current / Previous` → `1 - (Current / Previous)` (or
  `(Previous − Current)/Previous`) so lower consumption scores higher; confirm Min/Max band.
- [major] **R3-3 Reference (J):** `GRI 306-4` (waste mass) → `ESRS E3-4` (water recycled/reused).
- [major] **R3-4 Reference (J):** `SASB RT-CP-140a.1` (water-risk discussion) → `SASB
  RT-CP-130a.1` (quantitative water withdrawn/consumed), or drop the SASB token.
- [minor] **Comment (R) flags** (non-obvious adaptations only): R311 (treated-share author-
  defined, AM+22 missing), R312 (adapts ESRS E3-4 recycled/reused), R32 (direction flip note),
  R33 (retention-efficiency, author construction).

**Decisions needed from you:**
1. **R32 direction (blocker).** Confirm flipping to `1 − Current/Previous` (recommended;
   mirrors R224 energy and R33). As-is the metric scores backwards. Also seed/confirm its
   Min/Max band (currently appears unset, unlike R311/R312/R33).
2. **R3-3 citation (major).** Approve replacing `GRI 306-4` (waste-mass diversion) with
   `ESRS E3-4` (water recycled/reused, m³) — the matching water code.
3. **R3-4 SASB code (major).** Approve swapping `SASB RT-CP-140a.1` → `RT-CP-130a.1`, or
   dropping SASB (ESRS E3-4 + GRI 303-5 already ground it).
4. **R0 / R3 Formula-text refresh (minor).** Approve "R1+R2+R3" on R0; R3's "R31…R33" already
   matches and needs no change.

**SOURCE-NOT-FOUND codes:** `AM+22` ("Assessing water circularity in cities", References.tsv
line 50) — the **Label resolves** in References.tsv but **no PDF exists** in
`data/literature/Papers/` (verified by `find`/`ls`). It is the primary/only citation on R311,
R32, R3-1, R3-2 and a secondary on R312, R33, R3-4, R3-5 — so every water ratio that leans on
AM+22 is, for those tokens, ungrounded against a retrievable file. R312/R33/R3-4/R3-5 are
independently grounded (ESRS E3-4 / GRI 303-4/-5); R311/R32/R3-1/R3-2 rely on AM+22 and are
therefore ADAPTED/UNVERIFIABLE pending the file. Recorded, not substituted.

**Limits of this run:** Grounding quotes are confined to the files actually opened (ISO 14046,
GRI 303, GRI 306, ESRS E3, EN15804+A2, SASB RT-CP). I did **not** read the AM+22 paper (absent
from the corpus). I did not audit weights numerically beyond confirming R1/R2/R3 sum to ~1.0
and R311/R312 and R31/R32/R33 each carry sibling weights; I did not verify Min/Max band values
except to note R32 appears unseeded. Cross-domain parents (R0's role as a sibling of EN0/EC0/C0
under any global root) were not audited. The SASB 130a.1-vs-140a.1 distinction is read from
p.6 and p.16 of the one SASB C&P PDF; I did not exhaustively map every SASB topic code.
