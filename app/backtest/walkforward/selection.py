import logging
from typing import List, Dict, Any, Optional
from app.backtest.walkforward.models import (
    CandidateSelectionResult,
    FrozenStrategyBundle,
    WalkForwardConfig,
)
from app.backtest.walkforward.enums import SelectionPolicy, PromotionVerdict
from app.backtest.walkforward.exceptions import CandidateSelectionError
from app.backtest.models import BacktestResult
from app.strategies.models import StrategySpec
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


class CandidateSelector:
    def select(
        self,
        config: WalkForwardConfig,
        backtest_results: List[BacktestResult],
        specs_by_name: Dict[str, StrategySpec],
    ) -> CandidateSelectionResult:
        if not backtest_results:
            return CandidateSelectionResult(
                selected_candidate=None,
                selection_rationale="No backtest results provided.",
                verdict=PromotionVerdict.REJECTED,
                alternatives=[],
            )

        valid_candidates = []
        rejected_candidates = []

        for result in backtest_results:
            spec_name = (
                result.run.config.strategy_set
            )  # Using strategy_set as identifier for the spec here since we run single spec per run for selection
            perf = result.summary

            # Constraints
            if perf.total_trades < config.min_trades_is:
                rejected_candidates.append(
                    {
                        "name": spec_name,
                        "reason": f"Insufficient IS trades: {perf.total_trades} < {config.min_trades_is}",
                    }
                )
                continue

            if perf.expectancy <= 0:
                rejected_candidates.append(
                    {
                        "name": spec_name,
                        "reason": f"Negative or zero expectancy: {perf.expectancy}",
                    }
                )
                continue

            valid_candidates.append(result)

        if not valid_candidates:
            return CandidateSelectionResult(
                selected_candidate=None,
                selection_rationale="No candidates passed basic IS constraints (min_trades, expectancy > 0).",
                verdict=PromotionVerdict.REJECTED,
                alternatives=rejected_candidates,
            )

        # Sorting based on policy
        if config.selection_policy == SelectionPolicy.MAX_EXPECTANCY:
            valid_candidates.sort(key=lambda x: x.summary.expectancy, reverse=True)
        elif config.selection_policy == SelectionPolicy.MIN_DRAWDOWN:
            valid_candidates.sort(
                key=lambda x: x.summary.max_drawdown_pct
            )  # lower is better
        elif config.selection_policy == SelectionPolicy.BALANCED:
            # Custom scoring: expectancy / max(max_drawdown_pct, 0.01)
            def _score(s: BacktestResult) -> float:
                return s.summary.expectancy / max(s.summary.max_drawdown_pct, 0.01)

            valid_candidates.sort(key=_score, reverse=True)
        else:
            valid_candidates.sort(key=lambda x: x.summary.expectancy, reverse=True)

        chosen = valid_candidates[0]
        chosen_spec_name = chosen.run.config.strategy_set
        chosen_spec = specs_by_name.get(chosen_spec_name)

        if not chosen_spec:
            raise CandidateSelectionError(
                f"StrategySpec for chosen candidate {chosen_spec_name} not found."
            )

        now_str = datetime.now(timezone.utc).isoformat()

        bundle = FrozenStrategyBundle(
            spec=chosen_spec,
            metadata={
                "is_expectancy": chosen.summary.expectancy,
                "is_drawdown": chosen.summary.max_drawdown_pct,
                "is_trades": chosen.summary.total_trades,
                "portfolio_feasibility": True,
            },
            frozen_at=now_str,
        )

        alts = [
            {"name": c.run.config.strategy_set, "expectancy": c.summary.expectancy}
            for c in valid_candidates[1:]
        ] + rejected_candidates

        return CandidateSelectionResult(
            selected_candidate=bundle,
            selection_rationale=f"Selected {chosen_spec_name} via {config.selection_policy} policy. Expectancy: {chosen.summary.expectancy:.4f}",
            verdict=PromotionVerdict.PROMOTED,
            alternatives=alts,
        )
