from datetime import datetime, timezone, timedelta
from typing import List, Dict
from .models import StateObject
from .registry import state_registry

def now_utc():
    return datetime.now(timezone.utc)

def find_stuck_states(timeout_seconds: int = 3600) -> List[Dict[str, str]]:
    stuck = []
    now = now_utc()
    for obj in state_registry.get_all_objects():
        # A simple heuristic: if it hasn't transitioned in a while and is not terminal
        if not obj.transitions:
            continue

        last_transition = obj.transitions[-1]
        age = now - last_transition.timestamp

        lc = state_registry.get_lifecycle(obj.lifecycle_id)
        if lc and last_transition.to_state not in lc.terminal_states:
            if age > timedelta(seconds=timeout_seconds):
                stuck.append({
                    "state_id": obj.state_id,
                    "current_state": last_transition.to_state,
                    "age_seconds": age.total_seconds()
                })
    return stuck
