from typing import List
from app.backtest.walkforward.models import (
    WalkForwardAggregateResult,
    PromotionGateResult,
    WindowDiagnostic,
)


class WalkForwardReporter:
    def format_summary(
        self, agg: WalkForwardAggregateResult, gates: PromotionGateResult
    ) -> str:
        lines = []
        lines.append("=== WALK-FORWARD SUMMARY ===")
        lines.append(f"Segments: {agg.completed_segments} / {agg.total_segments}")
        lines.append(f"OOS Trades: {agg.total_oos_trades}")
        lines.append(f"OOS Return: {agg.aggregate_oos_return:.2f}%")
        lines.append(f"OOS Expectancy: {agg.aggregate_oos_expectancy:.4f}")
        lines.append(f"OOS Max Drawdown: {agg.aggregate_oos_max_drawdown:.2f}%")
        lines.append("")
        lines.append(f"Promotion Gate Verdict: {gates.verdict.value.upper()}")
        lines.append(f"Promotion Summary: {gates.summary}")
        return "\n".join(lines)

    def format_segments(self, agg: WalkForwardAggregateResult) -> str:
        lines = []
        lines.append("=== SEGMENT OOS PERFORMANCE ===")
        lines.append(
            f"{'SEG':<5} | {'STATUS':<15} | {'TRADES':<8} | {'EXPECTANCY':<12} | {'RETURN%':<10} | {'MAX DD%':<10}"
        )
        lines.append("-" * 75)
        for s in agg.segment_summaries:
            lines.append(
                f"{s.segment_index:<5} | {s.status:<15} | {s.oos_trades:<8} | {s.oos_expectancy:<12.4f} | {s.oos_total_return:<10.2f} | {s.oos_max_drawdown:<10.2f}"
            )
        return "\n".join(lines)

    def format_diagnostics(self, diagnostics: List[str]) -> str:
        if not diagnostics:
            return "No critical diagnostic warnings."
        lines = ["=== DIAGNOSTICS ==="]
        for d in diagnostics:
            lines.append(f"- {d}")
        return "\n".join(lines)
