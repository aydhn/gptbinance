from app.order_lifecycle.cancel import CancelOrchestrator
from app.order_lifecycle.attempts import AttemptManager
from app.order_lifecycle.submission import SubmissionOrchestrator
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType


def test_cancel_orchestrator():
    mgr = AttemptManager()
    att = mgr.create_attempt("plan1", "leg1", "int1", {})
    orch = SubmissionOrchestrator()
    att, _ = orch.prepare_submit(att)
    att.state, _ = LifecycleStateMachine.transition(
        att.attempt_id, att.state, LifecycleState.ACKNOWLEDGED_OPEN, TransitionType.ACK
    )

    cancel_orch = CancelOrchestrator()
    att, res, req = cancel_orch.request_cancel(att, "user request")
    assert res.success is True
    assert att.state.current_state.value == "CANCEL_REQUESTED"
