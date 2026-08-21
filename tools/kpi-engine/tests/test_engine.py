import pytest

from kpi_engine.engine import evaluate_all
from kpi_engine.model import Status
from tests.fixtures import mini


def test_raw_passthrough() -> None:
    results = evaluate_all(mini.build())
    assert results["EN2-1"].status is Status.OK
    assert results["EN2-1"].value == 30.0


def test_normalized_ratio() -> None:
    results = evaluate_all(mini.build())
    # EN21 = renewable/total = 30/100 = 0.3, normalized 0..1
    assert results["EN21"].value == pytest.approx(0.3)
    assert results["EN22"].value == pytest.approx(0.5)


def test_weighted_parent() -> None:
    results = evaluate_all(mini.build())
    # P = 0.25*0.3 + 0.75*0.5 = 0.45
    assert results["P"].value == pytest.approx(0.45)


def test_sum_strategy() -> None:
    results = evaluate_all(mini.build())
    # TOTAL = EN2-1 + EN2-2 = 30 + 100 = 130 (cost-style roll-up, not averaged)
    assert results["TOTAL"].value == pytest.approx(130.0)


def test_missing_data_reweighting() -> None:
    kpis = mini.build()
    kpis["EN2-3"].value = None  # EN22 loses an input -> EN22 missing
    results = evaluate_all(kpis)
    assert results["EN22"].status is Status.MISSING
    # P now averages only EN21 -> renormalizes to EN21's score
    assert results["P"].value == pytest.approx(0.3)


def test_self_normalizing_leaf() -> None:
    results = evaluate_all(mini.build())
    # EN6-1 normalizes its own value 5 against Min=0/Max=10 -> 0.5
    assert results["EN6-1"].status is Status.OK
    assert results["EN6-1"].value == pytest.approx(0.5)


def test_needs_review_propagates() -> None:
    results = evaluate_all(mini.build())
    # C4 = 1 - (10+10)/(2*100) = 0.9, flagged unverified
    assert results["C4"].value == pytest.approx(0.9)
    assert results["C4"].unverified is True


def test_formula_value_difference() -> None:
    results = evaluate_all(mini.build())
    # EC12 Net Profit = 200 - (100 + 20 + 10 + 5) = 65 (raw €, not normalized to [0,1])
    assert results["EC12"].status is Status.OK
    assert results["EC12"].value == pytest.approx(65.0)


def test_normalized_ratio_over_euro_totals() -> None:
    results = evaluate_all(mini.build())
    # EC1 ROI = EC12 / EC11 = 65/50 = 1.3, normalized against Min=0/Max=2 -> 0.65
    assert results["EC1"].value == pytest.approx(0.65)


def test_out_of_range_aggregate_is_hard_error() -> None:
    results = evaluate_all(mini.build())
    # BADAGG weighted-averages raw € (200, 100) -> 150, outside [0,1] -> ERROR, not a score
    assert results["BADAGG"].status is Status.ERROR
    assert "outside [0, 1]" in (results["BADAGG"].reason or "")


def test_missing_min_max() -> None:
    kpis = mini.build()
    kpis["EN21"].target_max = None
    results = evaluate_all(kpis)
    assert results["EN21"].status is Status.MISSING
    assert "Min/Max" in (results["EN21"].reason or "")
