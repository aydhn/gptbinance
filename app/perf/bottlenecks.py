from typing import List, Optional
from app.perf.models import PerfRun, BottleneckReport
from app.perf.enums import BottleneckType


class BottleneckAnalyzer:
    @staticmethod
    def analyze(run: PerfRun) -> List[BottleneckReport]:
        reports = []

        # Check CPU bound
        if run.cpu_summary.avg_cpu_percent > 80.0:
            top_comp = max(
                run.cpu_summary.top_components.items(),
                key=lambda x: x[1],
                default=("Unknown", 0.0),
            )[0]
            reports.append(
                BottleneckReport(
                    run_id=run.run_id,
                    bottleneck_type=BottleneckType.CPU_BOUND,
                    likely_component=top_comp,
                    evidence=f"Average CPU utilization was {run.cpu_summary.avg_cpu_percent:.1f}%",
                    impacted_workloads=[run.workload_type],
                    recommendation="Profile top CPU-consuming functions; consider optimizing algorithms.",
                )
            )

        # Check Memory leak / bound
        if run.memory_summary.leak_suspicion:
            reports.append(
                BottleneckReport(
                    run_id=run.run_id,
                    bottleneck_type=BottleneckType.MEMORY_BOUND,
                    likely_component="Overall",
                    evidence=f"Memory grew by {run.memory_summary.memory_growth_mb:.1f}MB and met leak criteria.",
                    impacted_workloads=[run.workload_type],
                    recommendation="Investigate object retention or caching strategies that grow unboundedly.",
                )
            )

        # Check I/O bound
        # A simple heuristic: if total write is high relative to duration
        if (
            run.duration_sec > 0
            and (run.disk_summary.total_write_mb / run.duration_sec) > 50.0
        ):  # 50MB/s
            reports.append(
                BottleneckReport(
                    run_id=run.run_id,
                    bottleneck_type=BottleneckType.IO_BOUND,
                    likely_component="Storage",
                    evidence=f"High write throughput: {run.disk_summary.total_write_mb / run.duration_sec:.1f}MB/s",
                    impacted_workloads=[run.workload_type],
                    recommendation="Check for excessive logging, frequent DB commits, or large artifact writes.",
                )
            )

        # Check Network bound
        if (
            run.duration_sec > 0
            and (run.network_summary.total_tx_kb / run.duration_sec) > 10000.0
        ):  # 10MB/s tx
            reports.append(
                BottleneckReport(
                    run_id=run.run_id,
                    bottleneck_type=BottleneckType.NETWORK_BOUND,
                    likely_component="Network",
                    evidence=f"High network TX: {run.network_summary.total_tx_kb / run.duration_sec:.1f}KB/s",
                    impacted_workloads=[run.workload_type],
                    recommendation="Check for large payload transfers or frequent remote calls.",
                )
            )

        return reports
