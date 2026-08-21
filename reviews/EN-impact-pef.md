# EN6 / EN7 / EN8 / EN9 — impact-category scores vs. LCIA/PEF literature

Scope: `snapshot/Environmental Impact.tsv` rows EN6 (+EN6-1..8), EN7 (+EN7-1..3),
EN8 (+EN8-1..3), EN9 (PEF Single Score). Question: are these scores' computation
(`WEIGHTED_AVERAGE_STRATEGY` over raw, mixed-unit impact results) supported by the cited
literature, and what is the correct approach?

Ground truth read this run: `ISO 14044` (LCIA optional-element clauses), `EN15804+A2`
(EF impact-category list + units), `ISO 14046` (water footprint). The PEF source the
metrics actually cite — `EUPEF+21` (Commission Recommendation (EU) 2021/2279) — and every
underlying-method paper (`USEtox2.0/2.1/2.2`, `AO+24`, `VZ+08`, `FR+00`, `BA+17`, `OL+02`,
`ReCiPe2008`, `ILCD2011`, `EUEP-FW`) have a row in `References.tsv` but **no PDF in
`data/literature/`** — see SOURCE-NOT-FOUND list at the end.

## Summary

| Metric | Verdict | Core finding |
|---|---|---|
| EN6 Pollution & Effects on Nature Score | CONTRADICTION (method) | Children are EF impact results in 8 different non-additive units; `WEIGHTED_AVERAGE` over raw values is not valid LCIA aggregation. Cited PEF source (EUPEF+21) absent. |
| EN6-1..EN6-8 | PARTIAL (adapted) / SOURCE-NOT-FOUND | Each is a genuine EF/EN15804 impact category with the correct unit (verified vs EN15804+A2), but each cited method PDF is absent. |
| EN7 Toxicity Score | CONTRADICTION (method) | CTUh + CTUh + CTUe averaged; same non-additivity defect. |
| EN7-1..EN7-3 | PARTIAL (adapted) / SOURCE-NOT-FOUND | Real EF toxicity categories with correct units (verified vs EN15804+A2 Table 4); USEtox PDFs absent. |
| EN8 Resource Deprivation Score | CONTRADICTION (method) | m³ + kg Sb eq + MJ averaged; non-additive. |
| EN8-1..EN8-3 | PARTIAL (adapted) / SOURCE-NOT-FOUND | Real EF resource categories, correct units (verified vs EN15804+A2); method PDFs absent. |
| EN9 PEF Single Score | CONTRADICTION (method) / SOURCE-NOT-FOUND | Formula text describes the correct normalize→weight→sum PEF sequence, but the metric is tagged `WEIGHTED_AVERAGE` and the workbook holds neither EF normalization nor weighting factors; EUPEF+21 absent. |

---

## Q1 — How a single weighted score across impact categories is built (the standard sequence)

The corpus confirms the canonical LCIA sequence in **ISO 14044** (printed pages 29–31;
PDF pages 33–35). Mandatory steps first:

- Classification — `data/literature/ISO 14XXX/ISO-14044.pdf` p.29: *"4.4.2.3 Assignment
  of LCI results to the selected impact categories (classification)"*.
- Characterization — p.30: *"4.4.2.4 Calculation of category indicator results
  (characterization) … the conversion of LCI results to common units and the aggregation
  of the converted results **within the same impact category**. This conversion uses
  characterization factors."* (Note: aggregation is only *within* one category.)

Then the **optional** steps that build a cross-category score:

- p.30: *"4.4.3.1 General … a) **normalization**: calculating the magnitude of category
  indicator results relative to reference information;"*
- p.31, 4.4.3.2.2: *"**Normalization** transforms an indicator result by dividing it by a
  selected reference value. Some examples of reference values are — the total inputs and
  outputs for a given area that may be global, regional, national or local, — the total
  inputs and outputs for a given area on a **per capita** basis or similar measurement…"*
