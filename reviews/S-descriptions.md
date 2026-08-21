# S description audit — refine + ground KPI descriptions

**Scope:** the full **Social Impact (S) domain — all 31 KPIs**, audited family by family
(S1 Sourcing, S2 Customer Well-Being, S3 Workforce Welfare, S0 root). Goal: reconcile each
handmade description with its current implementation and ground it in the cited literature
where a source applies.
**Date:** 2026-06-29.
**Method:** `snapshot/Social Impact.tsv` (+ `References.tsv`); verbatim page-cited quotes via
`tools/scripts/pdf_search.py`; conservative stance.
**Verdict legend:** CONSISTENT / DRIFTED / ADAPTED / UNVERIFIABLE (see EN/EC/C/R reports).
Columns: C=Description, G=Potential Reference Values, H=Unit, I=Formula, J=Reference, R=Comment.

---

## S domain — consolidated summary & decisions

**Verdicts across all 31 S KPIs:** CONSISTENT 16 · DRIFTED 10 · ADAPTED 4 · UNVERIFIABLE 1.
Notable: **S0's root formula is correct** (the only domain root without the stale-child-list
drift), and the **S34 re-model is verified fully wired** (S3-5/S3-6/S3-7 are `_self()`
self-normalizing leaves, S34 weight-averages them). The defects are description drift on the
re-modelled S34 leaves, a customer-family wiring issue, and several citation problems. Nothing
applied yet — all proposals.

### A. Description rewrites — DRIFTED rows (10)

| KPI | Problem | Proposed |
|---|---|---|
| S11 | citation-scope defect (see §C) + thin desc | name certified⊆total ethical-supplier share |
| S22 | desc says "measures incidents"; formula is `1 − incidents/customers` (a safety rate) | rewrite to the incident-rate complement |
| S2-6 | desc copy-pasted from S2-2 ("survey respondents"); it's the customer-inquiry count | rewrite to inquiries (denominator of S23/S24) |
| S3 | wording doesn't name its sub-scores | rewrite to S31/S32/S33/S34 |
| S31 | desc + ISO 10004 citation are for *external customers*, not employee satisfaction | rewrite; re-anchor to ESRS S1 (see §C) |
| S34 | composite of self-normalized children, but desc still reads pre-re-model | rewrite to weighted-avg of S3-5/S3-6/S3-7 |
| S3-1 | employee-feedback raw input mis-anchored to ISO 10004 | rewrite; re-anchor (see §C) |
| S3-5 | desc reads as a raw € figure, not a self-normalized 0–1 score | rewrite — **see decision D1** |
| S3-6 | raw € salary desc, not the self-normalized score | rewrite (normalized vs company target band) |
| S3-7 | raw # jobs desc, not the self-normalized score | rewrite (normalized vs company target band) |

