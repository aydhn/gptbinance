import pytest
from app.execution.live_runtime.start_gates import LiveStartGateEvaluator
from app.execution.live_runtime.models import LiveSessionConfig, LiveCapitalCaps
from app.execution.live_runtime.enums import LiveRolloutMode


def test_live_start_gate_evaluator():
    evaluator = LiveStartGateEvaluator()
    config = LiveSessionConfig(
        rollout_mode=LiveRolloutMode.CANARY_LIVE,
        capital_caps=LiveCapitalCaps(
            max_session_notional_usd=100,
            max_daily_loss_usd=10,
            max_live_exposure_usd=50,
            max_new_orders_per_session=5,
            allowlist=[],
        ),
    )

    # Test without arming
    context = {"mainnet_armed": False}
    report = evaluator.evaluate(config, context)
    assert not report.passed
    assert "Mainnet is not armed." in report.blockers[0]

    # Test with arming but no allowlist
    context = {
        "mainnet_armed": True,
        "ops_readiness_pass": True,
        "reconciliation_clean": True,
    }
    report = evaluator.evaluate(config, context)
    assert not report.passed
    assert "allowlist is empty" in report.blockers[0]