- p.31, 4.4.3.1 c) / p.32, 4.4.3.4.1: *"**weighting**: converting and possibly aggregating
  indicator results across impact categories using numerical factors based on
  value-choices; data prior to weighting should remain available;"* and *"Weighting is the
  process of converting indicator results of different impact categories by using numerical
  factors based on value-choices. It may include aggregation of the weighted indicator
  results."*

So the confirmed sequence is: **characterized result (per category) → normalization
(divide by a per-category reference/normalization factor) → weighting (multiply by a
per-category weighting factor) → sum across categories.** Two hard constraints from the
same source:

- p.32, 4.4.3.4.2: weighting aggregates *"the indicator results or **normalized results**
  across impact categories"* — i.e. you weight-sum *after* normalization, never raw
  characterized results in mixed units.
- p.20 (caution that directly bears on EN9): *"It should be recognized that there is no
  scientific basis for reducing LCA results to a single overall score or number."* and
  *"data prior to weighting should remain available"* (p.31).

The PEF method (`EUPEF+21`, the cited source) is the operationalization of exactly this —
"normalized to a global average person's emissions over one year" is the EF per-capita
normalization step named in EN9's own formula. But `EUPEF+21` (and its Annex I
normalization/weighting factors) is **not in the corpus**, so the actual EF 3.x factor
values cannot be quoted or verified here.

## Q2 — Are EN6's children standard EF/PEF impact categories?

Yes — all eight map 1:1 to impact categories in **EN15804+A2** (which adopts the EF/ILCD
category set), with units matching the workbook. `data/literature/EN15804+A2.pdf` Table 3
(printed p.41–42) and Table 4 (printed p.42–43):

| Workbook child | Workbook unit | EN15804+A2 category / unit (verbatim) | Page |
|---|---|---|---|
| EN6-1 Ozone depletion | kg CFC-11 eq | "Ozone Depletion … (ODP) — kg CFC 11 eq." | p.41 |
| EN6-2 Respiratory inorganics | Disease incidence | "Particulate Matter emissions … Disease incidence" (Table 4) | p.42 |
| EN6-3 Photochemical ozone formation | kg NMVOC eq | "Photochemical ozone formation … (POCP) — kg NMVOC eq." | p.42 |
| EN6-4 Eutrophication: Terrestrial | Mole of N eq | "Eutrophication terrestrial … Accumulated Exceedance — mol N eq." | p.41–42 |
| EN6-5 Eutrophication: Marine | kg N eq | "Eutrophication aquatic marine … (EP-marine) — kg N eq." | p.41 |
| EN6-6 Eutrophication: Freshwater | kg P eq | "Eutrophication aquatic freshwater … (EP-freshwater) — kg P eq." | p.41 |
| EN6-7 Acidification | Mole of H+ eq | "Acidification … Accumulated Exceedance (AP) — mol H+ eq." | p.41 |
| EN6-8 Ionizing radiation | kBq U-235 eq | "Ionizing radiation, human health … (IRP) — kBq U235 eq." (Table 4) | p.42 |

All eight are confirmed real EF categories with the workbook's units. Verdict for each
leaf: **PARTIAL (adapted)** on concept/unit (matches EN15804+A2), but the specific
*method* PDF each leaf cites is **SOURCE-NOT-FOUND**.

## Q3 — EN7 toxicity (CTUh / CTUe): are these defined and normalizable the same way?

The characterization units are confirmed in **EN15804+A2** Table 4 (printed p.42–43):

- EN7-1 Human toxicity: cancer (CTUh) ↔ *"Human toxicity, cancer … Potential Comparative
  Toxic Unit for humans (HTP-c) — CTUh"* (p.42).
- EN7-2 Human toxicity: non-cancer (CTUh) ↔ *"Human toxicity, non-cancer effects …
  Potential Comparative Toxic Unit for humans (HTP-nc) — CTUh"* (p.43).
- EN7-3 Ecotoxicity: freshwater (CTUe) ↔ *"Eco-toxicity (freshwater) … Potential
  Comparative Toxic Unit for ecosystems (ETP-fw) — CTUe"* (p.42).

