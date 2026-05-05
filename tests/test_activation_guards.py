import pytest
from app.activation.guards import ActivationGuards
from app.activation.models import ActivationIntent, ActivationScope
from app.activation.enums import ActivationClass
from app.activation.exceptions import ActivationPolicyViolation


def test_guards_block_no_board_ref():
    intent = ActivationIntent(
        intent_id="i-1",
        activation_class=ActivationClass.CANARY_LIMITED,
        board_decision_ref="",
        candidate_id="c-1",
        scope=ActivationScope(),
    )
    with pytest.raises(ActivationPolicyViolation):
        ActivationGuards.verify_pre_activation(intent, {})


def test_guards_block_capital_freeze():
    intent = ActivationIntent(
        intent_id="i-1",
        activation_class=ActivationClass.CANARY_LIMITED,
        board_decision_ref="b-1",
        candidate_id="c-1",
        scope=ActivationScope(),
    )
    with pytest.raises(ActivationPolicyViolation):
        ActivationGuards.verify_pre_activation(intent, {"capital_freeze_active": True})
