"""Catalog export tests against the real workbook (descriptive projection)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from kpi_engine.catalog import Catalog, load_catalog
from kpi_engine.report import catalog_to_json

WORKBOOK = Path(__file__).resolve().parents[3] / "data" / "KPI List.xlsx"

pytestmark = pytest.mark.skipif(
    not WORKBOOK.exists(), reason="canonical workbook not present")


@pytest.fixture(scope="module")
def catalog() -> Catalog:
    return load_catalog(WORKBOOK)


def test_loads_all_domains(catalog: Catalog) -> None:
    assert {d.id for d in catalog.domains} == {"EN", "EC", "C", "R", "S"}
    assert catalog.meta.kpi_count == len(catalog.kpis) > 200


def test_domain_score_present(catalog: Catalog) -> None:
    en0 = catalog.kpis["EN0"]
    assert en0.domain == "EN"
    assert en0.level == 1
    assert en0.underlying  # has children


def test_relations_are_id_lists(catalog: Catalog) -> None:
    en11 = catalog.kpis["EN11"]
    assert en11.parents == ["EN1"]
    assert "EN1-4" in en11.underlying


def test_cross_domain_parent_preserved(catalog: Catalog) -> None:
    # EN1-4 (Absolute PCF) feeds an Economic Viability score -> graph, not tree
    assert "EC5" in catalog.kpis["EN1-4"].parents


def test_raw_data_point_flag(catalog: Catalog) -> None:
    assert catalog.kpis["EN1-1"].is_raw_data_point is True
    assert catalog.kpis["EN0"].is_raw_data_point is False


def test_references_resolve(catalog: Catalog) -> None:
    # every cited code that exists in the bibliography resolves to a real entry
    cited = {code for k in catalog.kpis.values() for code in k.references}
    resolvable = cited & set(catalog.references)
    assert resolvable, "expected at least some citations to resolve"
    sample = catalog.references[next(iter(resolvable))]
    assert sample.title or sample.description


def test_no_compute_fields_leak(catalog: Catalog) -> None:
    # the descriptive catalog must not carry company-input / result machinery
    dumped = json.loads(catalog_to_json(catalog))
    any_kpi = next(iter(dumped["kpis"].values()))
    for forbidden in ("weight", "value", "targetMin", "targetMax", "status"):
        assert forbidden not in any_kpi


def test_json_keys_are_camel_case(catalog: Catalog) -> None:
    dumped = json.loads(catalog_to_json(catalog))
    any_kpi = next(iter(dumped["kpis"].values()))
    assert "isRawDataPoint" in any_kpi
    assert "calculationStrategy" in any_kpi
    assert "lifecycleStages" in any_kpi
