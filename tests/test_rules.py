from app.strategies.rules import (
    threshold_rule,
    crossover_rule,
    band_rule,
    slope_rule,
    all_of,
    any_of,
)


def test_threshold_rule():
    res = threshold_rule(10, 5, is_greater=True)
    assert res.passed

    res = threshold_rule(4, 5, is_greater=True)
    assert not res.passed


def test_crossover_rule():
    # Bullish cross
    res = crossover_rule(fast=10, slow=9, prev_fast=8, prev_slow=9)
    assert res.passed
    assert "Bullish" in res.reason

    # Bearish cross
    res = crossover_rule(fast=8, slow=9, prev_fast=10, prev_slow=9)
    assert res.passed
    assert "Bearish" in res.reason

    # No cross
    res = crossover_rule(fast=10, slow=9, prev_fast=9.5, prev_slow=8.5)
    assert not res.passed


def test_band_rule():
    res = band_rule(110, 100, 50)
    assert res.passed
    assert "Above" in res.reason

    res = band_rule(40, 100, 50)
    assert res.passed
    assert "Below" in res.reason

    res = band_rule(75, 100, 50)
    assert not res.passed


def test_slope_rule():
    res = slope_rule(10, 5, positive_required=True)
    assert res.passed

    res = slope_rule(5, 10, positive_required=True)
    assert not res.passed


def test_combinators():
    t1 = threshold_rule(10, 5)
    t2 = threshold_rule(4, 5)

    assert not all_of([t1, t2]).passed
    assert any_of([t1, t2]).passed
