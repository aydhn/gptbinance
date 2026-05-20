from typing import List, Dict, Any
from .registry import registry

def get_custody_chain(obj_id: str) -> List[Dict[str, Any]]:
    obj = registry.get(obj_id)
    if not obj: return []
    return obj.get("custody_chain", [{"step": "ingestion", "status": "VERIFIED"}])
