from app.order_lifecycle.models import OrderAttempt, TimeoutResolution
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, TimeoutClass
from datetime import datetime, timezone


class TimeoutManager:
    def mark_timeout_unknown(
        self, attempt: OrderAttempt, tclass: TimeoutClass
    ) -> tuple[OrderAttempt, TimeoutResolution]:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.TIMEOUT_UNKNOWN,
            TransitionType.MARK_TIMEOUT,
        )
        attempt.state = new_state
        res = TimeoutResolution(
            attempt_id=attempt.attempt_id,
            timeout_class=tclass,
            resolved_state=LifecycleState.TIMEOUT_UNKNOWN,
            timestamp=datetime.now(timezone.utc),
        )
        return attempt, res
