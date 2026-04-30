import pytest
from datetime import datetime, timezone
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioCandidate,
    PortfolioContext,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    PortfolioIntentBatch,
    OpportunityRank,
)
from app.portfolio.allocator import ConservativeAllocator
from app.portfolio.policies import PortfolioPolicyManager
from app.portfolio.budgets import BudgetManager
from app.portfolio.models import PortfolioConfig
from app.portfolio.enums import PortfolioVerdict


class DummyIntent:
    def __init__(self, sym, qty):
        self.symbol = sym
        self.side = OrderSide.BUY
        self.quantity = qty
        self.intent_id = sym


def test_allocator():
    config = PortfolioConfig(
        total_budget=1000.0, max_symbol_weight=0.20, reserve_cash_ratio=0.10
    )
    allocator = ConservativeAllocator(
        PortfolioPolicyManager(config), BudgetManager(config)
    )

    timestamp = datetime.now(timezone.utc)
    context = PortfolioContext(
        timestamp=timestamp,
        budget=PortfolioBudgetSnapshot(
            timestamp=timestamp,
            total_capital=1000.0,
            reserved_capital=100.0,
            available_capital=900.0,
            pending_allocations_notional=0.0,
        ),
        exposure=PortfolioExposureSnapshot(
            timestamp=timestamp, total_exposure=0, long_exposure=0, short_exposure=0
        ),
        correlation=CorrelationSnapshot(timestamp=timestamp),
        concentration=ConcentrationSnapshot(timestamp=timestamp),
    )

    cand1 = PortfolioCandidate(
        intent=DummyIntent("BTCUSDT", 1.5)
    )  # expects 150 notional
    cand1.rank = OpportunityRank(intent_id="BTCUSDT", score=100)

    cand2 = PortfolioCandidate(
        intent=DummyIntent("ETHUSDT", 2.5)
    )  # expects 250 notional
    cand2.rank = OpportunityRank(intent_id="ETHUSDT", score=90)

    batch = PortfolioIntentBatch(
        timestamp=timestamp, run_id="test", risk_approved_intents=[]
    )

    decisions_batch = allocator.allocate(batch, context, [cand1, cand2])

    assert len(decisions_batch.decisions) == 2

    # cand1 should be approved (150 <= 200 symbol limit)
    d1 = decisions_batch.decisions[0]
    assert d1.verdict == PortfolioVerdict.APPROVE
    assert d1.allocation.approved_notional == 150.0

    # cand2 should be rejected/reduced based on policy
    # Actually wait: 250 > 200 symbol limit
    d2 = decisions_batch.decisions[1]
    assert d2.verdict == PortfolioVerdict.REJECT
    assert len(d2.blocking_reasons) > 0
    assert "Max symbol weight exceeded" in d2.blocking_reasons[0]
