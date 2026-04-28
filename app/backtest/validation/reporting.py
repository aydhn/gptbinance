import json
from app.backtest.validation.models import ValidationSummary


class ValidationReporter:
    def format_summary(self, summary: ValidationSummary) -> str:
        lines = []
        lines.append("=" * 50)
        lines.append(f"VALIDATION SUMMARY (Status: {summary.status.value})")
        lines.append("=" * 50)
        lines.append(f"Strategy Run ID: {summary.strategy_run_id}")

        lines.append("\n--- COMPARISONS ---")
        for comp in summary.comparisons:
            bench_type = next(
                (
                    b.spec.benchmark_type.value
                    for b in summary.benchmarks
                    if b.spec.benchmark_id == comp.benchmark_run_id
                ),
                "Unknown",
            )
            lines.append(f"Benchmark: {bench_type}")
            lines.append(f"  Verdict: {comp.verdict.value}")
            if comp.caveat:
                lines.append(f"  Caveat: {comp.caveat}")
            for m in comp.metrics:
                lines.append(
                    f"  - {m.metric_name}: Strategy={m.strategy_value:.2f}, Bench={m.benchmark_value:.2f} (Better? {m.is_better})"
                )

        lines.append("\n--- ABLATIONS ---")
        for ab in summary.ablations:
            lines.append(f"Ablation: {ab.spec.ablation_type.value}")
            lines.append(
                f"  Return: {ab.summary.metrics.get('total_return_pct', 0):.2f}%"
            )

        lines.append("\n--- ROBUSTNESS ---")
        for rb in summary.robustness_checks:
            lines.append(f"Check: {rb.check_type.value}")
            lines.append(f"  Fragile? {rb.is_fragile} ({rb.description})")

        if summary.honesty_report:
            lines.append("\n--- HONESTY GUARDS ---")
            lines.append(f"Passed All: {summary.honesty_report.passed_all}")
            for w in summary.honesty_report.warnings:
                lines.append(
                    f"  [{w.severity.value}] {w.metric}: {w.message} (Val: {w.value})"
                )

        lines.append("=" * 50)
        return "\n".join(lines)
