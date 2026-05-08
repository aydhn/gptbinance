from typing import List
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate


class CrowdingEngine:
    def evaluate(self, candidates: List[AllocationCandidate]) -> List[str]:
        # Simple burst detection simulation
        cluster_burden = len(candidates)
        if cluster_burden > 10:
            return ["crowding_burst_detected"]
        return []
