# `data/` — inputs to the KPI system

This folder holds the inputs the KPI system is built from.

| Item | In git? | What it is |
|------|---------|------------|
| `KPI List.xlsx` | ✅ tracked | The canonical KPI workbook. See the [top-level README](../README.md) for how it is versioned. |
| `literature/` | ❌ local only | The reference corpus (~120 documents) the KPI definitions are grounded in. Not versioned. |
| `others/` | ❌ local only | Company- and workshop-specific inputs (scope decisions, notes) consumed by `build_company_kpi.py`. Not versioned. |

## Why `literature/` is not in the repository

Two reasons, and the second is the important one for a public repo:

1. **Size.** The corpus is ~200 MB of PDFs.
2. **Copyright.** Most sources — ISO and DIN standards, the GRI/SASB/ESRS/IFRS
   reporting standards, and paywalled journal articles — are copyrighted and **may not
   be redistributed**. They must stay out of git even though the folder is otherwise
   convenient to have locally.

This file therefore **documents** the corpus so maintainers and users know exactly what
the KPI system draws on, and can obtain each source themselves from the links below.

> The authoritative, per-indicator citation list lives in the workbook's **References**
> sheet (mirrored as text in [`../snapshot/References.tsv`](../snapshot/References.tsv)):
> each KPI's *Reference* field carries a **Label** code (e.g. `EN 15804`, `GRI 302-3`,
> `RM+23`) that resolves to a row there. The list below is the document-level view of the
> same body of sources, grouped by where each lives in `data/literature/`.

## The corpus

### Sustainability reporting frameworks

- **ESRS — European Sustainability Reporting Standards** (Commission Delegated Regulation
  (EU) 2023/2772): ESRS 1 & 2 (general), E1 Climate, E2 Pollution, E3 Water & marine,
  E4 Biodiversity, E5 Resource use & circular economy, G1 Governance, S1 Own workforce,
  S2–S4 Value-chain/affected communities/consumers.
  → https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj
- **GRI — Global Reporting Initiative** (Foundation, Universal, Topic and Sector standards;
  the 200 economic, 300 environmental and 400 social series, plus sector standards and the
  glossary). → https://www.globalreporting.org/how-to-use-the-gri-standards/gri-standards-english-language/
- **IFRS Sustainability Disclosure Standards** — IFRS S1 (general requirements) and
  IFRS S2 (climate-related disclosures). → https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/
- **SASB Standards** — industry standards used to apply IFRS S1/S2: Containers & Packaging
  (RT-CP), Industrial Machinery & Goods (RT-IG), Electrical & Electronic Equipment (RT-EE),
  Hardware (TC-HW), Software & IT Services (TC-SI), Road Transportation (TR-RO).
  → https://www.ifrs.org/issued-standards/sasb-standards/

### ISO standards

- **ISO 14XXX (environmental / LCA):** ISO 14021 (self-declared environmental claims),
  14025 (Type III environmental declarations / EPD), 14040 & 14044 (LCA principles and
  requirements), 14046 (water footprint), 14067 (product carbon footprint).
- **ISO 59XXX (circular economy):** ISO 59004, 59010, 59014, 59020 (measuring & assessing
  circularity performance), 59040.
- **ISO 26000** — Social responsibility.
- **ISO 10004** — Monitoring and measuring customer satisfaction.
- **ISO 9001** — Quality management systems (referenced for QMS context).

### European standards (EN / DIN SPEC)

- **EN 15804+A2** — Core EPD rules for construction products; the system focuses on the
  **Module D** update (benefits/loads beyond the system boundary: reuse, recovery,
  recycling). → https://www.din.de/en/getting-involved/standards-committees/nabau/publications/wdc-beuth:din21:344735627
- **EN 45553** — assessing the ability to **remanufacture** energy-related products.
- **EN 45554** — assessing the ability to **repair, reuse and upgrade** energy-related products.
- **EN 45557** — assessing the **proportion of recycled material content**.
- **EN 45560** — method to achieve **circular designs** of products.
- **DIN SPEC 91472:2023-06** — Remanufacturing (Reman): quality classification for circular processes.

### EPD & Digital Product Passport

- **EPD / Module D** materials — EN 15804+A2 and supporting Module-D whitepapers (incl. GreenDelta).
- **Digital Product Passport (DPP)** — Regulation (EU) 2024/1781 (ESPR) and the CISL
  "Digital Products Passport" report.

### Environmental Footprint & LCIA methods

- **PEF — Product Environmental Footprint**: Commission Recommendation (EU) 2021/2279,
  used for the 16 PEF impact categories (Annex I). → https://eur-lex.europa.eu/eli/reco/2021/2279
- **MCI — Material Circularity Indicator** (Ellen MacArthur Foundation), base for several
  circularity KPIs.
- **Characterization-factor / LCIA method sources:** USEtox 2.0 (ecotoxicity/human tox),
  AWARE (WULCA water scarcity, `BA+17`), abiotic depletion (`OL+02`), ILCD 2011
  (acidification), ReCiPe 2008, ozone-depletion CFs (`AO+24`), PM/ozone human-health CFs
  (`VZ+08`), ionising-radiation CFs (`FR+00`), freshwater eutrophication (EUEP-FW),
  biodiversity valuation (`JPL+19`, `JQ+25`).

### Databases

- **PSILCA** — Product Social Impact Life Cycle Assessment database. → https://psilca.net/

### Certification schemes

- **Cradle to Cradle Certified® Product Standard** (Full Scope, versions up to 5.x incl.
  the Material Reutilization category). → https://c2ccertified.org/the-standard

### Research papers

Grounding literature under `literature/Papers/` (reference code → topic; see the References
sheet for full titles and DOIs):

- **Circularity indicators & frameworks:** `CS+16`, `RE+20`, `FAC+21`, `SRS+20`, `MG+19`,
  `KHS+18`, `FE+16` / `JEF+16` (resource duration / longevity), `PJY+14` (reuse potential).
- **Repair & repairability:** `RM+23`, `FB+16`, `DS+22`.
- **Disassembly & remanufacturing:** `VP+18` (eDiM), `MM+17`, `DSK+00`, `NB+20`.
- **Repurposing:** `WS+24`.
- **Recycling & materials:** `GTE+11` (metal recycling rates).
- **Biodiversity in LCA:** `JPL+19`, `JQ+25`.
- **Eco-efficiency, water & other LCA:** `LGM+18`, `TF+25`, `EB+13` (sustainable business
  model archetypes), `EDNA` (data-centre efficiency metrics).

## Reproducing the corpus locally

Recreate `data/literature/` from the links above (or your institutional access) using the
folder layout the tooling expects: standards in per-body subfolders (`ISO 14XXX/`,
`ESRS .../`, `GRI .../`, `SASB .../`, …) and journal articles under `Papers/`, each PDF
**filename-prefixed with its reference code** (e.g. `RM+23-...pdf`). `tools/scripts/pdf_search.py`
and the `kpi-literature-crosschecker` review brief resolve sources by that code prefix.
