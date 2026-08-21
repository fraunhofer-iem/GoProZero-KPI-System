# EN4 Water-Footprint Phase Rows — Literature Cross-Check

Scope: **EN441, EN442, EN443, EN444, EN445** (the five "… Water Footprint Ratio" phase
rows). Context read but not individually audited: parent **EN44** (Lifecycle Water
Footprint Ratio, WEIGHTED_AVERAGE), grandparent **EN4** (Water Footprint Score), and the
type-children **EN4-1/EN4-2/EN4-3** (blue/green/gray) plus **EN4-4** (Absolute Water
Footprint). Source: `snapshot/Environmental Impact.tsv`.

## Summary

| Row | Indicator | Verdict | Core problem |
|-----|-----------|---------|--------------|
| EN441 | Sourcing Water Footprint Ratio | UNSUPPORTED (under-specified) | Children are water *types*, not a sourcing-stage input |
| EN442 | Production Water Footprint Ratio | UNSUPPORTED (under-specified) | Same; no production-stage input |
| EN443 | Distribution Water Footprint Ratio | UNSUPPORTED (under-specified) | Same; no distribution-stage input |
| EN444 | Use & Maintenance Water Footprint Ratio | UNSUPPORTED (under-specified) | Same; no use-stage input |
| EN445 | End-of-Life Water Footprint Ratio | UNSUPPORTED (under-specified) | Same; no EoL-stage input |

All five share one design defect, so the assessment is shared; per-row recommendations differ only in which stage-specific input must be supplied.

The root cause is a **conflation of two orthogonal axes**: water *type* (blue/green/gray) and *life-cycle stage* (A/B/C). The sources confirm these are independent dimensions, and that per-stage water footprints require per-stage inputs — which the model does not have.

---

## The two-axis finding (applies to all five rows)

**Axis 1 — life-cycle stage is the correct decomposition, and stage footprints are summable.**
ISO 14046 states the water footprint is modular by life-cycle stage:

- `data/literature/ISO 14XXX/ISO-14046.pdf` p.11: *"is modular (i.e. the water footprint of different life cycle stages can be summed to represent the water footprint)"*
- p.26: *"the water footprint assessment may be restricted to one or several life cycle stages."*
- p.34: *"Omitted life cycle stages, processes, inputs or outputs shall be clearly identified and the reasons … explained."*

EN 15804+A2 declares water **per information module** across the A/B/C/D life-cycle stages — the same modular structure as carbon:

- `data/literature/EPD/EN15804+A2.pdf` p.46: *"These additional environmental impact indicators shall be calculated and included in the project report for each module declared …"*
- p.48 (parameters describing resource use, per module): *"Net use of fresh water  m3"*
- p.47 lists the LCIA water indicator as *"Water (user) deprivation potential, deprivation-weighted water consumption (WDP)"* — a **single** water-consumption indicator reported per module, not a blue/green/gray split.

So a per-phase water footprint (EN441–445 by life-cycle stage) is a **legitimate construct** — but each phase needs its own stage-specific water input.

**Axis 2 — blue/green/gray are water *types*, an orthogonal axis, and none of the cited standards even use that terminology.**
The blue/green/gray scheme is the Water Footprint Network's (the `waterfootprintnetwork` code on EN4-1/2/3). Searching the cited standards:

- ISO 14046: no blue/green/gray terminology found. It frames water by **withdrawal vs. consumption** instead — p.16: *"water withdrawal … anthropogenic removal of water from any water body …"*; p.16: *"The term 'water consumption' is often used to describe water removed from, but not returned to, the same drainage basin."* Searches for "blue/green/grey/degradative/dilute/pollutant" returned only an unrelated "grey boxes" figure caption (p.54) and bibliography hits (p.75).
- GRI 303 decomposes water by **withdrawal / discharge / consumption** and by **source** (surface, ground, sea, produced, third-party), not by blue/green/gray and not by life-cycle stage — p.3 (disclosures 303-3/4/5); p.11: *"Total water withdrawal from all areas in megaliters, and a breakdown of this total by the following sources … Surface water; Groundwater; Seawater; Produced water; Third-party water."*
- ESRS E3 frames water as **water consumption** (DR E3-4) over operations and the up/downstream value chain — p.5: *"The undertaking shall disclose information on its water consumption performance …"*; p.2: *"It includes disclosure requirements on water consumption … as well as related information on water withdrawals and water discharges."* No blue/green/gray, no per-product-stage decomposition.
- TF+25 (`data/literature/Papers/TF+25-…macro-algae… .pdf`): an LCA water-footprint study, but "phase" hits are chemical phases (liquid/gas), and no blue/green/gray terminology was found (p.3–5).

