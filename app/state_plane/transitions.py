from .models import TransitionRecord
from .registry import state_registry
from .exceptions import IllegalStateJumpError

def record_transition(state_id: str, from_state: str, to_state: str) -> TransitionRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    lifecycle = state_registry.get_lifecycle(obj.lifecycle_id)
    if lifecycle:
        if to_state not in lifecycle.states:
            raise IllegalStateJumpError(f"Target state {to_state} not in lifecycle {obj.lifecycle_id}")

    record = TransitionRecord(state_id=state_id, from_state=from_state, to_state=to_state)
    obj.transitions.append(record)
    return record
