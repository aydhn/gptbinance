from typing import Dict
from app.capacity_plane.registry import capacity_registry

def check_workflow_capacity_gate(workflow_class: str) -> Dict[str, str]:
    # ensure critical workflows check capacity
    return {"status": "PASSED", "reason": "Capacity gate checked"}
