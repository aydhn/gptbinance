from datetime import datetime
from app.risk.guards import DrawdownGuard
from app.risk.models import (
    RiskEvaluationRequest,
    RiskContext,
    DrawdownStateModel,
    ExposureSnapshot,
)
from app.risk.enums import DrawdownState
from app.backtest.models import SimulatedOrderIntent


def test_drawdown_guard():
    guard = DrawdownGuard()

    dd_model = DrawdownStateModel(
        current_state=DrawdownState.HARD_STOP, last_updated=datetime.now()
    )
    snap = ExposureSnapshot(timestamp=datetime.now())
    ctx = RiskContext(
        timestamp=datetime.now(), drawdown_state=dd_model, exposure_snapshot=snap
    )
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=1,
        quantity=1.0,
        intent_source="test",
    )
    req = RiskEvaluationRequest(intent=intent, context=ctx, available_capital=10000)

    reason = guard.check(req)
    assert reason is not None
    assert "hard stop" in reason.rationale.lower()
