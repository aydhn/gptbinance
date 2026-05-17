from .models import SplitBrainRecord
from .registry import state_registry

def detect_split_brain(state_id: str) -> SplitBrainRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    observed = obj.observed.observed_state if obj.observed else None
    declared = obj.declared.declared_state if obj.declared else None

    if observed and declared and observed != declared:
        record = SplitBrainRecord(
            state_id=state_id,
            observed_state=observed,
            declared_state=declared,
            severity="high"
        )
        obj.split_brain = record
        return record
    return None
