# `data/`: inputs to the KPI system

This folder holds the inputs the KPI system builds on.

| Item | In git? | What it is |
|------|---------|------------|
| `KPI List.xlsx` | tracked | The canonical KPI workbook. See the [top-level README](../README.md) for the versioning scheme. |
| `literature/` | local only | The reference corpus (~120 documents) behind the KPI definitions. Not versioned. |
| `others/` | local only | Company- and workshop-specific inputs (scope decisions, notes) that `build_company_kpi.py` reads. Not versioned. |

## Why `literature/` is not in the repository

Two reasons, and the second is the important one for a public repo:

1. **Size.** The corpus is ~200 MB of PDFs.
2. **Copyright.** Copyright covers the ISO and DIN standards and the GRI/SASB/ESRS/IFRS
   reporting standards. It also covers the paywalled journal articles. We may not
   redistribute any of them, so they stay out of git even though the folder is convenient
   to have locally.

This file documents the corpus instead. Maintainers and users can see what the KPI system
draws on, and get each source themselves from the links below.

> The per-indicator citation list lives in the workbook's References sheet, mirrored as
> text in [`../snapshot/References.tsv`](../snapshot/References.tsv). Each KPI's
> *Reference* field carries a Label code (e.g. `EN 15804`, `GRI 302-3`, `RM+23`) that
> resolves to a row there. The list below groups the same sources by document, and by
> where each one lives in `data/literature/`.

## The corpus

### Sustainability reporting frameworks

| Standard | What it covers |
|---|---|
| [ESRS](https://eur-lex.europa.eu/eli/reg_del/2023/2772/oj), Commission Delegated Regulation (EU) 2023/2772 | European Sustainability Reporting Standards. ESRS 1 and 2 (general), E1 Climate, E2 Pollution, E3 Water and marine, E4 Biodiversity, E5 Resource use and circular economy, G1 Governance, S1 Own workforce, S2 to S4 value chain, affected communities and consumers. |
| [GRI](https://www.globalreporting.org/how-to-use-the-gri-standards/gri-standards-english-language/) | Global Reporting Initiative. Foundation, Universal, Topic and Sector standards. Covers the 200 economic, 300 environmental and 400 social series, plus the sector standards and the glossary. |
| [IFRS Sustainability Disclosure Standards](https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/) | IFRS S1 (general requirements) and IFRS S2 (climate-related disclosures). |
| [SASB Standards](https://www.ifrs.org/issued-standards/sasb-standards/) | Industry standards used to apply IFRS S1/S2. Containers and Packaging (RT-CP), Industrial Machinery and Goods (RT-IG), Electrical and Electronic Equipment (RT-EE), Hardware (TC-HW), Software and IT Services (TC-SI), Road Transportation (TR-RO). |

### ISO standards

| Standard | What it covers |
|---|---|
| ISO 14XXX (environmental / LCA) | 14021 (self-declared environmental claims), 14025 (Type III environmental declarations / EPD), 14040 and 14044 (LCA principles and requirements), 14046 (water footprint), 14067 (product carbon footprint). |
| ISO 59XXX (circular economy) | 59004, 59010, 59014, 59020 (measuring and assessing circularity performance), 59040. |
| ISO 26000 | Social responsibility. |
| ISO 10004 | Monitoring and measuring customer satisfaction. |
| ISO 9001 | Quality management systems (referenced for QMS context). |

<!-- plain-lint-disable title_case_heading -->
### European standards (EN and DIN SPEC)

| Standard | What it covers |
|---|---|
| [EN 15804+A2](https://www.din.de/en/getting-involved/standards-committees/nabau/publications/wdc-beuth:din21:344735627) | Core EPD rules for construction products. The system uses the Module D update: benefits and loads beyond the system boundary, which covers reuse, recovery and recycling. |
| EN 45553 | Assessing the ability to remanufacture energy-related products. |
| EN 45554 | Assessing the ability to repair, reuse and upgrade energy-related products. |
| EN 45557 | Assessing the proportion of recycled material content. |
| EN 45560 | Method to achieve circular designs of products. |
| DIN SPEC 91472:2023-06 | Remanufacturing (Reman): quality classification for circular processes. |

### EPD and the digital product passport

- EPD / Module D materials: EN 15804+A2 and supporting Module-D whitepapers, including GreenDelta.
- Digital Product Passport (DPP): Regulation (EU) 2024/1781 (ESPR) and the CISL "Digital Products Passport" report.

### Environmental footprint and LCIA methods

- [PEF, Product Environmental Footprint](https://eur-lex.europa.eu/eli/reco/2021/2279): Commission Recommendation (EU) 2021/2279. The system uses its 16 impact categories (Annex I).
- MCI, Material Circularity Indicator (Ellen MacArthur Foundation): the base for several circularity KPIs.

Characterization factors and LCIA methods come from:

- USEtox 2.0 (ecotoxicity and human toxicity)
- AWARE (WULCA water scarcity, `BA+17`)
- abiotic depletion (`OL+02`)
- ILCD 2011 (acidification)
- ReCiPe 2008
- ozone-depletion CFs (`AO+24`)
- PM and ozone human-health CFs (`VZ+08`)
- ionizing-radiation CFs (`FR+00`)
- freshwater eutrophication (EUEP-FW)
- biodiversity valuation (`JPL+19`, `JQ+25`)

### Databases

- [PSILCA](https://psilca.net/): Product Social Impact Life Cycle Assessment database.

### Certification schemes

- [Cradle to Cradle Certified® Product Standard](https://c2ccertified.org/the-standard): Full Scope, versions up to 5.x, including the Material Reutilization category.

### Research papers

Grounding literature lives under `literature/Papers/`. Each entry below maps a reference
code to its topic. The References sheet carries the full titles and DOIs.

- Circularity indicators and frameworks: `CS+16`, `RE+20`, `FAC+21`, `SRS+20`, `MG+19`,
  `KHS+18`, `FE+16` / `JEF+16` (resource duration / longevity), `PJY+14` (reuse potential).
- Repair and repairability: `RM+23`, `FB+16`, `DS+22`.
- Disassembly and remanufacturing: `VP+18` (eDiM), `MM+17`, `DSK+00`, `NB+20`.
- Repurposing: `WS+24`.
- Recycling and materials: `GTE+11` (metal recycling rates).
- Biodiversity in LCA: `JPL+19`, `JQ+25`.
- Eco-efficiency, water and other LCA: `LGM+18`, `TF+25`, `EB+13` (sustainable business
  model archetypes), `EDNA` (data-centre efficiency metrics).

## Reproducing the corpus locally

Recreate `data/literature/` from the links above, or from your institutional access. The
tooling expects a fixed folder layout. Put standards in per-body subfolders (`ISO 14XXX/`,
`ESRS .../`, `GRI .../`, `SASB .../`) and journal articles under `Papers/`. Prefix every
PDF filename with its reference code, for example `RM+23-....pdf`.
`tools/scripts/pdf_search.py` and the `kpi-literature-crosschecker` review brief resolve
sources by that code prefix.
