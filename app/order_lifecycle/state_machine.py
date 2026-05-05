from typing import List
from datetime import datetime, timezone
from app.order_lifecycle.enums import LifecycleState, TransitionType
from app.order_lifecycle.models import OrderLifecycleState, LifecycleTransition
from app.order_lifecycle.exceptions import InvalidLifecycleTransitionError


class LifecycleStateMachine:
    ALLOWED_TRANSITIONS = {
        LifecycleState.CREATED: [LifecycleState.READY_TO_SUBMIT],
        LifecycleState.READY_TO_SUBMIT: [LifecycleState.SUBMITTED_PENDING_ACK],
        LifecycleState.SUBMITTED_PENDING_ACK: [
            LifecycleState.ACKNOWLEDGED_OPEN,
            LifecycleState.REJECTED,
            LifecycleState.TIMEOUT_UNKNOWN,
        ],
        LifecycleState.ACKNOWLEDGED_OPEN: [
            LifecycleState.PARTIALLY_FILLED,
            LifecycleState.FULLY_FILLED,
            LifecycleState.CANCEL_REQUESTED,
            LifecycleState.REPLACE_REQUESTED,
        ],
        LifecycleState.PARTIALLY_FILLED: [
            LifecycleState.FULLY_FILLED,
            LifecycleState.CANCEL_REQUESTED,
            LifecycleState.TIMEOUT_UNKNOWN,
        ],
        LifecycleState.CANCEL_REQUESTED: [
            LifecycleState.CANCELLED,
            LifecycleState.TIMEOUT_UNKNOWN,
            LifecycleState.PARTIALLY_FILLED,
        ],
        LifecycleState.REPLACE_REQUESTED: [
            LifecycleState.REPLACED,
            LifecycleState.TIMEOUT_UNKNOWN,
            LifecycleState.REJECTED,
        ],
    }

    TERMINAL_STATES = {
        LifecycleState.FULLY_FILLED,
        LifecycleState.CANCELLED,
        LifecycleState.REJECTED,
        LifecycleState.ORPHANED,
        LifecycleState.DEAD_LETTERED,
    }

    @classmethod
    def transition(
        cls,
        attempt_id: str,
        current_state: OrderLifecycleState,
        to_state: LifecycleState,
        transition_type: TransitionType,
        explanation: str = "",
    ) -> tuple[OrderLifecycleState, LifecycleTransition]:
        if current_state.terminal:
            raise InvalidLifecycleTransitionError(
                f"Cannot transition from terminal state {current_state.current_state}"
            )

        allowed_next = cls.ALLOWED_TRANSITIONS.get(current_state.current_state, [])
        if (
            to_state not in allowed_next
            and current_state.current_state != LifecycleState.TIMEOUT_UNKNOWN
        ):
            raise InvalidLifecycleTransitionError(
                f"Invalid transition {current_state.current_state} -> {to_state}"
            )

        now = datetime.now(timezone.utc)

        new_state = OrderLifecycleState(
            current_state=to_state,
            last_updated=now,
            terminal=to_state in cls.TERMINAL_STATES,
            unresolved=to_state == LifecycleState.TIMEOUT_UNKNOWN,
        )

        transition = LifecycleTransition(
            transition_id=f"trn_{attempt_id}_{now.timestamp()}",
            attempt_id=attempt_id,
            from_state=current_state.current_state,
            to_state=to_state,
            transition_type=transition_type,
            timestamp=now,
            explanation=explanation,
        )

        return new_state, transition
