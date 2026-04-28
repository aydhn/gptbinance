import pytest
from unittest.mock import Mock
from app.backtest.validation.benchmarks import (
    FlatBaselineStrategy,
    BuyAndHoldBaselineStrategy,
)
from app.strategies.base import BaseStrategy


def test_flat_baseline():
    strat = FlatBaselineStrategy(spec=Mock())

    strat.broker = Mock()
    strat.on_kline({"close": 100})
    # Should do nothing
    assert True


def test_buy_and_hold():
    strat = BuyAndHoldBaselineStrategy(spec=Mock())
    strat.symbol = "BTCUSDT"

    strat.broker = Mock()
    strat.on_kline({"close": 100})
    assert strat.has_bought is True
