from typing import List, Dict, Optional
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate, PortfolioExposureSnapshot
from app.allocation.enums import ConstraintClass


class AllocationConstraint(BaseModel):
    constraint_id: str
    constraint_class: ConstraintClass
    limit_value: float
    is_hard_block: bool


class ConstraintRegistry:
    def __init__(self):
        self._constraints: Dict[str, AllocationConstraint] = {}
        self._init_defaults()

    def _init_defaults(self):
        self.register(
            AllocationConstraint(
                constraint_id="global_max_gross",
                constraint_class=ConstraintClass.MAX_GROSS,
                limit_value=200000.0,
                is_hard_block=True,
            )
        )
        self.register(
            AllocationConstraint(
                constraint_id="global_max_net",
                constraint_class=ConstraintClass.MAX_NET,
                limit_value=100000.0,
                is_hard_block=True,
            )
        )

    def register(self, constraint: AllocationConstraint):
        self._constraints[constraint.constraint_id] = constraint

    def list_all(self) -> List[AllocationConstraint]:
        return list(self._constraints.values())


class ConstraintEvaluator:
    def __init__(self, registry: ConstraintRegistry):
        self.registry = registry

    def evaluate(
        self, candidate: AllocationCandidate, snapshot: PortfolioExposureSnapshot
    ) -> List[str]:
        clip_reasons = []
        for c in self.registry.list_all():
            if c.constraint_class == ConstraintClass.MAX_GROSS:
                if (
                    snapshot.gross_notional + candidate.requested_notional
                    > c.limit_value
                ):
                    clip_reasons.append(f"constraint_violation_{c.constraint_id}")
            # Simplified for other constraints...
        return clip_reasons
