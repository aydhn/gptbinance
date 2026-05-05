from app.order_lifecycle.fills import FillProcessor
from app.order_lifecycle.attempts import AttemptManager
from app.order_lifecycle.submission import SubmissionOrchestrator
from app.order_lifecycle.models import FullFill
from datetime import datetime, timezone
from app.order_lifecycle.state_machine import LifecycleStateMachine
from app.order_lifecycle.enums import LifecycleState, TransitionType


def test_fill_processor():
    mgr = AttemptManager()
    att = mgr.create_attempt("plan1", "leg1", "int1", {})
    orch = SubmissionOrchestrator()
    att, _ = orch.prepare_submit(att)

    # Simulate Ack
    att.state, _ = LifecycleStateMachine.transition(
        att.attempt_id, att.state, LifecycleState.ACKNOWLEDGED_OPEN, TransitionType.ACK
    )

    proc = FillProcessor()
    fill = FullFill(
        attempt_id=att.attempt_id,
        fill_id="f1",
        price=100.0,
        quantity=1.0,
        timestamp=datetime.now(timezone.utc),
    )
    att = proc.process_full(att, fill)

    assert att.state.current_state.value == "FULLY_FILLED"
