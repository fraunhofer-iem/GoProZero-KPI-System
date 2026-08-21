import pytest

from kpi_engine.strategies import StrategyError, clamp, normalize, weighted_average


def test_clamp() -> None:
    assert clamp(-0.5) == 0.0
    assert clamp(1.5) == 1.0
    assert clamp(0.3) == 0.3


def test_normalize() -> None:
    assert normalize(0.3, 0.0, 1.0) == pytest.approx(0.3)
    assert normalize(50, 0, 100) == pytest.approx(0.5)
    # clamps out-of-range
    assert normalize(150, 0, 100) == 1.0
    assert normalize(-10, 0, 100) == 0.0


def test_normalize_degenerate_range_raises() -> None:
    with pytest.raises(StrategyError):
        normalize(5, 10, 10)


def test_weighted_average() -> None:
    assert weighted_average([(0.25, 0.3), (0.75, 0.5)]) == pytest.approx(0.45)


def test_weighted_average_renormalizes_when_a_child_drops() -> None:
    # only one of two children present -> its weight renormalizes to 1
    assert weighted_average([(0.25, 0.3)]) == pytest.approx(0.3)


def test_weighted_average_no_weights_raises() -> None:
    with pytest.raises(StrategyError):
        weighted_average([])
