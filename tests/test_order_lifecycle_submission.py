from app.order_lifecycle.submission import SubmissionOrchestrator
from app.order_lifecycle.attempts import AttemptManager


def test_submission_orchestrator():
    mgr = AttemptManager()
    att = mgr.create_attempt("plan1", "leg1", "int1", {})
    orch = SubmissionOrchestrator()
    att, req = orch.prepare_submit(att)
    assert req is not None
    assert att.state.current_state.value == "SUBMITTED_PENDING_ACK"
