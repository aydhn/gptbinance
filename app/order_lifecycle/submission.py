from app.order_lifecycle.models import SubmitRequest, SubmitResult, OrderAttempt
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType


class SubmissionOrchestrator:
    def prepare_submit(
        self, attempt: OrderAttempt
    ) -> tuple[OrderAttempt, SubmitRequest]:
        # Move from CREATED to READY_TO_SUBMIT
        new_state, trn = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.READY_TO_SUBMIT,
            TransitionType.INITIALIZE,
        )
        attempt.state = new_state

        # Move to SUBMITTED_PENDING_ACK
        new_state2, trn2 = LifecycleStateMachine.transition(
            attempt.attempt_id,
            attempt.state,
            LifecycleState.SUBMITTED_PENDING_ACK,
            TransitionType.SUBMIT,
        )
        attempt.state = new_state2

        req = SubmitRequest(
            attempt_id=attempt.attempt_id,
            payload={"clientOrderId": attempt.lineage.client_order_id},
        )
        return attempt, req
