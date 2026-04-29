import datetime
from typing import Optional
from app.optimizer.base import BaseTrialRunner, BaseScorer, BaseGuardEvaluator
from app.optimizer.models import (
    TrialConfig,
    SearchSpace,
    TrialResult,
    TrialMetrics,
    TrialLineage,
)
from app.optimizer.enums import PruningVerdict

# Imports for backtest bridging
from app.backtest.engine import BacktestEngine
from app.backtest.config import BacktestConfig
from app.strategies.registry import StrategyRegistry
from app.backtest.validation.honesty_guards import HonestyGuardEvaluator
from app.backtest.validation.benchmark_runner import BenchmarkRunner


class TrialRunner(BaseTrialRunner):
    """Orchestrates a single optimization trial."""

    def __init__(self, scorer: BaseScorer, guard_evaluator: BaseGuardEvaluator):
        self.scorer = scorer
        self.guard_evaluator = guard_evaluator

    def run_trial(
        self, config: TrialConfig, space: SearchSpace, bt_config: BacktestConfig
    ) -> TrialResult:
        now_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
        lineage = TrialLineage(
            run_id=config.run_id,
            trial_id=config.trial_id,
            candidate_id=config.candidate.candidate_id,
            space_name=space.name,
            generated_at=now_str,
        )

        try:
            # 1. Prepare Strategy Spec
            registry = StrategyRegistry()
            spec = registry.get_spec(space.strategy_family)
            if not spec:
                raise ValueError(
                    f"Strategy family '{space.strategy_family}' not found in registry."
                )

            # Override parameters with candidate values
            new_params = spec.parameters.copy()
            new_params.update(config.candidate.values)
            spec.parameters = new_params

            # 2. Run Backtest
            engine = BacktestEngine(config=bt_config, specs=[spec])
            engine.run()
            results = engine.get_results()

            if not results:
                raise ValueError("Backtest engine returned no results.")
            bt_result = results[0]
            summary = bt_result.summary

            # 3. Validation & Benchmark
            bm_runner = BenchmarkRunner(config=bt_config)
            bm_results = bm_runner.run_benchmarks()
            bh_summary = next(
                (
                    b.summary
                    for b in bm_results
                    if b.run.config.strategy_set == "buy_and_hold"
                ),
                None,
            )

            # 4. Honesty Guards
            honesty_eval = HonestyGuardEvaluator()
            honesty_report = honesty_eval.evaluate(summary)

            # 5. Compile Trial Metrics
            relative_strength = 0.0
            if bh_summary and bh_summary.total_return_pct != 0:
                relative_strength = (
                    summary.total_return_pct - bh_summary.total_return_pct
                ) / abs(bh_summary.total_return_pct)

            metrics = TrialMetrics(
                expectancy=summary.expectancy,
                profit_factor=summary.profit_factor,
                max_drawdown_pct=summary.max_drawdown_pct,
                total_trades=summary.total_trades,
                hit_rate=summary.hit_rate,
                benchmark_relative_strength=relative_strength,
            )

            # 6. Objective Scoring
            objective_score = self.scorer.score(metrics)

            if not honesty_report.passed_all:
                objective_score.penalties["honesty_penalty"] = -50.0
                objective_score.total_score -= 50.0
                objective_score.rationale += " | Applied honesty penalty"

            # 7. Optimizer Guards
            guard_report = self.guard_evaluator.evaluate(config.trial_id, metrics)

            return TrialResult(
                trial_id=config.trial_id,
                config=config,
                backtest_summary=summary,
                validation_summary=honesty_report.dict(),
                metrics=metrics,
                objective=objective_score,
                guard_report=guard_report,
                lineage=lineage,
            )

        except Exception as e:
            return TrialResult(
                trial_id=config.trial_id,
                config=config,
                lineage=lineage,
                error_message=str(e),
            )
