from typing import Dict
from app.capacity_plane.models import CapacityResource
from app.capacity_plane.registry import capacity_registry


def assess_readiness_headroom(resource_id: str) -> Dict[str, str]:
    res = capacity_registry.get_resource(resource_id)
    if not res:
        return {"status": "BLOCKED", "reason": "Resource not found in registry."}

    # Simulating headroom check
    return {
        "status": "READY",
        "reason": "Sufficient headroom observed.",
        "total_capacity": str(res.total_capacity),
    }
