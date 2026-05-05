from app.order_lifecycle.models import OrderAttempt, PartialFill, FullFill
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType


class FillProcessor:
    def __init__(self):
        self.fills = []

    def process_partial(self, attempt: OrderAttempt, fill: PartialFill) -> OrderAttempt:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.PARTIALLY_FILLED,
            TransitionType.PARTIAL_FILL,
        )
        attempt.state = new_state
        self.fills.append(fill)
        return attempt

    def process_full(self, attempt: OrderAttempt, fill: FullFill) -> OrderAttempt:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.FULLY_FILLED,
            TransitionType.FULL_FILL,
        )
        attempt.state = new_state
        self.fills.append(fill)
        return attempt
