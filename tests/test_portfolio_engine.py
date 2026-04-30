import pytest
from datetime import datetime, timezone
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioContext,
    PortfolioConfig,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    PortfolioIntentBatch,
)
from app.portfolio.engine import PortfolioEngine


class DummyIntent:
    def __init__(self, sym, qty):
        self.symbol = sym
        self.side = OrderSide.BUY
        self.quantity = qty
        self.intent_id = sym


def test_engine():
    config = PortfolioConfig(total_budget=1000.0)
    engine = PortfolioEngine(config)

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

    intent1 = DummyIntent("BTCUSDT", 1.0)
    intent2 = DummyIntent("ETHUSDT", 1.0)

    batch = PortfolioIntentBatch(
        timestamp=timestamp, run_id="run1", risk_approved_intents=[intent1, intent2]
    )

    decision_batch = engine.process_intents(batch, context)

    assert len(decision_batch.decisions) == 2
