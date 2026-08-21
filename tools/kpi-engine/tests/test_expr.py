import pytest

from kpi_engine.expr import ExprError, evaluate


def test_basic_arithmetic() -> None:
    assert evaluate("1 - a / b", {"a": 30, "b": 100}) == pytest.approx(0.7)
    assert evaluate("x * y", {"x": 2, "y": 3}) == 6
    assert evaluate("a + b + c", {"a": 1, "b": 2, "c": 3}) == 6


def test_functions() -> None:
    assert evaluate("avg(a, b, c)", {"a": 1, "b": 2, "c": 3}) == pytest.approx(2.0)
    assert evaluate("max(a, b)", {"a": 1, "b": 9}) == 9


def test_division_by_zero_raises() -> None:
    with pytest.raises(ExprError):
        evaluate("a / b", {"a": 1, "b": 0})


def test_unknown_variable_raises() -> None:
    with pytest.raises(ExprError):
        evaluate("a / b", {"a": 1})


def test_disallowed_syntax_raises() -> None:
    with pytest.raises(ExprError):
        evaluate("__import__('os')", {})
    with pytest.raises(ExprError):
        evaluate("a and b", {"a": 1, "b": 1})
