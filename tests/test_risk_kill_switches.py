from datetime import datetime
from app.risk.kill_switches import KillSwitchEvaluator
from app.risk.models import (
    RiskConfig,
    RiskContext,
    DrawdownStateModel,
    ExposureSnapshot,
)
from app.risk.enums import DrawdownState, KillSwitchType


def test_kill_switch_drawdown():
    config = RiskConfig()
    evaluator = KillSwitchEvaluator(config)

    dd_model = DrawdownStateModel(
        current_state=DrawdownState.HARD_STOP,
        drawdown_pct=25.0,
        last_updated=datetime.now(),
    )
    snap = ExposureSnapshot(
        timestamp=datetime.now(), total_equity=10000, total_gross_exposure=5000
    )
    ctx = RiskContext(
        timestamp=datetime.now(), drawdown_state=dd_model, exposure_snapshot=snap
    )

    state = evaluator.evaluate(ctx, datetime.now())

    assert state.is_active is True
    assert KillSwitchType.DRAWDOWN_BREACH in state.active_triggers


def test_kill_switch_exposure():
    config = RiskConfig()
    evaluator = KillSwitchEvaluator(config)

    dd_model = DrawdownStateModel(last_updated=datetime.now())
    snap = ExposureSnapshot(
        timestamp=datetime.now(), total_equity=10000, total_gross_exposure=60000
    )
    ctx = RiskContext(
        timestamp=datetime.now(), drawdown_state=dd_model, exposure_snapshot=snap
    )

    state = evaluator.evaluate(ctx, datetime.now())

    assert state.is_active is True
    assert KillSwitchType.EXPOSURE_EXPLOSION in state.active_triggers
