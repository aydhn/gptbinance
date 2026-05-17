from typing import List, Dict, Any
from .models import StateObject
from .registry import state_registry

def get_state_history(state_id: str) -> List[Dict[str, Any]]:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    history = []
    for t in obj.transitions:
        history.append({
            "transition_id": t.transition_id,
            "from_state": t.from_state,
            "to_state": t.to_state,
            "timestamp": t.timestamp.isoformat()
        })
    return history
