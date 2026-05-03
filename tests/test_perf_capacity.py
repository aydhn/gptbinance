from app.perf.capacity import CapacityAnalyzer
from app.perf.enums import HostClass, WorkloadType


def test_capacity_analyzer():
    report = CapacityAnalyzer.evaluate(
        HostClass.LOCAL_MINIMAL,
        [
            WorkloadType.PAPER_RUNTIME_CYCLE,
            WorkloadType.ANALYTICS_BATCH,
            WorkloadType.TESTNET_EXECUTION_SMOKE,
        ],
    )
    assert report.host_class == HostClass.LOCAL_MINIMAL
    assert len(report.unsupported_combinations) > 0
