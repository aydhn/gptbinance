import logging
from typing import List, Dict, Optional, Callable
from datetime import datetime, timezone

from app.backtest.walkforward.models import (
    WalkForwardConfig,
    WalkForwardWindow,
    WalkForwardSegmentResult,
    CandidateSelectionResult,
    WindowDiagnostic,
)
from app.backtest.walkforward.enums import SegmentStatus, PromotionVerdict
from app.backtest.walkforward.selection import CandidateSelector
from app.backtest.walkforward.freeze import FreezeManager
from app.backtest.models import BacktestConfig, BacktestResult
from app.strategies.models import StrategySpec

logger = logging.getLogger(__name__)


class SegmentRunner:
    def __init__(
        self,
        selector: CandidateSelector,
        freezer: FreezeManager,
        run_backtest_fn: Callable[[BacktestConfig], BacktestResult],
    ):
        """
        run_backtest_fn: A callable that takes a BacktestConfig and returns a BacktestResult.
        This allows injecting the actual engine run logic or a mock for testing.
        """
        self.selector = selector
        self.freezer = freezer
        self.run_backtest_fn = run_backtest_fn

    def _ts_to_dt(self, ts_ms: int) -> datetime:
        return datetime.fromtimestamp(ts_ms / 1000.0, tz=timezone.utc)

    def run_segment(
        self,
        config: WalkForwardConfig,
        window: WalkForwardWindow,
        candidate_specs: List[StrategySpec],
    ) -> WalkForwardSegmentResult:
        if not window.is_valid:
            return WalkForwardSegmentResult(
                segment_index=window.segment_index,
                window=window,
                status=SegmentStatus.SKIPPED_INSUFFICIENT_DATA,
                error_message=window.reason,
            )

        try:
            # --- IN-SAMPLE PHASE ---
            is_results = []
            for spec in candidate_specs:
                is_bt_config = BacktestConfig(
                    symbol=config.symbol,
                    interval=config.interval,
                    start_time=self._ts_to_dt(window.is_start),
                    end_time=self._ts_to_dt(window.is_end),
                    strategy_set=spec.name,
                    feature_set=config.feature_set,
                )
                # Execute backtest
                res = self.run_backtest_fn(is_bt_config)
                is_results.append(res)

            # --- SELECTION ---
            specs_by_name = {s.name: s for s in candidate_specs}
            selection = self.selector.select(config, is_results, specs_by_name)

            if (
                selection.verdict != PromotionVerdict.PROMOTED
                or selection.selected_candidate is None
            ):
                return WalkForwardSegmentResult(
                    segment_index=window.segment_index,
                    window=window,
                    status=SegmentStatus.COMPLETED,
                    selection=selection,
                    error_message="No candidate promoted to OOS.",
                )

            # --- FREEZE ---
            frozen_bundle = selection.selected_candidate
            snapshot = self.freezer.freeze(frozen_bundle)

            # Verify frozen bundle before OOS (just as a sanity check)
            if not self.freezer.verify(frozen_bundle, snapshot):
                raise ValueError(
                    "Frozen bundle verification failed immediately after freezing!"
                )

            # --- OUT-OF-SAMPLE PHASE ---
            oos_bt_config = BacktestConfig(
                symbol=config.symbol,
                interval=config.interval,
                start_time=self._ts_to_dt(window.oos_start),
                end_time=self._ts_to_dt(window.oos_end),
                strategy_set=frozen_bundle.spec.name,
                feature_set=config.feature_set,
            )

            oos_result = self.run_backtest_fn(oos_bt_config)

            # --- DIAGNOSTICS ---
            is_expectancy = frozen_bundle.metadata.get("is_expectancy", 0.0)
            oos_expectancy = oos_result.summary.expectancy

            decay = 0.0
            if is_expectancy > 0:
                decay = (is_expectancy - oos_expectancy) / is_expectancy

            warnings = []
            if decay > 0.5:
                warnings.append("High OOS expectancy decay (>50%)")
            if oos_result.summary.total_trades < config.min_trades_oos:
                warnings.append(
                    f"Low OOS trade count: {oos_result.summary.total_trades}"
                )

            diag = WindowDiagnostic(
                is_expectancy=is_expectancy,
                oos_expectancy=oos_expectancy,
                expectancy_decay=decay,
                is_trade_count=frozen_bundle.metadata.get("is_trades", 0),
                oos_trade_count=oos_result.summary.total_trades,
                oos_max_drawdown=oos_result.summary.max_drawdown_pct,
                warnings=warnings,
            )

            return WalkForwardSegmentResult(
                segment_index=window.segment_index,
                window=window,
                status=SegmentStatus.COMPLETED,
                selection=selection,
                oos_result=oos_result,
                diagnostics=diag,
            )

        except Exception as e:
            logger.exception(f"Segment {window.segment_index} failed: {e}")
            return WalkForwardSegmentResult(
                segment_index=window.segment_index,
                window=window,
                status=SegmentStatus.FAILED,
                error_message=str(e),
            )
