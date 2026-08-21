# EC description audit — refine + ground KPI descriptions

**Scope:** the full **Economic Viability (EC) domain — all 67 KPIs**, audited family by
family (the EC1 monetary subtree, the EC4 Circular Service Viability subtree + its raw cost
leaves, and EC3/EC5/EC0). Goal: reconcile each handmade description with its *current*
implementation (Calculation Strategy, Formula, parent/child relations after the gap-fix
re-model) and ground it in the cited literature where a source applies. Economic KPIs are
largely author-defined financial measures, so UNVERIFIABLE (no citable source) is a common,
legitimate verdict here — not a defect.
**Date:** 2026-06-29.
**Method:** current state from `snapshot/Economic Viability.tsv` (+ `References.tsv`); every
literature claim is a verbatim page-cited quote via `tools/scripts/pdf_search.py`; conservative
stance — intentional adaptations kept faithful + flagged, not rewritten to match a source.
**Verdict legend:** CONSISTENT = text matches current implementation (+ literature where cited);
DRIFTED = text no longer matches the current Formula / Strategy / relations (propose a fix);
ADAPTED = faithful adaptation of a source concept (keep + flag); UNVERIFIABLE = author-defined,
no citable source (legitimate).
Columns on the sheet: C=Description, G=Potential Reference Values, H=Unit, I=Formula,
J=Reference, R=Comment.

---

## EC domain — consolidated summary & decisions

**Verdicts across all 67 EC KPIs:** CONSISTENT 35 · DRIFTED 10 · ADAPTED 8 · UNVERIFIABLE 14.
The gap-fix re-model itself is sound (SUM_AGGREGATE cost totals, FORMULA_VALUE Net Profit,
NORMALIZED_RATIO for ROI/Gross Margin/viability ratios all match the live strategies). The
defects are stale description/Formula text and a few citation problems. Per-family detail and
full per-KPI blocks follow; each family keeps its own batch summary. Nothing applied yet — all
proposals.

### A. Description rewrites — DRIFTED rows (10)

| KPI | Problem | Proposed |
|---|---|---|
| EC0 | stale Formula `…+EC4`; desc names wrong child set | name all 5 children EC1–EC5; extend formula to EC5 |
| EC1 | cost list omits the lifecycle/EOL arms now under EC11 | rewrite to current EC12÷EC11 ROI wording |
| EC111 | omits the EC461 remanufacturing child (prose + Formula) | add it |
| EC112 | lists a "disposal" child that doesn't exist | drop it |
| EC121 | names 3 of 5 children; stale "Transfer Costs" → should be "Logistics Costs" (EC1-9) | fix children + label |
| EC3 | one-liner omits the band-normalization + fulfillment-vs-target intent | rewrite to the normalized share |
| EC4 | names only 3 of 7 pathways; Formula stops at EC45 | name all 7; extend formula |
| EC46 ⚠️ | **copy-paste error**: desc says "refurbishment" + "savings" but row is **Remanufacturing** with a Profit child & `Profits/Costs` | full rewrite to remanufacturing/profits |
| EC47 | desc inverts the live `Non-Virgin/Virgin` direction ("100% virgin → fully viable") | rewrite to match the ratio — **see decision D3** |
| EC4-17 | phrased as an activity, not a € cost, unlike its siblings | rewrite to cost wording |

### B. Adjacent-cell drift — Formula text (apply with the rewrites)

Stale Formula cells whose children changed in the gap-fix: `EC0` (`…+EC4`→EC5), `EC4`
(stops at EC45, omits EC46/EC47), `EC111` (omit→include EC461), `EC121` (3→5 children), and
**`EC461`** whose Formula lists the R5 refurbishment five-line set instead of the six R6
remanufacturing leaves (EC4-25…EC4-30) it actually sums. *(EC1/EC12/EC2 strategies are correct;
no formula change there.)*

### C. Citation issues

- **EC12 Net Profit** — cited `RE+20` does **not** define net profit (it's a standard
  accounting identity, no corpus source) → **decision D1**.
- **EC461 Remanufacturing Costs** — `CM+25` is in References.tsv but its PDF is absent from
  the corpus (SOURCE-NOT-FOUND) → **decision D2**.
- **EC4-24** — cites `SASB RT-IG-440b.1` (Industrial Machinery) while its sibling profit leaves
  use `RT-CP-410a.2` (Containers & Packaging) — likely a mis-coded sub-locator → **decision D4**.

### D. Decisions — RESOLVED 2026-06-29

1. **EC12 — drop `RE+20`. ✓** It doesn't define net profit; removed and EC12 marked
   UNVERIFIABLE (net profit = Revenue − costs is a standard identity).
2. **EC461 — re-cite DIN SPEC 91472. ✓** Replace the missing `CM+25` with DIN SPEC 91472
   (in the corpus, grounds remanufacturing).
3. **EC47 — rewrite the inverted description to match the live `Non-Virgin / Virgin` ratio
   (higher = more circular). ✓** Direction of the Target Min/Max band flagged for
   `reviews/min-max-sourcing.md` follow-up.
4. **EC4-24 — align the SASB citation to the sibling `SASB RT-CP-410a.2`. ✓** (the C&P
   revenue code; the RT-IG Industrial-Machinery code was a mis-locator.)

### E. ADAPTED Comment flags (8 rows, non-obvious only)

The viability sub-scores (EC41–EC46) and the profit leaves (EC4-1, EC4-6, EC4-12), plus EC3
and EC5, are faithful adaptations — keep the description, add a short Comment-cell note where
the adaptation isn't self-evident (e.g. EC5's cross-domain reuse of EN1-4/R2-7; the R-strategy
ratio framing). Skip obvious ones, matching the EN policy.

## EC1 — Monetary subtree (ROI / costs / Net Profit / COGS / Gross Margin)