**Conclusion on the modelling question (Q2):** "blue + green + gray summed" is a valid figure for a **water-type total of the whole product** (that is exactly what EN4-4 Absolute Water Footprint already computes: *"Sum of blue, green, gray water footprint"*). It is **not** a valid figure for a *single life-cycle phase*. By wiring every phase (EN441–445) to the same three type-children EN4-1/2/3, the engine necessarily sets every phase equal to the whole-product total — which is why it self-flagged `needs_review`. The model is **missing per-phase water inputs**; it has substituted the type axis for the stage axis.

**Min/Max (Q3):** No benchmark or normalization range for a per-phase water ratio was found in any cited source. ISO 14046, GRI 303, ESRS E3 and EN 15804+A2 specify *what* to quantify (consumption/withdrawal/WDP per module), not a 0–1 min–max scaling. The `(Actual - Min)/(Max - Min)` normalization is an **author construct** with no literature anchor; Min/Max should be set from the product's own target/benchmark policy, not from a standard. Record as NOT-CHECKABLE for the normalization endpoints specifically.

---

## Per-row blocks

### EN441 Sourcing Water Footprint Ratio
- Verdict: **UNSUPPORTED (under-specified)** — see two-axis finding.
- Reference(s): none cited on the row itself; inherits EN4's `ESRS E2-4 / GRI 303 / ISO 14046 / ISO 14044` and children's `waterfootprintnetwork / TF+25`.
- Evidence: ISO 14046 p.11, p.26 (stage modularity); EN15804 p.48 ("Net use of fresh water m3" per module). No source supports equating a sourcing-stage footprint with blue+green+gray of the whole product.
- Assessment: The *concept* (water footprint of raw-material procurement, life-cycle stage A1–A3 / module "S") is sound and standard-supported. The *wiring* is wrong: EN4-1/2/3 are whole-product type totals, so `Actual = blue+green+gray` ≠ sourcing-stage water.
- Issue: **[major]** Children are water types, not a sourcing-stage input.
- Recommendation: **(c) flag under-specified.** Missing input: *sourcing-stage water consumption* (m3, life-cycle stage S / EN15804 A1–A3). Re-model so EN441's `Actual` reads a sourcing-stage water figure.

### EN442 Production Water Footprint Ratio
- Verdict: **UNSUPPORTED (under-specified)**.
- Evidence: as above (ISO 14046 p.11/p.26; EN15804 p.48; EN15804 p.6 module map A4–A5/B/C).
- Assessment: Concept valid (manufacturing/assembly stage, module "M"). Same type-vs-stage conflation.
- Issue: **[major]** No production-stage water input.
- Recommendation: **(c) flag under-specified.** Missing input: *production-stage water consumption* (m3, stage M / EN15804 A3 manufacturing).

### EN443 Distribution Water Footprint Ratio
- Verdict: **UNSUPPORTED (under-specified)**.
- Evidence: as above.
- Assessment: Concept valid (distribution stage, module "D" / EN15804 A4). Same conflation.
- Issue: **[major]** No distribution-stage water input.
- Recommendation: **(c) flag under-specified.** Missing input: *distribution-stage water consumption* (m3, stage D / EN15804 A4).

### EN444 Use and Maintenance Water Footprint Ratio
- Verdict: **UNSUPPORTED (under-specified)**.
- Evidence: ISO 14046 p.11/p.26; EN15804 p.6 (B1–B7 use-stage modules — the use stage is where operational water typically dominates).
- Assessment: Concept valid (use/maintenance stage, module "U" / EN15804 B). Same conflation. This is the stage most likely to carry real water consumption for many products, so a correct per-stage input matters most here.
- Issue: **[major]** No use-stage water input.
- Recommendation: **(c) flag under-specified.** Missing input: *use & maintenance water consumption* (m3, stage U / EN15804 B1–B7).

