from app.order_lifecycle.timeouts import TimeoutManager
from app.order_lifecycle.attempts import AttemptManager
from app.order_lifecycle.submission import SubmissionOrchestrator
from app.order_lifecycle.enums import TimeoutClass


def test_timeout():
    mgr = AttemptManager()
    att = mgr.create_attempt("plan1", "leg1", "int1", {})
    orch = SubmissionOrchestrator()
    att, _ = orch.prepare_submit(att)

    tm = TimeoutManager()
    att, res = tm.mark_timeout_unknown(att, TimeoutClass.PENDING_ACK_TIMEOUT)
    assert att.state.current_state.value == "TIMEOUT_UNKNOWN"
    assert att.state.unresolved is True
