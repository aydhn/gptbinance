from app.perf.regression import RegressionEvaluator
from app.perf.models import (
    PerfRun,
    CpuProfileSummary,
    MemoryProfileSummary,
    DiskProfileSummary,
    NetworkProfileSummary,
)
from app.perf.enums import WorkloadType, HostClass, PerfVerdict
from datetime import datetime, timezone


def test_regression_evaluator():
    def create_run(cpu: float):
        return PerfRun(
            run_id="run1",
            workload_type=WorkloadType.STRATEGY_EVAL,
            host_class=HostClass.LOCAL_AVERAGE,
            start_time=datetime.now(timezone.utc),
            end_time=datetime.now(timezone.utc),
            duration_sec=10.0,
            cpu_summary=CpuProfileSummary(
                peak_cpu_percent=cpu, avg_cpu_percent=cpu, top_components={}
            ),
            memory_summary=MemoryProfileSummary(
                peak_memory_mb=100.0, memory_growth_mb=0.0, leak_suspicion=False
            ),
            disk_summary=DiskProfileSummary(
                total_read_mb=0.0, total_write_mb=0.0, peak_iops=0.0
            ),
            network_summary=NetworkProfileSummary(total_rx_kb=0.0, total_tx_kb=0.0),
            latencies=[],
            verdict=PerfVerdict.PASS,
        )

    b = create_run(10.0)
    t = create_run(20.0)  # 100% increase
    report = RegressionEvaluator.evaluate(b, t)
    assert report.severity.value in ["CRITICAL", "MAJOR"]
