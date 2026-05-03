import time
from typing import Dict, Any, Optional
from app.perf.base import ProfilerBase
from app.perf.resources import ResourceMonitor
from app.perf.latency import LatencyTracker
from app.perf.models import (
    PerfRun,
    CpuProfileSummary,
    MemoryProfileSummary,
    DiskProfileSummary,
    NetworkProfileSummary,
    PerfVerdict,
)
from app.perf.enums import WorkloadType, HostClass


class WorkloadProfiler(ProfilerBase):
    def __init__(self, run_id: str, workload_type: WorkloadType, host_class: HostClass):
        self.run_id = run_id
        self.workload_type = workload_type
        self.host_class = host_class
        self.resource_monitor = ResourceMonitor()
        self.latency_tracker = LatencyTracker()
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.start_dt: Optional[Any] = None
        self.end_dt: Optional[Any] = None

    def start(self) -> None:
        from datetime import datetime, timezone

        self.start_dt = datetime.now(timezone.utc)
        self.start_time = time.perf_counter()
        self.resource_monitor.start()

    def stop(self) -> None:
        self.resource_monitor.stop()
        self.end_time = time.perf_counter()
        from datetime import datetime, timezone

        self.end_dt = datetime.now(timezone.utc)

    def sample_resources(self) -> None:
        self.resource_monitor.sample()

    def get_summary(self) -> Dict[str, Any]:
        duration = (
            self.end_time - self.start_time
            if self.start_time and self.end_time
            else 0.0
        )
        return {
            "duration_sec": duration,
            "cpu": self.resource_monitor.get_cpu_summary(),
            "memory": self.resource_monitor.get_memory_summary(),
            "disk": self.resource_monitor.get_disk_summary(),
            "network": self.resource_monitor.get_network_summary(),
            "latencies": self.latency_tracker.get_summaries(),
        }

    def create_perf_run(self) -> PerfRun:
        summary = self.get_summary()
        return PerfRun(
            run_id=self.run_id,
            workload_type=self.workload_type,
            host_class=self.host_class,
            start_time=self.start_dt,  # type: ignore
            end_time=self.end_dt,  # type: ignore
            duration_sec=summary["duration_sec"],
            cpu_summary=summary["cpu"],
            memory_summary=summary["memory"],
            disk_summary=summary["disk"],
            network_summary=summary["network"],
            latencies=summary["latencies"],
            verdict=PerfVerdict.PASS,  # Placeholder, will be updated by admission/budget check
        )
