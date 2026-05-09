from app.workflow_plane.states import RunStateMachine
from app.workflow_plane.enums import RunState

def test_state_machine():
    sm = RunStateMachine()
    assert sm.can_transition(RunState.QUEUED, RunState.READY) is True
    assert sm.can_transition(RunState.COMPLETED, RunState.RUNNING) is False
