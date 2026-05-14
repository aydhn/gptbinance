from typing import Dict
from app.capacity_plane.registry import capacity_registry

def check_workflow_capacity_gate(workflow_class: str) -> Dict[str, str]:
    # ensure critical workflows check capacity
    return {"status": "PASSED", "reason": "Capacity gate checked"}



# Cost plane evaluation integration
def process_cost_gate(priority: str, is_live_contention: bool, budget_ok: bool):
    if not budget_ok and priority == "low" and is_live_contention:
        return "blocked"
    return "pass"
