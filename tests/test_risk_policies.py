from app.risk.enums import ExposureScope
from datetime import datetime
from app.risk.policies import MaxExposurePolicy
from app.risk.models import (
    RiskPolicy,
    RiskEvaluationRequest,
    RiskContext,
    ExposureSnapshot,
    DrawdownStateModel,
)
from app.backtest.models import SimulatedOrderIntent


def test_max_exposure_policy_pass():
    policy_def = RiskPolicy(
        name="max_gross", scope=ExposureScope.ACCOUNT, max_fraction=0.5
    )
    policy = MaxExposurePolicy(policy_def)

    snap = ExposureSnapshot(
        timestamp=datetime.now(), total_gross_exposure=400, total_equity=1000
    )
    ctx = RiskContext(
        timestamp=datetime.now(),
        drawdown_state=DrawdownStateModel(last_updated=datetime.now()),
        exposure_snapshot=snap,
    )
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=1,
        quantity=1,
        intent_source="test",
    )
    req = RiskEvaluationRequest(intent=intent, context=ctx, available_capital=1000)

    reason = policy.evaluate(req)
    assert reason is None


def test_max_exposure_policy_fail():
    policy_def = RiskPolicy(
        name="max_gross", scope=ExposureScope.ACCOUNT, max_fraction=0.5
    )
    policy = MaxExposurePolicy(policy_def)

    snap = ExposureSnapshot(
        timestamp=datetime.now(), total_gross_exposure=600, total_equity=1000
    )
    ctx = RiskContext(
        timestamp=datetime.now(),
        drawdown_state=DrawdownStateModel(last_updated=datetime.now()),
        exposure_snapshot=snap,
    )
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=1,
        quantity=1,
        intent_source="test",
    )
    req = RiskEvaluationRequest(intent=intent, context=ctx, available_capital=1000)

    reason = policy.evaluate(req)
    assert reason is not None
    assert reason.source == "max_gross"
