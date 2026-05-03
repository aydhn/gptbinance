import time
from app.perf.profilers import WorkloadProfiler
from app.perf.enums import WorkloadType, HostClass


def test_profiler():
    p = WorkloadProfiler(
        "run1", WorkloadType.PAPER_RUNTIME_CYCLE, HostClass.LOCAL_AVERAGE
    )
    p.start()
    with p.latency_tracker.measure("test"):
        time.sleep(0.01)
    p.sample_resources()
    p.stop()
    run = p.create_perf_run()
    assert run.duration_sec > 0
    assert len(run.latencies) == 1
    assert run.latencies[0].component_name == "test"
    assert run.cpu_summary is not None
