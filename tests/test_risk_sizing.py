from datetime import datetime
from app.risk.sizing import StandardPositionSizer
from app.risk.models import (
    RiskConfig,
    RiskEvaluationRequest,
    RiskContext,
    ExposureSnapshot,
    DrawdownStateModel,
)
from app.risk.enums import RegimeRiskMode
from app.backtest.models import SimulatedOrderIntent


def test_standard_sizing_normal():
    config = RiskConfig(default_risk_fraction=0.02)
    sizer = StandardPositionSizer(config)

    snap = ExposureSnapshot(timestamp=datetime.now(), total_equity=10000)
    ctx = RiskContext(
        timestamp=datetime.now(),
        drawdown_state=DrawdownStateModel(last_updated=datetime.now()),
        exposure_snapshot=snap,
        regime_mode=RegimeRiskMode.NORMAL,
        volatility_multiplier=1.0,
    )
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=1,
        quantity=1.0,
        intent_source="test",
    )
    req = RiskEvaluationRequest(intent=intent, context=ctx, available_capital=10000)

    res = sizer.calculate_size(req)
    assert res.approved_size == 1.0


def test_standard_sizing_caution():
    config = RiskConfig(default_risk_fraction=0.02)
    sizer = StandardPositionSizer(config)

    snap = ExposureSnapshot(timestamp=datetime.now(), total_equity=10000)
    ctx = RiskContext(
        timestamp=datetime.now(),
        drawdown_state=DrawdownStateModel(last_updated=datetime.now()),
        exposure_snapshot=snap,
        regime_mode=RegimeRiskMode.CAUTION,
        volatility_multiplier=1.0,
    )
    intent = SimulatedOrderIntent(
        timestamp=datetime.now(),
        symbol="BTC",
        side=1,
        quantity=1.0,
        intent_source="test",
    )
    req = RiskEvaluationRequest(intent=intent, context=ctx, available_capital=10000)

    res = sizer.calculate_size(req)
    assert res.approved_size == 0.5
