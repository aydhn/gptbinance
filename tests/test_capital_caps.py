import pytest
from app.execution.live_runtime.capital_caps import CapitalCapEnforcer
from app.execution.live_runtime.models import (
    LiveCapitalCaps,
    LiveSymbolAllowance,
    LivePositionBook,
    LivePnlSnapshot,
)
from app.execution.live_runtime.enums import LiveRuntimeVerdict, CapitalCapType


def test_capital_cap_enforcer():
    caps = LiveCapitalCaps(
        max_session_notional_usd=5000.0,
        max_daily_loss_usd=500.0,
        max_live_exposure_usd=2000.0,
        max_new_orders_per_session=2,
        allowlist=[
            LiveSymbolAllowance(
                symbol="BTCUSDT", max_notional_usd=1000.0, max_orders=10
            )
        ],
    )
    enforcer = CapitalCapEnforcer(caps)
    pb = LivePositionBook()

    # Allowlist check
    intent = {"symbol": "ETHUSDT", "qty": 1.0, "price": 100.0}
    decision = enforcer.evaluate_intent(intent, pb)
    assert decision.verdict == LiveRuntimeVerdict.REJECT

    # Max symbol notional check
    intent = {"symbol": "BTCUSDT", "qty": 1.0, "price": 2000.0}
    decision = enforcer.evaluate_intent(intent, pb)
    assert decision.verdict == LiveRuntimeVerdict.REJECT

    # Valid intent
    intent = {"symbol": "BTCUSDT", "qty": 0.01, "price": 50000.0}
    decision = enforcer.evaluate_intent(intent, pb)
    assert decision.verdict == LiveRuntimeVerdict.PROCEED

    # Record submits to hit session count
    enforcer.record_submit(500.0)
    enforcer.record_submit(500.0)

    # Session orders exceeded
    decision = enforcer.evaluate_intent(intent, pb)
    assert decision.verdict == LiveRuntimeVerdict.REJECT
    assert decision.cap_type == CapitalCapType.MAX_NEW_ORDERS

    # Daily loss
    pnls = [
        LivePnlSnapshot(symbol="BTCUSDT", realized_pnl=-400.0, unrealized_pnl=-200.0)
    ]
    decision = enforcer.evaluate_loss(pnls)
    assert decision.verdict == LiveRuntimeVerdict.HALT
    assert decision.cap_type == CapitalCapType.MAX_DAILY_LOSS
