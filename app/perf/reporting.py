import json
from app.perf.models import (
    PerfRun,
    BottleneckReport,
    CapacityReport,
    PerfRegressionReport,
    HostQualificationReport,
)


class PerfReporter:
    @staticmethod
    def format_run_summary(run: PerfRun) -> str:
        lines = [
            f"=== PERF RUN SUMMARY: {run.run_id} ===",
            f"Workload: {run.workload_type.value}",
            f"Host Class: {run.host_class.value}",
            f"Duration: {run.duration_sec:.2f}s",
            f"Verdict: {run.verdict.value}",
            "--- CPU ---",
            f"Peak: {run.cpu_summary.peak_cpu_percent:.1f}% | Avg: {run.cpu_summary.avg_cpu_percent:.1f}%",
            "--- Memory ---",
            f"Peak: {run.memory_summary.peak_memory_mb:.1f}MB | Growth: {run.memory_summary.memory_growth_mb:.1f}MB",
            f"Leak Suspicion: {run.memory_summary.leak_suspicion}",
            "--- Disk I/O ---",
            f"Read: {run.disk_summary.total_read_mb:.1f}MB | Write: {run.disk_summary.total_write_mb:.1f}MB",
            "--- Network ---",
            f"RX: {run.network_summary.total_rx_kb:.1f}KB | TX: {run.network_summary.total_tx_kb:.1f}KB",
        ]
        return "\n".join(lines)

    @staticmethod
    def format_bottleneck_report(reports: list[BottleneckReport]) -> str:
        if not reports:
            return "No bottlenecks detected."
        lines = ["=== BOTTLENECK REPORT ==="]
        for r in reports:
            lines.append(
                f"[{r.bottleneck_type.value}] Likely Component: {r.likely_component}"
            )
            lines.append(f"Evidence: {r.evidence}")
            lines.append(f"Recommendation: {r.recommendation}")
            lines.append("-")
        return "\n".join(lines)

    @staticmethod
    def format_capacity_report(report: CapacityReport) -> str:
        lines = [
            f"=== CAPACITY REPORT: {report.host_class.value} ===",
            f"Available Headroom: {report.available_headroom_percent:.1f}%",
            f"Reserve Recommendation: {report.reserve_capacity_recommendation}",
        ]
        if report.concurrency_cautions:
            lines.append("--- CAUTIONS ---")
            for c in report.concurrency_cautions:
                lines.append(f"WARNING: {c}")
        if report.unsupported_combinations:
            lines.append("--- UNSUPPORTED ---")
            for u in report.unsupported_combinations:
                lines.append(f"UNSUPPORTED: {u}")
        return "\n".join(lines)

    @staticmethod
    def format_regression_report(report: PerfRegressionReport) -> str:
        lines = [
            f"=== REGRESSION REPORT ===",
            f"Baseline: {report.baseline_run_id} | Target: {report.target_run_id}",
            f"Severity: {report.severity.value}",
            f"Recommendation: {report.recommendation}",
            "--- Findings ---",
        ]
        if not report.findings:
            lines.append("No findings.")
        for f in report.findings:
            marker = "[REGRESSION]" if f.is_regression else "[CHANGE]"
            lines.append(
                f"{marker} {f.metric_name}: {f.baseline_value:.2f} -> {f.target_value:.2f} ({f.delta_percent:+.1f}%)"
            )
        return "\n".join(lines)
