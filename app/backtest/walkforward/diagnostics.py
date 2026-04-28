from typing import List
from app.backtest.walkforward.models import WalkForwardSegmentResult
from app.backtest.walkforward.enums import SegmentStatus


class DiagnosticAnalyzer:
    def analyze(self, segments: List[WalkForwardSegmentResult]) -> List[str]:
        diagnostics = []

        completed = [
            s for s in segments if s.status == SegmentStatus.COMPLETED and s.diagnostics
        ]
        if not completed:
            diagnostics.append("No completed segments to analyze.")
            return diagnostics

        total_decay = sum(s.diagnostics.expectancy_decay for s in completed)
        avg_decay = total_decay / len(completed)

        if avg_decay > 0.3:
            diagnostics.append(f"High average OOS decay detected: {avg_decay:.2%}")

        negative_oos = sum(1 for s in completed if s.diagnostics.oos_expectancy <= 0)
        if negative_oos > len(completed) / 2:
            diagnostics.append(
                f"More than half of OOS segments have negative expectancy ({negative_oos}/{len(completed)})."
            )

        low_trades = sum(1 for s in completed if s.diagnostics.oos_trade_count < 2)
        if low_trades > 0:
            diagnostics.append(
                f"{low_trades} segment(s) suffered from trade drought in OOS."
            )

        return diagnostics
