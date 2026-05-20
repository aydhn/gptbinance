from typing import Dict, Any
from .registry import registry
from .exceptions import InvalidAttribution

def get_attribution(outcome_id: str) -> Dict[str, Any]:
    obj = registry.get(outcome_id)
    if not obj: return {}
    attribution = obj.get("attribution", {})
    if not attribution:
        raise InvalidAttribution(f"Missing attribution for {outcome_id}")
    return attribution
