from typing import List, Dict, Any
from app.perf.models import PerfRun, PerfRegressionReport, PerfFinding
from app.perf.enums import RegressionSeverity


class RegressionEvaluator:
    @staticmethod
    def evaluate(baseline: PerfRun, target: PerfRun) -> PerfRegressionReport:
        findings = []
        severity = RegressionSeverity.BENIGN

        def check_metric(
            name: str, base_val: float, targ_val: float, is_higher_worse: bool = True
        ) -> None:
            nonlocal severity
            if base_val == 0:
                delta_pct = float("inf") if targ_val > 0 else 0.0
            else:
                delta_pct = ((targ_val - base_val) / base_val) * 100.0

            is_regression = False
            # Check for significant degradation (> 10%)
            if is_higher_worse and delta_pct > 10.0:
                is_regression = True
                if delta_pct > 50.0:
                    severity = max(
                        severity,
                        RegressionSeverity.CRITICAL,
                        key=lambda s: ["BENIGN", "MINOR", "MAJOR", "CRITICAL"].index(
                            s.value
                        ),
                    )
                elif delta_pct > 25.0:
                    severity = max(
                        severity,
                        RegressionSeverity.MAJOR,
                        key=lambda s: ["BENIGN", "MINOR", "MAJOR", "CRITICAL"].index(
                            s.value
                        ),
                    )
                else:
                    severity = max(
                        severity,
                        RegressionSeverity.MINOR,
                        key=lambda s: ["BENIGN", "MINOR", "MAJOR", "CRITICAL"].index(
                            s.value
                        ),
                    )

            if abs(delta_pct) > 5.0:  # Only record meaningful changes
                findings.append(
                    PerfFinding(
                        metric_name=name,
                        baseline_value=base_val,
                        target_value=targ_val,
                        delta_percent=delta_pct,
                        is_regression=is_regression,
                    )
                )

        check_metric("duration_sec", baseline.duration_sec, target.duration_sec)
        check_metric(
            "peak_cpu",
            baseline.cpu_summary.peak_cpu_percent,
            target.cpu_summary.peak_cpu_percent,
        )
        check_metric(
            "avg_cpu",
            baseline.cpu_summary.avg_cpu_percent,
            target.cpu_summary.avg_cpu_percent,
        )
        check_metric(
            "peak_memory",
            baseline.memory_summary.peak_memory_mb,
            target.memory_summary.peak_memory_mb,
        )

        base_latencies = {l.component_name: l for l in baseline.latencies}
        for lat in target.latencies:
            if lat.component_name in base_latencies:
                base_lat = base_latencies[lat.component_name]
                check_metric(f"{lat.component_name}_p95", base_lat.p95_ms, lat.p95_ms)

        recommendation = "No significant regressions detected."
        if severity != RegressionSeverity.BENIGN:
            recommendation = f"Regression detected ({severity.value}). Inspect findings and bottleneck reports."

        return PerfRegressionReport(
            baseline_run_id=baseline.run_id,
            target_run_id=target.run_id,
            severity=severity,
            findings=findings,
            recommendation=recommendation,
        )
