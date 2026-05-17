from .models import EffectiveStateRecord
from .registry import state_registry

def set_effective_state(state_id: str, effective_state: str) -> EffectiveStateRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")
    record = EffectiveStateRecord(state_id=state_id, effective_state=effective_state)
    obj.effective = record
    return record
