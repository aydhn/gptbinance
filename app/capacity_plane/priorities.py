from pydantic import BaseModel, Field
from typing import Dict, Any, List
from app.capacity_plane.enums import PriorityClass


class PriorityPolicy(BaseModel):
    priority_class: PriorityClass
    description: str
    preemption_allowed: bool
    starvation_warning_threshold_sec: float
    metadata: Dict[str, Any] = Field(default_factory=dict)


_priorities: Dict[PriorityClass, PriorityPolicy] = {}


def define_priority_policy(
    priority_class: PriorityClass,
    description: str,
    preemption_allowed: bool,
    starvation_warning_threshold_sec: float,
    metadata: dict = None,
) -> PriorityPolicy:
    p = PriorityPolicy(
        priority_class=priority_class,
        description=description,
        preemption_allowed=preemption_allowed,
        starvation_warning_threshold_sec=starvation_warning_threshold_sec,
        metadata=metadata or {},
    )
    _priorities[priority_class] = p
    return p


def get_priority_policy(priority_class: PriorityClass) -> PriorityPolicy:
    return _priorities.get(priority_class)


def list_priority_policies() -> list[PriorityPolicy]:
    return list(_priorities.values())


# Setup basic priority policies without hidden overrides
define_priority_policy(
    PriorityClass.EMERGENCY_OVERRIDE, "Emergency actions only (break-glass)", False, 0.0
)
define_priority_policy(
    PriorityClass.CRITICAL, "Critical path operations (live execution)", False, 5.0
)
define_priority_policy(PriorityClass.HIGH, "Important synchronous actions", True, 30.0)
define_priority_policy(PriorityClass.NORMAL, "Standard operations", True, 60.0)
define_priority_policy(PriorityClass.BEST_EFFORT, "Best effort, droppable", True, 300.0)
