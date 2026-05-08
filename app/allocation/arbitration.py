from typing import List, Dict
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate
from app.allocation.sleeves import SleeveRegistry


class ArbitrationEngine:
    def __init__(self, sleeve_registry: SleeveRegistry):
        self.sleeve_registry = sleeve_registry

    def arbitrate(
        self, candidates: List[AllocationCandidate]
    ) -> List[AllocationCandidate]:
        """
        Sorts candidates by sleeve conflict priority, then by confidence.
        Same-symbol conflicts can be resolved here.
        For now, simply sorts them to give precedence during allocation.
        """

        def get_priority(cand: AllocationCandidate):
            sleeve = self.sleeve_registry.get_sleeve(cand.sleeve_ref)
            return (sleeve.conflict_priority, cand.confidence)

        return sorted(candidates, key=get_priority, reverse=True)
