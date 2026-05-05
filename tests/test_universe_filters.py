import pytest
from app.universe.filters import FilterEvaluator
from app.universe.models import ExchangeFilterSet, TickSizeRule, StepSizeRule


def test_validate_price_valid():
    filters = ExchangeFilterSet(
        tick_size=TickSizeRule(tick_size=0.01, min_price=0.01, max_price=10000.0)
    )
    assert FilterEvaluator.validate_price(100.05, filters) is True


def test_validate_price_invalid_tick():
    filters = ExchangeFilterSet(
        tick_size=TickSizeRule(tick_size=0.01, min_price=0.01, max_price=10000.0)
    )
    assert FilterEvaluator.validate_price(100.055, filters) is False


def test_round_price_down():
    filters = ExchangeFilterSet(
        tick_size=TickSizeRule(tick_size=0.01, min_price=0.01, max_price=10000.0)
    )
    assert FilterEvaluator.round_price_down(100.059, filters) == 100.05
