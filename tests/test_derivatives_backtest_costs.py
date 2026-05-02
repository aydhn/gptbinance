import pytest
from app.backtest.derivatives.costs import BacktestCostSimulator
from app.backtest.derivatives.models import DerivativeBacktestConfig
from app.products.enums import ProductType


def test_backtest_costs():
    cfg = DerivativeBacktestConfig(
        product_type=ProductType.FUTURES_USDM,
        initial_margin=1000,
        hourly_funding_rate=0.01,
    )
    sim = BacktestCostSimulator(cfg)
    sim.simulate_funding(12345, "BTC", 10, 100)  # 1000 notional, 1% rate = 10 cost
    assert sim.funding_events[0].amount == -10.0
