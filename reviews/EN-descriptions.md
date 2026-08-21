# EN description audit — refine + ground KPI descriptions

**Scope:** the full **Environmental Impact (EN) domain — all 64 KPIs**, audited family by
family (EN1 calibration batch first, then EN2–EN9 + the archived per-phase ratios). Goal:
refine the handmade descriptions so they (a) match each KPI's *current* implementation
(Calculation Strategy, Formula, parent/child relations after the gap-fix re-model) and
(b) are grounded in / validated against the cited literature in `data/literature/`.
**Date:** 2026-06-29.
**Method:** current state read from `snapshot/Environmental Impact.tsv` (+ `References.tsv`);
every literature claim is a verbatim quote retrieved with `tools/scripts/pdf_search.py`,
cited by file + page; conservative stance — intentional product-level adaptations are kept
faithful to what the KPI measures and flagged, not rewritten to match org-level sources.
**Verdict legend:** CONSISTENT = text matches current implementation + literature;
DRIFTED = text no longer matches the current Formula / Calculation Strategy / relations
(propose a fix); ADAPTED = faithful product-level adaptation of an org-level source
(keep + flag); UNVERIFIABLE = author-defined, no citable source (legitimate).

---

## EN domain — consolidated summary & decisions

**Verdicts across all 64 EN KPIs:** CONSISTENT 23 · DRIFTED 7 · ADAPTED 32 · UNVERIFIABLE 2.
Per-family detail and full per-KPI blocks follow below; each family keeps its own batch
summary. Nothing has been applied to the workbook — every change below is a proposal.

> **Status (2026-06-29):** decisions D1–D3 and §E scope are **RESOLVED** (see below); the
> author is reviewing this report before any workbook edits are applied. Apply is **on hold**.

### A. Description rewrites — DRIFTED rows (7; description contradicts current implementation)

| KPI | Problem | Proposed |
|---|---|---|
| EN1 | desc omits EN12; mentions only 2 of 3 children | rewrite to name EN11/EN12/EN13 |
| EN13 | desc lists GRI-305 components the single-ratio formula never computes | rewrite to PCF reduction-over-base-period (ESRS E1-4) |
| EN3 | parent desc scopes only "toxic waste"; undercounts the EN32 hazardous-share arm | rewrite to name both arms |
| EN32 | re-tagged formula `1−hazardous/total` ≠ old "substitution vs previous product" desc | rewrite — **see decision D1** |
| EN4 | desc triad mislabeled ISO 14046 (it is GRI 303 structure); inventory-input prose | rewrite to name EN41/EN42/EN43 |
| EN6-4 | generic aquatic "algae growth" boilerplate; no terrestrial-eutrophication qualifier | rewrite to N-deposition / accumulated exceedance |
| EN44 | desc "total" vs formula "avg" vs tag weighted-average (archived) | reconcile wording to weighted-average |

### B. Adjacent-cell drift — Formula text & citation codes (propose-and-apply with the rewrites)

