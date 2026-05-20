from typing import List, Dict, Any
from .registry import registry
from .exceptions import CustodyViolation

def check_custody_gaps(obj_id: str) -> str:
    obj = registry.get(obj_id)
    if not obj: return 'UNKNOWN'
    if obj.get("custody_gap", False) is True:
        raise CustodyViolation(f"Critical custody gap found in {obj_id}")
    return 'LOW'
