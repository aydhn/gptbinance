import pytest
from datetime import datetime, timezone
from app.backtest.models import SimulatedOrderIntent
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioCandidate,
    PortfolioContext,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    OverlapReport,
)
from app.portfolio.ranking import SimpleRankingModel
from app.portfolio.enums import OverlapType


class DummyIntent:
    def __init__(self, s, sym):
        self.symbol = sym
        self.side = s
        self.quantity = 1.0
        self.metadata = {"risk_score": 90.0}
        self.intent_id = sym


def test_rank_candidates():
    model = SimpleRankingModel()

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

    intent1 = DummyIntent(OrderSide.BUY, "BTCUSDT")
    cand1 = PortfolioCandidate(
        intent=intent1
    )  # using duck typing if possible, else might fail pydantic type check

    intent2 = DummyIntent(OrderSide.BUY, "ETHUSDT")
    intent2.metadata = {"risk_score": 50.0}
    cand2 = PortfolioCandidate(intent=intent2)
    cand2.overlap_report = OverlapReport(
        intent_id="ETHUSDT",
        overlap_type=OverlapType.SAME_SYMBOL_SAME_DIR,
        overlap_severity_score=5.0,
    )

    ranked = model.rank_candidates([cand1, cand2], context)

    assert len(ranked) == 2
    assert ranked[0].intent.symbol == "BTCUSDT"
    assert ranked[1].intent.symbol == "ETHUSDT"
    assert ranked[0].rank.score == 190.0
    assert ranked[1].rank.score == 100.0
