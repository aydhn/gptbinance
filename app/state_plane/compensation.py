from .models import StateObject
from .registry import state_registry
from .transitions import record_transition

def initiate_compensation(state_id: str, compensation_state: str):
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    current_state = obj.transitions[-1].to_state if obj.transitions else "unknown"
    record_transition(state_id, current_state, compensation_state)
    return True
