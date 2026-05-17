from datetime import datetime, timezone, timedelta
from .models import StateObject
from .registry import state_registry

def now_utc():
    return datetime.now(timezone.utc)

def evaluate_freshness(state_id: str, max_age_seconds: int = 300) -> bool:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    if not obj.observed:
        return False

    age = now_utc() - obj.observed.timestamp
    return age <= timedelta(seconds=max_age_seconds)