- **Stale Formula text** (children changed in the gap-fix, formula cell didn't): `EN1` (`…+EN14`),
  `EN4` (`…+EN44`), `EN0` (`EN1+…+EN5` → should be EN1…EN8), `EN9` (omits final sum), the
  `EN6`/`EN7`/`EN8` parents ("compared to a target value" — pre-re-model phrasing), and the
  six EN7/EN8 leaves (name only the characterization model, not the self-normalization).
- **Citation codes:** `EN13` GRI 305 → `ESRS E1-4` (**decision D2**); `EN6-2` `USEtox2.0` →
  PM model (`EUPEF+21`/`VZ+08`); EN7/EN8 leaves `USEtox2.0` vs PEF's `USEtox2.1` label.

### C. Citation hygiene (reference-cell fixes, low-risk)

- `WBCSD` orphan code on EN2-1 (no Label, no PDF) — drop or document.
- Blank Reference cells where the concept is groundable: `EN22` (add GRI 303 / ISO 14046),
  `EN32` (add ESRS E5-5 / GRI 306).
- Add `EUPEF+21` to the EN5/EN6/EN7/EN8 PEF leaves (the PEF PDF is now confirmed in the corpus
  and grounds every category/unit — also resolves a stale SOURCE-NOT-FOUND in the prior PEF review).
- Minor: SASB RT-CP-130a.1 vs 120a.1 numbering (EN21); double-spaces / stray tabs / trailing
  spaces in several names; a copy-paste "EN5-2 land use 'pt'" line left in EN7/EN8 parent Comments.

### D. Decisions — RESOLVED 2026-06-29

1. **EN32 — what does it measure? → Static hazardous-material share.** It is the share
   `1 − hazardous/total` (matches the live formula). **Action on apply:** rewrite the
   description to match the share formula and **drop the stale "Value of previous Product"**
   reference value. (Substitution-vs-previous-product reading rejected.)
2. **EN13 — GRI 305 vs ESRS E1-4. → Keep ESRS E1-4.** Drop the GRI-305 prose and the
   enumerated component list; keep the reduction-over-base-period framing (matches the
   formula + the cited code).
3. **EN43 — gray water in "Water Independence". → Comment-cell flag, no rewrite.** Add a
   note that counting gray water toward water independence is an author simplification; the
   formula stays as-is.

### E. ADAPTED Comment flags — RESOLVED 2026-06-29: non-obvious only

ADAPTED rows keep their description and get a short Comment-cell note (e.g. "Product-level
adaptation of org-level ESRS E1-6 / IFRS S2."), **but only where the adaptation is not
self-evident** — e.g. flag EN1-4 (PCF), EN9 (PEF single score) and the PEF impact leaves;
**skip the self-evident Scope 1/2/3 leaves** (EN1-1/-2/-3) and similar. The per-row Notes
mark which rows are obvious vs not.

---

### EN1 — Product Carbon Footprint Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall climate impact related to carbon footprint of a product. By combining PCF benchmark scores and its reduction rate, the PCF score provides a basis for an actionable measure for improving environmental performance."
- **Verdict:** DRIFTED — the description's child list ("PCF benchmark scores and its reduction rate") under-counts the three children now wired: EN11 (industry benchmark), EN12 (version improvement), EN13 (reduction rate); and the displayed Formula still says "EN11 + … + EN14".
- **Grounding:** ISO 14067 p.7: "The aim of this document is to quantify GHG emissions associated with the life cycle stages of a product, beginning with resource extraction and raw material sourcing and extending through the production, use and end-of-life stages of the product." (`data/literature/ISO 14XXX/ISO 14067.pdf`)
- **Implementation check:** `Underlying Metrics = EN11\nEN12\nEN13`, strategy WEIGHTED_AVERAGE. The description mentions only two of the three concepts (benchmark + reduction), omitting EN12 version improvement. The Formula cell reads "Sum (weight * EN11 + … + weight * EN14)" but EN14 is archived and is **not** a child of EN1 (EN14's Parent is None; EN1's children are EN11/EN12/EN13). This is gap-fix drift: the formula text still references the old EN14 grandchild grouping.
- **Proposed revision:** "Aggregates the product's carbon-footprint performance into one score by combining its industry benchmark (EN11), improvement versus previous versions (EN12), and reduction rate over time (EN13). Provides an actionable overview for improving the product's climate performance."
- **Notes:** Composite/parent — no single literature source expected; ISO 14067 grounds the PCF concept only. [minor] Formula text "EN11 + … + EN14" should read "EN11 + EN12 + EN13" to match the actual children. EN1 cites `ISO 14067` (resolves in References). EN1's `Parent Metrics` = EN0\nEN9 — EN9 is outside this batch; not verified here.

### EN11 — PCF Industry Performance  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the PCF performance comparison of a product compared to other comparable product to indicate eco-friendliness in the industry."
- **Verdict:** CONSISTENT — text matches the formula `Performance = 1 - Product / Industry` and the EN1-4 (product PCF) vs EN1-5 (industry PCF) children.
- **Grounding:** ISO 14067 p.7 (PCF concept, quote above). Industry-benchmark value itself is author-defined: EN15804+A2 p.23: "For the interpretation of a comparison, benchmarks or reference values are needed. This standard does not set benchmarks or reference values." (`data/literature/EPD/EN15804+A2.pdf`)
- **Implementation check:** Children EN1-4 (Absolute PCF) and EN1-5 (Comparable Industry PCF) both exist; Formula `Performance = 1 - Product / Industry`, then `(Performance - Min)/(Max - Min)`. The word "eco-friendliness" is loose relative to a CO₂e comparison. Unit % is consistent with a normalized ratio.
- **Proposed revision:** "Benchmarks the product's absolute PCF (EN1-4) against a comparable industry product's PCF (EN1-5): higher when the product emits less than the industry reference. Positions the product competitively on climate impact."
- **Notes:** Benchmark source (EN1-5) is author-defined; see EN1-5. [minor] replace vague "eco-friendliness" with the CO₂e comparison it actually computes.

### EN12 — PCF Version Improvement  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the PCF performance comparison of a product compared to previous versions to indicate  improvement in the product's life cycle."
- **Verdict:** CONSISTENT — matches `Improvement = 1 - Current / Previous`.
- **Grounding:** ISO 14067 p.7 (PCF concept, quote above). No literature prescribes a cross-version comparison value; "Previous Version Value" is an author/product input.
- **Implementation check:** Child EN1-4 (Absolute PCF) exists; Formula `Improvement = 1 - Current / Previous`. "Current" = this product's EN1-4; "Previous" = the prior version's PCF (a supplied reference value, listed under Potential Reference Values as "Previous Version Value"). Consistent. The phrase "improvement in the product's life cycle" is slightly ambiguous (could read as within-lifecycle rather than across versions).
- **Proposed revision:** "Compares the product's current absolute PCF (EN1-4) against the PCF of its previous version: higher when the new version emits less. Tracks continuous climate improvement across product generations."
- **Notes:** Double space in current text ("improvement  in"). [minor] "previous version" is a supplied value, not a child metric — confirm intended source per product.

### EN13 — PCF Reduction Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the reduction in the product’s carbon footprint over time. It includes: Scope 1 2 3, intensity, initiatives, ODS, and air emissions. It is based on GRI 305."
- **Verdict:** DRIFTED — the second/third sentences describe a GRI-305-style multi-component disclosure that the current implementation does not compute, and cite GRI 305 while the Reference cell actually carries `ESRS E1-4`.
- **Grounding:** ESRS E1 p.7 (DR E1-4): "GHG emission reduction targets shall be disclosed in absolute value (either in tonnes of CO2eq or as a percentage of the emissions of a base year) … (b) GHG emission reduction targets shall be disclosed for Scope 1, 2, and 3 GHG emissions, either separately or combined." (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E1 Delegated-act-2023-5303-annex-1_en.pdf`)
- **Implementation check:** Child EN1-4 only; Formula `Reduction = 1 - Now / PreviousTime`, then normalized. The implementation is a simple time-over-time PCF reduction ratio on the total PCF (EN1-4). The description's enumerated list ("intensity, initiatives, ODS, and air emissions") and "based on GRI 305" do **not** reflect this single-ratio computation and do not match the cited code `ESRS E1-4`. GRI 305 is not cited on the row and is not in scope of the formula. Classic gap-fix drift: the row was re-tagged to `ESRS E1-4` but the prose still says GRI 305.
- **Proposed revision:** "Measures the percentage reduction in the product's absolute PCF (EN1-4) over time, comparing the current value against an earlier base period. Tracks progress toward the product's climate targets."
- **Notes:** [major] description cites "GRI 305" but the Reference cell is `ESRS E1-4` — reconcile (drop the GRI 305 sentence, or add GRI 305 to the Reference if intended; ESRS E1-4 grounds the reduction-over-base-year framing well). ESRS E1-4 is org-level reduction *targets*; the KPI adapts it to a product-level realized reduction ratio — defensible, but the source is about target-setting not a computed rate, so this remains an ADAPTED grounding (flag retained).

### EN14 — Lifecycle Phase Emission  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY — ARCHIVED]
- **Current:** "Measures breakdown of emissions across different stages of the product lifecycle to identify hotspots (i.e., stages with the highest emissions)."
- **Verdict:** ADAPTED — concept is well grounded in ISO 14067 / EN15804+A2 stage breakdown, but the row is ARCHIVED and its children are mis-wired (carried over from `reviews/EN1-carbon-phases.md`).
- **Grounding:** ISO 14067 p.8: "GHGs can be emitted and removed throughout the life cycle of a product which includes acquisition of raw material, design, production, transportation/delivery, use and the end-of-life treatment." (`data/literature/ISO 14XXX/ISO 14067.pdf`)
- **Implementation check:** Children EN131–EN135 (the five phase ratios), strategy WEIGHTED_AVERAGE. Per `reviews/EN1-carbon-phases.md`, all five children currently resolve to the same Scope1+2+3 sum, so the weighted average degenerates to EN1-4 (EN14's own Comment confirms: "the result should be the same as EN1-4"). The description correctly states the *intent* (per-stage hotspots) but the implementation cannot deliver it until phase-specific inputs are wired. Row is ARCHIVED ("not in score").
- **Proposed revision:** keep as-is (description states the correct intent). Do not rewrite to match a broken implementation.
- **Notes:** [major, deferred] inherited from carbon-phases review — children need per-phase inputs (EN15804 modules A1–A3 / A3 / A4 / B1–B7 / C1–C4), not Scope1+2+3. Since the row is archived and out of score, this batch only flags it; the fix is tracked in `reviews/EN1-carbon-phases.md`. Optionally cite ISO 14067 / EN15804 on this row for the stage-breakdown basis.

### EN1-1 — Scope 1 - Direct Emissions  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Direct emissions from owned/controlled sources (e.g., fuel combustion, company vehicles)."
- **Verdict:** ADAPTED — verbatim-accurate Scope 1 definition, applied at product level; org-level sources cited.
- **Grounding:** ESRS E1 p.9: "(a) gross Scope 1 GHG emissions as required by paragraph 44 (a) is to provide an understanding of the direct impacts of the undertaking on climate change". IFRS S2 p.15: "(1) Scope 1 greenhouse gas emissions". SASB RT-CP p.8: "RT-CP-110a.1. Gross global Scope 1 emissions … The entity shall disclose its gross global Scope 1 greenhouse gas (GHG) emissions". (files: `…/ESRS E1 …annex-1_en.pdf`, `…/issb-2023-a-ifrs-s2-climate-related-disclosures.pdf`, `…/RT-CP-containers-and-packaging-standard_en-gb.pdf`)
- **Implementation check:** Raw leaf, no formula; feeds EN1-4 and the phase ratios. Description matches the Scope 1 "direct/owned/controlled" definition. Unit kg CO₂ eq. consistent. SASB sub-code is Scope-1-specific, correctly cited here only.
- **Proposed revision:** keep as-is.
- **Notes:** ADAPTED flag: the three cited standards are organisation-level GHG inventory; here the figure is the product's Scope 1 share. Faithful adaptation. (SASB code spelling differs across cells — see fixes.)

### EN1-2 — Scope 2 - Purchased Indirect Emissions  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Indirect emissions from purchased electricity, heat, or steam."
- **Verdict:** ADAPTED — accurate Scope 2 definition at product level.
- **Grounding:** IFRS S2 p.15: "(2) Scope 2 greenhouse gas emissions". ESRS E1 p.9–10 lists Scope 2 under DR E1-6 "Gross Scopes 1, 2, 3 and Total GHG emissions". (files as above)
- **Implementation check:** Raw leaf; feeds EN1-4 and phase ratios. Description (purchased electricity/heat/steam) matches Scope 2. Unit consistent. SASB code correctly **not** cited (RT-CP-110a.1 is Scope 1 only).
- **Proposed revision:** keep as-is.
- **Notes:** ADAPTED flag (org-level source, product-level figure).

### EN1-3 — Scope 3 - Other Indirect Emissions  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Other indirect emissions from the value chain (e.g., supply chain, business travel, product use)."
- **Verdict:** ADAPTED — accurate Scope 3 definition at product level.
- **Grounding:** IFRS S2 p.22: "Scope 3 greenhouse gas emissions … that occur in the value chain of an entity, including both upstream and downstream emissions." ESRS E1 p.9 DR E1-6 "(c) gross Scope 3 GHG emissions". (files as above)
- **Implementation check:** Raw leaf; feeds EN1-4 and phase ratios. Description (value-chain, supply chain, product use) matches Scope 3 upstream/downstream. Unit consistent.
- **Proposed revision:** keep as-is.
- **Notes:** ADAPTED flag (org-level source, product-level figure).

### EN1-4 — Absolute PCF  [Level 5, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current:** "The total greenhouse gas emissions associated with the product across its lifecycle"
- **Verdict:** ADAPTED — product-level total PCF, summed from Scopes 1/2/3; org-level "total GHG" source adapted (keep, flag).
- **Grounding:** ESRS E1 p.9 DR E1-6: "(a) gross Scope 1 … (b) gross Scope 2 … (c) gross Scope 3 … and (d) total GHG emissions." ISO 14067 p.7 (life-cycle CFP, quote above). (files as above)
- **Implementation check:** `Underlying Metrics = EN1-1\nEN1-2\nEN1-3`; Formula "Sum of 1,2,3 scope emissions"; strategy SUM_AGGREGATE. Children all exist; description ("total GHG across lifecycle") matches summing Scopes 1+2+3. Unit kg CO₂ eq. consistent with children. Parents EN11/EN12/EN13/EC5 — EC5 is cross-domain (Economic), not verified here.
- **Proposed revision:** keep as-is. (Optional clarification: "The product's total cradle-to-grave carbon footprint, summed from its Scope 1 (EN1-1), Scope 2 (EN1-2) and Scope 3 (EN1-3) emissions." — only if you want the child wiring explicit in prose.)
- **Notes:** ADAPTED flag — cited ESRS E1-6 / IFRS S2 are organisation-level "total GHG"; this KPI is a **product** carbon footprint (PCF). The row already also cites ISO 14067 and EN 15804 (both product-level, both resolve), which is the correct product-level grounding; keep them. Comment field notes "A part of PEF Impact Factor of Climate Change (kg CO₂ eq.)" — consistent. [minor] Level anomaly: EN1-4 is a composite (`SUM_AGGREGATE` of EN1-1/2/3) yet sits at `Level 5`, the same level as its leaf children — the level does not decrease from parent to child here. Likely an intentional flat raw-input tier (the three scopes + their sum); confirm, or bump EN1-4 to the tier above its children.

### EN1-5 — Comparable Industry PCF  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The total greenhouse gas emissions of a comparable industry product across its lifecycle, taken from a PEF/EPD sector benchmark (a Product Environmental Footprint or EPD sector reference value for the product category)."
- **Verdict:** UNVERIFIABLE — author-defined benchmark input; legitimate, no citable standard provides the value.
- **Grounding:** author-defined, no source for the value itself. EN15804+A2 p.23 confirms standards do not supply such benchmarks: "For the interpretation of a comparison, benchmarks or reference values are needed. This standard does not set benchmarks or reference values." (`data/literature/EPD/EN15804+A2.pdf`)
- **Implementation check:** Raw leaf feeding EN11 (industry comparison). No formula. Description now (post gap-fix) explicitly states the benchmark source (PEF/EPD sector reference) — this resolves fix #5 from `reviews/EN1.md`. Unit kg CO₂ eq. consistent with EN1-4 for the EN11 ratio.
- **Proposed revision:** keep as-is. Description is now auditable (states where the value comes from).
- **Notes:** UNVERIFIABLE is the correct status for an author-defined benchmark — not a defect. No reference code cited, which is appropriate for a supplied external value.

---

## Batch summary

**Counts (10 metrics):** CONSISTENT 2 (EN11, EN12); DRIFTED 2 (EN1, EN13); ADAPTED 5
(EN14, EN1-1, EN1-2, EN1-3, EN1-4); UNVERIFIABLE 1 (EN1-5).

**Proposed description rewrites:** EN1, EN11, EN12, EN13 (4 rows). EN14 and the four
Scope/PCF leaves keep their current text (faithful; do not chase org-level wording).

**Top decisions needed from you:**
1. **EN13 citation reconciliation (major).** The description says "based on GRI 305" but the
   Reference cell is `ESRS E1-4`. Decide which is canonical: drop the GRI-305 sentence and
   keep the ESRS E1-4 reduction-over-base-period framing (recommended, and matches the
   actual single-ratio formula), or add GRI 305 to the Reference if a multi-component
   disclosure is genuinely intended. The enumerated list (intensity/ODS/air emissions) does
   not match the current formula and should go either way.
2. **EN1 formula text vs children (minor-but-load-bearing).** EN1's children are
   EN11/EN12/EN13, but the Formula cell still reads "EN11 + … + EN14". Confirm EN14 is meant
   to be excluded (it is archived and not a child) and correct the formula text accordingly.
3. **ADAPTED flag policy for EN1-1..EN1-4 (confirm).** These cite organisation-level
   standards (ESRS E1-6, IFRS S2, SASB) for product-level figures. Per the conservative
   stance I kept the descriptions as-is and flagged the adaptation. Confirm you want the
   adaptation noted in a Comment rather than re-citing only product-level sources.

**SOURCE-NOT-FOUND codes:** none — ESRS E1 (incl. E1-4, E1-6), IFRS S2, SASB RT-CP,
ISO 14067 and EN 15804+A2 are all present and were read.

**Limits of this run:** I verified the *definitional* content (Scope 1/2/3 meaning, DR E1-6
"total GHG", DR E1-4 reduction-target framing, RT-CP-110a.1 title, ISO 14067 life-cycle
stages, EN15804 no-benchmarks) from the disclosure-definition pages only. I did not re-audit
the EN131–135 phase-ratio wiring (covered in `reviews/EN1-carbon-phases.md`; only summarised
for EN14 context), nor numeric reference values, Min/Max bands, weights, or cross-domain
parents (EN9 on EN1; EC5 on EN1-4). EN15804 no-benchmarks quote resolves to p.23 in the EPD
copy read here (`data/literature/EPD/EN15804+A2.pdf`); the earlier `reviews/EN1-carbon-phases.md`
cited p.19 from the root copy — page numbering differs by file copy, content identical.


---

## EN2 — Sustainable Resource Consumption

### EN2 — Sustainable Resource Consumption Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall sustainability of energy and water consumption throughout the product's lifecycle. It focuses on the consumption of renewable and reused resources."
- **Verdict:** CONSISTENT (composite parent; internal check) — the prose correctly describes a roll-up of a renewable-energy rate (EN21) and a reused/secondary-water rate (EN22), matching `Underlying = EN21\nEN22` and `Formula = Sum (weight * EN21 + weight * EN22)`.
- **Grounding:** composite/parent — no single literature source expected (Reference cell blank by design). Concept halves are grounded on the children's rows (RE+20 p.8 for renewable energy; GRI 303 p.7 / ISO 14046 for water reuse/consumption).
- **Implementation check:** Children EN21, EN22 both exist; strategy WEIGHTED_AVERAGE (each child weight 0.5). Unit % is compatible with averaging two 0–1/% sub-scores. "renewable and reused resources" maps cleanly onto EN21 (renewable energy) + EN22 (secondary/reused water). No drift.
- **Proposed revision:** keep as-is. (Optional, only if you want the children explicit: "Aggregates the product's resource-consumption performance into one score by combining its renewable-energy utilization rate (EN21) and its secondary (reused) water utilization rate (EN22). Higher means more of the product's energy and water comes from renewable/reused sources.")
- **Notes:** Blank Reference is correct for a composite parent — not a defect. Formula text already matches the two current children (no EN14-style stale-grandchild drift here).

### EN21 — Renewable Energy Utilization Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the proportion of renewable energy used throughout the product's life cycle."
- **Verdict:** CONSISTENT — text matches `Utilization = renewable / total used`, then `(Utilization - Min)/(Max - Min)`, over children EN2-1 (renewable energy) and EN2-2 (total energy).
- **Grounding:**
  - RE+20 p.8: "Renewable energy … Percentage of renewable energy sources in relation to the total energy used in manufacturing processes … The aim is to measure the quantity of renewable energy consumed in the manufacturing". (`data/literature/Papers/RE+20-Circular economy indicators for organizations considering sustainability and business models Plastic, textile and electro-electronic cases.pdf`)
  - SASB C&P p.14 (detail page, the authoritative metric body): "RT-CP-130a.1. (1) Total energy consumed, (2) percentage grid electricity, (3) percentage renewable and (4) total self-generated energy". (`data/literature/SASB - Sustainability Account Standards Board/RT-CP-containers-and-packaging-standard_en-gb.pdf`)
  - GRI 302 p.4: "Energy … can come from renewable sources (such as wind, hydro or solar) or from non-renewable sources … Using energy more efficiently and opting for renewable energy sources is essential". GRI 302-1 (p.8) reports "Total fuel consumption … from renewable sources" and "Total energy consumption within the organization" — the renewable-over-total numerator/denominator. (`data/literature/GRI - Global Reporting Initiative/GRI 302_ Energy 2016.pdf`)
- **Implementation check:** Both children exist (EN2-1 kWh renewable, EN2-2 kWh total); ratio is dimensionless then normalized to %, consistent with Unit %. Min/Max seeded 0/1 (Comment documents this; ratio is already a 0–1 score). No drift between prose, formula, and children.
- **Citation note — code is VALID but the source PDF is internally inconsistent:** EN21 cites `SASB RT-CP-130a.1`. The SASB C&P **detail pages** number the energy/renewable disclosure as `RT-CP-130a.1` (p.14 quote above), so the citation points to the right disclosure. **However** the SASB index/summary table on p.6 labels the *same* energy row `RT-CP-120a.1` and labels `RT-CP-130a.1` as "Water Management" — i.e. the PDF's own table and body disagree by one topic-shift. References.tsv also carries both `SASB RT-CP-120a.1` (line 95) and `SASB RT-CP-130a.1` (line 96) as separate Labels with identical generic descriptions, so the ambiguity is not resolved there. Flag for the author to pin which numbering is canonical (recommend the detail-page number actually used in the standard's body).
- **Proposed revision:** "Measures the share of the product's total energy use over its life cycle that comes from renewable sources (renewable energy ÷ total energy). Higher means less dependence on fossil energy."
- **Notes:** [minor] add `RE+20` and/or `GRI 302-2` (energy consumption outside the organization — the closest product/value-chain GRI energy code already in References) alongside the SASB code, since RE+20 is the tightest match to the renewable/total ratio and GRI 302 grounds it independently. [minor] resolve the SASB 120a.1-vs-130a.1 numbering ambiguity (see citation note). Comment-cell flag (product-level adaptation of org-level disclosures): "Product-level renewable-energy share; adapts org-level SASB RT-CP energy disclosure and GRI 302; tightest concept match is RE+20."

### EN22 — Secondary Water Utilization Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the proportion of secondary water used throughout the product's life cycle."
- **Verdict:** ADAPTED — faithful product-level "reused-water share" concept; grounded in GRI 303 / ISO 14046, but no standard supplies a single "secondary water utilization rate" datapoint, and the Reference cell is currently **blank**.
- **Grounding:**
  - GRI 303 p.7: "An organization can reduce its water withdrawal, consumption, discharge, and associated impacts through efficiency measures, such as water recycling and reuse, and process redesign". (`data/literature/GRI - Global Reporting Initiative/GRI 303_ Water and Effluents 2018.pdf`)
  - ISO 14046 p.16: "The term \"water consumption\" is often used to describe water removed from, but not returned to, the same drainage basin. Water consumption can be because of evaporation, transpiration, integration into a product, or release into a different drainage basin or the sea." (grounds the EN2-4 total-consumption denominator) (`data/literature/ISO 14XXX/ISO-14046.pdf`)
- **Implementation check:** `Utilization = secondary / total used`, then `(Utilization - Min)/(Max - Min)`; children EN2-3 (secondary/reused water, m³) and EN2-4 (total water consumption, m³) both exist and share unit m³, so the ratio is well-formed and Unit % is consistent. Min/Max seeded 0/1 (Comment documents this). Prose matches the formula and children — no implementation drift. Note `ExampleVal = max=1\nmin=0.5` on EN22 is a stray band example, not a computed value.
- **Proposed revision:** "Measures the share of the product's total water consumption over its life cycle that is met from secondary (reused/recycled) water rather than fresh withdrawal (secondary water ÷ total water consumption). Higher means less freshwater is withdrawn."
- **Notes:** [major] Reference cell is **blank**, while its sibling EN21 carries a code and the concept *is* groundable. Add `GRI 303` (line 78; grounds recycling/reuse) and optionally `ISO 14046` (line 54; grounds water consumption) so the row is auditable. ESRS E3-4 (water consumption, line 63) is the org-level analogue if a CSRD code is wanted. Comment-cell flag: "Product-level adaptation; GRI 303/ISO 14046 cover water reuse and consumption but set no 'secondary-water-share' benchmark — band is author-defined." [minor] "secondary water" is used in prose but the EN2-3 child name says "secondary sources" with a double space — align terminology.

### EN2-1 — Energy consumption from renewable sources  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total trackable renewable energy used throughout the product's lifecycle."
- **Verdict:** ADAPTED — accurate raw renewable-energy input at product level; org/CE-level sources adapted.
- **Grounding:**
  - RE+20 p.8: "Renewable energy … Percentage of renewable energy sources in relation to the total energy used in manufacturing processes". (renewable-energy quantity is the numerator the paper measures) (`…/Papers/RE+20-…cases.pdf`)
  - GRI 302 p.8 (302-1 a): "Total fuel consumption within the organization from renewable sources, in joules or multiples". (`…/GRI 302_ Energy 2016.pdf`)
- **Implementation check:** Raw leaf, no formula; feeds EN21 as the numerator. Unit kWh consistent with EN2-2 (also kWh) for the EN21 ratio. Description matches "renewable energy used". No drift.
- **Proposed revision:** keep as-is. (Optional: drop "trackable" if it has no operational meaning, or define it — it reads as a hedge: "Total renewable energy used across the product's life cycle (numerator of EN21).")
- **Notes:** [major] References cell `WBCSD\nRE+20` — `WBCSD` is an **orphan code** (no `WBCSD` Label in References.tsv). Either add a WBCSD bibliography row (e.g. a WBCSD/WRI GHG-Protocol or energy-accounting source the author intends) or drop the `WBCSD` token; `RE+20` resolves and already grounds this metric. Until resolved this is an unverifiable code, not a found source. Comment-cell flag (optional): "Renewable-energy input; concept per RE+20 / GRI 302."

### EN2-2 — Total energy used  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total energy consumed throughout the product's lifecycle."
- **Verdict:** ADAPTED — accurate raw total-energy denominator at product level; Reference blank.
- **Grounding:**
  - GRI 302 p.8 (302-1 e): "Total energy consumption within the organization, in joules or multiples." (`…/GRI 302_ Energy 2016.pdf`)
  - SASB C&P p.14: "RT-CP-130a.1. (1) Total energy consumed … 1 The entity shall disclose (1) the total amount of energy it consumed as an aggregate figure". (`…/RT-CP-containers-and-packaging-standard_en-gb.pdf`)
- **Implementation check:** Raw leaf; denominator of EN21. Unit kWh consistent with EN2-1. Description matches "total energy consumed". No drift.
- **Proposed revision:** keep as-is.
- **Notes:** [minor] Reference blank; if EN21/EN2-1 cite GRI 302 / SASB, mirror at least one onto this denominator leaf for traceability (`GRI 302-3`/`GRI 302-2` exist in References). Comment-cell flag (optional): "Total-energy denominator; per GRI 302 / SASB RT-CP energy disclosure."

### EN2-3 — Water consumption from secondary  sources  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total water utilized / reused from wastewater throughout the product's lifecycle."
- **Verdict:** ADAPTED — accurate raw secondary/reused-water input; concept grounded in GRI 303, no datapoint-level standard, Reference blank.
- **Grounding:** GRI 303 p.7: "An organization can reduce its water withdrawal, consumption, discharge, and associated impacts through efficiency measures, such as water recycling and reuse". (`…/GRI 303_ Water and Effluents 2018.pdf`)
- **Implementation check:** Raw leaf; numerator of EN22. Unit m³ consistent with EN2-4. `ExampleVal = 97500` (m³) is plausibly below EN2-4's 150000, so the EN22 ratio (97500/150000 ≈ 0.65) is well-formed. Description ("reused from wastewater") matches "secondary water" — though it narrows "secondary" specifically to wastewater reuse, while GRI 303 also counts harvested rainwater (p.11: "Surface water includes collected or harvested rainwater") and recycled water generally. Minor scope question for the author, not drift.
- **Proposed revision:** "Total secondary water used across the product's life cycle — i.e. reused or recycled water (e.g. treated wastewater, harvested rainwater) substituting for fresh withdrawal (numerator of EN22)."
- **Notes:** [minor] indicator **name has a double space**: "secondary  sources" → "secondary sources". [minor] Reference blank — add `GRI 303` for traceability. [minor] confirm whether "secondary water" is meant to include rainwater/other recycled water or wastewater-only (current prose says wastewater only). Comment-cell flag (optional): "Secondary-water input; reuse/recycling per GRI 303 (no datapoint-level benchmark)."

### EN2-4 — Total water consumption  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total water consumption throughout the product's lifecycle."
- **Verdict:** ADAPTED — accurate raw total-water denominator at product level; Reference blank.
- **Grounding:**
  - ISO 14046 p.16: "The term \"water consumption\" is often used to describe water removed from, but not returned to, the same drainage basin. Water consumption can be because of evaporation, transpiration, integration into a product, or release into a different drainage basin or the sea." (`…/ISO-14046.pdf`)
  - GRI 303 p.3/p.11: "Disclosure 303-5 Water consumption"; "Total water withdrawal from all areas in megaliters". (`…/GRI 303_ Water and Effluents 2018.pdf`)
- **Implementation check:** Raw leaf; denominator of EN22. Unit m³ consistent with EN2-3. `ExampleVal = 150000`. Description matches "total water consumption". No drift.
- **Proposed revision:** keep as-is. (Optional clarification toward ISO 14046's definition: "Total water consumed across the product's life cycle — water withdrawn and not returned to the same basin (denominator of EN22).")
- **Notes:** [minor] Reference blank; add `ISO 14046` and/or `GRI 303` (`GRI 303-5` water consumption exists in References, line 81) for traceability. Comment-cell flag (optional): "Total-water-consumption denominator; concept per ISO 14046 / GRI 303-5."

---

## Batch summary

**Counts (7 metrics):** CONSISTENT 2 (EN2 composite, EN21); ADAPTED 5 (EN22, EN2-1,
EN2-2, EN2-3, EN2-4); DRIFTED 0; UNVERIFIABLE 0. No prose contradicts its current
implementation — this family is well-aligned post gap-fix; the issues are citation
hygiene and naming, not description drift.

**Proposed description rewrites:** light/optional only — EN21 (sharpen to renewable÷total),
EN22 (sharpen to secondary÷total-consumption), EN2-3 (broaden "secondary water" wording).
EN2, EN2-1, EN2-2, EN2-4 keep current text (faithful; optional clarifications offered).

**Top decisions needed from you:**
1. **`WBCSD` orphan code on EN2-1 (major).** No `WBCSD` Label exists in References.tsv.
   Decide: add the intended WBCSD source as a References row, or drop the token (`RE+20`
   alone already grounds the metric).
2. **EN22 has no Reference but the concept is groundable (major).** Add `GRI 303`
   (recycling/reuse) and optionally `ISO 14046` so the secondary-water rate is auditable,
   mirroring EN21's citation discipline. Keep verdict ADAPTED + add the Comment flag.
3. **SASB 120a.1 vs 130a.1 numbering ambiguity (minor, citation hygiene).** The SASB C&P
   PDF's summary table (p.6) and its detail body (p.14/p.16) disagree on whether the
   renewable-energy disclosure is `120a.1` or `130a.1`. EN21's cited `RT-CP-130a.1`
   matches the detail-page body, so it is defensible — but pin the canonical number and,
   if helpful, cite `RE+20`/`GRI 302` as the cleaner primary ground for a product-level
   renewable share.
4. **Missing-citation mirroring on water/energy leaves (minor).** EN2-2, EN2-3, EN2-4
   carry no Reference; mirror the family's GRI 302 / GRI 303 / ISO 14046 codes onto them
   for traceability (the relevant Labels already exist in References.tsv).

**SOURCE-NOT-FOUND codes:** `WBCSD` (EN2-1) — code does not resolve to any References.tsv
Label and no WBCSD file is in the corpus; recorded, not substituted.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above; I did
not read full standard sections beyond the cited pages. ISO 14046 has no dedicated
"secondary/reused water" term — I grounded EN22's denominator via its p.16 water-
consumption definition and the numerator concept via GRI 303 p.7 (reuse/recycling); a
single ISO 14046 "secondary water share" datapoint does not exist (expected — these are
author-defined product rates). Cross-domain parent EN0 (EN2's parent) was not audited
here. The SASB numbering discrepancy is reported from the two cited pages of the same PDF;
I did not exhaustively map every SASB topic code.


---

## EN3 — Hazardous Material & Waste Management

### EN3 — Hazardous Material & Waste Management Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall handling, reduction, and utilization of toxic waste throughout the product's lifecycle."
- **Verdict:** DRIFTED — the description scopes the parent to *waste* only ("toxic waste"), but the two children now wired are EN31 (hazardous **waste** minimization) **and** EN32 (hazardous **material** share / substitution). The word "utilization" no longer maps to any child (there is no recovery/utilization child here), and "handling" is not computed by either child. The Objective cell ("reduce toxic material usage and hazardous waste generation") already names both arms; the Description undercounts EN32's material-substitution arm.
- **Grounding:** ESRS E5 p.2 (definition of circular economy / scope): "…minimising waste and the release of hazardous substances at all stages of their life cycle, including through the application of the waste hierarchy." (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E5 Delegated-act-2023-5303-annex-1_en.pdf`) — supports a combined waste + hazardous-substance scope. ESRS E5-5 itself (DR E5-5, p.7): "The undertaking shall also disclose the total amount of hazardous waste and radioactive waste generated by the undertaking…" (same file) grounds the hazardous-waste arm.
- **Implementation check:** `Underlying Metrics = EN31\nEN32`; Parent = EN0; strategy WEIGHTED_AVERAGE; Formula `Sum (weight * EN31 + weight * EN32)`. Both children exist (rows 26–27). Unit % consistent with averaging two 0–1 ratios. Formula text matches children — no formula drift here (unlike EN1). Cited code `ESRS E5-5` is org-level "Resource outflows" disclosure; it covers the hazardous-waste arm well but the hazardous-**material-share** arm (EN32) is closer to ISO 14021 / RE+20 territory — the parent's single ESRS E5-5 tag is defensible as the aggregate anchor but under-represents the substitution arm.
- **Proposed revision:** "Aggregates the product's handling of hazardous waste and hazardous materials into one score by combining the hazardous-waste minimization rate (EN31) and the hazardous-material share (EN32). Higher scores mean less hazardous waste generated and a smaller share of hazardous materials in the product."
- **Notes:**
  - [minor] Description omits EN32's material-substitution arm and uses "utilization," which has no corresponding child — proposed revision above fixes both.
  - Comment-cell flag (ADAPTED): "Product-level adaptation of org-level ESRS E5-5; aggregates a product-specific hazardous-waste + hazardous-material score."
  - Parent EN0 is outside this batch; not verified here.

### EN31 — Hazardous Waste Minimization Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the reduction in toxic waste generation throughout the product lifecycle. \tTracks efforts to reduce toxic waste." (note the stray `\t` tab and the duplicated second sentence that repeats the Objective cell verbatim)
- **Verdict:** CONSISTENT (text), with a formatting defect — the prose matches the formula `Minimization = (PreviousTime - Actual) / PreviousTime`, i.e. a time-over-time reduction in hazardous-waste mass (EN3-1). Verdict on substance: CONSISTENT; on hygiene: needs a cleanup.
- **Grounding:** ISO 14021 p.34 (7.13.1 Waste reduction): "Reduction in the quantity (mass) of material entering the waste stream as a result of a change in the product, process or packaging." (`data/literature/ISO 14XXX/ISO-14021.pdf`) grounds the "reduction in waste mass over time" framing. GRI 306-3 (cited) p.12: "Total weight of waste generated in metric tons, and a breakdown of this total by composition of the waste." (`data/literature/GRI - Global Reporting Initiative/GRI 306_ Waste 2020.pdf`) — GRI 306-3 is the *waste-generated quantity* disclosure (the input EN3-1), not a minimization *rate*; the rate itself is the author's reduction-over-base-period construction. RE+20 (cited) p.8: "4) Reduction of toxic substances … It aims to quantify the reduction of the use of toxic substances considering RoHS (Restriction of Certain Hazardous Substances)." (`data/literature/Papers/RE+20-...electro-electronic cases.pdf`) — RE+20's indicator is about reducing toxic *substance use*, conceptually adjacent but framed as material/substance reduction rather than waste-stream reduction.
- **Implementation check:** Child EN3-1 (Amount of hazardous waste, kg) exists; Formula `Minimization = (PreviousTime - Actual) / PreviousTime`, then `(Minimization - Min)/(Max - Min)`. "PreviousTime" = a supplied base-period hazardous-waste value (Potential Reference Values: "Value to a given value in time"). Unit % consistent with a normalized ratio. Strategy NORMALIZED_RATIO matches.
- **Proposed revision:** "Measures the percentage reduction in the product's hazardous-waste mass (EN3-1) over time, comparing the current amount against an earlier base-period amount. Higher when less hazardous waste is generated than before."
- **Notes:**
  - [minor] Current text contains a stray `\t` tab between the two sentences and the second sentence ("Tracks efforts to reduce toxic waste") merely restates the Objective cell — drop it from the Description.
  - Citation: GRI 306-3 grounds the *hazardous-waste quantity* input (EN3-1), not the rate. The rate is author-constructed. Consider adding `ISO 14021` (7.13 Waste reduction) which grounds the "reduction in waste mass" framing more directly; keep GRI 306-3 and RE+20.
  - Comment-cell flag (ADAPTED): "Product-level reduction rate built on org-level GRI 306-3 waste-generated quantity + RE+20 toxic-substance reduction; rate construction is author-defined."

### EN32 — Hazardous Material Share  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the toxic materials replaced with less toxic or non-toxic alternatives. Tracks progress in reducing hazardous material usage."
- **Verdict:** DRIFTED — the re-tag noted in the brief changed EN32 to NORMALIZED_RATIO with Formula `1 - (Hazardous Material / Total Material)`. That formula computes the **non-hazardous share of total material mass** (one minus the hazardous fraction), using children EN3-2 (hazardous material mass) and EN3-3 (total material mass). It does **not** measure "materials *replaced* with alternatives" (which would require a baseline/substituted quantity, not a hazardous/total ratio). The description still describes a substitution-tracking metric from the old design; it no longer matches the current `1 − hazardous/total` share computation.
- **Grounding:** RE+20 p.8: "4) Reduction of toxic substances … It aims to quantify the reduction of the use of toxic substances considering RoHS (Restriction of Certain Hazardous Substances)." (`data/literature/Papers/RE+20-...electro-electronic cases.pdf`) — supports the *concept* of quantifying hazardous-substance content/reduction in a product. ISO 14021 p.31 (7.10.1 Reduced resource use): "A reduction in the amount of material, energy or water used to produce or distribute a product…" (`data/literature/ISO 14XXX/ISO-14021.pdf`) grounds material-quantity claims generally. No retrieved source prescribes a "1 − hazardous/total material mass" share formula specifically; the share construction is author-defined.
- **Implementation check:** Children EN3-2 (Amount of hazardous materials, kg) and EN3-3 (Total materials used, kg) both exist (rows 29–30) and **both now carry Parent = EN32** — the EN33→EN32 parent correction in the gap-fix pass is reflected correctly (there is no EN33 row). Formula `1 - (Hazardous Material / Total Material)` = `1 - EN3-2/EN3-3`, a 0–1 share; unit % consistent. Strategy NORMALIZED_RATIO matches. Potential Reference Values cell = "Value of previous Product" — a vestige of the old version-comparison/substitution framing that the current `1 − hazardous/total` formula does **not** use (the formula needs no previous-product value).
- **Proposed revision:** "Measures the share of the product's total material mass that is non-hazardous, computed as one minus the ratio of hazardous-material mass (EN3-2) to total material mass (EN3-3). Higher when a smaller fraction of the product is made of hazardous materials."
- **Notes:**
  - [major] Description describes substitution ("toxic materials replaced with… alternatives") but the current formula computes a static hazardous/total share — reconcile via the proposed revision (or, if substitution-tracking is the true intent, the formula and children must change). As written, description and formula contradict.
  - [minor] Reference cell is **blank**; the concept is groundable. Recommend citing `RE+20` (Reduction of toxic substances) and optionally `ISO 14021` (material-content claims) on this row.
  - [minor] Potential Reference Values "Value of previous Product" is stale relative to the `1 − hazardous/total` formula (no previous-product value is consumed) — remove or replace with a target-band note, matching the Min/Max comment pattern used elsewhere.
  - Comment-cell flag (ADAPTED): "Product-level hazardous-material share; concept adapted from RE+20 toxic-substance reduction / ISO 14021 material claims. Share construction author-defined."

### EN3-1 — Amount of hazardous waste  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total mass of hazardous waste produced throughout the product's lifecycle."
- **Verdict:** CONSISTENT — accurate raw-input definition; matches unit kg and the EN31 formula's `Actual`/`PreviousTime` hazardous-waste inputs.
- **Grounding:** ESRS E5 p.7 (DR E5-5): "The undertaking shall also disclose the total amount of hazardous waste and radioactive waste generated by the undertaking…" (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS E5 Delegated-act-2023-5303-annex-1_en.pdf`). GRI 306 p.12 (306-3): "Total weight of waste generated in metric tons, and a breakdown of this total by composition of the waste." (`data/literature/GRI - Global Reporting Initiative/GRI 306_ Waste 2020.pdf`).
- **Implementation check:** Raw leaf, no formula; Parent = EN31; feeds the EN31 minimization ratio. Unit kg consistent with org-level "metric tons / tonnes" mass disclosures (product-level kg is the adaptation). Life-cycle stages D,U,E.
- **Proposed revision:** keep as-is.
- **Notes:** Comment-cell flag (ADAPTED): "Product-level hazardous-waste mass; org-level basis ESRS E5-5 / GRI 306-3 report tonnes at undertaking level."

### EN3-2 — Amount of hazardous materials  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total mass of hazardous material used throughout the product's lifecycle."
- **Verdict:** CONSISTENT — accurate raw-input definition; matches unit kg and the EN32 numerator (`Hazardous Material`).
- **Grounding:** RE+20 p.8: "4) Reduction of toxic substances … considering RoHS (Restriction of Certain Hazardous Substances)." (`data/literature/Papers/RE+20-...electro-electronic cases.pdf`) grounds the hazardous/toxic material concept at product level.
- **Implementation check:** Raw leaf; Parent = **EN32** (the EN33→EN32 correction is reflected). Feeds the EN32 share numerator. Unit kg, stages S,M. Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none beyond the parent-correction confirmation. Optionally cite `RE+20`/`ISO 14021` consistently with EN32 if leaf-level citations are desired (not required for raw inputs).

### EN3-3 — Total materials used  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total mass of materials used throughout the product's lifecycle."
- **Verdict:** CONSISTENT — accurate raw-input definition; matches unit kg and the EN32 denominator (`Total Material`).
- **Grounding:** GRI 301 concept (materials by weight) is the natural anchor; within this batch's cited corpus, ISO 14021 p.31 (7.10.1): "A reduction in the amount of material… used to produce or distribute a product…" (`data/literature/ISO 14XXX/ISO-14021.pdf`) confirms total-material-mass is a recognised quantity. (GRI 301-3 exists in References.tsv row 73 if a dedicated materials code is wanted.)
- **Implementation check:** Raw leaf; Parent = **EN32** (correction reflected). Feeds the EN32 denominator. Unit kg, stages P,S,M. Consistent. EN3-2 ⊆ EN3-3 (hazardous mass is a subset of total mass) so the `1 − EN3-2/EN3-3` share is in [0,1] as intended.
- **Proposed revision:** keep as-is.
- **Notes:** none. (Sanity: EN3-2 and EN3-3 must use the same mass basis/boundary for the EN32 share to be meaningful — worth a one-line Comment on EN32 if not already implied.)

---

## Batch summary

| ID | Name | Verdict | Description action |
|----|------|---------|--------------------|
| EN3 | Hazardous Material & Waste Management Score | DRIFTED | rewrite to name both arms (waste minimization + material share); drop "utilization" |
| EN31 | Hazardous Waste Minimization Rate | CONSISTENT (formatting defect) | clean stray `\t`, drop duplicated Objective sentence |
| EN32 | Hazardous Material Share | DRIFTED | rewrite from substitution-tracking to `1 − hazardous/total` share |
| EN3-1 | Amount of hazardous waste | CONSISTENT | keep as-is |
| EN3-2 | Amount of hazardous materials | CONSISTENT | keep as-is (parent EN33→EN32 confirmed) |
| EN3-3 | Total materials used | CONSISTENT | keep as-is (parent EN33→EN32 confirmed) |

**Counts:** CONSISTENT 4 (EN31 with a formatting defect; EN3-1/2/3), DRIFTED 2 (EN3, EN32),
ADAPTED 0 standalone (ADAPTED flags attached to EN3/EN31/EN32/EN3-1 as product-level
adaptations), UNVERIFIABLE 0. No SOURCE-NOT-FOUND (all cited codes resolve and all files
exist).

**Parent-correction verification:** EN3-2 and EN3-3 both carry Parent = EN32 (no EN33 row
exists) — the EN33→EN32 correction is correctly reflected, and EN32's children list
(`EN3-2\nEN3-3`) matches. EN32's NORMALIZED_RATIO re-tag and `1 − hazardous/total` formula
are internally consistent (children + unit), but the **Description still describes the old
substitution metric** — the main drift to fix.

**Proposed adjacent-cell fixes (drift beyond Description):**
1. [major] EN32 Reference cell is blank — add `RE+20` (and optionally `ISO 14021`) to ground the hazardous-material concept.
2. [minor] EN32 Potential Reference Values "Value of previous Product" is stale (the `1 − hazardous/total` formula consumes no previous-product value) — remove or replace with the target-band note.
3. [minor] EN31 Description contains a stray `\t` tab and a duplicated Objective sentence — clean both.
4. [minor] EN31 Reference — consider adding `ISO 14021` (7.13 Waste reduction) alongside the existing `GRI 306-3` + `RE+20`; GRI 306-3 grounds the waste-quantity input, not the rate.
5. No Formula-text drift found in this family (contrast EN1, where the displayed formula referenced an archived child). EN3 / EN31 / EN32 formula texts match their current children.

**Decisions needed (human):**
- EN32: confirm intent — is the metric the static **hazardous-material share** (`1 − hazardous/total`, as the current formula computes) or **substitution progress vs. a previous product** (as the current Description and the stale "Value of previous Product" suggest)? The proposed revision assumes the former (matches the live formula). If substitution is intended, formula + children must change instead.
- EN3 / EN31 / EN32 / EN3-1: approve the ADAPTED Comment-cell flags (product-level adaptations of org-level ESRS E5-5 / GRI 306-3).

**Limits of this run:** Grounding quotes are confined to the cited/relevant files actually
opened (ESRS E5, GRI 306 Waste 2020, ISO 14021, RE+20). No claim is made about ESRS E2 or
GRI 305 (not cited on these rows and not opened). Parent EN0 and the weight distribution
were not audited (out of scope). The EN32 "previous product" intent question cannot be
resolved from the snapshot alone — flagged for the author.


---

## EN4 — Water Footprint

### EN4 — Water Footprint Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the aggregation of water footprint assessment indicator compared to
  another timeframe or version. Indicators includes: withdrawal, discharge, consumption, and
  emissions stated in 14046. Implicitly it contains the amount of reused water."
- **Verdict:** DRIFTED — the prose describes a different construct than the current wiring.
  The Formula text references EN44 ("Sum (weight * EN41 + … + weight * EN44)") but the
  current `Underlying Metrics` are **EN41\nEN42\nEN43** only (EN44 is archived, Parent=None,
  not a child of EN4). The enumerated indicator list ("withdrawal, discharge, consumption,
  and emissions … stated in 14046") is mostly GRI 303's triad, not ISO 14046's framing, and
  "emissions" + "reused water" are not computed by any child of EN4.
- **Grounding:**
  - ISO 14046 p.11: *"is modular (i.e. the water footprint of different life cycle stages can
    be summed to represent the water footprint)"* (`data/literature/ISO 14XXX/ISO-14046.pdf`)
    — grounds *aggregation* of a water footprint, but by life-cycle stage, not by the
    intensity/reduction/independence children EN4 actually combines.
  - The withdrawal/discharge/consumption triad the prose attributes to "14046" is actually
    **GRI 303's** structure: GRI 303 p.3: *"Disclosure 303-3 Water withdrawal … 303-4 Water
    discharge … 303-5 Water consumption"*
    (`data/literature/GRI - Global Reporting Initiative/GRI 303_ Water and Effluents 2018.pdf`).
    ISO 14046 frames water by withdrawal vs. consumption — p.16: *"water withdrawal …
    anthropogenic removal of water from any water body …"* and (Note 2) *"The term 'water
    consumption' is often used to describe water removed from, but not returned to, the same
    drainage basin."* ISO 14046 does **not** make "discharge" or "emissions" primary footprint
    categories.
  - Caution on the "compared to … version" + weighted framing: ISO 14046 p.59: *"If weighting
    is applied, the results shall not be used as a basis for a comparative assertion that is
    intended to be disclosed to the public."* The KPI is internal, but a public eco-claim
    built on this weighted score would conflict with that clause — worth a Comment flag.
- **Implementation check:** `Underlying Metrics = EN41\nEN42\nEN43`; strategy
  WEIGHTED_AVERAGE; Parent EN0; Unit %. The three children are *normalized performance ratios*
  (intensity, reduction, independence), not raw withdrawal/discharge/consumption volumes. The
  description's indicator enumeration describes the *inputs to a water inventory*, not the
  *score's three child KPIs*. Classic gap-fix drift: children were reorganised (EN44 dropped
  to archived) but the prose and Formula text still reference the old EN41…EN44 grouping.
- **Proposed revision:** "Aggregates the product's water-footprint performance into one score
  by combining its water-use intensity (EN41), water-footprint reduction over time (EN42), and
  water-independence ratio (EN43). Provides an actionable overview for tracking and improving
  the product's water performance across its life cycle."
- **Notes:** Composite/parent — no single literature source expected; ISO 14046 grounds the
  water-footprint concept and its life-cycle aggregation only.
  - [major] Formula text "Sum (weight * EN41 + … + weight * EN44)" must read
    "Sum (weight * EN41 + weight * EN42 + weight * EN43)" — EN44 is archived and not a child.
  - [minor] Reference cell cites `ESRS E3-4`, `GRI 303`, `ISO 14046`, `ISO 14044` — **all four
    now resolve to Labels in References.tsv** (this fixes prior finding #2/#3 from
    `reviews/EN4-water-phases.md`; `ESRS E2-4` has already been corrected to `ESRS E3-4`).
    `ESRS E3-4` is "Water consumption" (ESRS E3 p.1) — correct standard for a water KPI.
  - Comment-flag suggestion: "Score attributes the withdrawal/discharge/consumption triad to
    ISO 14046, but that triad is GRI 303's structure; ISO 14046 frames water by withdrawal vs.
    consumption. 'Emissions'/'reused water' are not computed by EN41/42/43."

### EN41 — Water Footprint Intensity  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures water use per unit of output or produced units. Normalizes water use
  for comparison and benchmarking."
- **Verdict:** CONSISTENT — text matches the Formula `Intensity [m3/fu] = Water Use / Total
  Produced Units`, then `(Intensity - Min)/(Max - Min)`, and the child EN4-4 (Absolute Water
  Footprint, m3) divided by a produced-units figure (R2-7).
- **Grounding:** ISO 14046 p.11 (water footprint summable per life-cycle stage, quote above);
  the per-functional-unit normalization mirrors EN15804's functional-unit reporting — EN15804
  p.48: *"Net use of fresh water  m3"* (declared per module / functional unit)
  (`data/literature/EPD/EN15804+A2.pdf`). The Min/Max normalization band itself is an author
  construct (no standard provides a 0–1 water-intensity range).
- **Implementation check:** `Underlying Metrics = EN4-4\nR2-7`; EN4-4 exists (Absolute Water
  Footprint, m3); R2-7 is cross-domain (produced units) and not verified in this batch. Unit %
  is the normalized-ratio output; the intermediate intensity is m3/fu. Consistent.
- **Proposed revision:** "Measures the product's water footprint (EN4-4) per functional unit
  / unit of output (R2-7), normalized to a 0–1 score. Enables benchmarking of water-use
  efficiency against a target band."
- **Notes:** [minor] No Reference code cited on the row; the intensity construct is grounded
  by ISO 14046 / EN15804 (both resolve) — optionally cite one. Min/Max band is author-set
  (UNVERIFIABLE endpoints; legitimate) — `Potential Reference Values` already says "Target
  Value: Min, Max".

### EN42 — Water Footprint Reduction  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the percentage reduction in total water use compared to a previous
  time."
- **Verdict:** CONSISTENT — matches `Reduction = (PreviousTime - Now) / PreviousTime`, then
  normalized; child EN4-4 (total water footprint, m3) compared to its previous-period value.
- **Grounding:** ISO 14046 p.11 (water footprint concept/summable). GRI 303 p.7 confirms
  reduction-over-time as the management aim: *"An organization can reduce its water withdrawal,
  consumption, discharge, and associated impacts through efficiency measures, such as water
  recycling and reuse, and process redesign."* No standard prescribes the specific
  base-period reduction ratio (author construct, defensible).
- **Implementation check:** `Underlying Metrics = EN4-4`; `Potential Reference Values =
  Target Value: Min, Max\nTimeframed`; Comment notes Min/Max seeded 0/1 (already a 0–1 score).
  "Now" and "PreviousTime" are EN4-4 at two timeframes (the previous-period value is a supplied
  input, not a separate child). Consistent.
- **Proposed revision:** "Measures the percentage reduction in the product's total water
  footprint (EN4-4) versus an earlier base period. Higher means greater water savings over
  time; tracks progress toward the product's water-reduction targets."
- **Notes:** [minor] "previous time" value is a supplied per-product input, not a child metric
  — confirm the intended base period per product. No Reference code cited; reduction-over-time
  is grounded by GRI 303 p.7 (resolves) — optionally cite.

### EN43 — Water Independence Ratio  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the share of the product's water footprint that is not blue water
  (green + gray), i.e. its independence from freshwater withdrawal. Higher means less reliance
  on scarce surface and groundwater resources."
- **Verdict:** CONSISTENT (with one grounding caveat) — text matches the post-flip Formula
  `Independence = 1 - Blue/Absolute = (Green + Gray)/Absolute Water Footprint` and the children
  EN4-1 (Blue) + EN4-4 (Absolute). The gap-fix direction flip (Comment dated 2026-06-28) is
  faithfully reflected in Name, Description, and Formula. Min/Max seeded 0/1 (bounded ratio).
- **Grounding:**
  - The blue/green/gray scheme is **not** in ISO 14046 (searched "blue/green/grey/gray water"
    → no matches). It is defined in TF+25 p.6: *"The water footprint analysis of a system mainly
    includes blue water footprint, green water footprint and gray water footprint … blue water
    footprint is defined as the culture water directly consumed in the production process; green
    water footprint refers to the difference between the evaporation loss of raw materials and
    the average rainfall; gray water footprint is the content of pollution such as fertilizer
    contained in the discharged water."*
    (`data/literature/Papers/TF+25-…macro-algae… .pdf`).
  - ISO 14046 p.16 grounds blue water as the scarce-freshwater axis: *"water withdrawal …
    anthropogenic removal of water from any water body or from any drainage basin."*
- **Implementation check:** `Underlying Metrics = EN4-1\nEN4-4`; both exist; Formula consistent;
  Unit % (bounded 0–1). The flip from "Dependency = Blue/Absolute" to "Independence =
  (Green+Gray)/Absolute" correctly makes it higher=better under the ascending normalization
  (matches Comment rationale). **Grounding caveat:** the description equates "not blue water"
  with "independence from freshwater withdrawal," but (a) TF+25 defines **blue = water directly
  *consumed*,** not withdrawn — the "withdrawal" wording is slightly off-source; and (b)
  **gray water is dilution of pollution in *discharged* water**, so counting gray water toward
  "independence from freshwater" is a conceptual stretch (gray water is a pollution-load proxy,
  not a benign/independent source). Defensible as an author construct but should be flagged.
- **Proposed revision:** "Measures the share of the product's total water footprint (EN4-4) that
  is not blue water (i.e. green + gray, EN4-2 + EN4-3): `1 - Blue/Absolute`. Higher indicates
  less reliance on directly-consumed surface/groundwater (blue water, EN4-1). Note: the gray
  component represents a pollution-dilution load, so this ratio approximates — rather than
  strictly measures — freshwater independence."
- **Notes:** [minor] Align "withdrawal" wording with the cited definition (TF+25 defines blue
  water as *consumed*, ISO 14046 distinguishes withdrawal from consumption). [minor] No
  Reference code on the row; the blue/green/gray definitions trace to TF+25 (now resolves) and
  `waterfootprintnetwork` (does NOT resolve — see fixes) — consider citing TF+25 on EN43 / the
  EN4-1/2/3 leaves. Comment-flag suggestion: "Gray water is a pollution-dilution proxy, not an
  independent freshwater source; including it in the 'independence' numerator is an author
  simplification."

### EN44 — Lifecycle Water Footprint Ratio  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY — ARCHIVED]
- **Current:** "Measures the total water use across all lifecycle stages (e.g., raw material
  extraction, production, use, disposal)."
- **Verdict:** DRIFTED (minor, archived) — the description says "total water use across all
  lifecycle stages," but the Formula reads "Avg (Stage Water Footprint)" while the strategy is
  now WEIGHTED_AVERAGE_STRATEGY. "Total," "Avg," and "weighted average" are three different
  operations; the prose and the Formula text disagree with each other and with the tag. (The
  five children carry equal Weight 0.2, so a weighted average currently equals a plain average,
  but the wording should be reconciled.)
- **Grounding:** ISO 14046 p.11: *"is modular (i.e. the water footprint of different life cycle
  stages can be summed to represent the water footprint)"* — supports a per-stage life-cycle
  decomposition. EN15804 p.48: *"Net use of fresh water  m3"* declared per information module
  (A/B/C stages). So a per-stage construct is legitimate; the standards support *summing*
  stages to a total (ISO 14046 p.11), which is closer to the prose's "total" than to "Avg".
- **Implementation check:** `Underlying Metrics = EN441\nEN442\nEN443\nEN444\nEN445` (the five
  per-stage ratios), Parent=None, ARCHIVED, not in score. Per `reviews/EN4-water-phases.md`
  (re-verified context only), all five children currently wire to the same type-children
  EN4-1/4-2/4-3, so each phase degenerates to the whole-product total and the weighted average
  collapses to EN4-4 — the row cannot deliver per-stage hotspots until per-stage water inputs
  are wired. Row is out of score.
- **Proposed revision:** keep the intent but reconcile to the strategy:
  "Aggregates the product's per-stage water footprints (sourcing EN441, production EN442,
  distribution EN443, use & maintenance EN444, end-of-life EN445) into one weighted-average
  lifecycle ratio, to identify which stage dominates water use. (Archived — requires per-stage
  water inputs.)"
- **Notes:** [minor] Formula text "Avg (Stage Water Footprint)" should read "Weighted average
  of stage water-footprint ratios" to match the WEIGHTED_AVERAGE tag (or note weights are
  equal 0.2). [major, deferred] children EN441–445 need per-stage water inputs, not the
  type-children EN4-1/2/3 — tracked in `reviews/EN4-water-phases.md` (the five-phase batch),
  not re-litigated here. Since archived/out-of-score, this batch only flags it.

### EN4-1 — Blue Water Footprint  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Volume of freshwater withdrawn from surface or groundwater resources."
- **Verdict:** ADAPTED — recognizable blue-water definition; minor wording divergence from the
  cited source (withdrawal vs. consumption).
- **Grounding:** TF+25 p.6: *"blue water footprint is defined as the culture water directly
  consumed in the production process"* (`data/literature/Papers/TF+25-…macro-algae… .pdf`).
  ISO 14046 p.16: *"water withdrawal … anthropogenic removal of water from any water body or
  from any drainage basin"* and (Note 2) *"'water consumption' … water removed from, but not
  returned to, the same drainage basin."* The KPI says "withdrawn"; TF+25 (the source defining
  the scheme) says "consumed." Surface/groundwater scoping is consistent with ISO 14046's
  water-body framing.
- **Implementation check:** Raw leaf, Formula None, Unit m3; feeds EN4-4, EN43, and EN441–445.
  Consistent as a raw input.
- **Proposed revision:** "Volume of freshwater (surface or groundwater) consumed over the
  product's life cycle — i.e. withdrawn and not returned to the same basin." (Aligns 'withdrawn'
  with the consumption framing in TF+25 p.6 / ISO 14046 p.16; keep if the product genuinely
  measures gross withdrawal rather than consumption — confirm intent.)
- **Notes:** [minor] "withdrawn" vs. source's "consumed" — decide which the figure actually is;
  blue-water footprint in the literature is a *consumptive* figure. [minor] References
  `waterfootprintnetwork` (no Label, no PDF — SOURCE-NOT-FOUND) and `TF+25` (now resolves to a
  Label, paper present). Cite TF+25; document or replace `waterfootprintnetwork`.

### EN4-2 — Green Water Footprint  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Volume of rainwater consumed (stored in soil or vegetation) during a product's
  lifecycle."
- **Verdict:** ADAPTED — recognizable green-water definition (rainwater/soil-moisture), faithful
  to the concept.
- **Grounding:** TF+25 p.6: *"green water footprint refers to the difference between the
  evaporation loss of raw materials and the average rainfall."* The KPI's "rainwater consumed,
  stored in soil or vegetation" is the standard green-water (soil-moisture / evapotranspiration)
  framing — consistent in substance with TF+25's rainfall/evaporation basis.
- **Implementation check:** Raw leaf, Unit m3; feeds EN4-4 and EN441–445 (note: not EN43, which
  uses EN4-1 + EN4-4 only — green enters EN43 implicitly via the Absolute total). Consistent.
- **Proposed revision:** keep as-is. (Optional, to match TF+25 wording: "Volume of rainwater
  (soil moisture) consumed via evapotranspiration during the product's life cycle.")
- **Notes:** [minor] Same reference situation as EN4-1: `waterfootprintnetwork` SOURCE-NOT-FOUND;
  `TF+25` resolves. Cite TF+25.

### EN4-3 — Gray Water Footprint  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Volume of water required to dilute pollutants to meet water quality standards."
- **Verdict:** ADAPTED — accurate gray-water (pollution-assimilation) definition.
- **Grounding:** TF+25 p.6: *"gray water footprint is the content of pollution such as fertilizer
  contained in the discharged water"*, computed (Eq. A.7) as `W_F-grey = aA_ppl / (C_max -
  C_nat)` — i.e. the freshwater volume needed to dilute the pollutant load to the maximum
  acceptable concentration. The KPI's "volume of water required to dilute pollutants to meet
  water quality standards" matches this dilution-volume definition precisely.
- **Implementation check:** Raw leaf, Unit m3; feeds EN4-4 and EN441–445. Consistent.
- **Proposed revision:** keep as-is. (Strong match to TF+25 p.6.)
- **Notes:** [minor] Same reference situation: `waterfootprintnetwork` SOURCE-NOT-FOUND; `TF+25`
  resolves and is a good anchor for this definition. Note for EN43: gray water is a
  pollution-dilution load, not an independent freshwater source (see EN43 flag).

### EN4-4 — Absolute Water Footprint  [Level 5, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current:** "The total water footprint associated with the product across its lifecycle"
- **Verdict:** ADAPTED — product-level total water footprint, summed from the three water types;
  faithful to ISO 14046's summable footprint.
- **Grounding:** ISO 14046 p.11: *"is modular (i.e. the water footprint of different life cycle
  stages can be summed to represent the water footprint)"*. TF+25 p.6 confirms the total is the
  sum of blue + green + gray water footprints. EN15804 p.46 reports water as a single per-module
  indicator: *"Water (user) deprivation potential, deprivation-weighted water consumption (WDP)
  m3 world eq. deprived"* — i.e. standards report one water-consumption figure, not a
  blue/green/gray split; the type split is the Water Footprint Network / TF+25 scheme.
- **Implementation check:** `Underlying Metrics = EN4-1\nEN4-2\nEN4-3`; Formula "Sum of blue,
  green, gray water footprint"; strategy SUM_AGGREGATE (re-tagged from RAW_VALUE — confirmed and
  correct: it sums three children). Children all exist; Unit m3 consistent with children.
  Parents EN41/EN42/EN43. Consistent.
- **Proposed revision:** keep as-is. (Optional, to make wiring explicit: "The product's total
  life-cycle water footprint, summed from its blue (EN4-1), green (EN4-2) and gray (EN4-3)
  water footprints.")
- **Notes:** [minor] Description says "across its lifecycle" but the sum is over water *types*,
  not life-cycle stages (the stage decomposition is EN44's job). Minor wording; the figure is a
  whole-product total. Note that ISO 14046 / EN15804 report a single deprivation-weighted water
  figure (WDP), whereas this KPI sums an unweighted m3 blue+green+gray total — a different (and
  simpler) construct than the standards' impact-weighted indicator; defensible as a raw-volume
  total, flag if a WDP-style scarcity weighting is ever expected.

---

## Batch summary

**Counts (9 rows):** CONSISTENT 3 (EN41, EN42, EN43); DRIFTED 2 (EN4, EN44); ADAPTED 4
(EN4-1, EN4-2, EN4-3, EN4-4); UNVERIFIABLE 0 (Min/Max bands on EN41/42/43 are author-set
endpoints — legitimate, noted but not a row-level verdict).

**Proposed description rewrites:** EN4 (drop EN44 from child list + fix triad attribution),
EN44 (reconcile total/Avg/weighted-average wording). Light optional clarifications offered for
EN41, EN42, EN43, EN4-1, EN4-2, EN4-4; EN4-3 keeps its text (strong match to TF+25).

**Adjacent-cell (Formula / citation) fixes proposed:**
- EN4 Formula text "… + weight * EN44" → "EN41 + EN42 + EN43" (EN44 archived, not a child).
- EN44 Formula "Avg (Stage Water Footprint)" → weighted-average wording (or note equal weights).
- Cite TF+25 on EN43 / EN4-1 / EN4-2 / EN4-3 (now resolves); document/replace
  `waterfootprintnetwork`.

**Top decisions needed from you:**
1. **EN4 child list + Formula (major).** Confirm EN44 is intentionally excluded from EN4
   (archived, Parent=None). If so, correct the Formula text and the description's indicator
   enumeration (drop withdrawal/discharge/consumption/emissions/reused-water language — those
   are inventory inputs, not the EN41/42/43 children).
2. **EN4-1 / EN43 "withdrawal" vs "consumption" (minor, conceptual).** Decide whether blue
   water is measured as gross *withdrawal* (current EN4-1 wording) or *consumption* (TF+25 /
   ISO 14046 definition). This propagates into EN43's "independence from freshwater withdrawal"
   phrasing. Recommend aligning to *consumption* per source.
3. **EN43 gray-water-in-numerator (minor).** Confirm you accept counting gray water (a
   pollution-dilution load) toward "water independence." Recommend a Comment flag noting it is
   an author simplification, or excluding gray from the independence numerator.
4. **`waterfootprintnetwork` source (major).** Still SOURCE-NOT-FOUND (no Label, no PDF). Either
   add a documented Water Footprint Network reference, or re-anchor EN4-1/2/3 to TF+25 (which is
   now in References.tsv and does define the scheme).

### SOURCE-NOT-FOUND codes
- `waterfootprintnetwork` — no Label in References.tsv and no file in `data/literature/`. It is
  the de-facto origin of the blue/green/gray scheme but is undocumented in the bibliography.
  (Flagged, not invented.)

### Resolved since prior review (`reviews/EN4-water-phases.md`)
- `ISO 14046`, `ISO 14044`, `GRI 303`, `ESRS E3-4`, `TF+25` now all have Labels in
  References.tsv (prior findings #2/#3/#5 about orphan codes are resolved). `ESRS E2-4` →
  `ESRS E3-4` correction already applied on EN4.
- Prior claim "TF+25 does not define blue/green/gray" is **withdrawn** — TF+25 p.6 defines all
  three (re-verified this run).

### Limits of this run
- Min/Max normalization bands on EN41/EN42/EN43 have no literature anchor (author/target-policy
  construct); I verified only that the standards specify *what* to quantify, not a 0–1 band.
- R2-7 (produced-units input to EN41) is cross-domain and was not opened/verified in this batch.
- EN441–445 are archived and out of scope; their type-vs-stage wiring defect is summarised for
  EN44 context only and remains tracked in `reviews/EN4-water-phases.md`.
- ISO 14046 / EN15804 PDFs are bilingual (DE/EN); quotes are the English sentences as returned
  by the search tool. EN15804's water indicator (WDP, deprivation-weighted) differs from the
  unweighted m3 blue+green+gray sum the KPIs use — noted under EN4-4, not treated as a defect.


---

## EN5 / EN9 / EN0 — Biodiversity, PEF Single Score, Domain Root

### EN5 — Biodiversity Impact Score  [Level 2, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the product's impact on local ecosystems and biodiversity."
- **Verdict:** CONSISTENT (with one missing-citation flag) — the prose matches the formula
  `Impact = Quality Change * Land Use per FU`, then `(Impact - Min)/(Max - Min)`, and the two
  children EN5-1 (Land Quality Change) + EN5-2 (Land Use per FU).
- **Grounding:**
  - JPL+19 p.2: the UN Environment Life Cycle Initiative "deﬁned the impacts of land use as a
    function of quality (Q), area (A) and time (t) … the quality can be any indicator on which
    land use of a speciﬁc area has an impact over a speciﬁc period … as presented in this
    article, biodiversity." (`data/literature/Papers/JPL+19-Valuing Biodiversity in Life Cycle Impact Assessment.pdf`)
  - JPL+19 p.3: "The change of the quality (∆Q) can either be temporary if it is reversible,
    or permanent…" — i.e. EN5-1 = ∆Q.
  - PEF (the source EN9 cites) p.15 glossary, "Land use" entry: "Land occupation considers the
    effects of the land use, the amount of area involved and the duration of its occupation
    (changes in soil quality multiplied by area and duration)."
    (`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`) — this is *exactly* EN5's
    `Quality Change × (area × duration)` product.
  - GRI 101 p.3 lists "Disclosure 101-7 Changes to the state of biodiversity" and (p.3)
    "Table 2. Methods to measure or estimate ecosystem condition"; p.4 "An organization can
    have impacts on biodiversity through its activities…" — grounds the *concept* of measuring
    biodiversity impact, at org/site level.
- **Implementation check:** Children EN5-1 (∆Q, unit BVI) and EN5-2 (area×time, unit m²a/FU)
  both exist. Formula multiplies them → a land-use biodiversity impact, then min–max
  normalised to a 0–1 (%) score. Unit `%` is consistent with a normalised ratio (and with the
  NORMALIZED_RATIO_STRATEGY peers EN11/EN12). The phrase "**local** ecosystems … **around its
  production area**" (Objective cell) is slightly narrower than the method, which is a
  cradle-to-grave land-occupation impact across the supply chain (JPL+19 p.2: impacts "often
  take place far from the location of consumption"), but this is minor framing, not a defect.
- **Proposed revision:** "Measures the product's land-use impact on biodiversity, computed as
  the change in ecological land quality/naturalness (EN5-1) multiplied by the land area
  occupied over time per functional unit (EN5-2), then normalised to a 0–1 score. Based on the
  land-use Quality × Area × Time framework (higher score = lower biodiversity impact)."
- **Notes (proposed adjacent fixes + flags):**
  - [minor] **Missing citation:** EN5 cites `GRI 101\nJQ+25\nJPL+19` but the formula it actually
    implements is the LCA land-use Q×A×t model. JPL+19/JQ+25 ground that method well; GRI 101
    grounds only the *concept*. Consider adding `EUPEF+21` (PEF "Land use" EF category — the
    p.15 quote above is verbatim the formula) and optionally `ESRS E4` (see below) so the cited
    set matches the implemented method. Not a blocker — current cites are defensible.
  - [minor, optional] **ESRS E4** is *not* cited on any EN row but directly supports this KPI:
    DR E4-5 "Impact metrics related to biodiversity and ecosystems change" (E4 PDF p.8), and
    p.8 §36 "If the undertaking has identified material impacts with regards to land-use change
    … it may also disclose their land-use **based on a Life Cycle Assessment**." This is the
    org-level reporting hook for exactly EN5's product-level LCA land-use metric → ADAPTED
    grounding if added (org→product). Recommend adding to the Reference cell or a Comment flag;
    do not force it.
  - [minor] Objective wording "around its production area" understates the value-chain scope —
    consider "across its life cycle" to match JPL+19.
  - **Comment-cell flag (proposed):** "Land-use biodiversity impact via Q×A×t (JPL+19/JQ+25);
    GRI 101 / ESRS E4 ground the concept at org level (adapted to product)."

### EN5-1 — Land Quality Change  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Measures the difference in ecological quality (or \"naturalness\") of land
  before and after it is used for a specific purpose."
- **Verdict:** CONSISTENT — verbatim-faithful to the cited BVI/naturalness method.
- **Grounding:**
  - JPL+19 p.1 (abstract): the method "oﬀers a default valuation of biodiversity based on
    **naturalness**." p.3: "change from a reference situation (Qref) to another quality status…
    The change of the quality (∆Q)…" — EN5-1 = ∆Q, with naturalness as the quality indicator.
    (`…/Papers/JPL+19-…pdf`)
  - JQ+25 p.2: characterization factors "calculated in Excel based on the **default naturalness
    levels** provided by Fehrenbach et al. (2019) … following the **Biodiversity Value Increment
    (BVI) method**." (`…/Papers/JQ+25-…pdf`)
- **Implementation check:** Raw leaf, no formula; Unit `BVI` (the BVI characterization-factor
  unit — a legitimate unit label, **not** a reference code, so no orphan-code issue). Reference
  `JQ+25\nJPL+19`, both resolve. Feeds EN5 as the ∆Q (quality) factor. Description matches the
  ∆Q-via-naturalness definition.
- **Proposed revision:** keep as-is. (Optional tightening: "Measures the change in ecological
  land quality ('naturalness', ∆Q) caused by occupying/transforming the land for production —
  the per-area biodiversity characterization factor (BVI method).")
- **Notes:** Faithful to JPL+19/JQ+25; no defect. The `Objective/Goal` cell is `None` (peers
  EN5/EN5-2 differ — EN5-2 also `None`); leaving leaf objectives blank is consistent with other
  raw leaves, [minor] only if you want parity.

### EN5-2 — Land Use per Functional Unit  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Measures the amount of land used involved in manufacturing the product"
- **Verdict:** ADAPTED — faithful to the area×duration inventory flow; unit and "pt" note
  resolved via PEF; current prose under-specifies the time dimension.
- **Grounding:**
  - JPL+19 p.4: "the area (A) and the duration (∆t) of a land-using process can be understood
    as inventory ﬂows." (`…/Papers/JPL+19-…pdf`)
  - JQ+25 p.2: "Each characterization factor refers to **1 m² of annual land occupation**…"
    — i.e. m²·a, the unit EN5-2 carries (`m2a / FU`). (`…/Papers/JQ+25-…pdf`)
  - PEF p.15: "the amount of area involved and the **duration** of its occupation" — confirms
    the area×time basis; the EN9 Comment's "EN5-2 land use uses the 'pt' indicator" refers to
    the PEF EF "Land use" category whose result is a dimensionless soil-quality-index point
    (Pt). (`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf` p.15)
- **Implementation check:** Raw leaf; Unit `m2a / FU` (area × time per functional unit) —
  correct for the A·∆t inventory flow that, multiplied by EN5-1's ∆Q, gives the EN5 impact.
  Reference `JQ+25\nJPL+19`, both resolve. Comment "A part of PEF Impact Factor of Land Use
  (Pt.)" is consistent with PEF. **Caveat:** the EN9 Comment says EN9 should consume the land-use
  **'pt'** indicator (the characterised PEF result), **not** the raw `m²a/FU` — i.e. EN5-2's raw
  value must be characterised (×CF, the BVI/EF factor) before EN9. This is a wiring nuance, not
  a description defect (see EN9 Notes).
- **Proposed revision:** "Measures the quantity of land occupied to produce one functional
  unit of the product, expressed as area × occupation time (m²·a / FU). Combined with the land
  quality change (EN5-1) it yields the land-use biodiversity impact."
- **Notes:**
  - [minor] Current text "amount of land used involved in manufacturing" omits the **time**
    dimension that the unit (m²**a**) and both sources require — the proposed revision restores it.
  - [minor] "involved in manufacturing" is narrower than the life-cycle land occupation the
    method covers; "to produce one functional unit" is more faithful.
  - **Comment-cell flag (proposed):** keep the existing "part of PEF Land Use (Pt.)" note; add
    "raw m²a must be characterised (×CF) before feeding the PEF single score (EN9)."

### EN9 — PEF Single Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY (standalone, parent=None)]
- **Current:** "Measures the overall (EU) PEF performance of a product. The resulting score by
  itself does not represent anything and needs to be compared to another product's PEF single
  score."
- **Verdict:** ADAPTED / DRIFTED on the Formula text — the *description* is consistent with the
  PEF single-score concept and re-verifies cleanly against the now-present PEF PDF; but the
  **Formula cell text and the `WEIGHTED_AVERAGE_STRATEGY` tag describe a normalise-then-weight
  pipeline that the equal-weight average strategy does not itself implement** (carried over from
  `reviews/EN-impact-pef.md`). The Comment cell already documents the intended fix (enter EF
  normalisation factor as Target Max, EF weighting factor as Weight), so the *intent* is now
  captured; the prose should name that pipeline.
- **Grounding (RE-VERIFIED this run against the cited EUPEF+21 PDF — it IS in the corpus):**
  - PEF p.1: the 2021 update includes "(4) inclusion of **normalisation and weighting**".
    (`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`)
  - PEF p.16 glossary, "Normalisation": "after the characterisation step, normalisation is the
    step in which the life cycle impact assessment results are **divided by normalisation factors
    that represent the overall inventory of a reference unit (e.g. a whole country or an average
    citizen)**." → grounds EN9's "normalized to a global average person's emissions over one year."
  - PEF p.20 glossary, "Weighting": "PEF results are **multiplied by a set of weighting factors
    (in %), which reflect the perceived relative importance**…" → grounds "then weighted as
    instructed in the EF guidelines" and the Comment's "EF weighting factor as its Weight."
  - PEF p.8 ToC: §5.2 "Normalisation and weighting" (5.2.1 Normalisation of EF results, 5.2.2
    Weighting of EF results) — the operational section EN9 points to.
- **Implementation check:** `Underlying Metrics = EN1\nEN5\nEN6\nEN7\nEN8`; `Parent = None`
  (standalone, correctly unwired from EN0 per gap-fix). Strategy `WEIGHTED_AVERAGE_STRATEGY`,
  Weight 0.1112. The children are mixed-unit characterised scores (kg CO₂eq, biodiversity
  impact, and the EN6/EN7/EN8 mixed-unit sub-scores), so a *raw* weighted average is not a valid
  PEF single score (ISO 14044 / PEF require normalise → weight → sum across categories — see
  `reviews/EN-impact-pef.md` Q1). The Comment cell now prescribes the workaround (per-child EF
  normalisation factor as Target Max with Min=0 ⇒ division by NF; EF weighting factor as Weight),
  which *operationalises* normalise-then-weight inside the weighted-average machinery — this is
  the right target and resolves the prior blocker provided those EF factor values are entered.
- **Proposed revision:** "The product's PEF (EU Environmental Footprint) single score: each
  contributing impact category (climate EN1, biodiversity/land use EN5, pollution EN6, toxicity
  EN7, resource use EN8) is first normalised against a reference (a global average person, one
  year) and then weighted by its EF importance factor, and the weighted results are summed. The
  absolute value is not meaningful on its own; it is used to benchmark one product against
  another."
- **Notes:**
  - [major, from EN-impact-pef.md] The single score is only valid if EN9 (and the EN6/EN7/EN8
    sub-scores) consume **normalised** results, not raw mixed-unit values. The Comment now
    encodes the NF/WF-via-Target-Max/Weight mechanism — keep it; verify each child carries its
    EF normalisation factor (Target Max) and EF weighting factor (Weight). Until those values
    are entered, the score is structurally correct but numerically a placeholder.
  - [minor] **Formula-text drift:** the Formula cell stops at "normalized … then weighted" and
    omits the final **sum across categories**; the proposed revision and the Comment supply it.
  - [minor] EN5-2 (land use) must be the characterised **Pt** result, not raw m²a/FU, before
    normalisation (Comment already states this) — keep that note.
  - **EUPEF+21 is present** in the corpus (`PEF_CELEX_32021H2279_EN_TXT.pdf`) — this **corrects**
    the SOURCE-NOT-FOUND status that `reviews/EN-impact-pef.md` recorded for EUPEF+21. The
    recommendation/weighting *concept* is now corpus-grounded (quotes above); the specific EF 3.x
    **numerical NF/WF tables** live in Annex I and were not located as quotable tables in this
    text extract (see Limits).
  - **Comment-cell flag (proposed):** keep the existing detailed Comment as-is; it is accurate
    and decision-ready.

### EN0 — Environmental Impact Score  [Level 1 (domain root), composite, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the overall environmental impact of a product. It consists of metrics
  that specifically directly impacts the environments. The score ranges from 0 being damaging
  for the environment and 1 being the ideal case of an environmental friendly product."
- **Verdict:** UNVERIFIABLE (composite root, internal check) — author-defined aggregation of the
  domain's level-2 scores; no single literature source expected or required. Internally
  CONSISTENT: text matches the weighted-average-of-children design.
- **Grounding:** none expected. By design EN0 represents/aggregates its children; no standard
  publishes an "overall product environmental score." (ISO 14044 even cautions there is "no
  scientific basis for reducing LCA results to a single overall score" — see
  `reviews/EN-impact-pef.md` — which applies equally here; a value-choice caveat is appropriate.)
- **Implementation check (internal):**
  - Children: `EN1\nEN2\nEN3\nEN4\nEN5\nEN6\nEN7\nEN8` — all eight exist and are Level-2 scores
    (verified). Strategy `WEIGHTED_AVERAGE_STRATEGY`, Weight 1, Unit `%`.
  - Description "consists of metrics that … directly impact the environment" is consistent with
    aggregating the eight environmental sub-scores. The 0–1 (% normalised, higher = better)
    orientation is consistent with the children, which are all normalised 0–1 / % scores.
  - **Formula-text drift:** the Formula cell reads "Sum (weight * EN1 + … + weight * EN5)", which
    lists only up to EN5 while the actual children run EN1…EN8. Stale text from before the gap-fix
    re-model.
- **Proposed revision:** "Aggregates the product's eight environmental sub-scores — carbon
  footprint (EN1), resource consumption (EN2), hazardous material & waste (EN3), water footprint
  (EN4), biodiversity (EN5), pollution (EN6), toxicity (EN7) and resource deprivation (EN8) —
  into one weighted-average environmental score on a 0–1 scale (0 = most damaging, 1 = ideal /
  environmentally friendly). A single representative indicator for the product's overall
  environmental performance."
- **Notes:**
  - [minor] **Formula-text drift:** "EN1 + … + EN5" should read "EN1 + … + EN8" (or the explicit
    EN1…EN8 list) to match the eight children.
  - [minor] Grammar in current text: "specifically directly impacts the environments" → "directly
    impact the environment."
  - EN0 is the domain root (Parent = None) and is **distinct from EN9**: EN0 = weighted average of
    all 8 sub-scores (an author-defined dashboard roll-up); EN9 = the EU PEF single score over the
    5 PEF-method sub-scores (a standards-defined LCIA aggregate). They legitimately coexist; EN9 is
    not a child of EN0 (confirmed `Parent=None` on EN9). No defect — just confirm this dual-root
    design is intended.
  - **Comment-cell flag (proposed):** "Composite domain root: weighted average of EN1–EN8.
    No single literature source (author-defined roll-up); carry a value-choice caveat (cf.
    ISO 14044 'no single overall score')."

---

## Batch summary

**Counts (5 rows):** CONSISTENT 2 (EN5, EN5-1); ADAPTED 2 (EN5-2, EN9 — EN9 also DRIFTED on its
Formula text); UNVERIFIABLE 1 (EN0, composite root — internally CONSISTENT).

**Proposed description rewrites:** EN5, EN5-2, EN9, EN0 (4 rows). EN5-1 keeps its text
(faithful; optional tightening only).

**Proposed adjacent-cell fixes (drift):**
1. **EN0 Formula text** "Sum (weight * EN1 + … + weight * EN5)" → "… EN1 + … + EN8" (children
   are EN1…EN8). [minor but load-bearing]
2. **EN9 Formula text** add the final "sum across categories" step (currently stops at
   "normalized … then weighted"). [minor]
3. **EN0 grammar** "specifically directly impacts the environments" → "directly impact the
   environment." [minor]

**Citation fixes / decisions needed:**
1. **EN5 cited set vs implemented method (minor).** EN5 implements the LCA land-use Q×A×t model
   (JPL+19/JQ+25 ground it; GRI 101 grounds only the concept). Decide whether to add `EUPEF+21`
   (PEF "Land use" category — p.15 quote is verbatim the formula) and/or `ESRS E4` (DR E4-5
   land-use-based LCA biodiversity metric, E4 PDF p.8 §36) to the Reference cell. Recommended:
   add `EUPEF+21`; optionally `ESRS E4` as an ADAPTED org-level hook. Keep GRI 101.
2. **EN9 EF factors (major, carried from EN-impact-pef.md).** Confirm each EN9 child carries its
   EF normalisation factor (Target Max, Min=0) and EF weighting factor (Weight) per the Comment;
   otherwise the single score is a placeholder. EN5-2 must feed the characterised **Pt** result,
   not raw m²a/FU.
3. **Dual-root design (confirm).** EN0 (weighted avg of EN1–EN8) and EN9 (PEF single score over
   EN1/EN5/EN6/EN7/EN8) coexist as two separate roots; EN9 is correctly unwired from EN0. Confirm
   intended.

**SOURCE-NOT-FOUND codes:** none for this batch. All cited codes resolve **and** their PDFs are
present: `GRI 101`, `JQ+25`, `JPL+19`, `EUPEF+21`. **Correction to a prior review:** `EUPEF+21`
was marked SOURCE-NOT-FOUND in `reviews/EN-impact-pef.md`, but its PDF **is** in the corpus at
`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`; the PEF normalisation/weighting *concept* is
therefore corpus-grounded (quotes above). `BVI` on EN5-1 is a **unit**, not a reference code — not
an orphan. `ESRS E4` is present in the corpus but not currently cited by any EN row (optional add).

**Limits of this run:**
- I verified the **method/concept** for EN5/EN5-1/EN5-2 (Q×A×t land-use model, naturalness/∆Q,
  m²a occupation, BVI CF) from JPL+19 and JQ+25, and the **PEF concept** (normalisation =
  divide by reference; weighting = multiply by % factors; land use = soil-quality × area ×
  duration) from the PEF PDF glossary (p.15/16/20) and ToC (p.1, p.8). I did **not** locate the
  EF 3.x **numerical normalisation/weighting factor tables** (PEF Annex I) as quotable tables in
  this text extract, so the specific NF/WF *values* for EN9's children remain unverified from the
  corpus (concept verified, values not). The EN9 method blocker is summarised from
  `reviews/EN-impact-pef.md` (ISO 14044 non-additivity), not re-derived here.
- I did not re-audit EN6/EN7/EN8 internals (covered in `reviews/EN-impact-pef.md`) nor EN1
  (covered in `reviews/EN-descriptions.md`); they are referenced only as EN0/EN9 children.
- Numeric Min/Max bands, weights (0.125 / 0.1112 / 1), and Example Values were not assessed.


---

## EN6 — Pollution & Effects on Nature (PEF)

### EN6 — Pollution & Effects on Nature Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the product's pollution impact on humans and environment. Based on the PEF impact factor categorization."
- **Verdict:** CONSISTENT — the description is generic but accurate for the re-modelled aggregate; the only drift is in the **Formula text** cell, not the description.
- **Grounding:** PEF (EUPEF+21) groups exactly these pollution categories. PEF p.12: *"Acidification – EF impact category that addresses impacts due to acidifying substances in the environment…"*; p.14: *"…three EF impact categories are used: eutrophication, terrestrial; eutrophication, freshwater; eutrophication, marine."* (`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`). Category list/units in Table 2 (pp. L 471/226–228) — see leaves below.
- **Implementation check:** `Underlying Metrics = EN6-1…EN6-8` (all eight exist as `_self()` NORMALIZED leaves), strategy WEIGHTED_AVERAGE, equal 0.125 weights, unit %. Children are now normalized [0,1] before averaging, so the average is dimensionally valid — matches the description. **Formula cell** reads "Weighted sum of each underlying metrics compared to a target value" — this still describes the *old* raw "compared to a target value" model; it should say it weight-averages the children's **already-normalized** scores. The Comment cell is accurate (instructs entering EF NF as Target Max, EF WF as Weight).
- **Proposed revision:** "Aggregates the product's pollution-related environmental impacts into one score, covering the eight EF/PEF pollution impact categories (EN6-1…EN6-8: ozone depletion, particulate matter, photochemical ozone formation, the three eutrophication categories, acidification and ionising radiation). Each category is first self-normalized against its EF normalisation factor, then combined by EF weighting factors." (Keep it this explicit only if the sheet's style favours it; otherwise the current short text is acceptable.)
- **Notes:** Composite/parent — no single literature source expected; EUPEF+21 grounds the *category grouping* only, which is appropriate. [minor] **Formula text drift** — replace "Weighted sum … compared to a target value" with "Weighted average of the eight children's normalized scores (EF normalize → EF-weight → sum)". [minor] `Objective / Goal` cell is empty while EN1–EN5 carry one — add one (e.g. "Minimise the product's contribution to pollution-related impact categories"). `Parent Metrics = EN0\nEN9` — outside this batch, not verified here.

### EN6-1 — Ozone depletion  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the emissions of long-lived gases such as chlorofluorocarbons (CFCs), hydrochlorofluorocarbons (HCFCs), and Halons."
- **Verdict:** CONSISTENT (with one wording flag) — the description faithfully tracks the EF definition; the leaf self-normalizes its kg CFC-11 eq result.
- **Grounding:** PEF p.16: *"Ozone depletion – EF impact category that accounts for the degradation of stratospheric ozone due to emissions of ozone-depleting substances, for example long-lived chlorine and bromine containing gases (e.g. chlorofluorocarbons (CFCs), hydrochlorofluorocarbons (HCFCs), halons)."* Table 2 (p. L 471/226): *"Ozone depletion … Ozone depletion potential (ODP) … kg CFC-11 eq … EDIP model based on the ODPs of the World Meteorological Organisation (WMO) over an infinite time horizon (WMO 2014 + integrations)"* — robustness level I.
- **Implementation check:** `_self()` leaf; unit kg CFC-11 eq matches Table 2; Formula text "EDIP model from ODPs of the WMO over an infinite time horizon" matches the Table 2 model attribution verbatim in substance. Target Max (EF NF) blank — expected (NF delegated, PEF §5.2.1 fn.77).
- **Proposed revision:** "The product's stratospheric ozone-depletion impact (ODP), driven by emissions of long-lived ozone-depleting substances — chlorofluorocarbons (CFCs), hydrochlorofluorocarbons (HCFCs) and halons. Self-normalized against the EF ozone-depletion normalisation factor." (The current text describes *what is emitted* rather than *the impact measured*; the source frames it as "degradation of stratospheric ozone". Minor sharpening only.)
- **Notes:** Reference code `AO+24` (Dataset with updated ozone-depletion CFs). [minor] `AO+24` PDF is **not** in the corpus (SOURCE-NOT-FOUND); the concept/unit/model are fully grounded by the PEF PDF instead. Consider adding `EUPEF+21` to the Reference cell so the row traces to a present source. ADAPTED note: org/EF-level category applied at product level.

### EN6-2 — Respiratory inorganics  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the adverse health effects on humans caused by Particulate Matter (PM) and its precursors, such as nitrogen oxides (NOx), sulfur oxides (SOx), and ammonia (NH3​)"
- **Verdict:** CONSISTENT (concept) — almost verbatim the EF "Particulate matter" definition; flags on the **Reference code** and the **Formula/Unit** cells.
- **Grounding:** PEF p.17: *"Particulate matter – EF impact category that accounts for the adverse effects on human health caused by emissions of particulate matter (PM) and its precursors (NOx, SOx, NH3)."* Table 2 (p. L 471/227): *"Particulate matter … Impact on human health … Disease incidence … PM model (Fantke et al., 2016 in UNEP 2016)"* — robustness level I.
- **Implementation check:** `_self()` leaf. Description matches PEF almost word-for-word. **Unit** "Disease incidences per kg of PM2.5 (μm)" is more verbose / unit-confused than the EF category-indicator unit "Disease incidence" (the "per kg PM2.5" describes the *characterisation factor* dimension, not the indicator result). **Formula** cell reads "M Model" — garbled; Table 2 names the "PM model (Fantke et al., 2016)". **Reference** cites `USEtox2.0`, but PEF Table 2 attributes Particulate matter to the **PM model**, not USEtox (USEtox is the toxicity-category model). The USEtox citation here is therefore a category/model mismatch.
- **Proposed revision (description):** "The adverse human-health impact (disease incidence) caused by emissions of fine particulate matter (PM) and its precursors — nitrogen oxides (NOx), sulfur oxides (SOx) and ammonia (NH3). Self-normalized against the EF particulate-matter normalisation factor." (Keeps it faithful; drops the trailing-character artefact in the current cell.)
- **Notes:** [major] **Reference mismatch** — EN6-2 cites `USEtox2.0`, but the EF particulate-matter category uses the PM model (Fantke et al. 2016), not USEtox. Re-tag to `EUPEF+21` (present, grounds it via Table 2) and/or `VZ+08` (Van Zelm et al. 2008 — the PM10/ozone DALY CF paper), but **not** USEtox. [minor] Unit → "Disease incidence". [minor] Formula "M Model" → "PM model (Fantke et al., 2016) as in EF/PEF". `USEtox2.0` PDF not in corpus (SOURCE-NOT-FOUND). ADAPTED note: EF category at product level.

### EN6-3 — Photochemical ozone formation  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the formation of ground-level (tropospheric) ozone, often referred to as \"smog\". It is caused by the photochemical oxidation of volatile organic compounds (VOCs) and carbon monoxide in the presence of nitrogen oxides and sunlight, which can damage vegetation and human respiratory tracts."
- **Verdict:** CONSISTENT — closely tracks the EF definition (the only addition, the lay term "smog", is harmless).
- **Grounding:** PEF p.17: *"Photochemical ozone formation – EF impact category that accounts for the formation of ozone at the ground level of the troposphere caused by photochemical oxidation of volatile organic compounds (VOCs) and carbon monoxide (CO) in the presence of nitrogen oxides (NOx) and sunlight. High concentrations of ground-level tropospheric ozone damage vegetation, human respiratory tracts and manmade materials…"* Table 2 (p. L 471/227): *"Photochemical ozone formation, human health … Tropospheric ozone concentration increase … kg NMVOC eq … LOTOS-EUROS model (Van Zelm et al, 2008) as applied in ReCiPe 2008"* — robustness II.
- **Implementation check:** `_self()` leaf; unit kg NMVOC eq matches Table 2; Formula text "LOTOS-EUROS model in ReCiPe" matches the Table 2 model attribution. Reference `VZ+08` (Van Zelm et al. 2008) is the correct method citation per Table 2.
- **Proposed revision:** keep as-is (faithful and well grounded). Optional tightening: append "Self-normalized against the EF photochemical-ozone-formation normalisation factor." for consistency with siblings.
- **Notes:** [minor] `VZ+08` PDF not in corpus (SOURCE-NOT-FOUND) — but the citation is *correct* per PEF Table 2; concept/unit/model fully grounded by the PEF PDF. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

### EN6-4 — Eutrophication: Terrestrial  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the eutrophication occurs when excess nutrients (mainly nitrogen and phosphorus) from sources like fertilizers and sewage accelerate the growth of algae."
- **Verdict:** DRIFTED (wording) — the description is generic eutrophication boilerplate that does **not** say *terrestrial*, and its "growth of algae" framing is the aquatic mechanism, not the terrestrial one; the cited model and unit are correct.
- **Grounding:** PEF p.14: *"Eutrophication – EF impact category related to nutrients (mainly nitrogen and phosphorus) from sewage outfalls and fertilised farmland that accelerate the growth of algae and other vegetation in water… three EF impact categories are used: eutrophication, terrestrial; eutrophication, freshwater; eutrophication, marine."* Table 2 (p. L 471/227): *"Eutrophication, terrestrial … Accumulated exceedance (AE) … mol N eq … Accumulated exceedance (Seppälä et al. 2006, Posch et al, 2008)"* — robustness II.
- **Implementation check:** `_self()` leaf; unit "Mole of N eq" matches Table 2's "mol N eq" (the terrestrial AE indicator is the mol N eq one — confirmed). Formula "Accumulated Exceedance (AE) model" matches Table 2. The description is **shared verbatim** with EN6-5/EN6-6 except for the end-compartment clause, but EN6-4 has *no* terrestrial qualifier and wrongly uses the algae/aquatic mechanism for the terrestrial category.
- **Proposed revision:** "The product's contribution to **terrestrial** eutrophication: deposition of excess nitrogen compounds (from sources such as fertilisers and emissions) onto soils, measured as accumulated exceedance of critical loads (mol N eq). Self-normalized against the EF terrestrial-eutrophication normalisation factor."
- **Notes:** [major] description does not distinguish terrestrial from the marine/freshwater siblings and mis-uses the "algae growth" (aquatic) mechanism — revise as above. Reference `ILCD2011` (Acidification terrestrial and freshwater — AE). [minor] `ILCD2011` PDF not in corpus (SOURCE-NOT-FOUND); AE model attribution grounded by PEF Table 2. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

### EN6-5 — Eutrophication: Marine  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the eutrophication occurs when excess nutrients (mainly nitrogen and phosphorus) from sources like fertilizers and sewage accelerate the growth of algae, which reaches the marine end compartment."
- **Verdict:** CONSISTENT (with minor grammar) — the "marine end compartment" clause correctly distinguishes it; model/unit correct.
- **Grounding:** PEF p.14 (eutrophication definition + the three categories, quoted above). Table 2 (p. L 471/227): *"Eutrophication, marine … Fraction of nutrients reaching marine end compartment (N) … kg N eq … EUTREND model (Struijs et al, 2009) as applied in ReCiPe"* — robustness II.
- **Implementation check:** `_self()` leaf; unit "kg N eq" matches Table 2 (marine = kg N eq). Formula "EUTREND model" matches Table 2. The "marine end compartment" phrasing mirrors the EF indicator name "Fraction of nutrients reaching marine end compartment (N)".
- **Proposed revision:** "The product's contribution to **marine** eutrophication: the fraction of emitted nutrients (chiefly nitrogen) reaching the marine end compartment, where excess nutrients accelerate algal growth and oxygen depletion (kg N eq). Self-normalized against the EF marine-eutrophication normalisation factor."
- **Notes:** [minor] grammar ("Measures the eutrophication occurs"). Reference `ReCiPe2008` — correct per Table 2 (EUTREND as applied in ReCiPe). [minor] `ReCiPe2008` PDF not in corpus (SOURCE-NOT-FOUND); grounded by PEF Table 2. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

### EN6-6 — Eutrophication: Freshwater  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the eutrophication occurs when excess nutrients (mainly nitrogen and phosphorus) from sources like fertilizers and sewage accelerate the growth of algae, which reaches the freshwater end compartment."
- **Verdict:** CONSISTENT (with minor grammar) — "freshwater end compartment" correctly distinguishes it; model/unit correct. Note freshwater eutrophication is **phosphorus**-driven (kg P eq), so the "mainly nitrogen and phosphorus" generic phrasing is slightly off for this leaf.
- **Grounding:** PEF p.14 (quoted above). Table 2 (p. L 471/227): *"Eutrophication, freshwater … Fraction of nutrients reaching freshwater end compartment (P) … kg P eq … EUTREND model (Struijs et al, 2009) as applied in ReCiPe"* — robustness II.
- **Implementation check:** `_self()` leaf; unit "kg P eq" matches Table 2 (freshwater = kg P eq, phosphorus). Formula "EUTREND model" matches. Reference cell carries **two** codes `ReCiPe2008\nEUEP-FW`.
- **Proposed revision:** "The product's contribution to **freshwater** eutrophication: the fraction of emitted phosphorus reaching the freshwater end compartment, where excess nutrients accelerate algal growth and oxygen depletion (kg P eq). Self-normalized against the EF freshwater-eutrophication normalisation factor."
- **Notes:** [minor] grammar; [minor] the generic "nitrogen and phosphorus" wording understates that this leaf is the **phosphorus** (kg P eq) one. Reference `ReCiPe2008` (correct) + `EUEP-FW` (LCIA dataset: Eutrophication potential - freshwater; consistent). [minor] neither PDF in corpus (SOURCE-NOT-FOUND); grounded by PEF Table 2. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

### EN6-7 — Acidification  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the impact of acidifying substances primarily nitrogen oxides (NOx), ammonia (NH3​), and sulfur oxides (SOx), which release hydrogen ions when mineralized."
- **Verdict:** CONSISTENT — near-verbatim the EF acidification definition; model/unit correct.
- **Grounding:** PEF p.12: *"Acidification – EF impact category that addresses impacts due to acidifying substances in the environment. Emissions of NOx, NH3 and SOx lead to releases of hydrogen ions (H+) when the gases are mineralised. The protons contribute to the acidification of soils and water… resulting in forest decline and lake acidification."* Table 2 (p. L 471/227): *"Acidification … Accumulated exceedance (AE) … mol H+ eq … Accumulated exceedance (Seppälä et al. 2006, Posch et al, 2008)"* — robustness II.
- **Implementation check:** `_self()` leaf; unit "Mole of H+ eq" matches Table 2's "mol H+ eq". Formula "Accumulated Exceedance (AE) model" matches. Indicator Name has a **trailing space** ("Acidification ").
- **Proposed revision:** keep substance as-is; optional polish: "The product's acidification impact: emissions of acidifying substances (NOx, NH3, SOx) that release hydrogen ions (H+) when mineralised, contributing to soil and water acidification (accumulated exceedance, mol H+ eq). Self-normalized against the EF acidification normalisation factor."
- **Notes:** [minor] trailing space in Indicator Name "Acidification ". Reference `ILCD2011` (AE model) — consistent with Table 2 attribution. [minor] `ILCD2011` PDF not in corpus (SOURCE-NOT-FOUND); grounded by PEF Table 2. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

### EN6-8 — Ionizing radiation  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the adverse effects on human health resulting from exposure to radioactive releases into the environment."
- **Verdict:** CONSISTENT — near-verbatim the EF definition; model/unit correct.
- **Grounding:** PEF p.15: *"Ionising radiation, human health – EF impact category that accounts for the adverse health effects on human health caused by radioactive releases."* Table 2 (p. L 471/227): *"Ionising radiation, human health … Human exposure efficiency relative to U235 … kBq U235 eq … Human health effect model as developed by Dreicer et al. 1995 (Frischknecht et al, 2000)"* — robustness II.
- **Implementation check:** `_self()` leaf; unit "kBq U-235 eq" matches Table 2's "kBq U235 eq". Formula "Human health effect model" matches Table 2. Reference `FR+00` = Frischknecht et al. 2000 — exactly the model citation in Table 2.
- **Proposed revision:** keep as-is (faithful and well grounded). Optional sibling-consistency tail: "(kBq U-235 eq). Self-normalized against the EF ionising-radiation normalisation factor."
- **Notes:** [minor] `FR+00` PDF not in corpus (SOURCE-NOT-FOUND) — but the citation is *correct* per PEF Table 2; concept/unit/model fully grounded by the PEF PDF. Optionally add `EUPEF+21`. ADAPTED note: EF category at product level.

---

## Batch summary

**Counts (9 rows):** CONSISTENT 6 (EN6, EN6-1, EN6-3, EN6-5, EN6-6, EN6-7, EN6-8 — note
EN6-5/6/7/8 carry minor polish flags) → strictly 7 CONSISTENT, 2 DRIFTED.
Precisely: **CONSISTENT 7** (EN6, EN6-1, EN6-2*, EN6-3, EN6-5, EN6-6, EN6-7, EN6-8 — EN6-2
concept is consistent but its *Reference* drifted, see below), **DRIFTED 2** (EN6-4
wording mis-categorises terrestrial vs aquatic; EN6-2's Reference code mismatches). No
CONTRADICTION (the gap-fix re-model resolved the prior `EN-impact-pef.md` blocker — children
are now normalized before averaging). No UNVERIFIABLE — every leaf is grounded in the now-present
PEF PDF (EUPEF+21).

**Most important decisions needed:**
1. **EN6-4 (terrestrial eutrophication) description** — currently indistinct from the marine/
   freshwater siblings and uses the aquatic "algae growth" mechanism. Rewrite to the
   terrestrial-N / accumulated-exceedance framing (proposed text above). [major]
2. **EN6-2 Reference code** — `USEtox2.0` is the wrong model for the Particulate-matter
   category (EF uses the PM model, Fantke et al. 2016). Re-tag to `EUPEF+21` (and/or `VZ+08`),
   drop USEtox. Also fix the "M Model" Formula artefact and the Unit → "Disease incidence". [major]
3. **EN6 Formula text** — still says "compared to a target value" (old raw model); update to
   reflect normalize-then-weight-average over the eight normalized children. [minor]
4. **Optional but recommended:** add `EUPEF+21` to each leaf's Reference cell — it is the one
   cited source actually present in the corpus and it grounds every category/unit/model; the
   per-method codes (AO+24, VZ+08, ILCD2011, ReCiPe2008, EUEP-FW, FR+00) are correct
   attributions but their PDFs are absent. [minor]

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | major | EN6-4 | Description is generic aquatic-eutrophication ("growth of algae") with **no terrestrial qualifier**, indistinct from EN6-5/EN6-6; the terrestrial category is N-deposition / accumulated-exceedance (mol N eq), not algal growth | Rewrite to the proposed terrestrial-N / accumulated-exceedance text |
| 2 | major | EN6-2 | Reference `USEtox2.0` mismatches the EF Particulate-matter model (PEF Table 2, p.227: "PM model (Fantke et al., 2016)"); USEtox is the toxicity model (EN7) | Re-tag to `EUPEF+21` (and/or `VZ+08`); drop `USEtox2.0` |
| 3 | minor | EN6-2 | Formula cell "M Model" garbled; Unit "Disease incidences per kg of PM2.5 (μm)" describes the CF dimension, not the EF indicator unit | Formula → "PM model (Fantke et al., 2016) as in EF/PEF"; Unit → "Disease incidence" |
| 4 | minor | EN6 | Formula text "Weighted sum … compared to a target value" describes the pre-gap-fix raw model | Update to "Weighted average of the eight children's EF-normalized scores (normalize → EF-weight → sum)" |
| 5 | minor | EN6-6 | Description says "mainly nitrogen and phosphorus" but the freshwater leaf is the **phosphorus** (kg P eq) one | Sharpen wording to phosphorus-driven freshwater eutrophication |
| 6 | minor | EN6-7 | Indicator Name "Acidification " has a trailing space | Trim trailing space |
| 7 | minor | EN6-5, EN6-6 | Grammar: "Measures the eutrophication occurs when…" | Fix to "Measures eutrophication, which occurs when…" / use proposed revisions |
| 8 | minor | EN6, EN6-1..8 | Per-leaf method PDFs (AO+24, VZ+08, ILCD2011, ReCiPe2008, EUEP-FW, FR+00) and USEtox2.0 are absent from the corpus; only `EUPEF+21` (PEF PDF) is present and grounds all categories | Add `EUPEF+21` to each leaf's Reference cell so the row traces to a present source; optionally add the method PDFs |
| 9 | minor | EN6 | `Objective / Goal` cell empty while EN1–EN5 carry one | Add an objective (e.g. "Minimise the product's pollution-related impact-category burdens") |
| 10 | minor (re-model verify) | EN6-1..8 | Target Max (EF normalisation factor) is **blank** on every leaf — required for the NORMALIZED_RATIO to compute | Source EF NF per category from the JRC EF reference package (PEF §5.2.1 fn.77, p.283); do **not** invent — values are outside the corpus |

### SOURCE-NOT-FOUND codes (References row exists, no PDF in `data/literature/`)
`AO+24` (EN6-1), `USEtox2.0` (EN6-2, also a model mismatch), `VZ+08` (EN6-3),
`ILCD2011` (EN6-4, EN6-7), `ReCiPe2008` (EN6-5, EN6-6), `EUEP-FW` (EN6-6), `FR+00` (EN6-8).
These are correct method *attributions* per PEF Table 2 (except USEtox2.0/EN6-2), but their
PDFs are not in the corpus. The cited parent source `EUPEF+21`
(`data/literature/PEF_CELEX_32021H2279_EN_TXT.pdf`) **is** present and was read this run; it
grounds every category definition, unit and model attribution quoted above.

### Limits of this run
- The **EF normalisation-factor and weighting-factor numeric values are not in the PEF PDF**
  (delegated online — PEF §5.2.1/§5.2.2, fn.77–80, p. L 471/283), so each leaf's Target Max
  (NF) and the EF weights cannot be quoted or verified from the corpus and were not invented;
  blank Target Max is expected until sourced from the JRC EF reference package.
- I verified category definitions/units/models against `EUPEF+21` (the PEF glossary §2 and
  Table 2, pp. L 471/226–228) only; the individual method papers (AO+24, VZ+08, FR+00,
  ReCiPe2008, ILCD2011, EUEP-FW, USEtox2.0) could not be checked against their own documents —
  those PDFs are absent.
- Re-model semantics confirmed from `formulas.py` (EN6-1..8 = `_self()`) and the
  normalize/weighted-average logic in `engine.py`/`strategies.py`; I did not execute the
  engine on live data.
- Page citations use the OJ "L 471/N" printed page numbers; the `pdf_search` tool returned
  the PDF reader page index (e.g. p.12–17 for the glossary, where the printed pages are the
  L 471/xx headers) — quotes are verbatim from those hits.
- EN6's parents (EN0, EN9) are outside this batch and were not verified.


---

## EN7 / EN8 — Toxicity & Resource Deprivation (PEF)

### EN7 — Toxicity Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the product's toxic impact on humans and environment. Based on the PEF impact factor categorization."
- **Verdict:** CONSISTENT — the description matches the current implementation (a weighted average of the three normalized toxicity sub-categories) and is correctly attributed to the PEF/EF category set.
- **Grounding:** EUPEF+21 Table 2 (p.30) lists the three EF toxicity categories the children map to (Human toxicity cancer/non-cancer CTUh, Ecotoxicity freshwater CTUe). The "toxicity-related methods (human toxicity – cancer effects; human toxicity – non-cancer effects; eco-toxicity freshwater …)" grouping is named verbatim at p.2.
- **Implementation check:** `Underlying Metrics = EN7-1\nEN7-2\nEN7-3`; all three exist as `NORMALIZED_RATIO_STRATEGY` leaves. Parent strategy `WEIGHTED_AVERAGE_STRATEGY` over already-normalized (dimensionless ratio) children is now dimensionally valid — the old CTUh+CTUh+CTUe non-additivity defect is resolved by the self-normalizing children. Unit `%` is consistent with averaging normalized ratios. Parents `EN0\nEN9` (composite roots) are out of batch. The displayed Formula cell, however, still reads "Weighted sum of each underlying metrics compared to a target value." — this describes the *old* "compared to a target value" framing; under the re-model the target/normalisation now lives on each child (child Target Max = EF NF), so the parent simply weight-averages normalized children.
- **Proposed revision:** "Aggregates the product's human- and eco-toxicity impact into one score by weight-averaging its three normalized EF toxicity categories: human toxicity – cancer (EN7-1), human toxicity – non-cancer (EN7-2) and freshwater ecotoxicity (EN7-3). Based on the EU PEF / Environmental Footprint impact-category set."
- **Notes:** Composite/parent — no single literature source defines this aggregate; EUPEF+21 grounds the category set only, so the verdict rests on the internal check (children exist, units compatible after normalization, description aggregates them). [minor] Parent Formula text "Weighted sum … compared to a target value" is now stale — propose "Weighted average of the three normalized toxicity sub-categories (EN7-1, EN7-2, EN7-3)." [minor] `Objective / Goal` cell is empty (peers EN1–EN5 carry one) — carried over from `reviews/EN-impact-pef.md` fix #7; still open. The parent Comment already documents the PEF NF-as-Target-Max / WF-as-Weight modelling and is consistent.

### EN7-1 — Human toxicity: cancer  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the adverse health effects on human beings related to the intake of toxic substances that are known to cause cancer."
- **Verdict:** ADAPTED — near-verbatim paraphrase of the PEF glossary definition, applied as a self-normalizing product-level leaf; correct EF category and unit. Method PDF (USEtox) absent.
- **Grounding:** EUPEF+21 p.15: "Human toxicity – cancer – EF impact category that accounts for adverse health effects on human beings caused by the intake of toxic substances through inhalation of air, food/water ingestion, penetration through the skin – insofar as they are related to cancer." Table 2 p.30: "Human toxicity, cancer Comparative toxic unit for humans (CTUh) CTUh based on USEtox2.1 model …".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`; Unit `CTUh` matches Table 2 exactly. Description is faithful to the glossary. The self-normalizing ratio (characterised CTUh ÷ EF NF as Target Max, Min 0) is the PEF per-capita normalisation step (p.86) applied per leaf — consistent.
- **Proposed revision:** keep as-is (faithful to the PEF glossary). Optional explicit-unit version: "Adverse health effects on humans from intake of carcinogenic toxic substances (inhalation, ingestion, dermal). EF 'Human toxicity, cancer' category, characterised in CTUh and normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text.** Formula cell reads "USEtox model" — under the re-model the leaf computes a normalized ratio, not the raw USEtox characterisation; propose "Characterised result (CTUh, USEtox) ÷ EF normalisation factor (Target Max); Min = 0." **[minor] Citation version.** Reference is `USEtox2.0`, but EUPEF+21 attributes this category to "USEtox2.1 model (Fantke et al. 2017)". Per the brief, an earlier review deliberately collapsed USEtox2.1/2.2 → `USEtox2.0` because `USEtox2.0` is the only registered Label in References.tsv (2.1/2.2 are orphan codes). That keeps the code resolvable but the version label diverges from the PEF attribution — recommend either (a) updating the `USEtox2.0` References row title to note it stands in for the EF-recommended USEtox 2.x family, or (b) adding a `USEtox2.1` row. SOURCE-NOT-FOUND: no USEtox PDF in corpus (concept/unit grounded via EUPEF+21).

### EN7-2 — Human toxicity: non-cancer  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the adverse health effects on human beings caused by the intake of toxic substances that are related to non-cancer effects."
- **Verdict:** ADAPTED — near-verbatim PEF glossary paraphrase; correct EF category/unit. Method PDF absent.
- **Grounding:** EUPEF+21 p.15: "Human toxicity - non cancer – EF impact category that accounts for the adverse health effects on human beings caused by the intake of toxic substances through inhalation of air, food/water ingestion, penetration through the skin …". Table 2 p.30: "Human toxicity, non- cancer … (CTUh) CTUh based on USEtox2.1 model …".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`; Unit `CTUh` matches Table 2. Description faithful. EN7-1 and EN7-2 share the unit CTUh but are distinct EF categories; each is normalized against its own EF NF before EN7 averages them — correct.
- **Proposed revision:** keep as-is. Optional: "Adverse health effects on humans from intake of non-carcinogenic toxic substances. EF 'Human toxicity, non-cancer' category, CTUh, normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text** — same fix as EN7-1 (Formula "USEtox model" → normalized-ratio wording). **[minor] Citation version** — same `USEtox2.0` vs PEF-attributed "USEtox2.1" note as EN7-1 (deliberate collapse; flag retained). SOURCE-NOT-FOUND: USEtox PDF absent. Earlier review's note that this row once cited `USEtox2.1` is now resolved (current Reference is `USEtox2.0`).

### EN7-3 — Ecotoxicity: freshwater  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the toxic impacts of chemical releases on a freshwater ecosystem. It measures how toxic substances damage individual species and subsequently change the structure and function of the entire ecosystem."
- **Verdict:** ADAPTED — close paraphrase of the PEF glossary ecotoxicity definition; correct EF category/unit. Method PDF absent.
- **Grounding:** EUPEF+21 p.211 (also p.14): "Ecotoxicity, freshwater – EF impact category that addresses the toxic impacts on an ecosystem, which damage individual species and change the structure and function of the ecosystem." Table 2 p.30: "Ecotoxicity, freshwater Comparative toxic unit for ecosystems (CTUe) CTUe based on USEtox2.1 model …".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`; Unit `CTUe` matches Table 2 exactly. Description faithfully mirrors the glossary ("damage individual species … change the structure and function of the ecosystem"). Life-cycle stages `S,M` (vs `S,M,D,U` on EN7-1/2) — minor inconsistency across the toxicity leaves; not assessed against literature.
- **Proposed revision:** keep as-is (it is essentially the PEF glossary text). Optional explicit-unit close: "… EF 'Ecotoxicity, freshwater' category, characterised in CTUe and normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text** — "USEtox model" → normalized-ratio wording. **[minor] Citation version** — `USEtox2.0` vs PEF "USEtox2.1" (deliberate collapse; flag retained). SOURCE-NOT-FOUND: USEtox PDF absent. [minor] life-cycle-stage tag differs from sibling toxicity leaves (S,M vs S,M,D,U) — confirm intended.

---

## EN8 — Resource Deprivation family

### EN8 — Resource Deprivation Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the product's resource depletion impact on the environment. Covers the deprivation due to use of water, minerals, metals, and fossil."
- **Verdict:** CONSISTENT — description matches the current implementation (weighted average of the three normalized resource categories) and correctly enumerates its children's scope (water, minerals & metals, fossils).
- **Grounding:** EUPEF+21 Table 2 (p.30/p.158): the three EF resource categories — "Water use … (AWARE) … III", "Resource use, minerals and metals Abiotic resource depletion (ADP ultimate reserves) kg Sb eq …", "Resource use, fossils Abiotic resource depletion – fossil fuels (ADP-fossil) … MJ".
- **Implementation check:** `Underlying Metrics = EN8-1\nEN8-2\nEN8-3`; all exist as `NORMALIZED_RATIO_STRATEGY` leaves. Parent `WEIGHTED_AVERAGE_STRATEGY` over normalized (dimensionless) children is valid — the old m³+kg Sb eq+MJ non-additivity defect is resolved. Unit `%` consistent. The description's "water, minerals, metals, and fossil" maps exactly onto EN8-1 / EN8-2 / EN8-3. Parents `EN0\nEN9` out of batch.
- **Proposed revision:** "Aggregates the product's natural-resource depletion impact into one score by weight-averaging its three normalized EF resource categories: water use (EN8-1), minerals & metals depletion (EN8-2) and fossil-resource depletion (EN8-3). Based on the EU PEF / Environmental Footprint impact-category set."
- **Notes:** Composite/parent — verdict rests on the internal check (children exist, units compatible after normalization, description aggregates them). [minor] Parent Formula text "Weighted sum … compared to a target value" is stale under the re-model — propose "Weighted average of the three normalized resource sub-categories (EN8-1, EN8-2, EN8-3)." [minor] `Objective / Goal` empty (peers have one). Parent Comment documents the PEF NF/WF modelling — consistent. Note the Comment's trailing line "EN5-2 land use uses the 'pt' indicator, not m2a/FU" refers to a *different* leaf (EN5-2, outside this family) and reads as out of place on EN8 — see Notes/fixes.

### EN8-1 — Water Use Scarcity  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Total deprivation of freshwater resources. Assesses the product's water resource consumption. (weighted deprivation water consumption)"
- **Verdict:** ADAPTED — faithful to the EF Water use (AWARE) category concept and indicator name; correct category. Unit label is looser than the EF reference unit (see check). Method PDF absent.
- **Grounding:** EUPEF+21 p.20: "Water use – EF impact category that represents the relative available water remaining per area in a watershed, after demand from humans and aquatic ecosystems has been met. It assesses the potential for water deprivation …". Table 2 p.30: "Water use User deprivation potential (deprivation- weighted water consumption) m3 water eq of deprived water Available WAter REmaining (AWARE) model …".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`. Description's "(weighted deprivation water consumption)" matches the EF indicator name "User deprivation potential (deprivation-weighted water consumption)" — good. **Unit:** workbook `m3` vs EF reference unit "m3 water eq of **deprived** water". Same dimension but the EF value is AWARE deprivation-weighted, not raw m³ withdrawn — the stored value must be the AWARE-weighted result for the EF NF (Target Max) to apply. (Carried from `reviews/PEF-factors.md` fix #5.)
- **Proposed revision:** "The product's water-use impact measured as deprivation-weighted water consumption (AWARE): higher when water is consumed in more water-scarce watersheds. EF 'Water use' category, m³ world-eq of deprived water, normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text** — Formula "Available Water Remaining (AWARE) model" → normalized-ratio wording ("Characterised result (m³ deprived, AWARE) ÷ EF normalisation factor (Target Max); Min = 0"). **[minor] Unit precision** — set Unit to "m³ world eq. deprived" (or document that the stored m³ is AWARE-weighted) to match Table 2. SOURCE-NOT-FOUND: `BA+17` (AWARE / Boulay et al. 2018) PDF absent — concept/unit grounded via EUPEF+21 Table 2; the model attribution "AWARE (Boulay et al., 2018)" is consistent with the cited `BA+17`.

### EN8-2 — Resource Use: Minerals & Metals  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Total abiotic resource depletion (ADP ultimate reserves)"
- **Verdict:** ADAPTED — verbatim match to the EF indicator name; correct category and unit. Method PDF absent.
- **Grounding:** EUPEF+21 p.18: "Resource use, minerals and metals – EF impact category that addresses the use of non-renewable abiotic natural resources (minerals and metals)." Table 2 p.30: "Resource use, minerals and metals Abiotic resource depletion (ADP ultimate reserves) kg Sb eq van Oers et al., 2002 as in CML 2002 method, v.4.8 III".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`; Unit `kg Sb eq.` matches Table 2 exactly. Description "(ADP ultimate reserves)" matches the EF indicator "Abiotic resource depletion (ADP ultimate reserves)". The description is terse (a bare indicator name) — acceptable for a leaf, but could state what it measures.
- **Proposed revision (optional clarity):** "Depletion of non-renewable mineral and metal resources, measured as Abiotic Depletion Potential (ADP, ultimate reserves). EF 'Resource use, minerals and metals' category, kg Sb eq, normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text** — "CML2002 model" → normalized-ratio wording. SOURCE-NOT-FOUND: `OL+02` (van Oers et al. 2002 / CML ADP) PDF absent — concept/unit grounded via EUPEF+21 Table 2; the cited model "van Oers et al., 2002 as in CML 2002 method" is consistent with `OL+02`.

### EN8-3 — Resource Use: Fossil  [Level 5, leaf, NORMALIZED_RATIO_STRATEGY]
- **Current:** "Total abiotic resource depletion - fossil fuels (ADP fossil)"
- **Verdict:** ADAPTED — verbatim match to the EF indicator name; correct category and unit. Method PDF absent.
- **Grounding:** EUPEF+21 p.18: "Resource use, fossil – EF impact category that addresses the use of non-renewable fossil natural resources (e.g. natural gas, coal, oil)." Table 2 p.158: "Resource use, fossils Abiotic resource depletion – fossil fuels (ADP-fossil) … MJ".
- **Implementation check:** Leaf, `NORMALIZED_RATIO_STRATEGY`; Unit `MJ` matches Table 2. Description "(ADP fossil)" matches the EF indicator "Abiotic resource depletion – fossil fuels (ADP-fossil)". Terse but accurate.
- **Proposed revision (optional clarity):** "Depletion of non-renewable fossil energy resources (natural gas, coal, oil), measured as Abiotic Depletion Potential – fossil fuels (ADP-fossil). EF 'Resource use, fossils' category, MJ net calorific value, normalized against its EF reference value."
- **Notes:** **[minor] Stale Formula text** — "CML2002 model" → normalized-ratio wording. SOURCE-NOT-FOUND: `OL+02` PDF absent — concept/unit grounded via EUPEF+21 Table 2 (model attribution consistent).

---

## Batch summary

**Counts (8 metrics):** CONSISTENT 2 (EN7, EN8); ADAPTED 6 (EN7-1, EN7-2, EN7-3, EN8-1,
EN8-2, EN8-3). No CONTRADICTION (the gap-fix re-model resolved the prior non-additivity
defect), no UNVERIFIABLE.

**Proposed description rewrites:** EN7 and EN8 (the two parents) get a tightened aggregation
description that names the three children and the PEF basis. The six leaves keep their
current text (faithful PEF-glossary paraphrases / EF indicator names); optional explicit-unit
clarifications are offered but not required.

**Proposed adjacent-cell fixes (drift):**
- **Leaf Formula text (all six leaves)** still names only the characterisation model
  ("USEtox model" / "AWARE model" / "CML2002 model"). Under the `NORMALIZED_RATIO_STRATEGY`
  re-model each leaf computes characterised-result ÷ EF-NF(Target Max), Min 0. Update each
  Formula to that normalized-ratio wording (keep the model name in parentheses).
- **Parent Formula text (EN7, EN8)** "Weighted sum … compared to a target value" is stale;
  the per-leaf normalisation now carries the target, so the parents weight-average normalized
  children. Update to "Weighted average of the normalized sub-categories (EN7-1/2/3 resp.
  EN8-1/2/3)."

**Top decisions needed from you:**
1. **USEtox version label (minor, reference integrity).** EUPEF+21 attributes the three
   toxicity categories to "USEtox2.1 model"; the workbook cites `USEtox2.0` (the only
   registered Label; an earlier review deliberately collapsed 2.1/2.2 → 2.0). Decide: keep
   `USEtox2.0` and annotate its References row as the stand-in for the EF-recommended USEtox
   2.x family, or add a proper `USEtox2.1` row. Either resolves the version mismatch; current
   state is at least resolvable (not an orphan).
2. **EN8-1 water-use unit (minor).** `m3` vs EF "m3 water eq of deprived water". Confirm the
   stored value is AWARE deprivation-weighted and relabel the Unit accordingly, so the EF NF
   (defined per the deprivation-weighted indicator) applies directly.
3. **Misplaced Comment line on EN8.** EN8's parent Comment ends with "EN5-2 land use uses the
   'pt' indicator, not m2a/FU" — that note belongs to EN5-2, not the resource family; it reads
   as copy-paste residue. Remove from EN8 (and EN7) Comment or relocate to EN5-2.

**SOURCE-NOT-FOUND codes (References row exists, no PDF in corpus):** `USEtox2.0` (EN7-1/2/3),
`BA+17` (EN8-1), `OL+02` (EN8-2/3). The EF NF/WF numeric values referenced by the re-model are
delegated to the JRC EF reference package (EUPEF+21 §5.2.1, p.86, footnote) — expected absent,
not invented.

**Limits of this run:** I verified each leaf's **EF category, indicator name and unit** and
the toxicity/resource **glossary definitions** verbatim from `EUPEF+21`
(`PEF_CELEX_32021H2279_EN_TXT.pdf`, pages cited inline; pdf_search re-run this session). I did
**not** verify the underlying method documents (USEtox, AWARE, CML/ADP) — those PDFs are not in
the corpus — nor any EF NF/WF numeric value (delegated to the JRC package), nor the Min/Max
band values, weights (0.3333/0.3334 placeholders), or the cross-domain composite parents
(EN0, EN9). Page citations are the PDF reader page numbers returned by `pdf_search`; the same
Table 2 content appears at PDF p.30 and again at p.157, and the OJ-printed numbers (L 471/…)
used in `reviews/PEF-factors.md` differ by a constant offset.

## Inconsistencies & fixes

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | minor | EN7-1, EN7-2, EN7-3, EN8-1, EN8-2, EN8-3 | Leaf `Formula` text names only the characterisation model ("USEtox model" / "AWARE model" / "CML2002 model"); strategy is now `NORMALIZED_RATIO_STRATEGY` (characterised result ÷ EF NF) | Update each Formula to normalized-ratio wording, e.g. "Characterised result (unit, model) ÷ EF normalisation factor (Target Max); Min = 0" |
| 2 | minor | EN7, EN8 | Parent `Formula` text "Weighted sum … compared to a target value" predates the self-normalizing children; parents now weight-average already-normalized ratios | Update to "Weighted average of the normalized sub-categories (EN7-1/2/3 resp. EN8-1/2/3)" |
| 3 | minor | EN7-1, EN7-2, EN7-3 | Reference `USEtox2.0` diverges from EUPEF+21 Table 2 attribution "USEtox2.1 model" (deliberate collapse to the only registered Label) | Annotate the `USEtox2.0` References row as standing in for the EF-recommended USEtox 2.x family, or add a `USEtox2.1` row |
| 4 | minor | EN8-1 | Unit `m3` vs EF reference unit "m3 water eq of deprived water" (AWARE deprivation-weighted) | Relabel Unit to "m³ world eq. deprived" and confirm stored value is AWARE-weighted, not raw m³ |
| 5 | minor | EN8 (and EN7) Comment | Trailing Comment line "EN5-2 land use uses the 'pt' indicator, not m2a/FU" belongs to EN5-2, not the toxicity/resource family | Remove from EN7/EN8 Comment or relocate to EN5-2 |
| 6 | minor | EN7, EN8 | `Objective / Goal` cell empty while peers EN1–EN5 carry one (open from `reviews/EN-impact-pef.md` #7) | Add a one-line objective for each parent |
| 7 | minor | EN7-3 | Product Life Cycle Stages `S,M` differs from sibling toxicity leaves EN7-1/EN7-2 `S,M,D,U` | Confirm intended stage coverage; align if inconsistent |

### SOURCE-NOT-FOUND codes
`USEtox2.0` (EN7-1/2/3), `BA+17` (EN8-1), `OL+02` (EN8-2/3) — References rows exist, no PDF in
`data/literature/`. EF normalisation/weighting factor *values* (EUPEF+21 §5.2.1/§5.2.2) are
delegated to the online JRC EF reference package and are not files in the corpus — expected
absent; not invented.


---

## Archived per-phase ratios (EN131–135 carbon, EN441–445 water)

### EN131 — Sourcing Emission Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the emissions associated with the procurement of raw materials and inputs used in the product."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14067 p.7 ("raw material sourcing" as a life-cycle stage) and p.23 (emissions assigned to the stage in which they occur); maps to EN15804+A2 module A1 "Raw material supply" (per `reviews/EN1-carbon-phases.md`, EN15804+A2.pdf p.17/p.6). Re-verified this run.
- **Implementation check:** `Underlying Metrics = EN1-1\nEN1-2\nEN1-3` (Scopes 1/2/3); `Formula = (Actual - Min)/(Max - Min)`; strategy NORMALIZED_RATIO. `Actual` resolves to Scope1+2+3 of the whole product — **not** the sourcing-stage emissions the description names. So the row currently equals every other carbon phase (and the parent total), not a sourcing slice. Unit `%` is fine for a normalized ratio; the defect is the input wiring. Life-cycle-stage tag `S` (sourcing) is correct. Reference cell blank (children carry the Scope citations).
- **Proposed revision:** **keep as-is.** The description correctly states the sourcing-stage intent and matches the lifecycle stage it names; do not rewrite it to match the degenerate wiring.
- **Notes:** [major, deferred — not blocking] children should be a sourcing-stage emission input (EN15804 module A1–A3 / ISO 14067 partial CFP of sourcing processes), not Scope1+2+3. Row is ARCHIVED/out-of-score; fix tracked in `reviews/EN1-carbon-phases.md` (Inconsistencies items 1–2). Min/Max are external (EN15804 sets no benchmarks).

### EN132 — Production Emission Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the emissions generated from the manufacturing and assembly of the product."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14067 p.7/p.8 ("production"); EN15804+A2 module A3 "Manufacturing" (per phase review, p.17). Re-verified this run.
- **Implementation check:** Same wiring as EN131 (`EN1-1\nEN1-2\nEN1-3`, NORMALIZED_RATIO). `Actual` = Scope1+2+3 total, not production-stage emissions. Stage tag `M` (manufacturing) correct. Description names production/manufacturing/assembly — matches module A3 intent.
- **Proposed revision:** **keep as-is.** Description states correct production-stage intent.
- **Notes:** [major, deferred — not blocking] needs an A3 / production-stage partial-CFP input instead of Scope1+2+3. Tracked in `reviews/EN1-carbon-phases.md`.

### EN133 — Distribution Emission Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the emissions generated from the distribution of product to end users."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14067 p.8 ("transportation/delivery"); EN15804+A2 module A4 "Transport" (phase review, p.17). Re-verified this run.
- **Implementation check:** Same wiring (`EN1-1\nEN1-2\nEN1-3`). `Actual` = whole-product Scope1+2+3, not distribution-stage emissions. Stage tag `D` correct. Description names distribution-to-end-users — matches module A4 intent.
- **Proposed revision:** **keep as-is.**
- **Notes:** [major, deferred — not blocking] needs an A4 / distribution-stage input. Tracked in `reviews/EN1-carbon-phases.md`.

### EN134 — Use and Maintenance Emission Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the emissions during the operational use and maintenance of the product throughout its useful life."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14067 p.8 ("use"); EN15804+A2 use stage B1–B7 (B1 Use, B2 Maintenance, … B6 operational energy) (phase review, p.17/p.6). Re-verified this run.
- **Implementation check:** Same wiring (`EN1-1\nEN1-2\nEN1-3`). `Actual` = Scope1+2+3 total, not use-stage emissions. Stage tag `U` correct. Description (operational use + maintenance over useful life) mirrors B1 "Use" + B2 "Maintenance" — strong intent match.
- **Proposed revision:** **keep as-is.**
- **Notes:** [major, deferred — not blocking] needs a B1–B7 / use-stage input. Tracked in `reviews/EN1-carbon-phases.md`.

### EN135 — End-of-Life Emission Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the emissions associated with the processing and handling of the product when it reaches the end of its life cycle."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14067 p.8 ("end-of-life treatment"); EN15804+A2 modules C1–C4 (C1 Deconstruction, C2 Transport, C3 Waste processing, C4 Disposal) (phase review, p.17/p.6). Re-verified this run.
- **Implementation check:** Same wiring (`EN1-1\nEN1-2\nEN1-3`). `Actual` = Scope1+2+3 total, not EoL-stage emissions. Stage tag `E` correct. Description (processing/handling at end of life) matches C1–C4 intent.
- **Proposed revision:** **keep as-is.**
- **Notes:** [major, deferred — not blocking] needs a C1–C4 / EoL-stage input. Optional: note module D (recovery/recycling benefits beyond boundary) is excluded — acceptable for a screening KPI. Tracked in `reviews/EN1-carbon-phases.md`.

---

## Water phases (children of archived EN44)

### EN441 — Sourcing Water Footprint Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the water footprint associated with the procurement of raw materials and inputs used in the product."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14046 p.11 (water footprint is modular; per-stage footprints summable). Re-verified this run. Maps to EN15804+A2 module A1–A3 sourcing (per `reviews/EN4-water-phases.md`).
- **Implementation check:** `Underlying Metrics = EN4-1\nEN4-2\nEN4-3` (blue/green/gray *water types*); NORMALIZED_RATIO. `Actual` = blue+green+gray of the whole product (= EN4-4 Absolute Water Footprint), **not** a sourcing-stage water figure. Conflates the water-type axis with the life-cycle-stage axis, so every water phase equals the whole-product total. Stage tag `S` correct. Unit `%` fine. Reference blank on row.
- **Proposed revision:** **keep as-is.** Description correctly states the sourcing-stage water intent and matches its named stage.
- **Notes:** [major, deferred — not blocking] children should be a sourcing-stage water-consumption input (m3; EN15804 A1–A3), not blue+green+gray types. Row ARCHIVED/out-of-score; tracked in `reviews/EN4-water-phases.md` (Inconsistencies item 1). Min/Max external. Objective/Goal is blank (`None`) where active peers carry one — [minor, deferred] noted in the water review.

### EN442 — Production Water Footprint Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the water footprint associated from the manufacturing and assembly of the product."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14046 p.11 (stage modularity); EN15804+A2 A3 manufacturing (water review). Re-verified this run.
- **Implementation check:** Same wiring (`EN4-1\nEN4-2\nEN4-3`). `Actual` = blue+green+gray total, not production-stage water. Stage tag `M` correct. Description names manufacturing/assembly — matches A3 intent.
- **Proposed revision:** **keep the substance as-is**, with one optional grammar tidy: "associated **from**" → "associated **with**" (or simply "from the manufacturing and assembly"). Intent is correct; this is a wording nit only.
- **Notes:** [major, deferred — not blocking] needs a production-stage (A3) water input. [minor] grammar "associated from". Tracked in `reviews/EN4-water-phases.md`.

### EN443 — Distribution Water Footprint Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the water footprint associated from the distribution of product to end users."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14046 p.11; EN15804+A2 A4 transport (water review). Re-verified this run.
- **Implementation check:** Same wiring (`EN4-1\nEN4-2\nEN4-3`). `Actual` = blue+green+gray total, not distribution-stage water. Stage tag `D` correct. Description names distribution-to-end-users — matches A4 intent.
- **Proposed revision:** **keep the substance as-is**, optional grammar tidy "associated **from**" → "associated **with**".
- **Notes:** [major, deferred — not blocking] needs a distribution-stage (A4) water input. [minor] grammar "associated from". Tracked in `reviews/EN4-water-phases.md`.

### EN444 — Use and Maintenance Water Footprint Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the water footprint during the operational use and maintenance of the product throughout its useful life."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14046 p.11; EN15804+A2 B1–B7 use stage — operational water (B7) typically dominates here (water review). Re-verified this run.
- **Implementation check:** Same wiring (`EN4-1\nEN4-2\nEN4-3`). `Actual` = blue+green+gray total, not use-stage water. Stage tag `U` correct. Description (operational use + maintenance) matches B1–B7 intent; this is the stage where real product water use most often concentrates, so the missing per-stage input matters most here.
- **Proposed revision:** **keep as-is.**
- **Notes:** [major, deferred — not blocking] needs a use-stage (B1–B7) water input. Tracked in `reviews/EN4-water-phases.md`.

### EN445 — End-of-Life Water Footprint Ratio  [Level 4, aggregate(ratio), NORMALIZED_RATIO — ARCHIVED]
- **Current:** "Measures the water footprint associated with the processing and handling of the product when it reaches the end of its life cycle."
- **Verdict:** ADAPTED (implementation-gap flag).
- **Grounding:** ISO 14046 p.11; EN15804+A2 C1–C4 end-of-life (water review). Re-verified this run.
- **Implementation check:** Same wiring (`EN4-1\nEN4-2\nEN4-3`). `Actual` = blue+green+gray total, not EoL-stage water. Stage tag `E` correct. Description (processing/handling at end of life) matches C1–C4 intent.
- **Proposed revision:** **keep as-is.**
- **Notes:** [major, deferred — not blocking] needs an EoL-stage (C1–C4) water input. Tracked in `reviews/EN4-water-phases.md`.

---

## Inconsistencies & fixes

All findings below are **deferred / non-blocking** because the ten rows are archived
(`not in score`); they are recorded so the archived descriptions stay honest. The full
re-modelling fixes already live in the two phase reviews and are not duplicated here.

| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | major (deferred) | EN131/132/133/134/135 | All five carbon phases wire to identical children `EN1-1\nEN1-2\nEN1-3` (Scopes 1/2/3); `Actual` resolves to the whole-product Scope1+2+3 total, so each phase ratio degenerates to the parent total instead of its named lifecycle stage. Descriptions promise per-stage detail (correct intent) the impl cannot deliver. | Re-wire each phase to a stage-specific emission input per EN15804 module (A1–A3 / A3 / A4 / B1–B7 / C1–C4) or ISO 14067 partial CFP. **Keep descriptions** (correct intent). Tracked in `reviews/EN1-carbon-phases.md`. |
| 2 | major (deferred) | EN441/442/443/444/445 | All five water phases wire to identical children `EN4-1\nEN4-2\nEN4-3` (blue/green/gray *types*); `Actual` resolves to blue+green+gray of the whole product (= EN4-4), so each phase degenerates to the parent total. Conflates the water-type axis with the life-cycle-stage axis. | Re-wire each phase to a stage-specific water-consumption input (m3) per EN15804 modules A/B/C; reserve blue+green+gray sum for whole-product total EN4-4. **Keep descriptions.** Tracked in `reviews/EN4-water-phases.md`. |
| 3 | minor (deferred) | EN442, EN443 | Description grammar: "water footprint associated **from** …" (should be "associated **with**" / "from"). | Tidy wording; substance/intent unchanged. |
| 4 | minor (deferred) | EN441–445 | Objective/Goal blank (`None`) where active peers carry one. | Add objectives (already noted in `reviews/EN4-water-phases.md`). |

**SOURCE-NOT-FOUND codes:** none in this batch. The per-phase rows cite no reference codes
directly; the inherited-child reference orphans (`waterfootprintnetwork`, `TF+25`, the EN4
ISO/GRI codes, `WBCSD`) are out of scope for this lighter pass and are already documented in
the two phase reviews — not re-litigated here.

**Limits of this run:** this was a deliberately light description-vs-implementation pass on
archived rows. I re-verified only the two grounding citations carried forward (ISO 14067 p.7/
p.8/p.23 life-cycle stages; ISO 14046 p.11 stage modularity) via `pdf_search.py`; I did not
re-open EN15804+A2 or re-confirm the EN15804 module page numbers, the Min/Max benchmark
question, or the inherited-child reference codes — all of those remain as established in
`reviews/EN1-carbon-phases.md` and `reviews/EN4-water-phases.md`. I did not assess any numeric
values, weights, or bands. Verdicts here are intentionally ADAPTED (intent-correct,
implementation-incomplete) rather than UNSUPPORTED as in the deeper reviews, because this pass
judges the *description against its named lifecycle stage and the current impl*, not the
sufficiency of the wiring as a grounded computation.

## Batch summary

**Counts (10 archived rows):** ADAPTED (implementation-gap flag) 10; CONSISTENT 0; DRIFTED 0;
UNVERIFIABLE 0.

**Proposed description rewrites:** none substantive — all ten descriptions correctly state
their intended lifecycle stage and are kept as-is (conservative stance: do not rewrite to
match a broken implementation). Two optional grammar tidies only: EN442 and EN443 ("associated
from" → "associated with").

**User decisions needed:** none blocking. The single underlying defect — per-phase ratios
degenerate to the parent total because they reuse whole-product children — is **already
tracked** in `reviews/EN1-carbon-phases.md` (carbon) and `reviews/EN4-water-phases.md`
(water). Because all ten rows are archived / out-of-score, the re-wiring fix is **deferred**
and is not blocking. No new sources were invented; the two carried-forward citations were
re-verified.