ISO 14044 does not name CTUh/CTUe (it is method-agnostic); the USEtox documents that do
(`USEtox2.0`) are **not in the corpus**. Normalizability: CTUh and CTUe are characterized
indicator results just like the EN6 categories, so they follow the identical
ISO 14044 path — they must be normalized (divide by the per-category EF normalization
factor) and weighted *before* any cross-category sum. EN15804+A2 Table 5 (printed p.43)
flags all three as ILCD Type 3 (lowest robustness, disclaimer 2), which is a real-world
caution but does not change the math: they are still single-category results that cannot be
averaged with each other in raw form (CTUh and CTUe are different units anyway).

## Q4 — Do the cited codes resolve? (reference integrity)

`References.tsv` **has rows** for every code these metrics cite, so they are not orphan
labels. The defect is that the *files* are missing from `data/literature/`. Codes whose
References row exists but PDF is absent (→ SOURCE-NOT-FOUND for cross-check purposes):

- `EUPEF+21` (cited by EN6, EN7, EN8, EN9) — Commission Rec. (EU) 2021/2279. No PDF.
- `USEtox2.0` (EN6-2, EN7-1), `USEtox2.1` (EN7-2), `USEtox2.2` (EN7-3) — only `USEtox2.0`
  has a References row; **`USEtox2.1` and `USEtox2.2` have no References row at all**
  (orphan codes — likely meant to all point at the single USEtox 2.x documentation). No PDF
  for any.
- `AO+24` (EN6-1), `VZ+08` (EN6-3), `ILCD2011` (EN6-4, EN6-7), `ReCiPe2008` (EN6-5, EN6-6),
  `EUEP-FW` (EN6-6), `FR+00` (EN6-8), `BA+17` (EN8-1), `OL+02` (EN8-2, EN8-3) — all have
  References rows, none have a PDF in the corpus.

`WBCSD` and `ESRS E2-4` are mentioned in your brief but belong to EN1/EN4, outside this
batch; not assessed here. `WBCSD` has no row in `References.tsv` (orphan) — flagged for the
EN1 review, not re-flagged here.

---

## Per-metric blocks

### EN6 — Pollution & Effects on Nature Score
- Verdict: **CONTRADICTION (method)**
- Reference(s): `EUPEF+21` [row present in References.tsv → SOURCE-NOT-FOUND, no PDF]
- Evidence: ISO-14044 p.30: characterization aggregates only *"within the same impact
  category"*; p.32: weighting aggregates *"normalized results across impact categories"*.
- Assessment: EN6 is tagged `WEIGHTED_AVERAGE_STRATEGY` with equal 0.125 weights over eight
  children measured in eight incompatible units (kg CFC-11 eq, disease incidence,
  kg NMVOC eq, mol N eq, kg N eq, kg P eq, mol H+ eq, kBq U-235 eq). Averaging these raw
  values is dimensionally meaningless and contradicts the ISO 14044 rule that cross-category
  aggregation operates on **normalized** results. The category set itself is correct (Q2).
- Issues: **[blocker]** raw weighted-average over non-additive units; **[major]** cited
  `EUPEF+21` PDF absent so the prescribed normalization/weighting factors cannot be sourced
  from the corpus.
- Recommendation: re-model as normalize-then-weight-then-sum (see Recommended actions).

### EN6-1..EN6-8 — individual impact categories
- Verdict: **PARTIAL (adapted)** on concept/unit; **SOURCE-NOT-FOUND** on the cited method.
- Reference(s): per-leaf method codes (AO+24, USEtox2.0, VZ+08, ILCD2011, ReCiPe2008,
  EUEP-FW, FR+00) — all rows present, all PDFs absent.
- Evidence: EN15804+A2 p.41–42 (table mapping above) confirms each as a real EF category
  with the workbook's unit.
- Assessment: faithful adaptations of standard EF categories. Each is a raw characterized
  result (correct as a *leaf*). The defect is purely at the parent (EN6) aggregation and the
  missing method PDFs.
