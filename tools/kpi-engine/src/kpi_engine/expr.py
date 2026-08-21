"""A tiny, safe arithmetic expression evaluator.

Used to evaluate the encoded NORMALIZED_RATIO intermediate formulas (e.g.
``"1 - current / previous"``) against a namespace of named values. Only a fixed
whitelist of AST nodes is permitted; ``eval`` is never used.
"""
from __future__ import annotations

import ast
import operator
from collections.abc import Callable, Sequence
from typing import Final


class ExprError(ValueError):
    """Raised when an expression is malformed or cannot be evaluated."""


_BINOPS: Final[dict[type[ast.operator], Callable[[float, float], float]]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}

_UNARYOPS: Final[dict[type[ast.unaryop], Callable[[float], float]]] = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _avg(*xs: float) -> float:
    if not xs:
        raise ExprError("avg() needs at least one argument")
    return sum(xs) / len(xs)


_FUNCS: Final[dict[str, Callable[..., float]]] = {
    "min": min,
    "max": max,
    "sum": lambda *xs: float(sum(xs)),
    "avg": _avg,
}


def evaluate(expr: str, variables: dict[str, float]) -> float:
    """Evaluate ``expr`` using ``variables`` as the name namespace.

    Raises ``ExprError`` on unknown names, disallowed syntax, or division by zero.
    """
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:  # pragma: no cover - defensive
        raise ExprError(f"bad expression {expr!r}: {exc}") from exc
    return _eval(tree.body, variables)


def _eval(node: ast.AST, ns: dict[str, float]) -> float:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ExprError(f"non-numeric constant {node.value!r}")
        return float(node.value)
    if isinstance(node, ast.Name):
        if node.id not in ns:
            raise ExprError(f"unknown variable {node.id!r}")
        return float(ns[node.id])
    if isinstance(node, ast.BinOp):
        op = _BINOPS.get(type(node.op))
        if op is None:
            raise ExprError(f"operator {type(node.op).__name__} not allowed")
        right = _eval(node.right, ns)
        if isinstance(node.op, ast.Div) and right == 0:
            raise ExprError("division by zero")
        return op(_eval(node.left, ns), right)
    if isinstance(node, ast.UnaryOp):
        uop = _UNARYOPS.get(type(node.op))
        if uop is None:
            raise ExprError(f"unary operator {type(node.op).__name__} not allowed")
        return uop(_eval(node.operand, ns))
    if isinstance(node, ast.Call):
        return _eval_call(node, ns)
    raise ExprError(f"syntax element {type(node).__name__} not allowed")


def _eval_call(node: ast.Call, ns: dict[str, float]) -> float:
    if not isinstance(node.func, ast.Name) or node.func.id not in _FUNCS:
        raise ExprError("only min/max/sum/avg calls are allowed")
    if node.keywords:
        raise ExprError("keyword arguments not allowed")
    args: Sequence[float] = [_eval(a, ns) for a in node.args]
    return float(_FUNCS[node.func.id](*args))
