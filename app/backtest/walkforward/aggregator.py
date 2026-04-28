from typing import List
from app.backtest.walkforward.models import (
    WalkForwardSegmentResult,
    WalkForwardAggregateResult,
    WindowPerformanceSummary,
)
from app.backtest.walkforward.enums import SegmentStatus


class OOSAggregator:
    def aggregate(
        self, segments: List[WalkForwardSegmentResult]
    ) -> WalkForwardAggregateResult:
        total_segments = len(segments)
        completed_segments = [
            s
            for s in segments
            if s.status == SegmentStatus.COMPLETED and s.oos_result is not None
        ]

        summaries = []
        total_trades = 0
        total_return = 0.0
        max_dd = 0.0

        # In a more advanced implementation, we would stitch equity curves together.
        # Here we do a simple aggregation of metrics.
        for seg in segments:
            if seg.status == SegmentStatus.COMPLETED and seg.oos_result:
                perf = seg.oos_result.summary
                summaries.append(
                    WindowPerformanceSummary(
                        segment_index=seg.segment_index,
                        status=seg.status.value,
                        oos_trades=perf.total_trades,
                        oos_total_return=perf.total_return_pct,  # Or total_return
                        oos_expectancy=perf.expectancy,
                        oos_max_drawdown=perf.max_drawdown_pct,
                    )
                )
                total_trades += perf.total_trades
                total_return += perf.total_return_pct
                # Max DD across segments is an approximation if we don't stitch curves,
                # but we'll just take the max of the segment max_dds for now.
                if perf.max_drawdown_pct > max_dd:
                    max_dd = perf.max_drawdown_pct
            else:
                summaries.append(
                    WindowPerformanceSummary(
                        segment_index=seg.segment_index,
                        status=seg.status.value,
                        oos_trades=0,
                        oos_total_return=0.0,
                        oos_expectancy=0.0,
                        oos_max_drawdown=0.0,
                    )
                )

        agg_expectancy = 0.0
        if total_trades > 0:
            # Very rough approximation: average return per trade across all OOS segments
            # A proper calculation needs the actual trades list.
            agg_expectancy = total_return / total_trades if total_trades > 0 else 0.0

        return WalkForwardAggregateResult(
            total_segments=total_segments,
            completed_segments=len(completed_segments),
            total_oos_trades=total_trades,
            aggregate_oos_return=total_return,
            aggregate_oos_expectancy=agg_expectancy,
            aggregate_oos_max_drawdown=max_dd,
            segment_summaries=summaries,
        )