- Issues: **[major]** each cited method PDF missing from corpus; **[minor]** EN6-2 unit
  string "Disease incidences per kg of PM2.5" is more verbose than EN15804's "Disease
  incidence" — cosmetic.
- Recommendation: keep leaves as raw results; attach the EF normalization + weighting factor
  per leaf (sourced externally, see below).

### EN7 — Toxicity Score
- Verdict: **CONTRADICTION (method)**
- Reference(s): `EUPEF+21` [SOURCE-NOT-FOUND]
- Evidence: EN15804+A2 p.42–43 confirms CTUh (HTP-c, HTP-nc) and CTUe (ETP-fw); ISO-14044
  p.32 (normalize before weighting).
- Assessment: same non-additivity defect — EN7-1 (CTUh) + EN7-2 (CTUh) + EN7-3 (CTUe)
  cannot be raw-averaged; CTUh and CTUe are different units. EN7-1 and EN7-2 share the unit
  CTUh but are distinct categories that still require per-category normalization before any
  sum.
- Issues: **[blocker]** raw weighted-average over CTUh/CTUe; **[major]** EUPEF+21 absent.
- Recommendation: normalize-then-weight-then-sum.

### EN7-1..EN7-3 — toxicity categories
- Verdict: **PARTIAL (adapted)** on concept/unit; **SOURCE-NOT-FOUND** on USEtox.
- Evidence: EN15804+A2 p.42–43 (HTP-c CTUh, HTP-nc CTUh, ETP-fw CTUe).
- Issues: **[major]** USEtox PDFs absent; **[minor]** `USEtox2.1`/`USEtox2.2` are orphan
  codes (no References row) — only `USEtox2.0` is registered.
- Recommendation: collapse the three USEtox codes to the single registered `USEtox2.0`
  (or add proper rows); attach EF normalization/weighting per category.

### EN8 — Resource Deprivation Score
- Verdict: **CONTRADICTION (method)**
- Reference(s): `EUPEF+21` [SOURCE-NOT-FOUND]
- Evidence: EN15804+A2 p.41–42 (WDP m³, ADP-minerals&metals kg Sb eq, ADP-fossil MJ);
  ISO-14044 p.32.
- Assessment: EN8-1 (m³) + EN8-2 (kg Sb eq) + EN8-3 (MJ) raw-averaged — non-additive,
  contradicts ISO 14044. Categories themselves are correct EF resource categories.
- Issues: **[blocker]** raw weighted-average over mixed units; **[major]** EUPEF+21 absent.
- Recommendation: normalize-then-weight-then-sum.

### EN8-1..EN8-3 — resource categories
- Verdict: **PARTIAL (adapted)** on concept/unit; **SOURCE-NOT-FOUND** on method.
- Evidence: EN15804+A2 p.42 — "Water use … (WDP) — m³ world eq. deprived"; "Depletion of
  abiotic resources - minerals and metals … (ADP-minerals&metals) — kg Sb eq."; "… fossil
  fuels … (ADP-fossil) — MJ, net calorific value". EN8-1 cites AWARE model (`BA+17`),
  EN8-2/EN8-3 cite CML/ADP (`OL+02`) — both consistent with EN15804's model attribution
  (footnote d "ultimate reserve model of the ADP-minerals&metals model", p.42).
- Issues: **[major]** `BA+17`, `OL+02` PDFs absent.
- Recommendation: keep as raw leaves; attach EF normalization/weighting.

