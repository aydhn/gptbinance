from .models import DeclaredStateRecord
from .registry import state_registry

def set_declared_state(state_id: str, declared_state: str, authority: str = "control-plane") -> DeclaredStateRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")
    record = DeclaredStateRecord(state_id=state_id, declared_state=declared_state, authority=authority)
    obj.declared = record
    return record
