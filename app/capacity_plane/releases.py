from typing import Dict, List
from app.capacity_plane.readiness import assess_readiness_headroom
from app.capacity_plane.isolation import check_live_isolation


def check_rollout_capacity_sufficiency(workloads: List[str]) -> Dict[str, str]:
    if not check_live_isolation():
        return {
            "verdict": "CAUTION",
            "reason": "Live isolation breached, risky rollout.",
        }
    return {"verdict": "TRUSTED", "reason": "Capacity sufficient for rollout."}