### EN9 — PEF Single Score
- Verdict: **CONTRADICTION (method)** + **SOURCE-NOT-FOUND**
- Reference(s): `EUPEF+21` [row present → no PDF].
- Evidence: EN9 formula text: *"Each impact factors are normalized to a 'global average
  person's emissions over one year.' Then weighted as instructed in the EF guidelines."* —
  this **correctly describes** the ISO 14044 / EF normalize→weight→sum sequence
  (ISO-14044 p.31 names per-capita normalization; p.32 names weighting+aggregation). The
  problem is the metric is tagged `WEIGHTED_AVERAGE_STRATEGY` and reuses the **raw**
  leaves (EN1-4, EN5-2, EN6-*, EN7-*, EN8-*) with no normalization or weighting factor
  fields anywhere in the workbook. ISO-14044 p.20 also cautions *"there is no scientific
  basis for reducing LCA results to a single overall score or number"* — so the single
  score must carry the value-choice caveat and keep pre-weighting data available
  (p.31, *"data prior to weighting should remain available"*).
- Assessment: the description/formula is the right target; the implementation
  (WEIGHTED_AVERAGE over raw mixed-unit leaves, no EF factors) cannot produce a valid PEF
  single score. EN9 also reuses EN1-4 (climate, kg CO₂ eq) and EN5-2 (land use, m²a/FU) —
  both also raw, both also needing their own EF normalization/weighting.
- Issues: **[blocker]** strategy/formula mismatch — cannot weight-average raw EF results;
  no normalization factor or weighting factor inputs exist; **[major]** EUPEF+21 PDF (the
  only place the EF 3.x normalization & weighting factor *values* live) is absent from the
  corpus, so EN9 cannot be made computable from `data/literature/` alone.
- Recommendation: re-model with explicit per-category normalization-factor and
  weighting-factor inputs (EF 3.x), computed as Σ (characterized_i / NF_i) × WF_i.

---

## Recommended actions (decision-ready)

1. **Re-model EN6, EN7, EN8 and EN9 from raw weighted-average to normalize→weight→sum.**
   For each impact-category leaf *i*: `normalized_i = characterized_i / NF_i`, then
   `weighted_i = normalized_i × WF_i`, then `score = Σ weighted_i`. The current
   `WEIGHTED_AVERAGE_STRATEGY` directly applied to raw leaves is dimensionally invalid
   (ISO-14044 p.32: weighting aggregates *normalized* results, not raw mixed-unit ones).
   EN6/EN7/EN8 are sub-scores of EN9, so a clean design is: one normalize+weight pipeline
   feeding all of them, with EN9 summing across the full 16-category set.

