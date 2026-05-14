from pydantic import BaseModel, Field
from typing import Dict, Any
from app.capacity_plane.enums import WorkloadClass


class WorkloadDefinition(BaseModel):
    workload_class: WorkloadClass
    description: str
    isolation_requirements: list[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)


_workloads: Dict[WorkloadClass, WorkloadDefinition] = {}


def define_workload(
    workload_class: WorkloadClass,
    description: str,
    isolation_requirements: list[str],
    metadata: dict = None,
) -> WorkloadDefinition:
    w = WorkloadDefinition(
        workload_class=workload_class,
        description=description,
        isolation_requirements=isolation_requirements,
        metadata=metadata or {},
    )
    _workloads[workload_class] = w
    return w


def get_workload(workload_class: WorkloadClass) -> WorkloadDefinition:
    return _workloads.get(workload_class)


def list_workloads() -> list[WorkloadDefinition]:
    return list(_workloads.values())


# Pre-define some standard workloads
define_workload(
    WorkloadClass.LIVE_TRADING,
    "Live market execution and trading operations",
    ["Strict isolation from research/replay", "Dedicated queue lanes"],
)
define_workload(
    WorkloadClass.RESEARCH,
    "Offline research, backtesting, and model training",
    ["Low priority relative to live", "No live path access"],
)
