from kpi_engine.model import Kpi, Strategy
from kpi_engine.validate import validate
from tests.fixtures import mini


def _kinds(issues, kind):
    return [i for i in issues if i.kind == kind]


def _norm(kid: str, sheet: str, tmin: float, tmax: float) -> Kpi:
    return Kpi(id=kid, name=kid, sheet=sheet, strategy=Strategy.NORMALIZED,
               target_min=tmin, target_max=tmax)


def test_band_direction_flags_lower_is_better_with_ascending_band() -> None:
    # R222 (energy / units) is lower-is-better; an ascending band scores it backwards.
    issues = _kinds(validate({"R222": _norm("R222", "Resource Efficiency", 0.0, 25.0)}),
                    "band_direction")
    assert any(i.ids == ["R222"] for i in issues)


def test_band_direction_ok_for_lower_is_better_inverted_band() -> None:
    # Inverted band (Min > Max) is the correct orientation for a lower-is-better row.
    assert not _kinds(validate({"R222": _norm("R222", "Resource Efficiency", 25.0, 0.0)}),
                      "band_direction")


def test_band_direction_flags_higher_is_better_with_inverted_band() -> None:
    # EN21 (renewable share) is higher-is-better; an inverted band is wrong.
    issues = _kinds(validate({"EN21": _norm("EN21", "Environmental Impact", 1.0, 0.0)}),
                    "band_direction")
    assert any(i.ids == ["EN21"] for i in issues)


def test_band_direction_silent_on_default_fixture() -> None:
    # the mini fixture's bands are all correctly oriented
    assert not _kinds(validate(mini.build()), "band_direction")


def test_weight_missing_flagged_for_unweighted_children() -> None:
    # BADAGG (WEIGHTED_AVG) has children EC1-4 / EC121 with no weights set
    issues = validate(mini.build())
    missing = _kinds(issues, "weight_missing")
    assert any("BADAGG" in i.ids for i in missing)


def test_weight_sum_flagged_when_not_one() -> None:
    issues = validate(mini.build())
    summ = _kinds(issues, "weight_sum")
    assert any(i.ids == ["BADAGG"] for i in summ)


def test_balanced_parent_has_no_weight_issue() -> None:
    # P weights its children 0.25 + 0.75 = 1.0, both set -> no weight issue mentions P
    issues = validate(mini.build())
    weight_issues = _kinds(issues, "weight_missing") + _kinds(issues, "weight_sum")
    assert all("P" not in i.ids for i in weight_issues)


def test_weights_fixed_clears_issues() -> None:
    kpis = mini.build()
    kpis["EC1-4"].weight = 0.5
    kpis["EC121"].weight = 0.5
    issues = validate(kpis)
    assert not _kinds(issues, "weight_missing")
    assert not any(i.ids == ["BADAGG"] for i in _kinds(issues, "weight_sum"))
