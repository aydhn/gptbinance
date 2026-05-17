from .models import ObservedStateRecord
from .registry import state_registry

def set_observed_state(state_id: str, observed_state: str, authority: str = "telemetry") -> ObservedStateRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")
    record = ObservedStateRecord(state_id=state_id, observed_state=observed_state, authority=authority)
    obj.observed = record
    return record
