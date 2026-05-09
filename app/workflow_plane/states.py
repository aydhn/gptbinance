from app.workflow_plane.enums import RunState

class RunStateMachine:
    VALID_TRANSITIONS = {
        RunState.QUEUED: [RunState.GATED_WAIT, RunState.READY, RunState.CANCELLED],
        RunState.GATED_WAIT: [RunState.READY, RunState.CANCELLED],
        RunState.READY: [RunState.RUNNING, RunState.CANCELLED],
        RunState.RUNNING: [RunState.PARTIALLY_COMPLETED, RunState.COMPLETED, RunState.FAILED, RunState.CANCELLED],
        RunState.PARTIALLY_COMPLETED: [RunState.RUNNING, RunState.COMPLETED, RunState.FAILED],
        RunState.FAILED: [RunState.RESUMED, RunState.RERUN_SUPERSEDED],
        RunState.RESUMED: [RunState.RUNNING, RunState.CANCELLED],
    }

    def can_transition(self, current_state: RunState, new_state: RunState) -> bool:
        return new_state in self.VALID_TRANSITIONS.get(current_state, [])