2. **Add the two factor inputs the workbook currently lacks**, per impact category:
   - a **normalization factor (NF)** — the EF "global average person, one year" per-capita
     reference value (this is exactly what EN9's own formula text references);
   - a **weighting factor (WF)** — the EF robustness-based weighting set.
   Today neither EN6/EN7/EN8 children nor EN9 carry NF/WF fields; only equal placeholder
   weights (0.125 / 0.333 / 0.1112) exist, which are *not* EF weighting factors.

3. **Source the EF 3.x NF and WF values externally — they are NOT in `data/literature/`.**
   The cited `EUPEF+21` (Commission Rec. (EU) 2021/2279, whose Annex I carries the 16-category
   factor tables) has a References row but no PDF in the corpus. The normalization/weighting
   factor *values* therefore cannot be quoted or verified from the corpus and must be added
   from the EF 3.x dataset (EUPEF+21 Annex / EF reference package). Until then EN6/EN7/EN8/EN9
   are not computable as PEF scores. EN15804+A2 (present) confirms the *categories and units*
   but, like ISO 14044, leaves normalization/weighting optional and does not publish a single
   score (EN15804+A2 p.56 only "aggregates" the *same* indicator across life-cycle modules,
   i.e. within one category — not across categories).

4. **Fix the toxicity reference codes**: `USEtox2.1` and `USEtox2.2` are orphan codes with
   no `References.tsv` row. Collapse EN7-1/2/3 onto the single registered `USEtox2.0`, or add
   real rows for 2.1/2.2.

5. **Carry the single-score caveat on EN9** (ISO-14044 p.20: "no scientific basis for
   reducing LCA results to a single overall score") and keep pre-weighting per-category
   results available (p.31). EN9's own description already notes the score "by itself does
   not represent anything" — consistent with this; keep that note.

6. **Add the missing method PDFs** (or accept SOURCE-NOT-FOUND): without EUPEF+21 / USEtox /
   AWARE / CML / ReCiPe / ILCD PDFs, the leaf-level method citations cannot be verified
   against the corpus; only the EN15804+A2 category/unit mapping is corpus-grounded.

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | blocker | EN6, EN7, EN8 | `WEIGHTED_AVERAGE_STRATEGY` applied to children in different, non-additive units (kg CFC-11 vs CTUh vs kg P eq vs MJ …). ISO-14044 p.32: weighting aggregates *normalized* results across categories, not raw mixed-unit results. | Re-model to normalize→weight→sum: `Σ (characterized_i / NF_i) × WF_i`. |
| 2 | blocker | EN9 | Tagged `WEIGHTED_AVERAGE`; formula text correctly describes EF normalize-then-weight, but no normalization-factor or weighting-factor inputs exist; reuses raw leaves. | Add per-category NF & WF input fields; change strategy to PEF normalize+weight+sum over the 16 categories. |
| 3 | major | EN6/EN7/EN8/EN9 | `EUPEF+21` (EF normalization & weighting factor source, Annex I) cited but PDF absent from `data/literature/`. | Source EF 3.x NF/WF values from EUPEF+21 Annex / EF reference package; add the PDF to corpus. |
| 4 | major | EN6-1,3,4,5,6,7,8; EN7-1..3; EN8-1..3 | Each leaf's cited method PDF (AO+24, USEtox2.0, VZ+08, ILCD2011, ReCiPe2008, EUEP-FW, FR+00, BA+17, OL+02) is missing from corpus; only category/unit verifiable (via EN15804+A2). | Add the method PDFs, or accept SOURCE-NOT-FOUND and rely on EN15804+A2 for category/unit grounding. |
| 5 | major | EN7-2, EN7-3 | `USEtox2.1` and `USEtox2.2` are orphan reference codes — no row in `References.tsv` (only `USEtox2.0` is registered). | Point EN7-1/2/3 at the single `USEtox2.0` row, or add proper rows for 2.1/2.2. |
| 6 | minor | EN6 | Equal 0.125 weights (and 0.333/0.1112 elsewhere) are placeholders, not EF weighting factors. | Replace with EF weighting set once sourced; keep weights distinct from NF. |
| 7 | minor | EN6, EN7 | `Objective / Goal` cell is empty (peers EN1–EN5 have one). | Add an objective for EN6/EN7. |
| 8 | minor | EN6-2 | Unit string "Disease incidences per kg of PM2.5 (μm)" is more verbose / unit-confused vs EN15804+A2 "Disease incidence". | Normalize unit label to "Disease incidence". |

### SOURCE-NOT-FOUND codes (References row exists, but no PDF in `data/literature/`)
`EUPEF+21`, `USEtox2.0`, `AO+24`, `VZ+08`, `FR+00`, `BA+17`, `OL+02`, `ReCiPe2008`,
`ILCD2011`, `EUEP-FW`. Additionally `USEtox2.1` and `USEtox2.2` are orphan codes (no
References row at all).

### Limits of this run
- The **EF 3.x normalization and weighting factor values are not in `data/literature/`**
  (EUPEF+21 has no PDF), so I could not quote or verify the actual NF/WF figures; the
  recommendation to "normalize then weight" is grounded in ISO 14044 (present) and the
  category/unit mapping in EN15804+A2 (present), not in the EF factor tables themselves.
- Leaf-level *method* citations (USEtox, AWARE, CML, ReCiPe, ILCD, WMO/ODP) could not be
  checked against their own documents — those PDFs are absent. Concept and unit were
  verified against EN15804+A2 only.
- ISO 14044 page citations use the PDF's printed page numbers (29–32); these are PDF pages
  33–36. EN15804+A2 citations use the printed page numbers (41–43).
- EN1-4 and EN5-2 (reused by EN9) were assessed only insofar as they feed EN9; their own
  EN1/EN5 references are outside this batch.