### Key decisions the user must make
1. **EC12 Net Profit citation (`RE+20`).** RE+20 does **not** define net profit; its
   "Financial results / Cost reduction" indicator is a different concept (see EC12 block).
   Net profit = Revenue − costs is a standard accounting identity with no citable corpus
   source. **Decision:** drop `RE+20` from EC12-J and mark the row UNVERIFIABLE, **or**
   keep `RE+20` only as a loose CE-context pointer with a Comment flag. Recommendation:
   drop it (do not imply a definitional source that isn't there). GRI 201-1 is available
   if the user wants a real anchor for the revenue/operating-cost inputs.
2. **EC1-3 / EC1-4 `GRI 201-1`.** Confirmed groundable (revenues; operating costs are
   named line-items of GRI 201-1, see those blocks). Keep. The same code could optionally
   be added to EC11/EC12/EC121 to anchor the revenue/operating-cost inputs, but this is
   optional — those parents are author-defined aggregates.
3. **EC11/EC121 displayed Formula vs children.** Formula text lists named cost lines that
   do not 1:1 match the wired `Underlying Metrics` IDs (see EC11, EC121 blocks). Decide
   whether to keep the human-readable line names or align them to the child IDs.

---

### EC1 — Return On Investment (ROI)  [Level 2, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the return generated by the product relative to its
  development, production, marketing, and operational costs for a given time frame.
  Evaluates the profitability of a specific product to assess if it's worth the investment.
  Which is then compared to a given reference value."
- **Verdict:** DRIFTED (minor) — substance is right, but the cost list ("development,
  production, marketing, and operational") predates the re-model. ROI is now
  `EC12 / EC11`, where EC11 (Total Investment Cost) explicitly bundles Development,
  Marketing, Operating, **Lifecycle Management (EC111)** and **EOL (EC112)** costs — the
  description omits the lifecycle/EOL arms now wired in. "Production" is not a named child.
- **Grounding:** none required — ROI is a standard financial ratio defined by the author
  from its own children (EC12 numerator, EC11 denominator). No citable corpus source; not
  a defect.
- **Implementation check:** `Underlying Metrics = EC11\nEC12`, strategy
  NORMALIZED_RATIO_STRATEGY, Formula `(Net Profit / Total Investment Cost) * 100`,
  Comment confirms "normalizes against company Target Min/Max" and the
  WEIGHTED_AVERAGE→NORMALIZED_RATIO re-tag (T3.6). Reference cell J is blank — correct for
  an author-defined ratio. `Target Max = 0.2` is seeded (band you score against). Unit `%`.
  Children EC11/EC12 both exist. Consistent with the live model.
- **Proposed revision (C):** "Return generated by the product (Net Profit, EC12) relative
  to the total investment it required over the chosen time frame (Total Investment Cost,
  EC11 — development, marketing, operating, lifecycle-management and end-of-life costs).
  Indicates whether the product investment is worthwhile; the resulting ratio is normalized
  against a company-set target band (Min/Max) to produce the score."
- **Notes:** Parent = EC0 (outside batch). [minor] J blank is correct (author ratio); do
  **not** add a citation. No Comment flag needed beyond the existing T3.6 note.

### EC11 — Total Investment Cost  [Level 3, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current (C):** "Measures the overall costs associated with the product throughout it's
  lifecycle from development to it's end-of-life."
- **Verdict:** CONSISTENT — the description correctly frames a lifecycle-wide cost total,
  matching the SUM_AGGREGATE re-tag and the € unit.
- **Grounding:** none required — author-defined cost aggregate (denominator for ROI). The
  cost inputs (operating costs etc.) trace to GRI 201-1 line items if an anchor is wanted;
  GRI 201-1 p.8: "Economic value distributed: operating costs, employee wages and
  benefits, payments to providers of capital…" (`data/literature/GRI - Global Reporting
  Initiative/GRI 201_  Economic Performance 2016.pdf`).
- **Implementation check:** `Underlying Metrics = EC1-1\nEC1-2\nEC1-3\nEC111\nEC112`
  (Development, Marketing, Operating, Lifecycle Management, EOL — all five exist), strategy
  SUM_AGGREGATE_STRATEGY, unit €, Parent EC1. Comment confirms "€ total investment (incl.
  EC111/EC112)" + T3.6 re-tag. **Formula text drift:** Formula cell (I) reads "Development
  Costs + Marketing Costs + Operating Costs + Lifecycle Management Costs + EOL Costs" — this
  matches the five children by name (good), so no ID mismatch here. Consistent.
- **Proposed revision (C):** "Sum of all product costs across the lifecycle — development
  (EC1-1), marketing (EC1-2), operating (EC1-3), lifecycle-management (EC111) and
  end-of-life (EC112) costs. Serves as the denominator of ROI (EC1)."
- **Notes:** Strengthen the objective/scope wording to name the five children for
  traceability. [minor] Optionally add `GRI 201-1` to J to anchor the operating-cost input,
  but it is an author aggregate — keep J blank is also defensible. No Comment flag needed.

### EC111 — Lifecycle Management Costs  [Level 4, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current (C):** "Costs for repair, repurpose and refurbishment during the product's
  life."
- **Verdict:** DRIFTED (minor) — the description lists three cost lines (repair,
  repurpose, refurbishment) but the wired children are **four** R-strategy cost roots:
  `EC411` (Repair), `EC421` (Refurbishment), `EC431` (Repurpose) **and `EC461`
  (Remanufacturing)**. Remanufacturing is summed in but not named in the prose. The
  Formula cell also omits it.
- **Grounding:** none required — author-defined cost aggregate.
- **Implementation check:** `Underlying Metrics = EC411\nEC421\nEC431\nEC461` (all four
  exist; each is a SUM_AGGREGATE cost root), strategy SUM_AGGREGATE_STRATEGY, unit €,
  Parents EC11 + EC12. Comment confirms "€ total of cost lines" + T3.6 re-tag.
  **Formula text drift:** Formula cell (I) reads "Repair Costs + Refurbishment Costs +
  Repurpose Costs" — omits Remanufacturing Costs (EC461), so it undercounts the wired
  children.
- **Proposed revision (C):** "Total recurring in-life cost of the product's circular
  services — repair (EC411), refurbishment (EC421), repurpose (EC431) and remanufacturing
  (EC461) costs — incurred while the product is in use."
- **Notes:** [minor] **Formula (I) fix:** "Repair Costs + Refurbishment Costs + Repurpose
  Costs + Remanufacturing Costs" to match the four children. No citation needed.

### EC112 — EOL Costs  [Level 4, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current (C):** "Costs for disposal, recycling, or recovery at the end of the product's
  life."
- **Verdict:** DRIFTED (minor) — prose names three cost types (disposal, recycling,
  recovery) but the wired children are only **two**: `EC441` (Recycle Costs) and `EC451`
  (Recovery Costs). "Disposal" has no child metric and is not summed in.
- **Grounding:** none required — author-defined cost aggregate.
- **Implementation check:** `Underlying Metrics = EC441\nEC451` (both exist), strategy
  SUM_AGGREGATE_STRATEGY, unit €, Parents EC112 → EC11 + EC12. Comment confirms "€ total of
  cost lines" + T3.6 re-tag. Formula cell (I) "Recycling Costs + Recovery Costs" matches
  the two children. The description's "disposal" arm is unsupported by any child.
- **Proposed revision (C):** "Total end-of-life cost of the product — recycling (EC441)
  and recovery (EC451) costs incurred at the end of the product's life."
- **Notes:** [minor] Either drop "disposal" from the description (recommended — no child
  metric) or add a disposal-cost child if intended. Formula (I) already matches the two
  children. No citation needed.

### EC12 — Net Profit  [Level 3, raw(formula), FORMULA_VALUE_STRATEGY]
- **Current (C):** "Revenue minus COGS, operating costs, lifecycle management costs, and
  EOL costs."
- **Verdict:** CONSISTENT (description) but **citation DRIFTED** — the description matches
  the live formula exactly, but the cited code `RE+20` does not support "net profit."
- **Grounding:** **Cited `RE+20` does not define net profit.** RE+20's economic-dimension
  indicators are "Financial results", "Taxation/regulatory milestones", "Circular
  investment", "Recovery by-products" (p.6); its "Financial results" indicator is defined
  as cost reduction, not a profit identity — RE+20 p.8: "II)Economic 1)Financial results
  a) Cost reduction … Monetary value from circular business model provided by cost
  reduction from raw materials, energy, etc" (`data/literature/Papers/RE+20-Circular
  economy indicators…pdf`). A targeted search of RE+20 for "net profit / profit / ROI /
  gross margin" returned **no matches**. Net profit = Revenue − costs is a standard
  accounting identity → **UNVERIFIABLE** from the corpus. (The revenue/operating-cost
  *inputs* do trace to GRI 201-1 p.8: "Direct economic value generated: revenues; …
  Economic value distributed: operating costs…" — but that grounds the inputs, not the net
  profit measure.)
- **Implementation check:** `Underlying Metrics = EC1-3\nEC1-4\nEC111\nEC112\nEC121`
  (Operating, Revenue, Lifecycle Mgmt, EOL, COGS — all exist), strategy
  FORMULA_VALUE_STRATEGY, unit €, Parent EC1, Formula `Revenue − (COGS + Operating Costs +
  Lifecycle Management Costs + EOL Costs)`. Comment confirms "a € difference, not a mean"
  + T3.6 re-tag. Description and formula are fully aligned. Only the citation is wrong.
- **Proposed revision (C):** "The product's net financial contribution: revenue (EC1-4)
  minus the cost of goods sold (EC121), operating costs (EC1-3), lifecycle-management costs
  (EC111) and end-of-life costs (EC112). A € amount (not a mean or ratio)."
- **Notes:** **[major] Citation fix (J):** remove `RE+20` (it does not define net profit).
  Mark the measure UNVERIFIABLE (standard accounting identity) — do **not** invent a
  source. Optionally add `GRI 201-1` to anchor the revenue/operating-cost inputs only, with
  a Comment-cell flag: "Net profit is a standard accounting identity (no definitional
  corpus source); GRI 201-1 anchors only the revenue/operating-cost inputs." See decision 1.

### EC121 — Cost of Goods Sold (COGS)  [Level 4, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current (C):** "Measures the total cost of producing a sustainable, circular product,
  including non-/virgin materials, labor, and overhead. Any costs related to the recovery
  or refurbishment of materials for reuse should also be considered"
- **Verdict:** DRIFTED (minor) — description lists "materials, labor, overhead" (+ a
  recovery/refurbishment caveat) but the wired children are **five**: `EC1-5` (Material),
  `EC1-6` (Labor), `EC1-7` (Overhead), `EC1-8` (Packaging), `EC1-9` (Logistic). Packaging
  and logistics are summed in but not named in the prose; and the "recovery/refurbishment of
  materials" caveat has no corresponding COGS child (those costs live under EC111/EC112).
- **Grounding:** none required — author-defined cost aggregate. (The existing R-cell note
  on HGB vs IFRS scoping is a useful caveat, not a citation.)
- **Implementation check:** `Underlying Metrics = EC1-5\nEC1-6\nEC1-7\nEC1-8\nEC1-9` (all
  exist), strategy SUM_AGGREGATE_STRATEGY, unit €, Parents EC2 + EC12, Formula "Material
  Costs + Labor Costs + Overhead Costs + Packaging Costs + Transfer Costs". **Formula text
  drift:** Formula (I) lists "Transfer Costs" but the wired fifth child is `EC1-9`
  **Logistic Costs** (name = "Logistic Costs") — "Transfer Costs" appears to be stale
  naming for the logistics line. SUM_AGGREGATE over five children is consistent; only the
  Formula label and the prose enumeration drift.
- **Proposed revision (C):** "Total cost of producing the product — material (EC1-5),
  labor (EC1-6), overhead (EC1-7), packaging (EC1-8) and logistics (EC1-9) costs. The exact
  cost lines depend on the accounting scheme (e.g. HGB vs IFRS define COGS differently)."
  (Drop the "recovery/refurbishment of materials" sentence — those costs belong to
  EC111/EC112, not COGS, and have no child here.)
- **Notes:** [minor] **Formula (I) fix:** "…+ Packaging Costs + Logistics Costs" (rename
  "Transfer Costs" → "Logistics Costs" to match EC1-9). Keep the HGB/IFRS R-cell note. No
  citation needed.

### EC2 — Gross Margin  [Level 2, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the difference between the revenue generated from selling the
  product and the cost of goods sold (COGS) associated with the product. It is expressed as
  a percentage of revenue and indicates how efficiently a product is being produced and
  sold. Which is then compared to a given reference value."
- **Verdict:** CONSISTENT — description matches the live formula `(Revenue − COGS) /
  Revenue` and the NORMALIZED_RATIO re-tag; "expressed as a percentage of revenue" is
  exactly the ratio.
- **Grounding:** none required — gross margin is a standard financial ratio defined by the
  author from its children (EC1-4 Revenue, EC121 COGS). No citable corpus source; not a
  defect (UNVERIFIABLE).
- **Implementation check:** `Underlying Metrics = EC1-4\nEC121` (Revenue, COGS — both
  exist), strategy NORMALIZED_RATIO_STRATEGY, unit %, Parent EC0, Formula `(Revenue − COGS)
  / Revenue`. Comment confirms the WEIGHTED_AVERAGE→NORMALIZED_RATIO re-tag (T3.6) and that
  Min/Max are seeded 0/1 ("this ratio is already a 0-1 score"). The first Comment fragment
  ("Already included in Net Profit, but is separated to … production efficiency") justifies
  the separation from EC12 — consistent. J blank is correct.
- **Proposed revision (C):** "Share of revenue (EC1-4) left after the cost of goods sold
  (EC121): (Revenue − COGS) / Revenue. Expressed as a percentage of revenue, it shows how
  efficiently the product is produced and sold; the ratio is normalized against a
  company-set target band (Min/Max) to produce the score."
- **Notes:** [minor] J blank is correct (author ratio) — do not add a citation. Existing
  Comment fragments (separation rationale + Min/Max seeding note) are accurate; keep. No new
  Comment flag needed.

### EC1-1 — Development Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Expenses related to designing a circular product, which may include
  sustainable materials and eco-design principles."
- **Verdict:** CONSISTENT — raw € input leaf; description is clear and unit-compatible.
- **Grounding:** none required — raw cost input, author-defined.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC11, Formula None, J blank,
  Data? = x. Consistent with a leaf cost input.
- **Proposed revision (C):** keep as-is (clear). Optional tightening: "One-time costs of
  designing the product (e.g. eco-design, sustainable-material selection)."
- **Notes:** Leaf cost input — no citation expected. No issues.

### EC1-2 — Marketing Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Costs for promotional activities and campaigns to launch and promote
  the product."
- **Verdict:** CONSISTENT — raw € input leaf; description clear, unit-compatible.
- **Grounding:** none required — raw cost input.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC11, Formula None, J blank,
  Data? = x. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** Leaf cost input — no citation expected. No issues.

### EC1-3 — Operating Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Ongoing expenses related to manufacturing, distribution, and support."
- **Verdict:** CONSISTENT — raw € input leaf, and the cited `GRI 201-1` genuinely names
  "operating costs" as a reported line item.
- **Grounding:** GRI 201-1 p.8: "Economic value distributed: operating costs, employee
  wages and benefits, payments to providers of capital, payments to government by country,
  and community investments" (`data/literature/GRI - Global Reporting Initiative/GRI 201_
  Economic Performance 2016.pdf`). Operating costs is a named GRI 201-1 component → the
  citation is supported.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parents EC11 + EC12, J = `GRI
  201-1` (resolves to References row "GRI 201: Economic Performance 2016"). Consistent.
- **Proposed revision (C):** keep as-is. Optional: "Ongoing expenses to manufacture,
  distribute and support the product (operating costs in the GRI 201-1 sense)."
- **Notes:** Citation supported (keep `GRI 201-1`). No issues.

### EC1-4 — Revenue  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total sales revenue generated from the product also including all
  circular efforts such as revenue from refurbished products."
- **Verdict:** CONSISTENT — raw € input leaf; cited `GRI 201-1` names "revenues" as the
  direct-economic-value-generated component.
- **Grounding:** GRI 201-1 p.8: "Direct economic value generated: revenues" (`data/
  literature/GRI - Global Reporting Initiative/GRI 201_  Economic Performance 2016.pdf`).
  Citation supported. (The "including refurbished-product revenue" extension is an author
  product-level addition layered on top of the GRI revenue concept — minor, self-evident.)
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parents EC12 + EC2 + EC3, J = `GRI
  201-1`. Feeds EC12 (Net Profit), EC2 (Gross Margin) and EC3 (Market Share) — consistent
  with all three formulas. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** Citation supported (keep `GRI 201-1`). No issues.

### EC1-5 — Material Costs  [Level 5, aggregate, SUM_AGGREGATE_STRATEGY]
- **Current (C):** "Costs related to the material and its sourcing needed to manufacture
  the product."
- **Verdict:** CONSISTENT — but note this row is **not a pure leaf**: it has children
  `EC4-31` (Virgin) + `EC4-32` (Non-Virgin) and a SUM_AGGREGATE strategy + Formula "Virgin
  + Non-Virgin Material Costs". Description is consistent with summing the two material
  sub-costs.
- **Grounding:** none required — author-defined cost aggregate.
- **Implementation check:** `Underlying Metrics = EC4-31\nEC4-32` (both exist), strategy
  SUM_AGGREGATE_STRATEGY, unit €, Parent EC121, Formula "Virgin + Non-Virgin Material
  Costs". Note: `Data? = ""` (blank) here whereas the other EC1-x leaves are `x` — this row
  is an aggregate, so blank Data? is consistent with being computed, not entered. Consistent.
- **Proposed revision (C):** "Total material cost to manufacture the product, summing
  virgin (EC4-31) and non-virgin/secondary (EC4-32) material costs."
- **Notes:** [minor] This row is a sum-of-two, not a raw leaf — the proposed wording names
  its two children for traceability. No citation needed.

### EC1-6 — Labor Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Costs related to the labor directly involved in the production of the
  product."
- **Verdict:** CONSISTENT — raw € input leaf; clear, unit-compatible.
- **Grounding:** none required — raw cost input.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC121, Formula None, J
  blank, Data? = x. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** Leaf cost input — no citation expected. No issues.

### EC1-7 — Overhead Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Indirect costs related to the production e.g. rent, utilities,
  deprecation, tools, etc."
- **Verdict:** CONSISTENT — raw € input leaf; clear.
- **Grounding:** none required — raw cost input.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC121, Formula None, J
  blank, Data? = x. Consistent.
- **Proposed revision (C):** keep; fix the typo "deprecation" → "depreciation".
- **Notes:** [minor] Typo "deprecation" → "depreciation". No citation expected.

### EC1-8 — Packaging Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Costs related to the production of packaging needed for the product."
- **Verdict:** CONSISTENT — raw € input leaf; clear, unit-compatible.
- **Grounding:** none required — raw cost input.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC121, Formula None, J
  blank, Data? = x. Consistent.
- **Proposed revision (C):** keep as-is.
- **Notes:** Leaf cost input — no citation expected. No issues.

### EC1-9 — Logistic Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Costs related to the logistics of materials, products, etc. throughout
  the product's lifecycle."
- **Verdict:** CONSISTENT — raw € input leaf; clear, unit-compatible.
- **Grounding:** none required — raw cost input.
- **Implementation check:** RAW_VALUE_STRATEGY, unit €, Parent EC121, Formula None, J
  blank, Data? = x. **Naming consistency:** Indicator Name is "Logistic Costs"; its parent
  EC121's Formula text calls this line "Transfer Costs" — see EC121 Formula-fix note. The
  leaf itself is consistent.
- **Proposed revision (C):** keep as-is (optionally "Logistics Costs" to match plural usage
  elsewhere).
- **Notes:** [minor] Drives the EC121 "Transfer Costs" Formula-label fix (align to
  "Logistics Costs"). No citation expected.

---

## Batch summary

**Verdict counts (16 rows):**
- CONSISTENT 9 — EC11, EC2, EC1-2, EC1-3, EC1-4, EC1-6, EC1-7, EC1-8, EC1-9
  (EC12's description is also consistent, but its *citation* is flagged → counted under
  DRIFTED below).
- DRIFTED 3 — EC1 (cost list omits lifecycle/EOL arms), EC111 (omits remanufacturing
  child), EC112 (lists "disposal" with no child), EC121 (lists 3 of 5 children + stale
  "Transfer Costs" / off-scope recovery caveat), EC1-5 (aggregate, name only).
  *(Note: counting EC12's citation drift makes the "rows needing an edit" total higher than
  3; see the consolidated fix list.)*
- ADAPTED 0.
- UNVERIFIABLE 4 — EC1 (ROI), EC2 (Gross Margin), EC12 (Net Profit), and the EC11/EC121
  cost aggregates as accounting constructs (standard financial measures; no citable corpus
  source — legitimate, no defect).

**Adjacent-cell fixes proposed (Formula I / Citation J):**
- **[major]** EC12-J: remove `RE+20` — it does not define net profit (RE+20 p.8 defines
  "Financial results = cost reduction", a different concept). Mark UNVERIFIABLE or anchor
  inputs to `GRI 201-1` with a Comment flag. **Needs user decision (decision 1).**
- **[minor]** EC111-I: add "+ Remanufacturing Costs" (EC461 is a wired child but missing
  from the formula text).
- **[minor]** EC121-I: rename "Transfer Costs" → "Logistics Costs" (EC1-9) to match the
  wired child; description should name all five children.
- **[minor]** EC112: drop "disposal" from the description (no child metric) or add a
  disposal-cost child.
- **[minor]** EC1-7: typo "deprecation" → "depreciation".

**Decisions the user must make:**
1. EC12 `RE+20` citation — drop (recommended) vs keep as loose CE pointer with Comment
   flag. (See "Key decisions" 1.)
2. Whether to add `GRI 201-1` as an input-anchor on EC11/EC12/EC121 (optional) or leave J
   blank on these author-defined aggregates.
3. EC11/EC121 Formula text — keep human-readable cost-line names (recommended, after the
   EC111/EC121 fixes) vs align them to child IDs.
4. EC112 "disposal" — remove from description vs add a disposal-cost child metric.

**Comment-cell flags proposed (non-obvious adaptations only):**
- EC12: "Net profit is a standard accounting identity — no definitional corpus source; any
  cited code anchors only the revenue/cost inputs." (only if a citation is retained)
- None of the EC1 ROI / EC2 Gross Margin ratios need a Comment flag — they are self-evident
  standard financial ratios; their existing T3.6 re-tag notes are sufficient.

**SOURCE-NOT-FOUND codes:** none in this subtree. `GRI 201-1` resolves
(`data/literature/GRI - Global Reporting Initiative/GRI 201_  Economic Performance
2016.pdf`); `RE+20` resolves (`data/literature/Papers/RE+20-…pdf`) but does **not** support
the EC12 measure attached to it.

**Limits of this run:** Verdicts on EC1 (ROI) and EC2 (Gross Margin) treat them as
author-defined financial ratios — I did not search beyond GRI 201 and RE+20 for a
definitional source for ROI/gross margin/net profit, because these are standard accounting
identities and the task explicitly says not to force literature onto author-defined
financial ratios (UNVERIFIABLE is legitimate). Parent EC0 and siblings EC3/EC4/EC5 are
outside scope and were not audited. Whether `Data?` blanks on aggregate rows are intended
was inferred from strategy, not confirmed with the author.


---

## EC3 / EC5 / EC0 — Market Share, CO2 Cost Performance, Domain Root

### EC0 — Economic Viability Score  [Level 1, domain root / composite, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures how viable the product in the market and how it performs
  economically. Consists of indicators concerning the product's financial and market status."
- **Verdict:** DRIFTED — only on the **Formula text (I)**, and lightly on the description's
  child enumeration. The composite itself is internally consistent, but the displayed Formula
  `Sum (weight * EC1 + ... + weight * EC4)` stops at EC4 and **omits EC5**, while
  `Underlying Metrics = EC1\nEC2\nEC3\nEC4\nEC5` (five children) and strategy is
  WEIGHTED_AVERAGE. This is the same stale-formula drift flagged for EN0 in
  `reviews/EN-descriptions.md` (§B): a child was added in the gap-fix pass (EC5 CO2 Cost
  Performance) but the Formula cell text was not updated.
- **Grounding:** composite/domain-root — **no single literature source is expected**, and the
  Reference cell (J) is blank **by design** (correct, per the composite-root convention used
  for EN0/EC4). Internal check only: judge CONSISTENT/UNVERIFIABLE from the weighting, not a
  source.
- **Implementation check:** `Underlying Metrics = EC1\nEC2\nEC3\nEC4\nEC5`; each of EC1–EC5
  carries `Parent Metrics = EC0` (verified in the TSV: EC1 row 3, EC2 row 4, EC3 row 19, EC4
  row 21, EC5 row 67). Strategy WEIGHTED_AVERAGE, Unit %. All five children exist and each is
  itself a %-valued level-2 score, so a weighted mean into a single % is unit-compatible. The
  description ("financial and market status") fairly summarises the children — EC1 ROI, EC2
  Gross Margin and EC5 CO2-cost are financial; EC3 Market Share is market; EC4 Circular Service
  Viability is circular-economics — so the prose is *accurate but undercounts*: it names
  "financial and market" but does not signal the **circular-service** (EC4) or **carbon-cost**
  (EC5) arms. The only hard defect is the Formula text omitting EC5.
- **Proposed revision (C):** "Aggregates the product's economic performance into a single
  weighted score from its five level-2 indicators: Return on Investment (EC1), Gross Margin
  (EC2), Market Share Fulfillment (EC3), Circular Service Viability (EC4) and CO2 Cost
  Performance (EC5). Provides one figure for how financially and commercially viable the
  product and its circular services are."
- **Proposed Formula-text fix (I):** `Sum (weight * EC1 + ... + weight * EC5)` (extend the
  "..." terminus from EC4 to EC5 so it covers all five wired children — mirror the EN0 fix).
- **Notes:**
  - [minor] Formula text (I) stops at EC4 but the metric has five children including EC5 —
    stale-formula drift, parallel to EN0. Fix the terminus to EC5.
  - Blank Reference (J) is correct for a composite domain root — **not a defect** (matches the
    EN0 / EC4 convention).
  - Verdict on substance: the weighting matches the children → **CONSISTENT as a composite**;
    DRIFTED tag is carried only because the Formula text is demonstrably stale. No source to
    contradict; no UNVERIFIABLE concern.

### EC3 — Market Share Fulfillment  [Level 2, aggregate (ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the product market share."
- **Verdict:** DRIFTED (mild) — the one-line description is *too thin* to match the current
  two-step Formula and misses the **fulfillment / vs-target** framing that the indicator name
  and the Objective cell both carry. The Formula (I) is
  `Share = Revenue / Total Market Revenue` then `(Share - Min) / (Max - Min)` — i.e. it first
  computes a raw market share and then **scores that share against a target band**, which is
  the "Fulfillment" the name refers to. The description states only the first half ("market
  share") and omits that the output is a band-normalized performance score, not the raw share.
- **Grounding (ADAPTED — concept is real, computation is author-defined):**
  - RE+20 p.8 (Table 7, II) Economic → 1) Financial results → b) Revenue generation, Measure
    column): "a) Competitive advantage: percentage of market share of the circular business
    model compared with the competitors."
    (`data/literature/Papers/RE+20-Circular economy indicators for organizations considering sustainability and business models Plastic, textile and electro-electronic cases.pdf`)
    — grounds the **concept** of market share as a circular-economy economic indicator
    benchmarked against competitors. RE+20 does **not** prescribe the
    `Revenue / Total Market Revenue` ratio or the `(Share - Min)/(Max - Min)` band-scoring;
    that two-step construction is the author's.
- **Implementation check:** `Underlying Metrics = EC1-4\nEC3-1`; both children exist — EC1-4
  Revenue (row 10, €) is the numerator and EC3-1 Total Market Revenue (row 20, €) is the
  denominator, so `Share = Revenue / Total Market Revenue` is well-formed and dimensionless.
  Strategy NORMALIZED_RATIO matches the second step `(Share - Min)/(Max - Min)`. Unit % is
  consistent with a normalized score. Min/Max seeded to default 0/1 (Comment R documents this;
  G = "Target Value: min, max\nIndustry Average"). The Reference (J) `RE+20` resolves
  (References.tsv line 29) and grounds the market-share concept — appropriate.
- **Proposed revision (C):** "Measures the product's market share — its revenue (EC1-4) as a
  fraction of the total market revenue for comparable products (EC3-1) — and scores that share
  against a company-set target band. Higher means the product captures more of its market
  relative to the target."
- **Notes:**
  - [minor] Description is a single clause that omits the band-normalization step and the
    "fulfillment vs. target" intent that the name and Objective carry — proposed revision
    restores both without changing the formula.
  - Grounding is ADAPTED: RE+20 supports market share as a CE economic indicator; the
    revenue/total-market ratio and the target-band scoring are author-defined. Keep `RE+20`.
  - Comment-cell flag (R, non-obvious adaptation — worth a note): "Market-share *concept* per
    RE+20 (competitive-advantage indicator); the Revenue/Total-Market ratio and target-band
    scoring are author-defined." (The existing R note about Min/Max seeding stays.)

### EC3-1 — Total Market Revenue  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "Total sales revenue generated from competitors or similar products in the
  market."
- **Verdict:** CONSISTENT — accurate raw-input definition; it is exactly the denominator the
  EC3 `Share = Revenue / Total Market Revenue` formula consumes.
- **Grounding:** no source expected for a supplied raw market figure; the *concept* of a
  total-market / competitor revenue baseline is implied by RE+20's "market share … compared
  with the competitors" (p.8 quote above), but the figure itself is an author/company input.
- **Implementation check:** raw leaf, no formula (I = None), `Underlying = None`,
  `Parent = EC3`; Unit € is consistent with EC1-4 Revenue (€) for the EC3 ratio to be
  dimensionless. Data? = x (supplied). Stages = All. No drift.
- **Proposed revision (C):** keep as-is.
- **Notes:** Reference (J) blank is appropriate for an externally-supplied market figure — not
  a defect. (Optional R note: "Company-supplied market-size input; denominator of EC3.")

### EC5 — CO2 Cost Performance  [Level 2, aggregate (ratio), CROSS-DOMAIN, NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Measures the carbon cost performance per unit of product by combining the
  total CO2 cost with the product carbon footprint."
- **Verdict:** UNVERIFIABLE — the construction is author-defined (no citable source in the
  corpus prescribes a "CO2 cost per produced unit, scored against a band" metric), and the
  description is *broadly* right but does not yet name the cross-domain inputs or the per-unit
  denominator precisely. The Formula (I) is
  `Cost = Cost of CO2 x (Absolute PCF / Produced Units)` then
  `Performance = (Cost - Min) / (Max - Min)` — i.e. CO2 price × per-unit carbon footprint,
  then band-scored. The description says "total CO2 cost … per unit" but the formula does not
  compute a *total* CO2 cost; it computes a **per-unit** CO2 cost (PCF divided by produced
  units, times the CO2 price). Minor wording mismatch ("total") + missing the explicit
  per-unit / cross-domain wiring.
- **Grounding:** **CROSS-DOMAIN, author-defined — no single source.** The constituent concepts
  are grounded elsewhere in the model, not on this row:
  - The product carbon footprint input (EN1-4 Absolute PCF) is grounded in the EN domain
    (ISO 14067 / ESRS E1-6 / EN 15804; see `reviews/EN-descriptions.md` EN1-4). Not re-quoted
    here — that is the cross-domain parent edge, not an error.
  - The produced-units input (R2-7 Total produced units) is grounded in the Resource Efficiency
    domain (`snapshot/Resource Efficiency.tsv` row 31). Cross-domain edge, intentional.
  - The CO2 price (EC5-1, nEHS) is an external regulatory price — no corpus source.
  No retrieved literature prescribes the `price × (PCF / units)` per-unit-cost construction;
  it is the author's. → UNVERIFIABLE is the correct status (legitimate for an author-defined
  composite), **not** a defect.
- **Implementation check:** `Underlying Metrics = EC5-1\nR2-7\nEN1-4`; `Parent Metrics = EC0`.
  All three children exist and the cross-domain ones are confirmed: **EN1-4** (Absolute PCF,
  Environmental Impact domain, kg CO2 eq.) and **R2-7** (Total produced units, Resource
  Efficiency domain) — these are **intentional shared/cross-domain edges**, not broken
  references. EC5-1 (Cost of CO2, € / kgCO2eq) is the EC-domain leaf. Dimensional check of
  the Formula: `(€/kgCO2eq) × (kgCO2eq / units) = € / unit` → a per-unit CO2 cost, then
  band-normalized to a % performance score — units are coherent. Strategy NORMALIZED_RATIO
  matches the `(Cost - Min)/(Max - Min)` step. Unit % consistent. Reference (J) blank is
  acceptable for an author-defined cross-domain composite.
- **Proposed revision (C):** "Measures the product's carbon cost per produced unit by applying
  the CO2 price (EC5-1) to the product's per-unit carbon footprint — the absolute product
  carbon footprint (EN1-4) divided by the total produced units (R2-7) — and scoring the result
  against a company-set cost band. Higher performance means a lower CO2 cost per unit. (Draws
  on the environmental PCF, EN1-4, and produced-units, R2-7, by design.)"
- **Proposed Formula-text note:** the Formula itself is fine; only the description's word
  "total" was inaccurate (the formula is per-unit). No change to I.
- **Notes:**
  - [minor] Description says "total CO2 cost … per unit"; the formula computes a **per-unit**
    cost (`PCF / Produced Units` × price), not a total — proposed revision corrects this and
    names EC5-1 / EN1-4 / R2-7 explicitly.
  - **Cross-domain reuse is intentional** — EN1-4 and R2-7 are shared edges from the
    Environmental Impact and Resource Efficiency domains; do **not** treat them as dangling/
    wrong references. Worth a brief Comment flag because it is non-obvious.
  - Comment-cell flag (R, recommended — non-obvious): "CROSS-DOMAIN: reuses EN1-4 (product
    carbon footprint, EN domain) and R2-7 (produced units, Resource Efficiency domain) as
    shared inputs by design. Per-unit CO2-cost construction is author-defined (UNVERIFIABLE);
    CO2 price is the external nEHS price (EC5-1)."
  - Reference (J) blank is acceptable here (author-defined composite); if a CSRD/PCF anchor is
    wanted for the carbon side, the EN1-4 chain already cites ISO 14067 / ESRS E1-6 — no need
    to duplicate on EC5.

### EC5-1 — Cost of CO2  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current (C):** "The monetary cost applied to greenhouse gas emissions, based on CO2
  pricing by the nEHS."
- **Verdict:** CONSISTENT — accurate raw-input definition; it is the CO2 price the EC5 formula
  multiplies by the per-unit PCF.
- **Grounding:** the nEHS (national Emissions Trading System / *nationales Emissionshandels-
  system*) CO2 price is an **external regulatory price**, not a corpus source — none expected.
  No literature claim is made; nothing to quote. (Data Source cell already records "nEHS".)
- **Implementation check:** raw leaf, no formula (I = None), `Underlying = None`,
  `Parent = EC5`; Unit `€ / kgCO2eq` is exactly the price factor the EC5 formula needs to turn
  per-unit kgCO2eq into € — dimensionally correct. Data? = x (supplied), Data Source = nEHS,
  Stages = All. No drift.
- **Proposed revision (C):** keep as-is. (Optional clarification only, if "nEHS" should be
  spelled out for non-DE readers: "The monetary price applied per kilogram of CO2-equivalent
  emissions, taken from the German national emissions-trading scheme (nEHS) carbon price.")
- **Notes:** Reference (J) blank is appropriate for an external regulatory price input — not a
  defect. nEHS is a Data Source, not a bibliography Label; no References.tsv row is needed.

---

## Inconsistencies & fixes

| # | Severity | Where (col) | Inconsistency | Fix |
|---|----------|-------------|---------------|-----|
| 1 | minor | EC0 / Formula (I) | Formula text `Sum (weight * EC1 + ... + weight * EC4)` stops at EC4 but the metric has five wired children EC1–EC5 (EC5 added in gap-fix; same drift as EN0) | Change terminus to `... + weight * EC5` |
| 2 | minor | EC0 / Description (C) | Description names "financial and market status" but undercounts the circular-service (EC4) and carbon-cost (EC5) arms | Apply proposed revision naming all five children |
| 3 | minor | EC3 / Description (C) | One-line "Measures the product market share" omits the band-normalization step and the fulfillment-vs-target intent the formula + name carry | Apply proposed revision (share = Revenue/Total Market Revenue, scored vs. target band) |
| 4 | minor | EC3 / Comment (R) | Market-share *concept* is from RE+20 but the Revenue/Total-Market ratio + target-band scoring are author-defined — non-obvious adaptation, currently unflagged | Add Comment flag (text in EC3 Notes); keep `RE+20` in J |
| 5 | minor | EC5 / Description (C) | Says "total CO2 cost … per unit" but the formula computes a **per-unit** cost (`price × PCF/units`), and does not name the cross-domain inputs | Apply proposed revision (per-unit, names EC5-1/EN1-4/R2-7) |
| 6 | minor | EC5 / Comment (R) | Cross-domain reuse of EN1-4 (EN domain) and R2-7 (Resource Efficiency) is intentional but non-obvious and unflagged | Add Comment flag documenting the cross-domain edges + author-defined construction |

No [blocker] or [major] findings in this batch: all child/cross-domain references resolve,
all units are coherent, and the two raw leaves (EC3-1, EC5-1) are correct as-is. The two
DRIFTED items (EC0, EC3) are description/formula-text wording, not contradictions.

**SOURCE-NOT-FOUND codes:** none cited that fail to resolve. `RE+20` (EC3) resolves to
References.tsv line 29 and the PDF is present and was read. `nEHS` (EC5-1) is a Data-Source
label (external regulatory carbon price), not a bibliography code — no References row expected
or missing.

**Cross-domain note:** EC5's children EN1-4 (Absolute PCF, Environmental Impact) and R2-7
(Total produced units, Resource Efficiency) were both confirmed present in their home sheets
and are **intentional shared edges** — reported as design, not as broken references.

**Limits of this run:** (1) EC0 and EC5 carry no single citable source (composite root /
author-defined cross-domain construction); their verdicts rest on the internal weighting and
formula/relations check, not on literature. (2) Grounding for EC3 rests only on the single
RE+20 Table-7 quote retrieved (p.8); I did not read the rest of RE+20's economic indicator
section. (3) The cross-domain grounding of EN1-4 and R2-7 was confirmed by existence in their
home sheets only — their own description audits live in `reviews/EN-descriptions.md` (EN1-4)
and the Resource Efficiency review (R2-7); not re-verified against literature here. (4) Weights,
Min/Max target bands, and numeric example values were not audited (out of scope). (5) The
nEHS carbon price (EC5-1) is an external regulatory figure not in the corpus and was not
independently verified.


---

## EC4 — Circular Service Viability: sub-scores + cost roll-ups

### EC4 — Circular Service Viability  [Level 2, aggregate, WEIGHTED_AVERAGE_STRATEGY]
- **Current (C):** "Measures how viable current circular efforts are. It consists of
  R-strategies processes such as repair, refurbishment, and repurpose and compares its
  profit & costs. It also contains the direct comparison of the circular materials used in
  the product."
- **Verdict:** DRIFTED — the description names only three pathways ("repair, refurbishment,
  and repurpose") but the row now wires **seven** children: EC41 Repair, EC42 Refurbishment,
  EC43 Repurpose, EC44 Recycling, EC45 Recovery, EC46 Remanufacturing, EC47 Circular
  Material Viability. Recycling, recovery and remanufacturing are omitted. The displayed
  Formula (I) "Sum (weight * EC41 + ... + weight * EC45)" stops at EC45 and omits EC46/EC47.
- **Grounding:** Composite/parent — no single literature source expected; the R-strategy set
  it aggregates is grounded by FAC+21 p.2 (R4–R9, quoted above). Internal check: all seven
  children exist in the sheet; unit % and WEIGHTED_AVERAGE are consistent with averaging
  seven 0–1 sub-scores.
- **Implementation check:** `Underlying Metrics = EC41…EC47` (7), strategy WEIGHTED_AVERAGE,
  unit %. Each child is itself a normalized 0–1 ratio, so a weighted average is coherent. The
  Formula text and the prose both under-count the children (classic gap-fix drift after EC44/
  EC45/EC46/EC47 were added).
- **Proposed revision (C):** "Aggregates the economic viability of the product's circular
  service pathways into one score. Combines the per-pathway cost-vs-profit (or cost-vs-
  savings) sub-scores for repair (EC41), refurbishment (EC42), repurpose (EC43), recycling
  (EC44), recovery (EC45) and remanufacturing (EC46), together with the circular-material
  cost comparison (EC47), to prioritise which circular efforts are worth scaling."
- **Notes:** [minor] Formula (I) "EC41 + ... + EC45" should read "weight * EC41 + … + weight
  * EC47" to match the seven children. [minor] G holds "Target Value: min, max" although the
  parent is a weighted average of already-normalized children, not itself a min/max-banded
  ratio — confirm whether the band applies at this level or only at the EC4x children.
  Composite — Reference (J) blank is by design.

### EC41 — Repair Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and profits connected to repairing to highlight its
  economic viability."
- **Verdict:** ADAPTED — matches the formula `Ratio = Profits / Costs` then `(Ratio - Min)/
  (Max - Min)`; the repair concept is grounded, the cost/profit ratio framing is the author's
  product-level construction.
- **Grounding:** DIN SPEC 91472 p.8 (3.9, repair definition, quoted above); R4 = repair in
  FAC+21 p.2. Neither source prescribes a profit/cost viability ratio — that is author-defined.
- **Implementation check:** Children EC4-1 (Repair Profits) + EC411 (Repair Costs) both
  exist; Formula `Profits / Costs` normalized; unit cell is blank (peers EC42–EC47 carry "%").
  Description is consistent with the formula.
- **Proposed revision (C):** "Scores the economic viability of the repair (R4) service by
  comparing repair profits (EC4-1) against repair costs (EC411): higher when repair revenue
  outweighs its cost. Indicates whether offering repair is profitable and scalable."
- **Notes:** [minor] Unit (H) is blank — set to "%" to match EC42–EC47 (all NORMALIZED_RATIO
  sub-scores). ADAPTED flag for Comment (R) is **non-obvious** (the profit/cost ratio is an
  author construction, not in DIN SPEC): add e.g. "Cost/profit viability ratio is
  author-defined; repair concept per DIN SPEC 91472 (3.9) / R4."

### EC411 — Repair Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with repairing a sustainable product,
  including labor, parts, and any additional resources required to restore the product to
  working condition."
- **Verdict:** CONSISTENT — description ("total expenses … including …") matches a
  SUM_AGGREGATE of its € leaves; gap-fix re-tag to SUM_AGGREGATE confirmed.
- **Grounding:** UNVERIFIABLE by design — plain € cost roll-up, no citable source for the
  cost breakdown. Repair concept itself per DIN SPEC 91472 p.8 (3.9).
- **Implementation check:** `Underlying Metrics = EC4-2…EC4-5` (R4 Material, Diagnostic, QA/
  Testing, Logistics); Formula (I) "R4 Material + R4 Diagnostic + R4 QA/Testing + R4
  Logistics" — matches the four children exactly. Strategy SUM_AGGREGATE, unit €. Parent set
  `EC111\nEC41` is correct (feeds both the Lifecycle-Management roll-up and the Repair
  Viability ratio).
- **Proposed revision (C):** keep, with a small alignment to the actual leaves: "Total repair
  (R4) expenses, summed from R4 material, diagnostic, QA/testing and logistics costs (EC4-2…
  EC4-5). Captures the cost drivers of offering a repair service."
- **Notes:** none material. Wording "labor, parts" loosely maps to the leaves (parts ≈
  material; labor is implicit in diagnostic/QA) — the proposed revision names the actual four
  cost lines to remove that small mismatch. [minor] optional only.

### EC42 — Refurbishment Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and profits connected to refurbishment to highlight its
  economic viability."
- **Verdict:** ADAPTED — matches `Ratio = Profits / Costs` normalized; refurbishment concept
  grounded, ratio author-defined.
- **Grounding:** DIN SPEC 91472 p.7 (3.6, refurbishment definition, quoted above); R5 =
  refurbish (FAC+21 p.2).
- **Implementation check:** Children EC4-6 (Refurbishment Profits) + EC421 (Refurbishment
  Costs) exist; Formula `Profits / Costs` normalized; unit %. Consistent.
- **Proposed revision (C):** "Scores the economic viability of the refurbishment (R5) service
  by comparing refurbishment profits (EC4-6) against refurbishment costs (EC421): higher when
  resale revenue from refurbished units outweighs the refurbishment cost."
- **Notes:** ADAPTED flag (R) non-obvious (ratio author-defined): add "Cost/profit viability
  ratio author-defined; refurbishment per DIN SPEC 91472 (3.6) / R5."

### EC421 — Refurbishment Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with restoring a sustainable product to a
  like-new condition, including costs for repairs, replacement of parts, cleaning, and any
  upgrades or enhancements made during the refurbishment process."
- **Verdict:** CONSISTENT — "total expenses … including …" matches SUM_AGGREGATE of its
  five € leaves.
- **Grounding:** UNVERIFIABLE by design (€ cost roll-up). Refurbishment concept per DIN SPEC
  91472 p.7 (3.6).
- **Implementation check:** `Underlying Metrics = EC4-7…EC4-11` (R5 Material, Diagnostic, QA/
  Testing, Logistics, Update); Formula (I) lists exactly those five "R5 …" lines — matches.
  SUM_AGGREGATE, €. Parent `EC111\nEC42` correct.
- **Proposed revision (C):** keep. Optional tightening: "Total refurbishment (R5) expenses,
  summed from R5 material, diagnostic, QA/testing, logistics and update costs (EC4-7…EC4-11)."
- **Notes:** [minor] the current prose says "like-new condition" — DIN SPEC reserves the
  "as-new / new-product" claim for *remanufacturing* (p.9: "remanufactured product … at least
  the same functionality and performance of the original product"), while refurbishment is
  "a fully functional high-quality used product" (3.6). Consider softening "like-new" to
  "high-quality functional" to avoid blurring the refurbish/remanufacture boundary. Optional,
  low severity.

### EC43 — Repurpose Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and profits connected to repurposing to highlight its
  economic viability."
- **Verdict:** ADAPTED — matches `Ratio = Profits / Costs` normalized; repurpose grounded only
  at framework level.
- **Grounding:** R7 = repurpose (FAC+21 p.2). No standalone repurpose definition surfaced in
  DIN SPEC 91472 or ISO 59020 — see "shared grounding" note. The EC4-12 leaf description
  ("selling (modified) product for an originally unintended use case") is itself a reasonable
  repurpose definition but is author-supplied, not lifted from a cited source.
- **Implementation check:** Children EC4-12 (Repurpose Profit) + EC431 (Repurpose Costs)
  exist; Formula `Profits / Costs` normalized; unit %. Consistent.
- **Proposed revision (C):** "Scores the economic viability of the repurpose (R7) service by
  comparing repurpose profits (EC4-12) against repurpose costs (EC431): higher when revenue
  from giving the product a new, originally-unintended use outweighs the modification cost."
- **Notes:** ADAPTED flag (R) non-obvious: add "Cost/profit viability ratio author-defined;
  repurpose = R7 (FAC+21). No standalone repurpose definition in the cited corpus." Do **not**
  add a DIN SPEC citation to J for repurpose — the standard does not define it.

### EC431 — Repurpose Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with modifying a sustainable product to
  serve a different function or use than its original design, including costs for labor,
  materials, and any necessary alterations or enhancements to facilitate the new use."
- **Verdict:** CONSISTENT — "total expenses … including …" matches SUM_AGGREGATE of its
  two € leaves.
- **Grounding:** UNVERIFIABLE by design (€ cost roll-up).
- **Implementation check:** `Underlying Metrics = EC4-13` (R7 Modification) + `EC4-14` (R7
  Logistics); Formula (I) "R7 Modification Costs + R7 Logistics Costs" — matches the two
  children. SUM_AGGREGATE, €. Parent `EC111\nEC43` correct.
- **Proposed revision (C):** keep. Optional: "Total repurpose (R7) expenses, summed from R7
  modification and logistics costs (EC4-13, EC4-14)." Note the prose mentions "labor,
  materials" but the leaves are only Modification + Logistics — the modification line is
  assumed to absorb labor/materials; naming the two actual leaves removes the ambiguity.
- **Notes:** [minor] only (cost-line wording vs leaves).

### EC44 — Recycling Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and savings connected to recyling to highlight its
  economic viability."
- **Verdict:** ADAPTED — matches `Ratio = Savings / Costs` normalized (note: **savings**, not
  profits — correctly distinct from EC41/EC42/EC43). Recycling concept grounded.
- **Grounding:** DIN SPEC 91472 p.7 (3.5, recycling definition, quoted above); R8 = recycle
  (FAC+21 p.2). The savings/cost ratio is author-defined.
- **Implementation check:** Children EC4-15 (Recycling Savings) + EC441 (Recycle Costs) exist;
  Formula `Savings / Costs` normalized; unit %. Description consistent (savings, not profits).
- **Proposed revision (C):** "Scores the economic viability of recycling (R8) by comparing the
  material-cost savings from recycled inputs (EC4-15) against recycling costs (EC441): higher
  when avoided material cost outweighs the cost of recycling."
- **Notes:** [minor] typo "recyling" → "recycling" in current C. ADAPTED flag (R) non-obvious:
  add "Savings/cost viability ratio author-defined; recycling per DIN SPEC 91472 (3.5) / R8."

### EC441 — Recycle Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with the collection, processing, and
  conversion of a sustainable product or its components into raw materials for reuse,
  including costs for labor, equipment, transportation, and any fees paid to recycling
  facilities."
- **Verdict:** CONSISTENT — "total expenses … including …" matches SUM_AGGREGATE of its
  three € leaves.
- **Grounding:** UNVERIFIABLE by design (€ cost roll-up). Recycling concept per DIN SPEC 91472
  p.7 (3.5).
- **Implementation check:** `Underlying Metrics = EC4-16` (R8 Processing) + `EC4-17` (R8
  Quality Control) + `EC4-18` (R8 Logistics); Formula (I) "R8 Processing + R8 Quality Control
  + R8 Logistics" — matches. SUM_AGGREGATE, €. Parent `EC112\nEC44` correct (feeds EOL Costs +
  Recycling Viability).
- **Proposed revision (C):** keep. Optional: "Total recycling (R8) expenses, summed from R8
  processing, quality-control and logistics costs (EC4-16…EC4-18)."
- **Notes:** none material.

### EC45 — Recovery Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and savings connected to recovery to highlight its
  economic viability."
- **Verdict:** ADAPTED — matches `Ratio = Savings / Costs` normalized (savings, consistent
  with EC4-19 Recovery Savings). Recovery concept grounded.
- **Grounding:** ISO 59020 p.35 (8.4.5, recovering resource value, quoted above); R9 =
  recovery (FAC+21 p.2). Savings/cost ratio author-defined.
- **Implementation check:** Children EC4-19 (Recovery Savings) + EC451 (Recovery Costs) exist;
  Formula `Savings / Costs` normalized; unit %. Consistent.
- **Proposed revision (C):** "Scores the economic viability of recovery (R9) by comparing the
  savings from recovered energy/materials (EC4-19) against recovery costs (EC451): higher when
  recovered value outweighs the cost of recovery."
- **Notes:** [minor] Objective (D) typo "sustanable". ADAPTED flag (R) non-obvious: add
  "Savings/cost viability ratio author-defined; recovery per ISO 59020 (8.4.5) / R9."

### EC451 — Recovery Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with reclaiming valuable materials or
  components from a product at the end of its life cycle, including costs for dismantling,
  processing, and any fees incurred during the recovery process."
- **Verdict:** CONSISTENT — "total expenses … including …" matches SUM_AGGREGATE of its
  four € leaves.
- **Grounding:** UNVERIFIABLE by design (€ cost roll-up). Recovery concept per ISO 59020 p.35
  (8.4.5).
- **Implementation check:** `Underlying Metrics = EC4-20…EC4-23` (R9 Energy Extraction,
  Material Extraction, Infrastructure, Maintenance); Formula (I) "R9 Energy Extraction + R9
  Material Extraction + R9 Infrastructure + R9 Maintenance" — matches the four children.
  SUM_AGGREGATE, €. Parent `EC112\nEC45` correct.
- **Proposed revision (C):** keep. Optional: "Total recovery (R9) expenses, summed from R9
  energy-extraction, material-extraction, infrastructure and maintenance costs (EC4-20…
  EC4-23)."
- **Notes:** [minor] prose says "dismantling, processing" but the leaves are energy/material
  extraction + infrastructure + maintenance — naming the actual four lines removes the small
  mismatch. Optional.

### EC46 — Remanufacturing Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs and savings connected to refurbishment to highlight its
  economic viability."
- **Verdict:** DRIFTED — the description says **"savings connected to refurbishment"**, but
  the row is *Remanufacturing* Viability: its child is EC4-24 (Remanufacturing **Profit**, not
  savings) and EC461 (Remanufacturing Costs), and the Formula is `Ratio = Profits / Costs`.
  Both the pathway name ("refurbishment") and the value type ("savings" vs profits) are wrong
  — copy-paste drift from EC42/EC44.
- **Grounding:** DIN SPEC 91472 p.8 (3.7 process steps) + p.9 (as-new functionality, market
  warranty), quoted above; R6 = remanufacture (FAC+21 p.2). The profit/cost ratio is
  author-defined. CJ+12 (References) notes "Remanufacturing typically costs 40–60% less than
  manufacturing new products" — context only, not cited on this row.
- **Implementation check:** Children EC4-24 (Remanufacturing Profit) + EC461 (Remanufacturing
  Costs) exist; Formula `Profits / Costs` normalized; unit %. The description contradicts the
  formula (savings) and mislabels the pathway (refurbishment).
- **Proposed revision (C):** "Scores the economic viability of remanufacturing (R6) by
  comparing remanufacturing profits (EC4-24) against remanufacturing costs (EC461): higher
  when revenue from selling remanufactured, as-new-warranted units outweighs the
  remanufacturing cost."
- **Notes:** [blocker] description names the wrong pathway ("refurbishment") and wrong value
  type ("savings") vs the live `Profits / Costs` formula and the EC4-24 Remanufacturing Profit
  child — rewrite as proposed. [minor] Objective (D) "determine if manufacturing is
  profitable" → "remanufacturing". ADAPTED flag (R) non-obvious: add "Profit/cost viability
  ratio author-defined; remanufacturing per DIN SPEC 91472 (3.7) / R6."

### EC461 — Remanufacturing Costs  [Level 4, aggregate(€ sum), SUM_AGGREGATE_STRATEGY]
- **Current (C):** "The total expenses associated with restoring a sustainable product to a
  new or better condition, including costs for the inspection, disassembly, testing, repair,
  cleaning, component replacement and assembly made during the remanufacturing process."
- **Verdict:** CONSISTENT (description) — "total expenses … inspection, disassembly, testing,
  repair, cleaning, component replacement and assembly" closely tracks the DIN SPEC 91472
  process steps and the EC4-25…EC4-30 leaves; SUM_AGGREGATE re-tag confirmed. **But two
  adjacent-cell defects** (Formula + Reference) need fixing — see Notes.
- **Grounding:** DIN SPEC 91472 p.8 (3.7): "The usual remanufacturing process steps include
  product identification, sorting, disassembly, cleaning, restoring, assembly and quality
  inspection." — strongly supports the description's step list.
- **Implementation check:** `Underlying Metrics = EC4-25…EC4-30` (six R6 lines: Material,
  Diagnostic, Repair, QA/Testing, Logistics, Dis-/Assembly). The Formula (I) cell instead
  reads **"R5 Material Costs + R5 Diagnostic Costs + R5 QA / Testing Costs + R5 Logistics
  Costs + R5 Update Costs"** — that is the **EC421 (R5 refurbishment) formula, five lines**,
  not the six R6 lines this row actually sums. Stale copy-paste. SUM_AGGREGATE, €. Parent
  `EC111\nEC46` correct.
- **Proposed revision (C):** keep the description (well-grounded). Fix Formula (I) to:
  "R6 Material Costs + R6 Diagnostic Costs + R6 Repair Costs + R6 QA / Testing Costs + R6
  Logistics Costs + R6 Dis-/Assembly Costs" (the six EC4-25…EC4-30 leaves).
- **Notes:** [major] Formula (I) names the wrong leaves (R5 five-line refurbishment set
  instead of the R6 six-line remanufacturing set EC4-25…EC4-30) — replace as above.
  [major] Reference (J) = `CM+25`, but **no `CM+25` file exists in `data/literature/Papers/`**
  (Glob/ls returned nothing) — the References sheet lists CM+25 (DOI 10.1016/j.clscn.2025.100260)
  but the PDF is absent: **SOURCE-NOT-FOUND**. CM+25 is a remanufacturing-KPI literature
  review, so the *code* is topically plausible, but the claim cannot be grounded here.
  Recommend either adding the CM+25 PDF to the corpus, or re-citing the groundable
  `DIN SPEC 91472` (and optionally CJ+12 for the cost-saving context) on this row.

### EC47 — Circular Material Viability  [Level 3, aggregate(ratio), NORMALIZED_RATIO_STRATEGY]
- **Current (C):** "Compares costs of the non-virgin material used in production with the
  virgin counterparts. It assumes that with 100% virgin material use, the circular materials
  are completely viable. Meaning there are no more incentives to use non-virgin material."
- **Verdict:** DRIFTED (clarity) — the formula is `Ratio = Non-Virgin / Virgin` then
  normalized, but the second/third sentences ("with 100% virgin material use, the circular
  materials are completely viable … no more incentives to use non-virgin material") read
  backwards and are confusing: if a product used 100% virgin material, Non-Virgin/Virgin → 0,
  which is the **least** circular state, not "completely viable." The interpretation sentence
  contradicts the direction of the ratio. The first sentence (cost comparison non-virgin vs
  virgin) is correct.
- **Grounding:** C2C 5.x p.8 (Product Circularity) + §5.3 "Incorporating Cycled and/or
  Renewable Content", quoted above — grounds the virgin-vs-cycled-material comparison concept.
  The specific cost-ratio and the "100% virgin = fully viable" assumption are author-defined
  (no source supports that assumption; it should be stated as an author convention, not as a
  literature claim).
- **Implementation check:** Children EC4-31 (Virgin Material Costs) + EC4-32 (Non-Virgin
  Material Costs) exist; Formula `Non-Virgin / Virgin` normalized; unit %. The ratio rises as
  non-virgin spend rises relative to virgin spend — so a higher score reflects greater reliance
  on (or cost of) circular material, which the band Min/Max must interpret. The current prose's
  "100% virgin = completely viable" inverts this and should be removed/reworded.
- **Proposed revision (C):** "Compares the cost of non-virgin (secondary) materials used in
  production against the cost of their virgin counterparts. A higher non-virgin-to-virgin cost
  ratio signals greater reliance on circular materials; the score is then normalised against a
  target band. (Author convention: the band is set so that economically sound circular-material
  use scores well.)"
- **Notes:** [major] remove the contradictory "with 100% virgin material use, the circular
  materials are completely viable … no more incentives" sentences — they invert the ratio's
  direction and assert an author assumption as if it were established. Confirm with the author
  the intended scoring direction (is higher non-virgin/virgin "good"?) so the Target Min/Max
  band (G) is set consistently — flag for `reviews/min-max-sourcing.md`. ADAPTED grounding to
  C2C is non-obvious: add a Comment (R) "Virgin-vs-cycled material concept per C2C Product
  Circularity §5.3; cost-ratio and viability assumption author-defined." Weight 0.1426 (vs the
  other six pathways at 0.1429) is a rounding artefact of 1/7 — harmless [minor].

---

## Batch summary

| KPI | Name | Verdict | Key action |
|---|---|---|---|
| EC4 | Circular Service Viability | DRIFTED | Rewrite C to name all 7 children; fix Formula "…EC45" → "…EC47" |
| EC41 | Repair Viability | ADAPTED | Refine C (name EC4-1/EC411); set Unit "%"; non-obvious flag |
| EC411 | Repair Costs | CONSISTENT | Keep (optional: name the 4 leaves) |
| EC42 | Refurbishment Viability | ADAPTED | Refine C; non-obvious flag |
| EC421 | Refurbishment Costs | CONSISTENT | Keep (optional: soften "like-new") |
| EC43 | Repurpose Viability | ADAPTED | Refine C; flag (no standalone source for repurpose) |
| EC431 | Repurpose Costs | CONSISTENT | Keep |
| EC44 | Recycling Viability | ADAPTED | Refine C; fix typo "recyling"; flag |
| EC441 | Recycle Costs | CONSISTENT | Keep |
| EC45 | Recovery Viability | ADAPTED | Refine C; fix "sustanable"; flag |
| EC451 | Recovery Costs | CONSISTENT | Keep |
| EC46 | Remanufacturing Viability | DRIFTED | **Rewrite C** — wrong pathway ("refurbishment") + wrong value type ("savings") |
| EC461 | Remanufacturing Costs | CONSISTENT (desc) | **Fix Formula** (R5→R6 six leaves); **Reference CM+25 SOURCE-NOT-FOUND** |
| EC47 | Circular Material Viability | DRIFTED | Remove contradictory "100% virgin = viable" sentences; confirm direction |

**Verdict tally (14 rows):** CONSISTENT 5 · ADAPTED 5 · DRIFTED 4 · UNVERIFIABLE 0 (the five
CONSISTENT cost roll-ups are *grounded-as-€-sums*; their underlying cost breakdowns are
UNVERIFIABLE-by-design, which is legitimate). Nothing applied to the workbook — all proposals.

**Inconsistencies & fixes (most severe first):**

| # | Severity | Where (col) | Inconsistency | Fix |
|---|----------|-------------|---------------|-----|
| 1 | blocker | EC46 / C, D | Description says "savings connected to **refurbishment**"; row is Remanufacturing with child EC4-24 **Profit** and formula `Profits/Costs` | Rewrite C to remanufacturing profit-vs-cost (proposed text); fix Objective "manufacturing"→"remanufacturing" |
| 2 | major | EC461 / I | Formula lists the **R5 refurbishment** 5-line set, not the **R6** six leaves EC4-25…EC4-30 it actually sums | Replace with the six R6 cost lines |
| 3 | major | EC461 / J | `CM+25` cited but **no CM+25 PDF in the corpus** (SOURCE-NOT-FOUND) | Add CM+25 PDF, or re-cite `DIN SPEC 91472` (+ optionally CJ+12) |
| 4 | major | EC47 / C | "with 100% virgin material use, the circular materials are completely viable … no incentives" inverts the `Non-Virgin/Virgin` ratio direction | Remove those sentences; reword per proposal; confirm scoring direction + band (G) |
| 5 | minor | EC4 / C, I | Description names only 3 of 7 pathways; Formula stops at "EC45" (omits EC46/EC47) | Rewrite C to all 7 children; fix Formula to "…* EC47" |
| 6 | minor | EC41 / H | Unit blank while peer ratios EC42–EC47 are "%" | Set Unit "%" |
| 7 | minor | EC44 / C; EC45 / D | Typos "recyling"; "sustanable" | Correct spelling |
| 8 | minor | EC41/42/43/44/45/46/47 / R | ADAPTED grounding (cost/profit/savings ratio author-defined over a real R-strategy concept) is non-obvious | Add short Comment-cell flags per per-KPI Notes; **do not** add a repurpose source to EC43 (none exists in corpus) |
| 9 | minor | EC411/421/431/441/451 / C | Cost-line prose loosely lists labor/parts vs the actual named leaves | Optional: name the actual EC4-x leaves (proposed texts) |
| 10 | minor | EC421 / C | "like-new condition" blurs the refurbish/remanufacture boundary (DIN SPEC reserves as-new for reman) | Optional: soften to "high-quality functional" |

**SOURCE-NOT-FOUND codes:** `CM+25` (Reference label exists in References.tsv with DOI
10.1016/j.clscn.2025.100260, but no `Papers/CM+25*` PDF is in `data/literature/`) — cited on
EC461 only within this batch.

**Limits of this run:** (1) CM+25 could not be opened (file absent), so the EC461 citation is
unverifiable rather than confirmed/refuted. (2) Repurpose (EC43/EC431) has no standalone
definition in the cited corpus (DIN SPEC 91472, ISO 59020) — grounded only at the R0–R9
framework level via FAC+21; I did not assert a definition the corpus does not contain.
(3) The raw EC4-1…EC4-32 profit/cost leaves and their SASB/FAC+21 citations are out of scope
(separate batch) and were checked only for existence/wiring, not grounded. (4) Target Min/Max
band direction for EC4 and EC47 (scoring orientation) needs author confirmation — flagged, not
resolved here.


---

## EC4 — Raw cost line-items EC4-1…EC4-16

### EC4-1 — Repair Profits  [L5, raw, RAW_VALUE]
- **Current** (C): "Profits generated with a product repair service, guaranteeing product repair for its lifespan /  defined time span." · H=€ · I=None · J=`SASB RT-CP-410a.2`, `FAC+21` · R=blank
- **Verdict:** ADAPTED (profit row) — but see Implementation note (this is a *profit*, not a cost).
- **Grounding:** `data/.../SASB/RT-CP-containers-and-packaging-standard_en-gb.pdf` p.7: "Revenue from products that are reusable, recyclable, or compostable … Presentation currency … RT-CP-410a.2". Org-level *revenue from circular products*; the KPI narrows it to **repair-service profit** for one product — a reasonable product-level adaptation. `FAC+21` resolves (circularity-performance framework paper); not separately quoted.
- **Implementation check:** Feeds EC41 as the **Profits** numerator of `Ratio = Profits / Costs`. Unit € and RAW_VALUE consistent. Note the row is a *profit* leaf among cost leaves — wiring is correct (it is the numerator, not part of EC411 cost sum).
- **Proposed revision:** drop the double space before "defined" → "…for its lifespan / defined time span." Optionally tighten: "Profit (revenue minus cost) from the product's repair service over its lifespan / a defined time span; feeds the Repair Viability ratio as the profit term." Otherwise keep-as-is.
- **Notes:** [minor] stray double space in description. Source code valid and on point — no extra Comment flag needed.

### EC4-2 — R4 Material Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated with materials necessary for repair." · H=€ · I=None · J=blank · R=blank · weight 0.25
- **Verdict:** UNVERIFIABLE (author-defined cost input — legitimate).
- **Grounding:** none cited; none expected.
- **Implementation check:** Child of **EC411 Repair Costs** (SUM of R4 Material + Diagnostic + QA + Logistics). Description matches the "Material Costs" term; € + RAW_VALUE consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-3 — R4 Diagnostic Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated with problem diagnosis before performing any repair." · H=€ · I=None · J=blank · weight 0.25
- **Verdict:** UNVERIFIABLE.
- **Grounding:** none expected.
- **Implementation check:** Child of EC411 Repair Costs. Text matches; € + RAW_VALUE consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-4 — R4 QA / Testing Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated to ensure that the product functions correctly according to standards." · H=€ · I=None · J=blank · weight 0.25
- **Verdict:** UNVERIFIABLE.
- **Grounding:** none expected.
- **Implementation check:** Child of EC411 Repair Costs. Text describes QA/testing for repair; consistent.
- **Proposed revision:** minor grammar — "Costs **to** ensure …" or "Costs **incurred to** ensure the repaired product functions correctly according to standards." Identical boilerplate is reused for EC4-9 and EC4-28 with no R-stage qualifier; consider adding "(repaired unit)" to disambiguate from the refurbishment/remanufacture QA leaves. Low priority.
- **Notes:** [minor] description identical to EC4-9 (R5 QA) — name disambiguates, but text alone is ambiguous across R-stages.

### EC4-5 — R4 Logistics Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Transportation costs for moving items necessary for repair" · H=€ · I=None · J=blank · weight 0.25
- **Verdict:** UNVERIFIABLE.
- **Grounding:** none expected.
- **Implementation check:** Child of EC411 Repair Costs. Consistent.
- **Proposed revision:** add trailing period for consistency with peers ("…necessary for repair."). Otherwise keep.
- **Notes:** [minor] missing terminal period (peers EC4-10/EC4-14 have one).

### EC4-6 — Refurbishment Profits  [L5, raw, RAW_VALUE]
- **Current** (C): "Profits generated from selling refurbished products." · H=€ · I=None · J=`SASB RT-CP-410a.2`, `FAC+21` · R=blank
- **Verdict:** ADAPTED (profit row).
- **Grounding:** same as EC4-1 — RT-CP-410a.2 "Revenue from products that are reusable, recyclable, or compostable" (SASB RT-CP PDF p.7). Refurbished-product resale is a faithful product-level narrowing.
- **Implementation check:** Profit numerator of **EC42 Refurbishment Viability** `Ratio = Profits / Costs`. € + RAW_VALUE consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none. Source code valid; adaptation self-evident.

### EC4-7 — R5 Material Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated with materials necessary for refurbishment." · H=€ · I=None · J=blank · weight 0.2
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of **EC421 Refurbishment Costs** (SUM of 5 R5 leaves). Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-8 — R5 Diagnostic Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated with problem diagnosis before performing any refurbishment process." · H=€ · I=None · J=blank · weight 0.2
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of EC421. Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-9 — R5 QA / Testing Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated to ensure that the product functions correctly according to standards." · H=€ · I=None · J=blank · weight 0.2
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of EC421. Consistent.
- **Proposed revision:** same boilerplate as EC4-4 (and EC4-28). Optionally append "(refurbished unit)" to disambiguate; grammar "Costs **to** ensure …". Low priority.
- **Notes:** [minor] description identical to EC4-4 — disambiguated only by name.

### EC4-10 — R5 Logistics Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Transportation costs for moving items necessary for refurbishment." · H=€ · I=None · J=blank · weight 0.2
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of EC421. Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-11 — R5 Update Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs associated with updates to the refurbished product." · H=€ · I=None · J=blank · weight 0.2
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of EC421 (the 5th R5 leaf; EC421 formula explicitly lists "R5 Update Costs"). Consistent. This leaf is unique to the refurbishment arm (no repair equivalent) — appropriate, as firmware/feature updates fit refurbishment.
- **Proposed revision:** keep as-is. (Optional clarity: "Costs of software/feature/component updates applied during refurbishment.")
- **Notes:** none.

### EC4-12 — Repurpose Profit  [L5, raw, RAW_VALUE]
- **Current** (C): "Profits generated by selling (modified) product for an originally unintended use case." · H=€ · I=None · J=`SASB RT-CP-410a.2`, `FAC+21` · R=blank
- **Verdict:** ADAPTED (profit row).
- **Grounding:** same RT-CP-410a.2 revenue-from-circular-products anchor (SASB RT-CP PDF p.7); repurpose resale is a faithful adaptation.
- **Implementation check:** Profit numerator of **EC43 Repurpose Viability** `Ratio = Profits / Costs`. € + RAW_VALUE consistent.
- **Proposed revision:** keep as-is. (Name "Repurpose **Profit**" singular vs EC4-1/-6 "Profit**s**" — cosmetic only.)
- **Notes:** [minor] singular/plural inconsistency in name vs sibling profit rows.

### EC4-13 — R7 Modification Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs for modifying existing products for a new use." · H=€ · I=None · J=blank · weight 0.5
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of **EC431 Repurpose Costs** (SUM of Modification + Logistics). Consistent with the R7/repurpose framing.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-14 — R7 Logistics Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs related to transporting or storing repurposed items." · H=€ · I=None · J=blank · weight 0.5
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of EC431. Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-15 — Recycling Savings  [L5, raw, RAW_VALUE]
- **Current** (C): "Savings in material costs made possible by the reuse of recycled materials." · H=€ · I=None · J=blank · R=blank
- **Verdict:** UNVERIFIABLE.
- **Grounding:** none cited; none expected. (Note: unlike the repair/refurb/repurpose arms, the recycling arm's positive term is a **Savings** row, not a Profit — and it correctly carries no `SASB RT-CP-410a.2` revenue code, consistent with EC44 using `Ratio = Savings / Costs`.)
- **Implementation check:** Feeds **EC44 Recycling Viability** as the **Savings** numerator (`Ratio = Savings / Costs`). € + RAW_VALUE consistent. Description correctly frames it as avoided material cost, not revenue.
- **Proposed revision:** keep as-is. (Optional precision: "Avoided material-purchase costs from using recycled instead of virgin material.")
- **Notes:** none. The Savings-vs-Profit distinction vs the other three arms is by design, not drift.

### EC4-16 — R8 Processing Costs  [L5, raw, RAW_VALUE]
- **Current** (C): "Costs related to sorting, cleaning, and processing recyclable materials." · H=€ · I=None · J=blank · weight 0.3333
- **Verdict:** UNVERIFIABLE.
- **Implementation check:** Child of **EC441 Recycle Costs** (SUM of Processing + QC + Logistics; weights 0.3333/0.3333/0.3334). Consistent.
- **Proposed revision:** keep as-is.
- **Notes:** none.

---

## Batch summary

**Verdicts (16 rows):** UNVERIFIABLE 13 (the plain cost leaves — legitimate, author-defined) ·
ADAPTED 3 (the profit rows EC4-1, EC4-6, EC4-12, all cite `SASB RT-CP-410a.2` + `FAC+21`).
No DRIFTED, no CONTRADICTION.

**Reference integrity:** `SASB RT-CP-410a.2` and `FAC+21` both resolve to Labels in
`References.tsv` and both files are present in the corpus. RT-CP-410a.2 verified as
"Revenue from products that are reusable, recyclable, or compostable" (SASB RT-CP PDF p.7) —
a loose org-level anchor for circular-service profit, faithfully adapted. No orphan codes.

**Wiring:** all 16 `Parent Metrics` references (EC41/411, EC42/421, EC43/431, EC44/441)
resolve to real rows; each leaf sits in the correct cost-sum or viability-ratio it feeds.
Unit (€), Formula (None), and `RAW_VALUE_STRATEGY` are uniform and correct across the batch.

**Issues found (all minor — no blockers, no majors):**
| # | Severity | Where | Inconsistency | Fix |
|---|----------|-------|---------------|-----|
| 1 | minor | EC4-1 | double space "lifespan /  defined" | collapse to single space |
| 2 | minor | EC4-4 / EC4-9 / (EC4-28) | identical QA/Testing boilerplate across R-stages; ambiguous without name | append "(repaired/refurbished unit)" qualifier; fix "Costs to ensure" |
| 3 | minor | EC4-5 | missing terminal period | add "." for peer consistency |
| 4 | minor | EC4-12 | name "Repurpose Profit" singular vs siblings "Profits" | align to "Profits" (cosmetic) |

**Rows needing a decision:** none. The Savings-vs-Profit asymmetry (EC4-15 vs EC4-1/-6/-12)
and the recycling arm correctly *not* carrying the SASB revenue code are intentional design,
not defects.

**SOURCE-NOT-FOUND codes:** none.

**Limits of this run:** I confirmed RT-CP-410a.2 is a *revenue* (not a cost) metric and used
it only as a loose anchor for the three profit rows; I did not deep-read `FAC+21` to confirm
it discusses repair/refurb/repurpose profit specifically (resolved as a circularity-framework
paper, accepted as a secondary cite). The 13 cost leaves were not literature-searched by
design — they are author-defined cost categories with no citable source, correctly left
blank. No workbook edits were made; all items above are proposals.


---

## EC4 — Raw cost line-items EC4-17…EC4-32

### EC4-17 — R8 Quality Control Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Ensuring that recycled materials meet quality standards."
- **Verdict:** DRIFTED (minor) — phrased as an activity, not a **cost**. Every sibling
  cost leaf reads "Costs … associated with …"; this row's text never says "costs", so it
  doesn't match its € unit / RAW_VALUE role or the parent label "R8 Quality Control Costs".
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC441` (Recycle Costs,
  SUM_AGGREGATE) ✓ — feeds the recycling cost arm of EC44 Recycling Viability. Wiring fine;
  only the prose is off.
- **Proposed revision:** "Costs of quality control to ensure recycled materials meet the
  required quality standards."
- **Notes:** [minor] description style fix only; no Unit/Formula/parent change.

### EC4-18 — R8 Logistics Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs of transporting materials to recycling facilities."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC441` ✓. Reads as a cost,
  matches the R8 recycling-logistics label.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-19 — Recovery Savings  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Savings in energy costs made possible by the recovery from production waste."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC45` (Recovery Viability) ✓.
  This is the **savings** numerator of EC45's `Ratio = Savings / Costs`, not a cost leaf —
  description correctly says "savings", consistent with the role.
- **Proposed revision:** keep as-is.
- **Notes:** Not a cost line despite the EC4-1x numbering — the savings arm of EC45. No action.

### EC4-20 — R9 Energy Extraction Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Expenses for extracting useful energy from waste."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓ ("Expenses" reads as cost), RAW_VALUE ✓, parent
  `EC451` (Recovery Costs) ✓. Matches the R9 energy-extraction label.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-21 — R9 Material Extraction Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Expenses for extracting useful materials from waste."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC451` ✓. Matches label.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-22 — R9 Infrastructure Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Investment in facilities or technology for recovery processes."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓ ("Investment" = cost), RAW_VALUE ✓, parent `EC451` ✓.
  Matches the R9 infrastructure label.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-23 — R9 Maintenance Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Ongoing costs to maintain recovery operations"
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC451` ✓. Matches label.
- **Proposed revision:** keep as-is (optionally add a trailing period for consistency with
  siblings — purely cosmetic).
- **Notes:** [minor] missing terminal period; cosmetic only.

### EC4-24 — Remanufacturing Profit  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Profits generated from selling remanufactured products."
- **Verdict:** CONSISTENT (description) — but **citation code looks wrong** (see Notes).
- **Grounding:** cited `SASB RT-IG-440b.1` + `FAC+21`. Not verified in this light pass; the
  sibling profit leaves (EC4-6/EC4-12) cite `SASB RT-CP-410a.2`. `RT-IG-…` is the SASB
  Industrial-Machinery code, whereas the rest of this domain uses `RT-CP-…` (Containers &
  Packaging). Possible mis-coded sub-locator — flag for the literature pass, do not "fix"
  blindly.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC46` (Remanufacturing
  Viability) ✓. This is the **profit** numerator of EC46's `Ratio = Profits / Costs` —
  description correctly says "profits", consistent with role.
- **Proposed revision:** keep description as-is.
- **Notes:** [minor] J-column: `SASB RT-IG-440b.1` is inconsistent with the `RT-CP-…`
  codes on the other circular-profit leaves — verify the correct SASB sub-code in a
  literature pass; out of scope to resolve here. Description itself fine.

### EC4-25 — R6 Material Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with materials necessary for remanufacturing."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` (Remanufacturing Costs) ✓.
- **Proposed revision:** keep as-is.
- **Notes:** Parent `EC461` Formula text lists "R5 Material Costs + …" while its six
  children are named **R6** (EC4-25…EC4-30) — formula/child label mismatch on the parent.
  Out of scope to edit (EC461 is not in this batch) but recorded for the EC4-parent pass.

### EC4-26 — R6 Diagnostic Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with problem diagnosis before performing any disassembly process."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` ✓. Reads as a cost.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-27 — R6 Repair Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with the repair of components from EoL units."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` ✓. Distinct from EC411
  repair costs by being a remanufacturing sub-step (component repair on EoL units) — clear.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-28 — R6 QA / Testing Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated to ensure that the product functions correctly according to standards for new-quality unit."
- **Verdict:** CONSISTENT (minor grammar).
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` ✓.
- **Proposed revision:** optional tidy — "Costs to ensure the remanufactured unit functions
  correctly to new-quality standards." (clarifies the trailing "for new-quality unit").
- **Notes:** [minor] grammar/clarity only; not a wiring issue.

### EC4-29 — R6 Logistics Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Transportation costs for moving items necessary for remanufacturing."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` ✓.
- **Proposed revision:** keep as-is.
- **Notes:** none.

### EC4-30 — R6 Dis-/Assembly Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with the disassembly of components from EoL units and the assembly of remanufactured components into a unit."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, parent `EC461` ✓. Description matches
  the combined dis-/assembly scope.
- **Proposed revision:** keep as-is.
- **Notes:** Parent `EC461` Formula lists only 5 R5-labelled lines (Material, Diagnostic,
  QA/Testing, Logistics, Update) but actually has 6 R6 children, and this dis-/assembly
  line is absent from the formula text (an "R5 Update Costs" line appears instead, which
  has no matching child). Formula-vs-children drift on the parent — recorded for the
  EC4-parent pass; out of scope to edit here.

### EC4-31 — Virgin Material Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with the usage of virgin material for producing the product. It could be the total cost of components made with virgin materials or the raw cost of virgin materials used for producing a functional unit."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, dual parent `EC1-5\nEC47` ✓ — feeds both
  Material Costs (EC1-5) and the Circular Material Viability ratio (EC47, virgin
  denominator). Description correctly states the two acceptable measurement bases.
- **Proposed revision:** keep as-is.
- **Notes:** Note the deliberate dual parenting (EC1-5 + EC47); intentional, no defect.

### EC4-32 — Non-Virgin Material Costs  [Level 5, raw, RAW_VALUE_STRATEGY]
- **Current:** "Costs associated with the usage of non-virgin or secondary material for producing the product. It could be the total cost of components made with non-virgin materials or the raw cost of non-virgin materials used for producing a functional unit."
- **Verdict:** CONSISTENT.
- **Grounding:** none — author-defined cost input. UNVERIFIABLE.
- **Implementation check:** Unit € ✓, RAW_VALUE ✓, dual parent `EC1-5\nEC47` ✓ — the
  non-virgin numerator of EC47's `Ratio = Non-Virgin / Virgin`. Description consistent.
- **Proposed revision:** keep as-is.
- **Notes:** Mirrors EC4-31; intentional dual parenting. No defect.

---

## Batch summary

**16 rows audited (EC4-17 … EC4-32).**
Verdicts: CONSISTENT 14 · DRIFTED 1 (EC4-17) · ADAPTED 0 · UNVERIFIABLE basis on all
author-defined cost/savings leaves (legitimate; no literature expected).

**Description rewrite proposed (1):**
- `EC4-17` [minor, DRIFTED] — text reads as an activity, not a cost; doesn't match the €
  / RAW_VALUE role. → "Costs of quality control to ensure recycled materials meet the
  required quality standards."

**Optional cosmetic tidy (2, not blocking):**
- `EC4-23` — add terminal period (sibling consistency).
- `EC4-28` — clarify trailing "for new-quality unit" grammar.

**Adjacent drift recorded but OUT OF SCOPE here (belongs to the EC4-parent pass):**
- `EC461` (parent of EC4-25…EC4-30) Formula text lists **R5**-labelled lines for **R6**
  children, names only 5 lines vs 6 children, and includes an "R5 Update Costs" line with
  no matching child while omitting EC4-30 Dis-/Assembly. [major] formula-vs-children drift.
- `EC4-24` Reference `SASB RT-IG-440b.1` uses the Industrial-Machinery (`RT-IG`) code while
  sibling profit leaves use `RT-CP-410a.2`. [minor] likely mis-coded sub-locator — verify
  in a literature pass, do not auto-fix.

**Names / formatting hygiene:** no stray leading/trailing spaces or tabs in any of the 16
indicator names; all units are `€`; all strategies `RAW_VALUE_STRATEGY`. No duplicate IDs
in range.

**Decisions needed:** none in this batch (EC4-17 rewrite is low-risk; the EC461 formula
and EC4-24 citation are deferred to their owning passes).

**Limits of this run:** literature was not pulled — by design these are author-defined €
cost/savings inputs (UNVERIFIABLE is correct, not a gap). The `SASB RT-IG-440b.1`
(EC4-24), `SASB RT-CP-410a.2`, `FAC+21`, `CM+25`, and `RE+20` codes were **not**
resolved against `References.tsv`/PDFs here; flagged for the parent/profit citation pass.
EC4-15/EC4-16 (part 1 of this subtree) and the EC4 parents/Viability ratios are outside
this batch.
