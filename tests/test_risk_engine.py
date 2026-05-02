from datetime import datetime
from app.risk.engine import RiskEngine
from app.risk.models import (
    RiskConfig,
    RiskContext,
    DrawdownStateModel,
    ExposureSnapshot,
    RiskPolicy,
)
from app.risk.enums import RiskVerdict, ExposureScope
from app.risk.state import RiskStateManager
from app.backtest.models import SimulatedOrderIntent

from app.risk.models import RiskEvaluationRequest


def test_risk_engine_approve():
    config = RiskConfig()
    state_mgr = RiskStateManager()
    engine = RiskEngine(config, state_mgr)

    dd_model = DrawdownStateModel(last_updated=datetime.now())
    snap = ExposureSnapshot(timestamp=datetime.now(), total_equity=10000)
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

    bundle = engine.evaluate_intent(req)
    assert bundle.decision.verdict == RiskVerdict.APPROVE
    assert bundle.decision.approved_intent.quantity == 1.0


def test_risk_engine_reject():
    pass
