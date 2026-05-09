from app.experiment_plane.models import ExposureAllocationPlan
from typing import Dict


def build_standard_split(
    plan_id: str, splits: Dict[str, float]
) -> ExposureAllocationPlan:
    if sum(splits.values()) != 1.0:
        raise ValueError("Splits must sum to 1.0")
    return ExposureAllocationPlan(plan_id=plan_id, split_ratios=splits)
