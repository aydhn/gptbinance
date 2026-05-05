import pytest
from app.activation.plans import RolloutPlanner
from app.activation.models import ActivationIntent, ActivationScope
from app.activation.enums import ActivationClass, ActivationStage


def test_build_canary_plan():
    intent = ActivationIntent(
        intent_id="intent-1",
        activation_class=ActivationClass.CANARY_LIMITED,
        board_decision_ref="b-1",
        candidate_id="c-1",
        scope=ActivationScope(allowed_symbols=["BTCUSDT"]),
    )

    planner = RolloutPlanner()
    plan = planner.build_plan(intent)

    assert len(plan.steps) == 3
    assert plan.steps[0].stage == ActivationStage.PREFLIGHT
    assert plan.steps[1].stage == ActivationStage.STAGE_0_OBSERVE
    assert plan.steps[2].stage == ActivationStage.STAGE_1_LIMITED_SYMBOLS
