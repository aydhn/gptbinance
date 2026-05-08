from typing import List
from app.allocation.models import AllocationCandidate


class ScenarioEngine:
    def stress_test(self, candidates: List[AllocationCandidate]) -> List[str]:
        # Return scenario warnings if any
        return []
