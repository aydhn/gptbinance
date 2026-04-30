import pytest
from datetime import datetime, timezone
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioDecision,
    AllocationSlice,
    PortfolioDecisionBatch,
)
from app.portfolio.enums import PortfolioVerdict
from app.portfolio.explain import ExplainabilityEngine


class DummyIntent:
    def __init__(self, sym):
        self.symbol = sym


def test_explain():
    engine = ExplainabilityEngine()

    intent = DummyIntent("BTCUSDT")
    alloc = AllocationSlice(
        intent_id="BTCUSDT",
        requested_notional=100.0,
        approved_notional=50.0,
        reduction_ratio=0.5,
    )

    decision = PortfolioDecision(
        intent_id="BTCUSDT",
        verdict=PortfolioVerdict.REDUCE,
        original_intent=intent,
        allocation=alloc,
        blocking_reasons=["Max symbol weight"],
        rationale="Ranked 1",
    )

    batch = PortfolioDecisionBatch(
        timestamp=datetime.now(timezone.utc), run_id="run1", decisions=[decision]
    )

    text = engine.explain_batch(batch)
    assert "Portfolio Decision Batch: run1" in text
    assert "Verdict: REDUCE" in text
    assert "Max symbol weight" in text
    assert "Ranked 1" in text
    assert "Approved:  50.00" in text
