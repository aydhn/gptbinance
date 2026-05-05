from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType
from app.order_lifecycle.models import OrderLifecycleState
from datetime import datetime, timezone
import pytest
from app.order_lifecycle.exceptions import InvalidLifecycleTransitionError


def test_valid_transition():
    state = OrderLifecycleState(
        current_state=LifecycleState.CREATED, last_updated=datetime.now(timezone.utc)
    )
    new_state, trn = LifecycleStateMachine.transition(
        "att_1", state, LifecycleState.READY_TO_SUBMIT, TransitionType.INITIALIZE
    )
    assert new_state.current_state == LifecycleState.READY_TO_SUBMIT


def test_invalid_transition():
    state = OrderLifecycleState(
        current_state=LifecycleState.CREATED, last_updated=datetime.now(timezone.utc)
    )
    with pytest.raises(InvalidLifecycleTransitionError):
        LifecycleStateMachine.transition(
            "att_1", state, LifecycleState.FULLY_FILLED, TransitionType.FULL_FILL
        )