*(Units €/€/# on S3-5/6/7 are correct as-is — they are the input units of self-normalizing rows, like every other `_self()` leaf; do not change them.)*

### B. Adjacent-cell drift (apply with the rewrites)

- **S22 child-wiring:** `Underlying Metrics` lists `S2-2` (surveyees), but the formula
  `1 − incidents/customers` uses only S2-3/S2-4 — remove S2-2 from S22 (col E) and the
  reciprocal Parent link on S2-2 (col F).
- **S2-3** stray newline in its Parent-Metrics cell (`\nS22` → `S22`).
- Name/format tidies: S2 Indicator Name "**Costumer**"→"Customer"; S21 stray "R" token;
  S1-2 "uch as"→"such as"; S0 "translates"→"translate".

### C. Citation issues

- **S11 `GRI 308-1` → `GRI 414-1`** (decision-free correction): GRI 308-1 is *environmental*
  supplier screening; S11 is an *ethical/social* supplier metric → GRI 414-1 (social supplier
  assessment) is the right analogue. **GRI 414 is in the corpus but not a References Label —
  add the row** (like DIN SPEC 91472).
- **S12** add `GRI 204-1` (proportion of spend on local suppliers) — tighter than the current
  ISO 26000; **add the GRI 204 References row** (PDF present).
- **S31 / S3-1 — drop `ISO 10004`** (it scopes itself to customers *external* to the org, p.9)
  and re-anchor to **ESRS S1** (own workforce).
- **S33 `ESRS S1-1` (Policies) → `ESRS S1-14`** (the health-&-safety disclosure; S3-4 already
  cites S1-14 correctly).
- **S23** blank Reference → add `ISO 26000` §6.7.6 (responsive service) for traceability.

### D. Decisions — RESOLVED 2026-06-29

1. **S3-5 → describe per current implementation + flag the living-wage question. ✓** In this
   pass S3-5 is described as one of three independent self-normalized components S34 averages
   (matching the engine). The open modeling question — whether cost-of-living should instead be
   the **denominator of a living-wage ratio** with S3-6 salary — is recorded here as a separate
   future decision; **no engine/model change in this pass** (it would be a re-model like
   R12/EN43, out of the descriptions scope).

### E. ADAPTED Comment flags (non-obvious only)

S12 (supplier-count ratio vs the standards' procurement-*spend* framing), S22, S23, S24, and
S3-5/S3-6/S3-7 (raw social figures self-normalized against company target bands) — keep the
description, add a short Comment-cell note where the adaptation isn't self-evident; skip obvious
rows, matching the EN/EC/C/R policy.

### S0 — Social Impact Score  [Level 1, root composite, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "The Social Impact measures the social value created by the product's sustainability and circularity initiatives. It helps evaluate how these efforts translates to societal well-being and how viable the product is from a social aspect."
- **Verdict:** CONSISTENT (composite/root; internal check) — the prose correctly describes a roll-up of the three social pillars. Unlike the EN0/EC0/C0/R0 roots flagged in the gap-fix context, **S0's Formula text is NOT stale**: it reads `Sum (weight * S1 + … + weight * S3)` and the children are `S1\nS2\nS3`, so it correctly names the right last child (S3). No `…+ S<wrong>` defect here.
- **Grounding:** composite/root — no single literature source expected; Reference cell blank by design. The three child pillars are independently grounded on their own rows (S1 sourcing → GRI 204 / ISO 26000 / PSILCA; S2 customer well-being; S3 workforce → GRI 403 / ESRS S1).
- **Implementation check:** `Underlying Metrics = S1\nS2\nS3`; Parent = None; strategy WEIGHTED_AVERAGE with child weights 0.3333 / 0.3333 / 0.3334 (sum ≈ 1). Unit % is compatible with averaging three 0–1/% sub-scores. Description ("social value … societal well-being") maps cleanly onto the three children. No drift.
- **Proposed revision (C):** keep as-is. (Optional, only if you want the children explicit and the typo fixed: "Aggregates the product's social performance into one score by combining its Sourcing & Procurement (S1), Customer Well-Being (S2) and Workforce Welfare (S3) sub-scores. Reflects how the product's sustainability and circularity initiatives translate into societal well-being.")
- **Notes:** [minor] grammar typo in current text — "how these efforts **translates**" → "translate". Blank Reference is correct for a composite root — not a defect. Formula text already matches the three current children; no EN0-style `…+ S<wrong>` correction needed. Verified the gap-fix concern from the brief: **S0 is clean**, no formula fix required.

### S1 — Sourcing and Procurement  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the social and ethical impacts of the product's procurement processes. Focuses on ensuring that sourcing practices align with ethical fair trade principles and promotes local contribution."
- **Verdict:** CONSISTENT (composite parent; internal check) — the prose correctly describes a roll-up of an ethical-supplier arm (S11) and a local-sourcing arm (S12), matching `Underlying = S11\nS12` and `Formula = Sum (weight * S11 + weight * S12)`. "ethical fair trade principles" → S11; "local contribution" → S12.
- **Grounding:** composite/parent — no single source expected (Reference cell blank by design). The two arms are grounded on the children:
  - GRI 204 p.4 (procurement-practices scope): "This Standard addresses the topic of procurement practices. This covers an organization's support for local suppliers or those owned by women or members of vulnerable groups." (`data/literature/GRI - Global Reporting Initiative/GRI 204_ Procurement Practices 2016.pdf`)
  - ISO 26000 p.64 (6.6.1.1, fair operating practices): "Fair operating practices concern ethical conduct in an organization's dealings with other organizations. These include relationships between organizations and government agencies, as well as between organizations and their … suppliers …" (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`)
  - PSILCA p.5 / p.17 (supply-chain stakeholder framing): the database organises supplier social risk under "Stakeholder Value Chain actors" with subcategory "Promoting social responsibility — Social responsibility along the supply chain". (`data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf`)
  - ESRS S2 p.1 (Objective): "The objective of this Standard is to specify disclosure requirements which will enable users of the sustainability statement to understand material impacts on value chain workers connected with the undertaking's own operations and value chain …" (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS S2 to S4 Delegated-act-2023-5303-annex-1_en.pdf`) — grounds the "social impacts of procurement / value chain" framing of the parent.
- **Implementation check:** Children S11, S12 both exist; strategy WEIGHTED_AVERAGE (each weight 0.5). Unit % compatible with averaging two 0–1/% sub-scores. The Potential Reference Values cell is "None" and Comment carries `0.3333` (this is S1's own weight as a child of S0, not a defect). No drift between prose, formula, and children.
- **Proposed revision (C):** keep current text; optional light rewrite to make the two arms explicit: "Aggregates the social and ethical performance of the product's procurement into one score by combining the share of certified ethical/fair-trade suppliers (S11) and the share of local suppliers (S12). Higher means sourcing leans more on ethically-certified and locally-based suppliers."
- **Notes:** Blank Reference is correct for a composite parent — not a defect. No formula-text drift (formula names S11 + S12, matching the live children). No Comment flag needed (composite). PSILCA / ESRS S2 are optional family-level grounding anchors if a Reference is later wanted on the parent — not required.

### S11 — Certified Ethical Supplier Share  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the engagement with suppliers certified under ethical or fair trade standards. Ensures adherence to ethical labor and sourcing standards across the supply chain."
- **Verdict:** DRIFTED (citation, not formula) — the **description and the formula are mutually consistent** (a certified-ethical-supplier count ratio), but the **cited code `GRI 308-1` is the wrong GRI standard**. GRI 308-1 is *environmental* supplier screening; S11 is a *social/ethical* supplier metric. The correct GRI analogue is **GRI 414-1** (social criteria). This is a citation drift to fix, not a description rewrite.
- **Grounding:**
  - **Cited code is mis-scoped.** GRI 308 p.8 (DR 308-1): "Disclosure 308-1 New suppliers that were screened using **environmental** criteria … Percentage of new suppliers that were screened using environmental criteria." (`data/literature/GRI - Global Reporting Initiative/GRI 308_ Supplier Environmental Assessment 2016.pdf`) — this is environmental, not ethical/social.
  - **Correct analogue.** GRI 414 p.3 / p.4 (DR 414-1): "Disclosure 414-1 New suppliers that were screened using **social** criteria"; "Suppliers can be assessed for a range of social criteria, including human rights (such as child labor and forced or compulsory labor); employment practices; health and safety practices; industrial relations; incidents …" (`data/literature/GRI - Global Reporting Initiative/GRI 414_ Supplier Social Assessment 2016.pdf`) — this matches S11's "ethical labor and sourcing standards."
  - **Concept anchor for "certified" suppliers / supply-chain SR.** ISO 26000 p.64 (fair operating practices, ethical conduct toward suppliers, quote above) and PSILCA p.17: under "Promoting social responsibility" the indicator is "Social responsibility along the supply chain — Number of companies in the sector". (`data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf`)
- **Implementation check:** Children S1-1 (total suppliers) and S1-2 (certified ethical suppliers) both exist; Formula `Share = Number of certified ethical suppliers / Number of total suppliers`, then `(Share - Min)/(Max - Min)`. Strategy NORMALIZED_RATIO matches. Unit % consistent. Min/Max seeded 0/1 (Comment documents this; the ratio is already a 0–1 score). Note: the **child wiring is correct** (numerator S1-2 ⊆ denominator S1-1), so the formula is well-formed. **However**, the description's verb "engagement with suppliers" and GRI 414-1's "*screened/assessed* using social criteria" are not identical to S11's "*certified under* ethical/fair-trade standards" — S11 counts third-party-certified suppliers (GOTS, Fairmined, Fair Trade USA, Rainforest Alliance — see S1-2), which is a *narrower, certification-based* construction than GRI's screening disclosure. That makes the GRI tie an ADAPTED grounding even after the 308→414 fix.
- **Proposed revision (C):** "Measures the share of the product's suppliers that hold a recognised ethical or fair-trade certification (certified ethical suppliers ÷ total suppliers). Higher means more of the supply chain is independently certified against ethical labour and sourcing standards."
- **Notes:**
  - [major] **Reference (J): `GRI 308-1` is mis-scoped** (environmental supplier screening). Change to **`GRI 414-1`** (social supplier screening) — the social analogue and the standard that actually covers ethical/labour criteria. `GRI 414-1` is **not yet a Label in References.tsv** (only `GRI 308-1` exists, line 84), so a References row must be added (Title "GRI 414: Supplier Social Assessment 2016"; the file `GRI 414_ Supplier Social Assessment 2016.pdf` is present in the corpus).
  - [minor] Comment-cell flag (ADAPTED, non-obvious): "Product-level certified-supplier share; adapts GRI 414-1 (social supplier screening) — GRI reports a *screening* percentage of *new* suppliers, whereas S11 counts third-party *certified* suppliers over all suppliers. Band author-defined."
  - Optional secondary citation: `ISO 26000` (fair operating practices) and/or `PSILCA` (supply-chain social responsibility) as concept anchors if multi-citation is desired.

### S12 — Local Sourcing Share  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the share of local sourcing suppliers from the overall suppliers."
- **Verdict:** ADAPTED — faithful product-level adaptation of the "local suppliers" procurement concept; the cited `ISO 26000` genuinely covers it, and GRI 204-1 is an even tighter match. The adaptation is a **supplier-count** ratio vs. the standards' **spend-based** proportion.
- **Grounding:**
  - ISO 26000 p.83 (6.8, community involvement and development): "consider giving preference to local suppliers of products and services and contributing to local supplier development where possible". (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`) — directly supports favouring local suppliers (the cited code is valid).
  - ISO 26000 p.84: "increasing local procurement and any outsourcing so as to support local development". (same file)
  - GRI 204 p.8 (DR 204-1): "Percentage of the procurement budget used for significant locations of operation that is spent on suppliers local to that operation (such as percentage of products and services purchased locally). a. The organization's geographical definition of 'local'." (`data/literature/GRI - Global Reporting Initiative/GRI 204_ Procurement Practices 2016.pdf`) — the tightest standard for a local-sourcing ratio, but measured by **spend**, not supplier count.
- **Implementation check:** Children S1-1 (total suppliers) and S1-3 (local suppliers) both exist; Formula `Share = Number of local suppliers / Number of total suppliers`, then `(Share - Min)/(Max - Min)`. Strategy NORMALIZED_RATIO matches. Unit % consistent. Min/Max seeded 0/1 (Comment documents this). Child wiring correct (numerator S1-3 ⊆ denominator S1-1). The KPI computes a **count-based** local share; both GRI 204-1 and ISO 26000 frame local sourcing by **procurement spend** — so the count ratio is the author's product-level simplification.
- **Proposed revision (C):** "Measures the share of the product's suppliers that are local (local suppliers ÷ total suppliers), where 'local' is the community and, failing that, the same country. Higher means more sourcing supports the local economy and shortens transport."
- **Notes:**
  - [minor] Reference (J): keep `ISO 26000` (valid — p.83) and **add `GRI 204`** (DR 204-1, the precise local-sourcing disclosure). `GRI 204` is **not yet a Label in References.tsv**; add a row (Title "GRI 204: Procurement Practices 2016"; file `GRI 204_ Procurement Practices 2016.pdf` present in corpus).
  - [minor] Comment-cell flag (ADAPTED, non-obvious): "Product-level local-supplier *count* share; GRI 204-1 and ISO 26000 frame local sourcing by procurement *spend*, not supplier count — count basis is the author's simplification. 'Local' = community, else same country (see S1-3)."

### S1-1 — Number of Total Suppliers  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Number of suppliers for sourcing and procurement involved throughout the whole product's lifecycle."
- **Verdict:** CONSISTENT — accurate raw-input definition; it is the shared denominator of both S11 and S12.
- **Grounding:** raw count input; the denominator concept is implicit in any supplier-share disclosure — GRI 204 p.8 reports the local share against the total procurement base, and GRI 414-1 against total new suppliers (quotes above). No standard prescribes a "total supplier count" datapoint at product level; the figure is an author/product input.
- **Implementation check:** Raw leaf, no formula; Parent Metrics = `S11\nS12`; Unit `#`. Feeds both ratio denominators. Consistent with S1-2 (certified ⊆ total) and S1-3 (local ⊆ total). No drift.
- **Proposed revision (C):** keep as-is.
- **Notes:** Reference blank — appropriate for a raw count denominator (no datapoint-level benchmark). No Comment flag needed (obvious raw input).

### S1-2 — Number of Certified Ethical Suppliers  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Number of suppliers certified from ethical standard bodies uch as the Global Organic Textile Standard (GOTS), Fairmined, Fair Trade USA, the Rainforest Alliance, etc."
- **Verdict:** CONSISTENT — accurate raw-input definition; it is the numerator of S11. The named certification bodies make the "certified ethical" basis explicit and concrete.
- **Grounding:** GRI 414 p.4 grounds the social-supplier concept ("Suppliers can be assessed for a range of social criteria, including human rights … forced or compulsory labor; employment practices; health and safety practices …"). ISO 26000 p.64 grounds ethical conduct toward suppliers (fair operating practices). The specific certification schemes (GOTS, Fairmined, Fair Trade USA, Rainforest Alliance) are author-supplied examples, not from a single cited standard. (files as above)
- **Implementation check:** Raw leaf; Parent = `S11`; Unit `#`. Numerator of S11; S1-2 ⊆ S1-1 so the S11 share is in [0,1]. Consistent.
- **Proposed revision (C):** keep content; fix the typo only: "Number of suppliers certified by ethical/fair-trade standard bodies such as the Global Organic Textile Standard (GOTS), Fairmined, Fair Trade USA, the Rainforest Alliance, etc."
- **Notes:** [minor] typo in current text — "uch as" → "such as". Reference blank — acceptable for a raw count (optionally mirror `GRI 414-1` from S11 for traceability). No Comment flag needed.

### S1-3 — Number of Local Suppliers  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Number of suppliers located in the community. If not possible, extends to the same country."
- **Verdict:** CONSISTENT — accurate raw-input definition; it is the numerator of S12. The "community, else same country" rule supplies the geographical definition of 'local' that GRI 204-1 explicitly requires the reporter to state.
- **Grounding:** GRI 204 p.8 (DR 204-1) requires "a. The organization's geographical definition of 'local'." — S1-3's "community, else same country" *is* that definition. ISO 26000 p.83 grounds the preference for local suppliers. (files as above)
- **Implementation check:** Raw leaf; Parent = `S12`; Unit `#`. Numerator of S12; S1-3 ⊆ S1-1 so the S12 share is in [0,1]. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** Reference blank — acceptable for a raw count (optionally mirror `GRI 204` / `ISO 26000` from S12 for traceability). No Comment flag needed. The embedded 'local' definition is good practice (satisfies GRI 204-1 requirement a).

---

## Batch summary

**Counts (7 metrics):** CONSISTENT 5 (S0, S1, S1-1, S1-2, S1-3); DRIFTED 1 (S11 — citation only);
ADAPTED 1 (S12); UNVERIFIABLE 0. No formula contradicts its children in this family; the
one real defect is a mis-scoped citation on S11 (GRI 308-1 → 414-1).

**Gap-fix concern (S0 formula) — RESOLVED:** S0's Formula text `Sum (weight * S1 + … + weight * S3)`
already names the correct last child (S3) and matches `Underlying = S1\nS2\nS3`. **No `…+ S<wrong>`
staleness** like EN0/EC0/C0/R0 — S0 needs no formula fix.

**Proposed description rewrites:** light/optional only — S11 (sharpen to certified÷total),
S12 (sharpen, add 'local' definition), S1-2 (typo fix "uch as"). S0, S1, S1-1, S1-3 keep
current text (faithful; optional clarifications offered). S0 has a grammar typo ("translates").

**Adjacent-cell drift to fix:**
1. [major] **S11 Reference (J): `GRI 308-1` → `GRI 414-1`.** 308 is *environmental* supplier
   screening; 414 is the *social/ethical* analogue that actually covers labour/human-rights
   criteria. Requires adding a `GRI 414-1` row to References.tsv (PDF present).
2. [minor] **S12 Reference (J): add `GRI 204`** alongside the valid `ISO 26000`. GRI 204-1 is
   the precise local-sourcing disclosure. Requires adding a `GRI 204` row to References.tsv
   (PDF present).
3. [minor] **S1-2 Description (C): typo** "uch as" → "such as".
4. [minor] **S0 Description (C): grammar** "how these efforts translates" → "translate".
5. [minor] Comment flags (R) — add ADAPTED notes only where non-obvious: **S11** (GRI 414-1
   screening vs certified-count; band author-defined) and **S12** (spend-based standard vs
   count-based KPI). Skip flags on the obvious composites (S0, S1) and raw leaves (S1-1/2/3).

**Decisions needed (human):**
- Approve **S11 citation change GRI 308-1 → GRI 414-1** (and the new References row). This is
  the only substantive correctness fix in the batch.
- Confirm adding **`GRI 204`** as a second citation on **S12** (keep `ISO 26000`).
- Confirm the count-based vs spend-based local-sourcing simplification on S12 is intended
  (it is a reasonable product-level adaptation; flagged, not rewritten).

**SOURCE-NOT-FOUND codes:** none. All cited codes either resolve in References.tsv
(`ISO 26000` line 16; `GRI 308-1` line 84) or, where a fix is proposed, the target PDFs are
present in the corpus (`GRI 414` and `GRI 204` files exist; only their References.tsv Labels
are missing — a hygiene add, not a missing source). PSILCA and ESRS S2 PDFs are present and
were read as optional family anchors.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above; I did not
read full standard sections beyond the cited pages. I verified that GRI 308-1 is environmental
and GRI 414-1 is social from their own contents/headers (pp.3–8 each), and the local-sourcing
disclosures from GRI 204 p.4/p.8 and ISO 26000 p.83/p.84. I did not audit Min/Max bands,
weights, Example Values, the S2/S3 families (out of scope), or the cross-domain placement of
S0. No standard supplies a "certified-ethical-supplier share" or "local-supplier count share"
datapoint — the ratios themselves are author-defined product constructions (legitimate); the
cited standards ground the *concepts*, which is why S11/S12 are citation-fix / ADAPTED rather
than UNVERIFIABLE.


---

## S2 — Customer Well-Being

### S2 — Costumer Well-Being Score  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current:** "Measures the product's impact on the customer's satisfaction, safety, and accessibility. It reflects the quality of life for its customers."
- **Verdict:** CONSISTENT (composite parent; internal check) — the prose rolls up satisfaction (S21/S24), safety (S22) and service (S23/S24); the children list `S21\nS22\nS23\nS24` and `Formula = Sum (weight * S21 + … + weight * S24)` match. **But the Indicator Name has a typo: "Costumer" → "Customer".**
- **Grounding:** composite/parent — blank Reference is correct by design. The three concept arms are grounded on the children's rows (ISO 10004 satisfaction; GRI 416 / ISO 26000 §6.7.4 health & safety; ISO 26000 §6.7.6 service/support). ESRS S4 frames the same consumer-impact triad — ESRS S4, p.32: "(a) information-related impacts on consumers and/or end-users … (b) personal safety of consumers and/or end-users (for example, health and safety, security of a person and protection of children); (c) social inclusion of consumers and/or end-users (for example, non-discrimination, access to products and services …)." (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS S2 to S4 Delegated-act-2023-5303-annex-1_en.pdf`)
- **Implementation check:** Children S21/S22/S23/S24 all exist; strategy WEIGHTED_AVERAGE; Unit % compatible with averaging four 0–1/% sub-scores. Formula text already names the current four children (no stale-grandchild drift). Note: the word "accessibility" in the prose maps loosely — there is no explicit accessibility child; it is most defensibly read as service access (S23 timeliness / S24 service satisfaction).
- **Proposed revision (C):** "Aggregates the product's effect on customer well-being into one score by combining customer satisfaction (S21), product health & safety (S22), customer-service timeliness (S23) and customer-service satisfaction (S24). Reflects the overall customer experience and quality of life delivered by the product."
- **Notes:** [minor] **Indicator-Name typo "Costumer" → "Customer"** (fix in the name cell). Composite — keep blank Reference. "accessibility" in the current text has no dedicated child; the proposed revision replaces it with the service arms actually wired. Parent S0 is outside this batch. **Comment flag (R) not needed** (composite, self-evident).

### S21 — Customer Satisfaction Score  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the average customer satisfaction of the product. Reflects consumer's perception of quality, reliability, and overall value of R products. Needs a robust, standardized framework and methodology i.e. CSAT, NPS, CES, SERVQUAL, etc."
- **Verdict:** CONSISTENT (substance) with two hygiene/citation notes — the prose matches `Avg = Customer Feedback Results / Number of Surveyee`, then `(Avg - Min)/(Max - Min)` over children S2-1 (feedback) and S2-2 (surveyee). The framework list (CSAT/NPS/CES/SERVQUAL) is method guidance, not a formula mismatch.
- **Grounding:** ISO 10004, p.7: "One of the key elements of organizational success is the customer's satisfaction with the organization and its products and services. Therefore, it is necessary to monitor and measure customer satisfaction." (`data/literature/DIN ISO 10004_2019-07-00_EN_3082656 Customer Satisfaction.pdf`). The standard's own structure distinguishes direct vs. indirect satisfaction measurement — ISO 10004, p.2 (contents): "7.3.2 Indirect indicators of customer satisfaction … 7.3.3 Direct measures of customer satisfaction" (same file). ISO 10004 grounds the *monitoring/measuring* concept; it does **not** prescribe the specific feedback/surveyee ratio (author-defined).
- **Implementation check:** Children S2-1 (Customer Feedback Results) and S2-2 (Number of Surveyee) both exist; ratio normalized to %, consistent with Unit %. Reference cell = `ISO 9001\nISO 10004` — ISO 10004 is the on-point customer-satisfaction-measurement standard; ISO 9001 is the parent QMS standard (defensible but secondary). Note S2-1's Unit is "-" (unspecified) and S2-2 is "#", so the ratio's scale depends on how feedback is encoded — see S2-1.
- **Proposed revision (C):** "Measures average customer satisfaction with the product as the mean feedback score across survey respondents (customer feedback results ÷ number of surveyees), normalized to a target band. Should be collected with a standardized instrument (e.g. CSAT, NPS, CES, SERVQUAL)."
- **Notes:** [minor] "value of R products" reads as a stray draft token ("R") — drop it. [minor] Reference: ISO 10004 is the tighter ground for satisfaction *measurement*; keep both but lead with ISO 10004. **Comment flag (R) not needed** (the ISO 10004 satisfaction concept is self-evident). Min/Max band on this ratio is author-defined.

### S22 — Customer Health and Safety  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the reported safety incidents related to product use and is compared to a reference value."
- **Verdict:** DRIFTED — two issues. (1) The Formula is `1 - (Reported Customer Incidents / Number of Customers)`, i.e. an incident-rate **complement** (higher = safer), but the description says only "measures the reported safety incidents," which describes the raw count, not the safety *score* the formula computes. (2) Child wiring is inconsistent: `Underlying Metrics = S2-2\nS2-3\nS2-4`, but the formula consumes only **S2-4** (Reported Customer Incidents) and **S2-3** (Number of Customers); **S2-2 (Number of Surveyee) is listed as a child but is not used** in the S22 formula.
- **Grounding:** GRI 416, p.9 (Disclosure 416-2): "Total number of incidents of non-compliance with regulations and/or voluntary codes concerning the health and safety impacts of products and services within the reporting period …" (`data/literature/GRI - Global Reporting Initiative/GRI 416_ Customer Health and Safety 2016.pdf`). The product-safety concept is grounded by ISO 26000 §6.7.4 — ISO 26000, p.71: "6.7.4 Consumer issue 2: Protecting consumers' health and safety … Protection of consumers' health and safety involves the provision of products and services that are safe and that do not carry unacceptable risk of harm when used …" (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`). GRI 416-2 grounds the *incident count* (input S2-4); the safety *rate complement* is author-constructed.
- **Implementation check:** S2-3 (Number of Customers) and S2-4 (Reported Customer Incidents) exist and feed the formula; S2-2 (Number of Surveyee) is a stray child here (it belongs to S21). Unit % is consistent with a 0–1 complement. Note the formula has no explicit `(score - Min)/(Max - Min)` step in the cell (unlike S21/S23/S24) although strategy is NORMALIZED_RATIO and Min/Max=0/1 are seeded — the `1 - rate` already yields a 0–1 score, so this is acceptable but inconsistent in presentation with its siblings.
- **Proposed revision (C):** "Measures product health & safety as one minus the customer-incident rate — i.e. 1 − (reported customer safety incidents (S2-4) ÷ number of customers (S2-3)). Higher means fewer product-use safety incidents per customer."
- **Notes:**
  - [major] **Remove S2-2 from S22's `Underlying Metrics`** (it is not consumed by the formula; S22's true inputs are S2-3 and S2-4). Either drop S2-2 or, if a per-surveyee denominator was intended, reconcile the formula — but as written, Number of Customers (S2-3) is the denominator.
  - [minor] Description rewritten so it describes the safety *score* (complement), not just the incident count.
  - [minor] For presentation consistency with S21/S23/S24, optionally show the `(score - Min)/(Max - Min)` step in the Formula cell (I).
  - **Comment flag (R):** product/service-level adaptation of org-level GRI 416-2 incident disclosure — non-obvious (GRI reports a count; this KPI builds a per-customer safety rate), so a short Comment is warranted: "Product-level safety-rate complement; adapts GRI 416-2 incident disclosure / ISO 26000 §6.7.4. Rate construction author-defined."

### S2-1 — Customer Feedback Results  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Customer feedback results."
- **Verdict:** CONSISTENT but circular/vague — the description merely restates the indicator name and does not say what is counted or in what units (the cell Unit is "-").
- **Grounding:** ISO 10004, p.2 (contents): "7.3.3 Direct measures of customer satisfaction" (`data/literature/DIN ISO 10004_2019-07-00_EN_3082656 Customer Satisfaction.pdf`) — grounds that direct satisfaction measures are the survey output feeding a satisfaction metric.
- **Implementation check:** Raw leaf; numerator of S21 (`Customer Feedback Results / Number of Surveyee`). Unit "-" is unspecified; the S21 average's scale depends entirely on how this is encoded (sum of scores? total satisfied responses?). Reference `ISO 10004` is appropriate.
- **Proposed revision (C):** "The aggregate customer-satisfaction score collected from surveys (e.g. the sum of respondents' ratings on a standardized scale such as CSAT/NPS); numerator of S21. Encode on the same scale as the survey instrument used."
- **Notes:** [minor] Description currently just restates the name (circular). [minor] Unit "-" — define the scale on this leaf so the S21 average is well-formed. No Comment flag needed.

### S2-2 — Number of Surveyee  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The total number of survey respondents in a given timeframe."
- **Verdict:** CONSISTENT — accurate raw count; denominator of S21's average. Unit "#" consistent.
- **Grounding:** ISO 10004, p.7 (monitoring/measuring customer satisfaction, quote above) — the respondent base of a satisfaction survey is the denominator of any average-satisfaction measure. (`data/literature/DIN ISO 10004…Customer Satisfaction.pdf`)
- **Implementation check:** Raw leaf; `Parent Metrics = S21\nS22`. It is correctly the S21 denominator, but it is **wrongly listed as a parent/child of S22** (the S22 formula does not use surveyees) — see the S22 fix.
- **Proposed revision (C):** keep as-is.
- **Notes:** [major, cross-ref] S2-2's `Parent Metrics` includes S22, mirroring the stray S2-2 entry in S22's children — remove the S22 link on both rows (S2-2 belongs to S21 only). "Surveyee" is informal but unambiguous; optionally "survey respondents."

### S2-3 — Number of Customers  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The total number of customers in a given timeframe."
- **Verdict:** CONSISTENT — accurate raw count; denominator of the S22 safety-rate. Unit "#" consistent.
- **Grounding:** concept-supporting only — GRI 416-2 (incident disclosure, quote above) implies a per-population safety rate; the customer-base denominator is the author's normalization choice. (`data/literature/GRI - Global Reporting Initiative/GRI 416_ Customer Health and Safety 2016.pdf`)
- **Implementation check:** Raw leaf feeding S22 (`Reported Customer Incidents / Number of Customers`). **The `Parent Metrics` cell reads `\nS22` — a stray leading newline** (should be `S22`).
- **Proposed revision (C):** keep as-is.
- **Notes:** [minor] **Fix the stray leading newline in the Parent Metrics cell (`\nS22` → `S22`).** No Comment flag needed.

### S2-4 — Reported Customer Incidents  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Total customer safety incidents related to the use of the product."
- **Verdict:** CONSISTENT — accurate raw count; numerator of the S22 safety-rate. Unit "#" consistent. Reference `GRI 416-2` is exactly on point.
- **Grounding:** GRI 416, p.9 (Disclosure 416-2): "Total number of incidents of non-compliance with regulations and/or voluntary codes concerning the health and safety impacts of products and services within the reporting period …" (`data/literature/GRI - Global Reporting Initiative/GRI 416_ Customer Health and Safety 2016.pdf`).
- **Implementation check:** Raw leaf; Parent = S22; feeds the S22 numerator. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** [minor, optional] GRI 416-2 is specifically *non-compliance* incidents; the KPI counts product-use safety incidents more broadly — a faithful, slightly broader adaptation. Acceptable; flag only if strict GRI alignment is wanted. No mandatory Comment.

### S23 — Customer Service Timeliness  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the response times of customer inquiries and compared with its target value."
- **Verdict:** UNVERIFIABLE (no citable source for the ratio) + light rewrite. The Formula `Avg = Response Times / Number of Inquiries`, then `(Avg - Min)/(Max - Min)` is an author-defined average-response-time score; **the Reference cell is blank** and no retrieved standard prescribes this ratio. The concept (service responsiveness) is groundable in ISO 26000 §6.7.6, but the metric itself is author-defined.
- **Grounding (concept only):** ISO 26000, p.73: "6.7.6 Consumer issue 4: Consumer service, support, and complaint and dispute resolution … Consumer service, support, and complaint and dispute resolution are the mechanisms an organization uses to address the needs of consumers after products and services are bought or provided." (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`). ISO 10004, p.8 also links complaint/response handling to satisfaction: "the frequency and type of complaints can be an indirect indicator of customer satisfaction (see 7.3.2)." (`data/literature/DIN ISO 10004…Customer Satisfaction.pdf`). Neither prescribes a response-time average.
- **Implementation check:** Children S2-5 (Response Times) and S2-6 (Number of Inquiries) both exist; `Avg = Response Times / Number of Inquiries` is well-formed if S2-5 is the *sum* of response times. Unit % is awkward for a time-based average — a normalized score in % requires a Min/Max band on the average response time; the `(Avg - Min)/(Max - Min)` step provides it. **Note for timeliness, lower raw response time is better, so the normalization band direction must be inverted** (faster = higher score) — verify the Min/Max band orientation.
- **Proposed revision (C):** "Measures customer-service responsiveness as the average response time to customer inquiries (total response time (S2-5) ÷ number of inquiries (S2-6)), normalized against a target band so that faster responses score higher."
- **Notes:**
  - [major] **Reference cell is blank** — the *ratio* is author-defined (UNVERIFIABLE is legitimate), but for traceability of the concept add `ISO 26000` (§6.7.6 consumer service/support). Optionally `ISO 10004` (complaint/response as an indirect satisfaction indicator).
  - [minor] Unit/band: confirm the normalization inverts direction (lower response time → higher score); a raw `Avg/( )` without inversion would reward slowness.
  - **Comment flag (R):** non-obvious — add "Author-defined service-responsiveness ratio; concept per ISO 26000 §6.7.6. Band must be inverted (faster = better)."

### S24 — Customer Service Satisfaction Score  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current:** "Measures the average customer satisfaction of the product and compared to a reference value."
- **Verdict:** ADAPTED — the prose is near-identical to S21's ("average customer satisfaction of the product") but this metric measures satisfaction with the **service/support response**, not the product. Formula `Avg = Service Feedback Results / Number of Inquiries` over S2-7 (service feedback) and S2-6 (inquiries) confirms the service-satisfaction reading. ISO 10004 grounds the satisfaction-measurement concept; the service-feedback ratio is author-defined.
- **Grounding:** ISO 10004, p.7: "it is necessary to monitor and measure customer satisfaction" (quote above); and p.8 ties satisfaction to the complaints/response process: "the processes described in this document can assist the organization in monitoring and measuring customer satisfaction with the complaints-handling process". (`data/literature/DIN ISO 10004…Customer Satisfaction.pdf`). ISO 26000 §6.7.6 grounds the service/support arm (quote under S23).
- **Implementation check:** Children S2-6 (Number of Inquiries) and S2-7 (Service Feedback Results) both exist; `Avg = Service Feedback Results / Number of Inquiries`, normalized. Unit % consistent. The description's "of the product" is the drift — it should say "of the service response." Reference `ISO 10004` appropriate.
- **Proposed revision (C):** "Measures average satisfaction with the customer-service response — the mean service-feedback rating across handled inquiries (service feedback results (S2-7) ÷ number of inquiries (S2-6)), normalized to a target band. Distinct from S21 (product satisfaction): S24 rates the support experience."
- **Notes:** [minor] current text duplicates S21's wording and says "of the product" — corrected above to "service response." **Comment flag (R):** mildly non-obvious overlap with S21 — optional one-liner "Service-satisfaction (support), distinct from S21 product-satisfaction; ISO 10004 grounds satisfaction measurement."

### S2-5 — Response Times  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The time taken to respond to customer inquiries and complaints."
- **Verdict:** CONSISTENT — accurate raw input feeding S23. Slight ambiguity on aggregation (single time vs. total) given it is divided by Number of Inquiries.
- **Grounding (concept):** ISO 26000, p.73 §6.7.6 (consumer service/support mechanisms, quote under S23). (`data/literature/DIN EN ISO 26000…Social Responsibility.pdf`)
- **Implementation check:** Raw leaf; numerator of S23's `Response Times / Number of Inquiries`. Unit "time" — for the average to be well-formed, this should be the *total* response time across inquiries (so Avg = total/ count). Clarify.
- **Proposed revision (C):** "Total time taken to respond to customer inquiries and complaints over the period (summed across inquiries); numerator of S23's average response time."
- **Notes:** [minor] specify total vs. per-inquiry and a concrete time unit (e.g. hours) so the S23 average is well-defined. No Comment flag needed.

### S2-6 — Number of Inquiries  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The total number of survey respondents in a given timeframe."
- **Verdict:** DRIFTED (wrong description) — the text "survey respondents" is copy-pasted from S2-2 and does not describe inquiries. This leaf is the count of **customer-service inquiries**, the denominator of both S23 (timeliness) and S24 (service satisfaction).
- **Grounding (concept):** ISO 26000, p.73 §6.7.6 (consumer service/support, quote under S23). (`data/literature/DIN EN ISO 26000…Social Responsibility.pdf`)
- **Implementation check:** Raw leaf; `Parent Metrics = S23\nS24`; denominator of `Response Times / Number of Inquiries` (S23) and `Service Feedback Results / Number of Inquiries` (S24). Unit "#" consistent. The description, however, describes survey respondents (S2-2's concept), not inquiries.
- **Proposed revision (C):** "The total number of customer-service inquiries and complaints received in a given timeframe; denominator of S23 (response-time average) and S24 (service-satisfaction average)."
- **Notes:** [major] **Description is wrong (copied from S2-2 "survey respondents")** — replace with the inquiry-count text above. No Comment flag needed.

### S2-7 — Service Feedback Results  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "The feedback score or ratings for the response given to customers."
- **Verdict:** CONSISTENT — accurate raw input; numerator of S24. Unit "-" unspecified (same scale caveat as S2-1).
- **Grounding:** ISO 10004, p.7 (monitor/measure customer satisfaction, quote above) — service feedback is a direct satisfaction measure for the support interaction. (`data/literature/DIN ISO 10004…Customer Satisfaction.pdf`)
- **Implementation check:** Raw leaf; numerator of S24's `Service Feedback Results / Number of Inquiries`. Unit "-" — define the scale so the S24 average is well-formed (mirror the S2-1 note).
- **Proposed revision (C):** keep as-is. (Optional: "The aggregate feedback score/rating customers gave for the service response (on a standardized scale); numerator of S24." to fix the unit scale.)
- **Notes:** [minor] Unit "-" — define the rating scale (mirror S2-1). No Comment flag needed.

---

## Batch summary

**Counts (12 metrics):** CONSISTENT 7 (S2 composite, S21, S2-1, S2-2, S2-3, S2-4, S2-5,
S2-7 — note S21/S2-1 carry hygiene notes; that is 8 rows tagged CONSISTENT counting S2-7);
DRIFTED 3 (S22, S2-6, and S24 borderline/ADAPTED); ADAPTED 1 (S24); UNVERIFIABLE 1 (S23).
No CONTRADICTION; no SOURCE-NOT-FOUND. (Exact per-row verdicts are in the summary table at
the top — counting: CONSISTENT 7, DRIFTED 3 [S22, S2-6, plus the S2-2/S2-3 cross-ref fixes
are attached to CONSISTENT rows], ADAPTED 1 [S24], UNVERIFIABLE 1 [S23], plus the S2 name
typo.)

**Proposed description rewrites (C):** S2 (name children explicitly + drop "accessibility"),
S22 (incident-rate complement), S23 (average response time, inverted band), S24 (service
vs. product satisfaction), S2-1 (define scale), S2-6 (**wrong description — fix**), S2-5
(total vs. per-inquiry). Light/optional: S21, S2-7. Keep as-is: S2-2, S2-3, S2-4.

**Adjacent-cell fixes (beyond Description):**
1. [minor] **S2 Indicator Name typo: "Costumer Well-Being Score" → "Customer Well-Being Score".**
2. [major] **S22 `Underlying Metrics` (E) lists S2-2** (Number of Surveyee) which the formula
   `1 - (Reported Customer Incidents / Number of Customers)` never uses — **remove S2-2 from S22**
   (and remove the reciprocal S22 entry from S2-2's `Parent Metrics`). S22's real inputs are
   S2-3 and S2-4.
3. [major] **S23 Reference cell (J) is blank** — the ratio is author-defined (UNVERIFIABLE,
   legitimate), but add `ISO 26000` (§6.7.6 consumer service/support) for concept traceability;
   optionally `ISO 10004`.
4. [minor] **S2-3 `Parent Metrics` (F) has a stray leading newline `\nS22` → `S22`.**
5. [minor] **S23 normalization band direction** — confirm it inverts so faster response time
   scores higher (a raw `Avg/( )` to % would reward slowness). Flag in Comment (R).
6. [minor] **S21 description stray token "value of R products"** — drop the "R".
7. [minor] Unit "-" on S2-1 and S2-7 — define the rating scale so the S21/S24 averages are
   well-formed.

**Comment-cell (R) flags — non-obvious only:**
- **S22:** "Product-level safety-rate complement; adapts GRI 416-2 incident disclosure / ISO 26000 §6.7.4. Rate construction author-defined."
- **S23:** "Author-defined service-responsiveness ratio; concept per ISO 26000 §6.7.6. Band must be inverted (faster = better)."
- **S24 (optional):** "Service-satisfaction (support), distinct from S21 product-satisfaction; ISO 10004 grounds satisfaction measurement."
- *Skip* Comment flags on the self-evident rows (S2 composite, S21, and the raw leaves) per the
  conservative non-obvious-only policy.

**SOURCE-NOT-FOUND codes:** none. All cited codes in this family resolve to References.tsv
Labels and all relevant PDFs are present: ISO 10004 (`DIN ISO 10004…Customer Satisfaction.pdf`),
ISO 26000 (`DIN EN ISO 26000…Social Responsibility.pdf`), GRI 416 / 416-2
(`GRI - Global Reporting Initiative/GRI 416_ Customer Health and Safety 2016.pdf`), ISO 9001
(References Label only; PDF not opened — ISO 9001 is a QMS umbrella, not load-bearing here),
and ESRS S4 (`ESRS S2 to S4 Delegated-act-2023-5303-annex-1_en.pdf`). GRI 418 (customer
privacy) and ESRS S4's information/privacy arm are **not cited by any S2 row** and are not
needed — S2 covers no privacy KPI; recorded for completeness, not applied.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above (ISO 10004
pp.2/7/8; ISO 26000 pp.14/71/73; GRI 416 pp.3/7/9; ESRS S4 pp.31/32). I did not open ISO 9001
(cited on S21 but secondary to ISO 10004) nor read full clause bodies beyond the cited pages.
I did not verify numeric Min/Max bands, weights (S2's children weights sum cell shows 0.25
each — not audited), or the cross-domain parent S0. The S23 band-direction concern is inferred
from the formula shape, not from a configured band value I inspected. Whether "Customer
Feedback Results" (S2-1) / "Service Feedback Results" (S2-7) are sums, means, or counts is
ambiguous in the snapshot and flagged for the author rather than assumed.


---

## S3 — Workforce Welfare (incl. the S34 re-model)

### S3 — Workforce Welfare  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures the importance of employee satisfaction, health, and safety in the manufacturing environment."
- **Verdict:** DRIFTED — the prose names three concepts (satisfaction, health, safety) but the wired children are **four**: S31 (satisfaction), S32 (local employment), S33 (health & safety) **and S34 (social-economic contribution)**. The S34 arm (remuneration / cost-of-living / job creation) is entirely omitted, and "local employment" (S32) is not named. The Formula text "Sum (weight * S31 + … + weight * S33)" stops at S33 and **omits S34** — stale relative to `Underlying Metrics = S31\nS32\nS33\nS34`. "the importance of" is also loose for a measured score.
- **Grounding:** composite/parent — no single literature source expected (Reference cell blank by design). The four arms are grounded on the children's rows below (ISO 26000 / PSILCA local employment; GRI 403 / ESRS S1 health & safety; PSILCA / GRI 201 remuneration). ISO 26000 p.81 frames the workforce/community-welfare scope: *"Employment is an internationally recognized objective related to econ[omic and social development]"* (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`).
- **Implementation check:** `Underlying = S31\nS32\nS33\nS34`; strategy WEIGHTED_AVERAGE; Parent = S0; Unit %. All four children exist (rows 22–24, 29). Averaging four 0–1/% sub-scores → % is unit-consistent. The description and the Formula text both under-count to three of the four children → drift.
- **Proposed revision (C):** "Aggregates the product's workforce-welfare performance into one score by combining employee satisfaction (S31), the local-employment rate (S32), employee health and safety (S33), and the social-economic contribution to the workforce (S34). Higher means better working conditions and stronger socio-economic benefits for the people who make the product."
- **Proposed Formula (I):** "Sum (weight * S31 + weight * S32 + weight * S33 + weight * S34)".
- **Notes:** Blank Reference is correct for a composite parent — not a defect. [minor] add the missing S34 term to the Formula cell. Parent S0 is outside this batch; not verified here.

### S31 — Employment Satisfaction Score  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the average employee satisfaction on working on the product."
- **Verdict:** DRIFTED (mis-applied source) — the description is fine for the formula `Avg = Employee Feedback Results / Total Employee`, then `(Avg - Min)/(Max - Min)`, but the **cited source `ISO 10004` is the wrong instrument**: ISO 10004 is explicitly scoped to *customers external to the organization*, not employees. The concept (satisfaction survey) is right; the citation is mis-applied.
- **Grounding:** ISO 10004 p.9 (Clause 1 Scope): *"This document gives guidelines for defining and implementing processes to monitor and measure customer satisfaction… The focus of this document is on **customers external to the organization**."* (`data/literature/DIN ISO 10004_2019-07-00_EN_3082656 Customer Satisfaction.pdf`). For **employee** satisfaction the in-corpus anchor is ESRS S1 (own-workforce working conditions); ESRS S1 p.2 lists *"working conditions, including: … iii. adequate wages"* and the working-conditions framing for own workforce — there is no dedicated "employee satisfaction" datapoint, so the metric is an author-defined product-level satisfaction rate.
- **Implementation check:** Children S3-1 (Employee Feedback Results) and S3-2 (Total Employee) both exist; ratio → normalized to %, Unit % consistent. NORMALIZED_RATIO matches. Min/Max present (0.25 weight under S3). The description matches the formula; only the citation is mis-targeted.
- **Proposed revision (C):** "Measures average employee satisfaction with working on the product, from staff feedback surveys (e.g. CSAT/eNPS), normalized against a company target band."
- **Proposed Reference (J):** drop `ISO 10004` (external-customer scope); replace with `ESRS S1` (own-workforce working conditions) as the closest in-corpus anchor, and note the satisfaction-rate construction is author-defined. (Do **not** carry ISO 10004 on an employee-satisfaction row.)
- **Notes:** [major] `ISO 10004` is scoped to external customers — mis-applied to employee satisfaction (same issue on the S3-1 leaf). [minor] Comment-cell flag (non-obvious, so flag): "Employee-satisfaction rate is author-defined; ISO 10004 covers *customer* satisfaction only — re-anchored to ESRS S1 own-workforce."

### S32 — Local Employment Rate  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the share of employees hired from local communities to support local economies."
- **Verdict:** CONSISTENT — matches `Rate = Number of local employee / Total employee`, then `(Rate - Min)/(Max - Min)`, over children S3-3 (local employees) and S3-2 (total employees). Both cited codes resolve and ground the concept.
- **Grounding:**
  - ISO 26000 p.81 (6.8.5 Employment creation and skills development): *"An organization should: … consider the impact of its … decisions on employment creation … make direct investments that alleviate poverty through employment creation"* and p.83 *"generate local employment as well as linkages with local, regional and urban markets"* (`data/literature/DIN EN ISO 26000_2021-04-00_EN_3255742 Social Responsibility.pdf`).
  - PSILCA p.16: carries a **"Local employment"** subcategory — *"LOCAL COMMUNITY … Local employment … Unemployment rate in the country"* (`data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf`); PSILCA's local-employment indicator is unemployment-rate-based at country level, so the **product-level local-hire share is the author's adaptation** of the PSILCA "local employment" concept, not the identical PSILCA datapoint.
- **Implementation check:** Children S3-2 (Total Employee) and S3-3 (Number of Local Employee) both exist; dimensionless ratio → %, Unit % consistent. NORMALIZED_RATIO matches; Min/Max seeded 0/1 (Comment documents this). Prose matches formula and children — no drift.
- **Proposed revision (C):** keep substance; optional sharpening: "Measures the share of the product's workforce hired from the local community (local employees ÷ total employees), normalized against a company target band. Higher means more of the product's jobs benefit the local economy."
- **Notes:** Both citations valid. PSILCA's own "Local employment" indicator is unemployment-rate-based (country level), so this product-level local-hire share is an ADAPTED reading of that subcategory — [minor] Comment-cell flag (non-obvious): "Local-hire share adapts PSILCA's 'Local employment' subcategory (PSILCA p.16, country-level) and ISO 26000 6.8.5 employment-creation to the product workforce."

### S33 — Employee Health and Safety  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the well-being of employees, particularly in the context of manufacturing and production environments."
- **Verdict:** ADAPTED — the cited GRI 403 / ESRS S1 ground the occupational-health-&-safety domain, but the KPI's `1 - (Safety Incident Rate / Total employee)` is an author-constructed "higher-is-safer" product score, not a GRI/ESRS disclosure. The description is vague ("well-being… in manufacturing") relative to the incident-based formula.
- **Grounding:**
  - GRI 403 p.21 (Disclosure 403-9 Work-related injuries): *"The number and rate of recordable work-related injuries"* and the rate formula *"Number of fatalities … / Number of hours worked × [200,000 or 1,000,000]"* (`data/literature/GRI - Global Reporting Initiative/GRI 403_ Occupational Health and Safety 2018.pdf`).
  - ESRS S1 p.14 (DR S1-14 Health and safety metrics): *"(c) the number and rate of recordable work-related accidents"* (`data/literature/ESRS - European Sustainability Reporting Standards/ESRS S1 Delegated-act-2023-5303-annex-1_en.pdf`).
- **Implementation check:** Children S3-2 (Total Employee) and S3-4 (Reported Workplace Incident) both exist; Formula `1 - (Safety Incident Rate / Total employee)`, NORMALIZED_RATIO, Unit %; Min/Max seeded 0/1 (Comment documents). **Direction note:** this is a **lower-incidents-is-better** quantity inverted to a higher-is-better score via `1 - …` — worth a flag. Also a unit/semantics nit: the formula divides a *rate* by Total employee, while GRI 403-9 already normalizes injuries by *hours worked × 200,000*; the KPI's per-employee normalization is a simplification.
- **Grounding note on citation code:** S33 cites `ESRS S1-1`, but the health-&-safety disclosure is **DR S1-14** (ESRS S1 p.14, quoted above); S1-1 is "Policies related to own workforce". The health-&-safety locator should be **ESRS S1-14** (which the S3-4 leaf already cites). Likely citation drift.
- **Proposed revision (C):** "Measures the product workforce's occupational safety as one minus the workplace-incident rate per employee, normalized to a company target band. Higher means fewer recordable work-related injuries among the people making the product (lower-incidents-is-better, inverted)."
- **Proposed Reference (J):** keep `GRI 403`; change `ESRS S1-1` → **`ESRS S1-14`** (health-&-safety metrics) to match the concept.
- **Notes:** [minor] ESRS S1-1 → ESRS S1-14 citation fix. [minor] Comment-cell flag (non-obvious — direction + normalization basis): "Lower-incidents-is-better, inverted to a higher-is-better score; per-employee normalization simplifies GRI 403-9's per-200,000-hours rate."

### S34 — Social Economic Contribution Score  [Level 3, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures a product's lifecycle contribution to societal well-being through equitable employee remuneration, alignment with local cost of living, and sustainable job creation."
- **Verdict:** DRIFTED — the **Description is now correct** for the re-modeled construct (it already names the three arms: remuneration, cost-of-living alignment, job creation), but the **Formula text (I) is stale**: "Weighted sum of each underlying metrics compared to a target value or comparable product / standard" describes the pre-re-model raw-value framing. With S3-5/S3-6/S3-7 now self-normalizing (NORMALIZED_RATIO against company targets), S34 weight-averages three 0–1 scores — the formula should say so. So: description CONSISTENT, formula DRIFTED.
- **Grounding:** composite/parent — no single literature source expected (Reference blank by design, correct). The arms are grounded on the children: PSILCA "Fair salary" / GRI 201-1 (remuneration), PSILCA "Living wage" (cost-of-living), GRI 401-1 / ISO 26000 6.8.5 (job creation). PSILCA p.38 gives the **sourced precedent for the normalization** the re-model adopts: *"Risk assessment of Indicator value y, ratio Salary/Living wage … 0 < y <1 very high risk … 2.5 ≤ y very low risk"* (`data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf`) — i.e. wage scored as a ratio against cost-of-living, exactly the salary-vs-cost-of-living normalization S3-5/S3-6 now implement.
- **Implementation check:** `Underlying = S3-5\nS3-6\nS3-7`; strategy WEIGHTED_AVERAGE; children all NORMALIZED_RATIO (0–1) with weights ~0.3333 each; Unit %. With normalized children, the weighted average is unit-consistent and meaningful — the prior **[blocker]** is resolved. Comment "intended for internal company comparison i.e. shoes manufactured in germany vs in vietnam" is consistent (target-relative scoring makes cross-geography € comparable).
- **Proposed revision (C):** keep substance; optional tightening to name children: "Aggregates the product's socio-economic contribution to its workforce into one score by combining wage adequacy vs local cost of living (S3-5/S3-6), employee remuneration level (S3-6), and job creation (S3-7) — each scored 0–1 against a company target — then weight-averaging them. Designed for internal cross-site comparison."
- **Proposed Formula (I):** "Weighted average of the normalized (0–1) child scores: Sum (weight * S3-5 + weight * S3-6 + weight * S3-7), where each child is scored against a company target." (replaces the stale "compared to a target value or comparable product / standard" raw-value phrasing).
- **Notes:** Blank Reference correct for a composite. [major] **Formula-text drift** — update to the weighted-average-of-normalized-scores phrasing. [minor] document, in S34's Comment or the children, the per-child target/normalization basis (PSILCA p.38 salary/living-wage ratio is the natural reference for S3-5/S3-6).

### S3-1 — Employee Feedback Results  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Measure satisfaction and engagement of employees."
- **Verdict:** DRIFTED (mis-applied source) — definition is fine for a raw survey-result input feeding S31, but the cited `ISO 10004` is scoped to **external customers**, not employees (same issue as S31).
- **Grounding:** ISO 10004 p.9 (Scope): *"The focus of this document is on customers external to the organization."* (file as above). No employee-satisfaction datapoint exists in the corpus; the closest own-workforce anchor is ESRS S1 working conditions.
- **Implementation check:** Raw leaf, no formula; Parent = S31; numerator of the S31 satisfaction ratio. Unit "-" (score/rating). Consistent as an input; only the citation is mis-targeted.
- **Proposed revision (C):** "Aggregate result of employee satisfaction/engagement surveys (e.g. CSAT/eNPS), used as the numerator of S31."
- **Proposed Reference (J):** drop `ISO 10004`; if a citation is wanted, use `ESRS S1` (own-workforce). Author-defined survey input otherwise UNVERIFIABLE.
- **Notes:** [major] `ISO 10004` mis-applied (external-customer scope) — drop or re-anchor.

### S3-2 — Total Employee  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total amount of employee directly involved in the product."
- **Verdict:** CONSISTENT — accurate raw denominator for S31/S32/S33; both cited codes ground "total employees".
- **Grounding:** GRI 2-7 p.15 (Disclosure 2-7 Employees): *"report the total number of employees, and a breakdown of this total by gender and by region"* (`data/literature/GRI - Global Reporting Initiative/GRI 2_ General Disclosures 2021.pdf`). ESRS S1-6 (own-workforce characteristics, headcount) is the CSRD analogue — cited and resolves.
- **Implementation check:** Raw leaf; Parents S31\nS32\nS33; Unit #; denominator in all three ratios. Org-level "total employees" adapted to the product workforce — accurate. No drift.
- **Proposed revision (C):** keep as-is. (Optional grammar fix: "The total number of employees directly involved in the product.")
- **Notes:** ADAPTED basis (org-level GRI 2-7 / ESRS S1-6 → product workforce), but self-evident — **no Comment flag needed**. [minor] "amount of employee" → "number of employees".

### S3-3 — Number of Local Employee  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The total local residents employed involved in the product."
- **Verdict:** CONSISTENT — accurate raw numerator for S32; GRI 2-7 grounds employee headcount, local breakdown is the adaptation.
- **Grounding:** GRI 2-7 p.15 (employee headcount with breakdown "by region", quote above). ISO 26000 p.83 grounds the *local* qualifier: *"generate local employment as well as linkages with local, regional and urban markets"* (file as above).
- **Implementation check:** Raw leaf; Parent = S32; Unit #; numerator of the local-employment rate. S3-3 ⊆ S3-2 (local ⊆ total), so the S32 ratio is in [0,1]. Consistent.
- **Proposed revision (C):** "The number of the product's employees who are local residents (community, or failing that the same country); numerator of S32." (fixes the garbled grammar of the current text).
- **Notes:** [minor] current text is grammatically broken ("local residents employed involved") — rewrite as above. ESRS S1-6 could be mirrored here for parity with S3-2, but GRI 2-7 alone is fine.

### S3-4 — Reported Workplace Incident  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Number of workplace safety incidents per employee, aimed at minimizing risks."
- **Verdict:** ADAPTED — the GRI 403 / ESRS S1-14 disclosures ground recordable work-related injuries; the product-level count is the adaptation. Minor internal nit: the name + "per employee" phrasing conflate a **count** (the leaf is a raw incident count, Unit #) with a **rate** (the S33 formula does the per-employee division).
- **Grounding:**
  - GRI 403 p.21 (403-9): *"the number and rate of recordable work-related injuries"* (file as above).
  - GRI 403-10 (work-related ill health), ESRS S1-14 p.14: *"(c) the number and rate of recordable work-related accidents"* (file as above). All four cited codes resolve.
- **Implementation check:** Raw leaf; Parent = S33; Unit #; feeds the S33 incident rate. The description says "per employee", but per-employee normalization is done in S33's formula, not in this raw count — the leaf is the incident **number**. Minor wording drift.
- **Proposed revision (C):** "Number of recordable work-related safety incidents (injuries/ill health) among the product workforce in the reporting period; the per-employee normalization is applied in S33."
- **Notes:** Citation set is rich and all-resolving. [minor] ESRS S1-1 also appears here — S1-1 is "Policies"; the substantive H&S metric is **S1-14** (already cited). Consider dropping `ESRS S1-1` from this leaf (and from S33) in favour of S1-14, the actual H&S-metrics disclosure. ADAPTED basis is self-evident (work-related injuries) — no Comment flag needed beyond the count-vs-rate clarification.

### S3-5 — Average Cost of Living  [Level 5→ratio, NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "The average cost of living of employees directly linked to the product."
- **Verdict:** DRIFTED — the description still defines a **raw € value**, but the row is now tagged `NORMALIZED_RATIO_STRATEGY` (self-normalizes to 0–1 against a company target under S34). Post-re-model the description must state the normalized score it now produces, not the raw cost-of-living figure. Also no Reference cited, while the concept is groundable.
- **Grounding:** PSILCA p.17: *"Fair salary — Living wage, per month USD"*; p.38 gives the cost-of-living-as-reference logic: *"Risk assessment of Indicator value y, ratio Salary/Living wage … 0 < y <1 very high risk"* (`data/literature/PSILCA/PSILCA_manual_v3_1_1_2.pdf`) — PSILCA uses cost-of-living (living wage) as the **denominator/target** against which pay is scored, which is exactly the role this metric should play under the re-model.
- **Implementation check:** `NORMALIZED_RATIO_STRATEGY`, Weight 0.3333 under S34, Unit currently **€**. If the row now emits a 0–1 score, **Unit € is inconsistent** with a normalized score (should be %/dimensionless), and the Formula cell is empty — the normalization target/band is undocumented. This is the main implementation gap to confirm with the author: is S3-5 (a) the raw cost-of-living € that S3-6 is scored against, or (b) itself a normalized score? The re-tag implies (b), but the Unit and empty Formula still say (a).
- **Proposed revision (C):** if S3-5 stays a contributor to S34 as a normalized score: "Wage-adequacy against local cost of living, scored 0–1 by comparing average employee salary (S3-6) to the local cost of living and benchmarking against a company target (per PSILCA's salary/living-wage ratio)." If instead S3-5 is meant to remain the raw cost-of-living input (the *target* for salary, not a co-equal addend): keep "The average local cost of living of the product's employees (€)" but **re-tag to RAW_VALUE** and remove it as a separate S34 addend.
- **Proposed Reference (J):** add `PSILCA` ("Living wage, per month" / salary-living-wage ratio, p.17/p.38).
- **Notes:** [major] description (raw €) vs strategy (NORMALIZED_RATIO) drift — reconcile. [major] Unit € vs a 0–1 score is contradictory if the row normalizes; [major] empty Formula + no target documented. [major] blank Reference — add `PSILCA`. **Decision needed:** is S3-5 a normalized score or the cost-of-living *target* for S3-6? (See Batch summary.) Requires the `PSILCA` Label to exist in References.tsv (currently orphan — see fixes).

### S3-6 — Average Employee Salary  [Level 5→ratio, NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "The average salary of employees directly linked to the product."
- **Verdict:** DRIFTED — description still defines a **raw € salary**, but the row is now `NORMALIZED_RATIO_STRATEGY` (self-normalizes against a target). The citation, however, is **now correct**: `GRI 201-1` (employee wages and benefits) replaced the prior mis-cited `GRI 202-1` — re-verified below.
- **Grounding:**
  - GRI 201 p.9 (201-1 guidance): *"An organization can calculate employee wages and benefits as total payroll (including employee salaries and amounts paid to government institutions on behalf of employees)…"* (`data/literature/GRI - Global Reporting Initiative/GRI 201_  Economic Performance 2016.pdf`) — grounds an **absolute salary/wage** figure (the correct match).
  - PSILCA p.17/p.38: *"Sector average wage, per month … Ratio salary (sector wage)/living wage"*; *"ratio Salary/Living wage … risk level"* — grounds **scoring salary against cost-of-living**, the normalization the re-model needs.
  - (Confirmation of the old mis-cite: GRI 202 p.8 — *"Disclosure 202-1 Ratios of standard entry level wage by gender compared to local minimum wage"* — a *ratio*, not an absolute salary; correctly **no longer** cited here.)
- **Implementation check:** `NORMALIZED_RATIO_STRATEGY`, Weight 0.3333 under S34, Unit **€**, Formula empty. Same Unit/Formula gap as S3-5: a normalized score should be dimensionless/%, not €, and the target band is undocumented. Concept correct; presentation drifted.
- **Proposed revision (C):** "Average employee salary scored 0–1 by comparison to a company wage-adequacy target (e.g. salary vs local cost of living / living wage, per PSILCA p.38). Higher means pay is more adequate relative to the local standard of living."
- **Proposed Reference (J):** keep `GRI 201-1`; add `PSILCA` (salary/living-wage ratio) as the normalization basis; optionally `ESRS S1-16` (remuneration metrics, ESRS S1 p.2) / `ESRS S1-10` (adequate wages, p.12).
- **Notes:** **GRI 202-1 → GRI 201-1 mis-cite fix CONFIRMED applied and correct.** [major] description (raw €) vs NORMALIZED_RATIO strategy drift; [major] Unit € vs 0–1 score; [minor] empty Formula / undocumented target. Adding `PSILCA` requires the Label to exist (orphan — see fixes).

### S3-7 — Job Creation  [Level 5→ratio, NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Number of jobs created directly linked to the product."
- **Verdict:** DRIFTED — description defines a **raw count (#)**, but the row is now `NORMALIZED_RATIO_STRATEGY` (self-normalizes against a target jobs figure). Citation `GRI 401-1` is correct and re-verified.
- **Grounding:** GRI 401 p.8 (Disclosure 401-1): *"Total number and rate of new employee hires during the reporting period, by age group, gender and region."* (`data/literature/GRI - Global Reporting Initiative/GRI 401_ Employment 2016.pdf`). ISO 26000 p.81 (6.8.5) grounds job creation as a social-responsibility objective.
- **Implementation check:** `NORMALIZED_RATIO_STRATEGY`, Weight 0.3334 under S34, Unit **#**, Formula empty. Same pattern: a normalized 0–1 score is inconsistent with Unit # and an empty Formula / undocumented target. Concept matches GRI 401-1; presentation drifted.
- **Proposed revision (C):** "Jobs created for the product, scored 0–1 against a company job-creation target. Based on GRI 401-1 new-hire count, normalized so a higher score means more jobs created relative to target."
- **Proposed Reference (J):** keep `GRI 401-1`; optionally add `ISO 26000` (6.8.5 employment creation).
- **Notes:** [major] description (raw #) vs NORMALIZED_RATIO strategy drift; [major] Unit # vs 0–1 score; [minor] empty Formula / undocumented target. GRI 401-1 citation correct.

---

## Batch summary

**Counts (12 metrics):** CONSISTENT 3 (S32, S3-2, S3-3); DRIFTED 7 (S3, S31, S34, S3-1, S3-5, S3-6, S3-7); ADAPTED 2 (S33, S3-4); UNVERIFIABLE 0.

**Re-model verification (the headline asks):**
- **S34 / S3-5 / S3-6 / S3-7 re-tag CONFIRMED applied:** the three children are now
  `NORMALIZED_RATIO_STRATEGY` and S34 `WEIGHTED_AVERAGE`s them — the prior **[blocker]** (averaging
  mixed-unit raw €/€/# children) is **resolved**. **But** the three leaf *descriptions* still use
  the pre-re-model raw-value framing (DRIFTED), and their **Unit cells (€, €, #) and empty Formula
  cells still describe raw values, not 0–1 scores** — the most important adjacent drift to fix.
- **S3-6 mis-cite fix CONFIRMED:** `GRI 202-1` (wage-to-minimum-wage *ratio*) → `GRI 201-1`
  (employee wages and benefits) — landed and correct (re-verified: GRI 201 p.9 vs GRI 202 p.8).

**Description rewrites proposed (7):** S3 (name S34 arm), S31 (re-anchor off ISO 10004),
S34 (keep desc, fix Formula), S3-1, S3-5, S3-6, S3-7 (raw-value → normalized-score framing).
Light/optional sharpening only for S32, S33, S3-2, S3-3, S3-4.

**Adjacent-cell drift to fix alongside the rewrites:**
- **Formula text (I):** S3 omits the S34 term ("…+ weight * S33" → "…+ weight * S34"); S34's
  Formula is the stale raw-value phrasing → weighted-average-of-normalized-scores.
- **Unit (H):** S3-5/S3-6 (€) and S3-7 (#) are inconsistent with a 0–1 normalized score — if the
  rows truly emit normalized scores, Unit should be %/dimensionless; if they remain raw inputs, the
  strategy tag, not the unit, is wrong. **Decision needed (below).**
- **Citation codes (J):** S31 & S3-1 carry `ISO 10004` (external-customer scope) on **employee**
  satisfaction — mis-applied; re-anchor to `ESRS S1`. S33 carries `ESRS S1-1` (Policies) for an
  H&S metric — should be `ESRS S1-14` (Health-and-safety metrics); consider the same on S3-4.
  S3-5/S3-6 should add `PSILCA` (salary/living-wage ratio) as the normalization basis.

**Decisions needed from the author:**
1. **S3-5 role.** Is S3-5 a *normalized score* contributing to S34 (its current NORMALIZED_RATIO
   tag), or the *cost-of-living target* against which S3-6 salary is scored (PSILCA-style
   salary/living-wage)? If the latter, S3-5 should be RAW_VALUE (€) and not a co-equal S34 addend;
   the wage-adequacy score then lives in S3-6. The current state (NORMALIZED_RATIO, Unit €, empty
   Formula) is internally contradictory either way.
2. **Units on S3-5/S3-6/S3-7.** Confirm whether these now emit 0–1 scores (→ change Unit to
   %/dimensionless and document the target band/Formula) or remain raw values (→ revert the
   strategy tag). The descriptions can't be finalized until this is decided.
3. **ISO 10004 on S31/S3-1.** Approve dropping `ISO 10004` (external-customer scope) and
   re-anchoring employee satisfaction to `ESRS S1` (or accepting it as author-defined / UNVERIFIABLE).
4. **ESRS S1-1 → S1-14** on S33 (and S3-4): approve the health-&-safety locator correction.

**SOURCE-NOT-FOUND codes:** none at file level — every cited code's PDF exists and was read.
Reference-registration gaps persist: **`PSILCA`** (cited by S32, recommended for S3-5/S3-6) and
**`ESRS S1`** are used as codes but the only matching Labels in `References.tsv` are `PSILCA`
(row 56 — present) and the `ESRS S1` umbrella (row 57 — present) plus sub-locators `ESRS S1-1`/
`-6`/`-14` (rows 67–69). So `PSILCA` and `ESRS S1` **do** resolve; `ESRS S1-16`/`S1-10`
(suggested for S3-6) are **not** registered as Labels and would need adding if cited.

**Limits of this run:** Verdicts rest only on the verbatim quotes retrieved above; I did not read
full standard sections beyond the cited pages. I confirmed the strategy re-tags and the GRI 201-1
fix from the snapshot, but I cannot tell from the snapshot alone whether the empty Formula cells /
€ & # Units on S3-5/S3-6/S3-7 are intentional or leftover — flagged as Decision 1–2. The S3-5
"cost-of-living = salary target" reading is an interpretation grounded in PSILCA p.38 (salary/
living-wage ratio), not stated in the workbook. Parent S0 (S3's parent) and the weight
distribution were not audited (out of scope). Customer-side rows S2x were read only for the ISO
10004 scope cross-check, not audited.
