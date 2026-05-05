import os

files = {
    "app/order_lifecycle/submission.py": """from app.order_lifecycle.models import SubmitRequest, SubmitResult, OrderAttempt
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType

class SubmissionOrchestrator:
    def prepare_submit(self, attempt: OrderAttempt) -> tuple[OrderAttempt, SubmitRequest]:
        # Move from CREATED to READY_TO_SUBMIT
        new_state, trn = LifecycleStateMachine.transition(
             attempt.attempt_id, attempt.state, LifecycleState.READY_TO_SUBMIT, TransitionType.INITIALIZE
        )
        attempt.state = new_state

        # Move to SUBMITTED_PENDING_ACK
        new_state2, trn2 = LifecycleStateMachine.transition(
             attempt.attempt_id, attempt.state, LifecycleState.SUBMITTED_PENDING_ACK, TransitionType.SUBMIT
        )
        attempt.state = new_state2

        req = SubmitRequest(
            attempt_id=attempt.attempt_id,
            payload={"clientOrderId": attempt.lineage.client_order_id}
        )
        return attempt, req
""",
    "app/order_lifecycle/events.py": """from app.order_lifecycle.models import VenueAck, VenueReject, PartialFill, FullFill

class VenueEventMapper:
    def map_ack(self, payload: dict) -> VenueAck:
        pass
    def map_reject(self, payload: dict) -> VenueReject:
        pass
""",
    "app/order_lifecycle/fills.py": """from app.order_lifecycle.models import OrderAttempt, PartialFill, FullFill
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType

class FillProcessor:
    def __init__(self):
        self.fills = []

    def process_partial(self, attempt: OrderAttempt, fill: PartialFill) -> OrderAttempt:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id, attempt.state, LifecycleState.PARTIALLY_FILLED, TransitionType.PARTIAL_FILL
        )
        attempt.state = new_state
        self.fills.append(fill)
        return attempt

    def process_full(self, attempt: OrderAttempt, fill: FullFill) -> OrderAttempt:
        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id, attempt.state, LifecycleState.FULLY_FILLED, TransitionType.FULL_FILL
        )
        attempt.state = new_state
        self.fills.append(fill)
        return attempt
""",
    "app/order_lifecycle/cancel.py": """from app.order_lifecycle.models import OrderAttempt, CancelRequest, CancelResult
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, CancelVerdict

class CancelOrchestrator:
    def request_cancel(self, attempt: OrderAttempt, reason: str) -> tuple[OrderAttempt, CancelResult, CancelRequest]:
        if attempt.state.terminal:
            return attempt, CancelResult(attempt_id=attempt.attempt_id, success=False, verdict=CancelVerdict.FORBIDDEN_TERMINAL), None

        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id, attempt.state, LifecycleState.CANCEL_REQUESTED, TransitionType.REQUEST_CANCEL, reason
        )
        attempt.state = new_state
        req = CancelRequest(attempt_id=attempt.attempt_id, reason=reason)
        return attempt, CancelResult(attempt_id=attempt.attempt_id, success=True, verdict=CancelVerdict.ALLOWED), req
""",
    "app/order_lifecycle/replace.py": """from app.order_lifecycle.models import OrderAttempt, ReplaceRequest, ReplaceResult
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType, ReplaceVerdict
import uuid

class ReplaceOrchestrator:
    def request_replace(self, attempt: OrderAttempt, price: float=None, qty: float=None) -> tuple[OrderAttempt, ReplaceResult, ReplaceRequest]:
        if attempt.state.terminal:
             return attempt, ReplaceResult(success=False, verdict=ReplaceVerdict.FORBIDDEN_TERMINAL), None

        new_state, _ = LifecycleStateMachine.transition(
            attempt.attempt_id, attempt.state, LifecycleState.REPLACE_REQUESTED, TransitionType.REQUEST_REPLACE
        )
        attempt.state = new_state
        req = ReplaceRequest(
             old_attempt_id=attempt.attempt_id,
             new_attempt_id=f"att_{uuid.uuid4()}",
             price=price,
             quantity=qty
        )
        return attempt, ReplaceResult(success=True, verdict=ReplaceVerdict.ALLOWED), req
""",
}

for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
