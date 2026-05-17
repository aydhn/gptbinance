from .models import ReconciledStateRecord
from .registry import state_registry

def reconcile_state(state_id: str) -> ReconciledStateRecord:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    # Simple reconciliation logic
    effective = obj.effective.effective_state if obj.effective else None
    desired = obj.desired.desired_state if obj.desired else None

    is_converged = bool(effective and desired and effective == desired)
    reconciled_state = effective if effective else "unknown"

    record = ReconciledStateRecord(
        state_id=state_id,
        reconciled_state=reconciled_state,
        is_converged=is_converged
    )
    obj.reconciled = record
    return record
