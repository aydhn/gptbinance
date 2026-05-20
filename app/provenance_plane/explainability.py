from typing import Dict, Any
from .registry import registry
from .exceptions import InvalidExplainabilityRecord

def check_explainability(obj_id: str) -> bool:
    obj = registry.get(obj_id)
    if not obj: return False
    if not obj.get("explanation"):
        raise InvalidExplainabilityRecord(f"Non-defensible explanation for {obj_id}")
    return True
