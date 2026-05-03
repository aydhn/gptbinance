from app.perf.workloads import WorkloadRegistry
from app.perf.enums import WorkloadType, ProfileScope


def test_workload_registry():
    w = WorkloadRegistry.get(WorkloadType.PAPER_RUNTIME_CYCLE)
    assert w is not None
    assert w.measurement_scope == ProfileScope.END_TO_END
    assert "paper" in w.safe_modes
