from app.order_lifecycle.models import OrderAttempt, CancelRequest, CancelResult
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, CancelVerdict


class CancelOrchestrator:
    def request_cancel(
        self, attempt: OrderAttempt, reason: str
    ) -> tuple[OrderAttempt, CancelResult, CancelRequest]:
        if attempt.state.terminal:
            return (
                attempt,
                CancelResult(
                    attempt_id=attempt.attempt_id,
                    success=False,
                    verdict=CancelVerdict.FORBIDDEN_TERMINAL,
                ),
                None,
            )

        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.CANCEL_REQUESTED,
            TransitionType.REQUEST_CANCEL,
            reason,
        )
        attempt.state = new_state
        req = CancelRequest(attempt_id=attempt.attempt_id, reason=reason)
        return (
            attempt,
            CancelResult(
                attempt_id=attempt.attempt_id,
                success=True,
                verdict=CancelVerdict.ALLOWED,
            ),
            req,
        )
