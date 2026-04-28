from typing import List, Dict, Any
from app.backtest.walkforward.models import (
    WalkForwardAggregateResult,
    PromotionGateResult,
)
from app.backtest.walkforward.enums import AggregateVerdict


class PromotionGateEvaluator:
    def __init__(
        self, min_segments: int = 3, min_trades: int = 10, min_expectancy: float = 0.0
    ):
        self.min_segments = min_segments
        self.min_trades = min_trades
        self.min_expectancy = min_expectancy

    def evaluate(self, aggregate: WalkForwardAggregateResult) -> PromotionGateResult:
        checks: List[Dict[str, Any]] = []
        fails = 0
        cautions = 0

        # Check 1: Minimum completed segments
        if aggregate.completed_segments < self.min_segments:
            checks.append(
                {
                    "name": "Min Segments",
                    "status": "fail",
                    "message": f"{aggregate.completed_segments} < {self.min_segments}",
                }
            )
            fails += 1
        else:
            checks.append(
                {
                    "name": "Min Segments",
                    "status": "pass",
                    "message": f"{aggregate.completed_segments} >= {self.min_segments}",
                }
            )

        # Check 2: Minimum trades
        if aggregate.total_oos_trades < self.min_trades:
            checks.append(
                {
                    "name": "Min Trades",
                    "status": "fail",
                    "message": f"{aggregate.total_oos_trades} < {self.min_trades}",
                }
            )
            fails += 1
        elif aggregate.total_oos_trades < self.min_trades * 2:
            checks.append(
                {
                    "name": "Min Trades",
                    "status": "caution",
                    "message": f"Low trades: {aggregate.total_oos_trades}",
                }
            )
            cautions += 1
        else:
            checks.append(
                {
                    "name": "Min Trades",
                    "status": "pass",
                    "message": f"{aggregate.total_oos_trades} trades",
                }
            )

        # Check 3: Expectancy
        if aggregate.aggregate_oos_expectancy <= self.min_expectancy:
            checks.append(
                {
                    "name": "Expectancy",
                    "status": "fail",
                    "message": f"{aggregate.aggregate_oos_expectancy:.4f} <= {self.min_expectancy}",
                }
            )
            fails += 1
        else:
            checks.append(
                {
                    "name": "Expectancy",
                    "status": "pass",
                    "message": f"{aggregate.aggregate_oos_expectancy:.4f} > {self.min_expectancy}",
                }
            )

        if fails > 0:
            verdict = AggregateVerdict.FAIL
            summary = f"Failed {fails} gate checks."
        elif cautions > 0:
            verdict = AggregateVerdict.CAUTION
            summary = f"Passed with {cautions} cautions."
        else:
            verdict = AggregateVerdict.PASS
            summary = "Passed all gate checks."

        return PromotionGateResult(verdict=verdict, checks=checks, summary=summary)