### EN445 End-of-Life Water Footprint Ratio
- Verdict: **UNSUPPORTED (under-specified)**.
- Evidence: ISO 14046 p.11/p.26; EN15804 p.6 (C1–C4 end-of-life modules).
- Assessment: Concept valid (EoL stage, module "E" / EN15804 C). Same conflation.
- Issue: **[major]** No EoL-stage water input.
- Recommendation: **(c) flag under-specified.** Missing input: *end-of-life water consumption* (m3, stage E / EN15804 C1–C4).

---

## Reference-integrity findings (check A)

All checked against `snapshot/References.tsv` Labels.

- **EN4** cites `ESRS E2-4`, `GRI 303`, `ISO 14046`, `ISO 14044`. **None** of these resolve to a Label in References.tsv. The only related Labels present are `EN 15804`, `ESRS E1`, `ISO 14067`, and a bare `GRI`. → 4 orphan codes. (The underlying *PDFs* do exist on disk — ISO-14046.pdf, ISO-14044.pdf, GRI 303 2018, ESRS E3 — but note EN4 cites ESRS **E2** while the water standard on disk is ESRS **E3**; ESRS E2 is the *Pollution* standard, so `ESRS E2-4` looks like a wrong-standard reference for a water KPI.)
- **EN4-1/EN4-2/EN4-3** cite `waterfootprintnetwork` and `TF+25`.
  - `waterfootprintnetwork`: no Label in References.tsv and **no PDF in the corpus** → SOURCE-NOT-FOUND. This is the actual origin of the blue/green/gray scheme; it is undocumented in the bibliography.
  - `TF+25`: no Label in References.tsv (orphan code), **but the paper file exists**: `data/literature/Papers/TF+25-Environmental impact and water footprint of biofuel production from macro-algae biomass based on life cycle assessment.pdf`. The paper is an LCA water-footprint study and does **not** define blue/green/gray; it is a weak/inappropriate anchor for those definitions.

## Internal-consistency findings (check B)

- **EN441–445 all list identical children EN4-1/EN4-2/EN4-3** with no phase-specific differentiation → guarantees every phase equals the whole-product total. (Confirmed in `snapshot/Environmental Impact.tsv` rows 36–40.)
- **Objective/Goal blank** on all five phase rows (EN441–445) where peers (EN41–EN43) have objectives → **[minor]** clarity gap.
- **EN44 formula vs. strategy mismatch:** EN44 Formula reads *"Avg (Stage Water Footprint)"* but Calculation Strategy is `WEIGHTED_AVERAGE_STRATEGY`. "Avg" and "weighted average" differ unless weights are equal; the five children carry equal Weight 0.2, so it is currently a plain average — reconcile the wording. **[minor]**
- **Unit:** EN441–445 Unit is `%` (normalized ratio output), consistent with NORMALIZED_RATIO; the underlying water inputs are `m3` (EN4-1/2/3, EN4-4). Unit of the ratio is fine; the defect is the *input wiring*, not the unit.
- **EN4-4 already is the correct type-sum total** (*"Sum of blue, green, gray water footprint"*, m3) — so EN441–445 are not duplicating it by intent, but as wired they each replicate it.

---

## Recommended actions (for an editor)

1. **Re-model EN441–445 (primary fix).** Replace the children EN4-1/EN4-2/EN4-3 on each phase row with a **phase-specific water input**:
   - EN441 ← sourcing-stage water consumption (m3; EN15804 A1–A3)
   - EN442 ← production-stage water consumption (m3; EN15804 A3)
   - EN443 ← distribution-stage water consumption (m3; EN15804 A4)
   - EN444 ← use & maintenance water consumption (m3; EN15804 B1–B7)
   - EN445 ← end-of-life water consumption (m3; EN15804 C1–C4)
   Create five new raw `m3` leaf metrics (one per stage) if they do not exist. Keep blue/green/gray (EN4-1/2/3) as the *type* axis feeding the whole-product total EN4-4 only.
   This makes EN44 = weighted/average over genuinely distinct stages and the parent EN4 meaningful.
