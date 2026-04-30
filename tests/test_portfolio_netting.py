import pytest
from datetime import datetime, timezone
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioCandidate,
    PortfolioContext,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    CorrelationSnapshot,
    ConcentrationSnapshot,
)
from app.portfolio.netting import NettingEstimator


class DummyIntent:
    def __init__(self, side, qty):
        self.side = side
        self.quantity = qty


def test_netting():
    estimator = NettingEstimator()

    timestamp = datetime.now(timezone.utc)
    context = PortfolioContext(
        timestamp=timestamp,
        budget=PortfolioBudgetSnapshot(
            timestamp=timestamp,
            total_capital=1000.0,
            reserved_capital=0,
            available_capital=1000.0,
            pending_allocations_notional=0.0,
        ),
        exposure=PortfolioExposureSnapshot(
            timestamp=timestamp, total_exposure=0, long_exposure=0, short_exposure=0
        ),
        correlation=CorrelationSnapshot(timestamp=timestamp),
        concentration=ConcentrationSnapshot(timestamp=timestamp),
    )

    cand1 = PortfolioCandidate(intent=DummyIntent(OrderSide.BUY, 1.0))
    cand2 = PortfolioCandidate(intent=DummyIntent(OrderSide.SELL, 0.5))

    res = estimator.evaluate_net_exposure([cand1, cand2], context)

    # +100 - 50 = +50
    assert res["net_impact_notional"] == 50.0
