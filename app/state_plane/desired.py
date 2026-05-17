from .models import DesiredStateRecord
from .registry import state_registry

def set_desired_state(state_id: str, desired_state: str, authority: str = "operator") -> DesiredStateRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")
    record = DesiredStateRecord(state_id=state_id, desired_state=desired_state, authority=authority)
    obj.desired = record
    return record