2. **Do not keep `sum(blue,green,gray)` per phase.** That figure belongs to EN4-4 (whole product), not to any single stage. Remove the engine's `needs_review` only after rewiring.
3. **Set Min/Max from product target policy**, not from a standard — no source provides a normalization range (NOT-CHECKABLE).
4. **Fix references on EN4:** add proper Labels (or correct existing codes) for `ISO 14046`, `ISO 14044`, `GRI 303`; and verify `ESRS E2-4` — water lives in **ESRS E3** (E3-4 Water consumption), so this is likely a typo for `ESRS E3-4`.
5. **Document the blue/green/gray source:** add a `waterfootprintnetwork` Label to References.tsv (with a real citation/link) or replace it; add a `TF+25` Label pointing to the existing Papers PDF. Note TF+25 does not actually define blue/green/gray, so it should not be the authority for EN4-1/2/3 definitions.
6. **Fill EN441–445 Objective/Goal** and **reconcile EN44 "Avg" vs WEIGHTED_AVERAGE_STRATEGY** wording.

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | EN441–445 | All five phase rows wire to the same type-children EN4-1/2/3 (blue/green/gray), so every life-cycle phase equals the whole-product total; engine self-flagged `needs_review`. Conflates water-type axis with life-cycle-stage axis (ISO 14046 p.11 stages are summable & distinct; EN15804 p.48 water is per-module). | Re-model: feed each phase a stage-specific water-consumption input (m3) per EN15804 modules A/B/C; reserve blue+green+gray sum for whole-product total EN4-4. |
| 2 | major | EN4 | `ESRS E2-4` cited for a water KPI, but ESRS E2 is Pollution; water disclosures are in ESRS E3 (E3-4 Water consumption, p.5). Likely wrong standard. | Change to `ESRS E3-4` (verify intended datapoint). |
| 3 | major | EN4 | `ISO 14046`, `ISO 14044`, `GRI 303` cited but absent from References.tsv Labels (only `EN 15804`/`ESRS E1`/`ISO 14067`/bare `GRI` exist). PDFs exist on disk. | Add Label rows for ISO 14046, ISO 14044, GRI 303. |
| 4 | major | EN4-1/2/3 | `waterfootprintnetwork` is the de-facto authority for blue/green/gray but has no Label and no PDF in corpus (SOURCE-NOT-FOUND). | Add a documented Water Footprint Network reference (Label + link), or re-anchor definitions to a corpus source. |
| 5 | minor | EN4-1/2/3 | `TF+25` is an orphan code (no Label); the paper exists but is an algae-biofuel LCA that does not define blue/green/gray water. | Add a `TF+25` Label; do not rely on it for blue/green/gray definitions. |
| 6 | minor | EN44 | Formula says "Avg (Stage Water Footprint)" but strategy is WEIGHTED_AVERAGE_STRATEGY (children equal-weighted 0.2). | Reconcile wording to weighted average, or note weights are equal. |
| 7 | minor | EN441–445 | Objective/Goal blank where peer rows have one. | Add objectives. |

### SOURCE-NOT-FOUND codes
- `waterfootprintnetwork` — no Label, no file in `data/literature/`.

### Limits of this run
- I could not verify any **Min/Max benchmark range** for water-phase ratios: no cited source provides normalization endpoints (NOT-CHECKABLE; an author construct).
- ISO 14046 and EN15804 PDFs are bilingual (DE/EN) extractions; quotes are the English sentences as returned by the search tool. ISO 14044 itself was not opened (it is the generic LCA framework; the stage-modularity point is already established by ISO 14046 p.11 which is the water-specific standard).
- `ESRS E2-4` was assessed by elimination (E3 is the water standard on disk); I did not open ESRS E2 to confirm it lacks a per-product blue/green/gray water-stage requirement — the recommendation to switch to E3 stands on the E3 water-consumption evidence.
- I did not exhaustively read EN4-1/2/3 definitional text against a Water Footprint Network source because that source is not in the corpus.
