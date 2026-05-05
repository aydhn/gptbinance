from app.order_lifecycle.models import OrderAttempt, ReplaceRequest, ReplaceResult
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, ReplaceVerdict
import uuid


class ReplaceOrchestrator:
    def request_replace(
        self, attempt: OrderAttempt, price: float = None, qty: float = None
    ) -> tuple[OrderAttempt, ReplaceResult, ReplaceRequest]:
        if attempt.state.terminal:
            return (
                attempt,
                ReplaceResult(success=False, verdict=ReplaceVerdict.FORBIDDEN_TERMINAL),
                None,
            )

        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.REPLACE_REQUESTED,
            TransitionType.REQUEST_REPLACE,
        )
        attempt.state = new_state
        req = ReplaceRequest(
            old_attempt_id=attempt.attempt_id,
            new_attempt_id=f"att_{uuid.uuid4()}",
            price=price,
            quantity=qty,
        )
        return attempt, ReplaceResult(success=True, verdict=ReplaceVerdict.ALLOWED), req
