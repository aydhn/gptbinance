import uuid
import datetime
from typing import Optional
from app.optimizer.base import BaseOptimizerEngine
from app.optimizer.models import (
    OptimizerConfig,
    SearchSpace,
    OptimizerRun,
    TrialConfig,
    OptimizerSummary,
)
from app.optimizer.enums import OptimizerStatus
from app.optimizer.generators import DeterministicGenerator
from app.optimizer.objectives import CompositeObjectiveScorer
from app.optimizer.guards import StandardGuardEvaluator
from app.optimizer.ranking import Ranker
from app.optimizer.trial_runner import TrialRunner
from app.backtest.config import BacktestConfig


class OptimizerEngine(BaseOptimizerEngine):
    """Orchestrates the full optimization process."""

    def __init__(self, config: OptimizerConfig, space: SearchSpace):
        self.config = config
        self.space = space
        self.run_id = f"opt_{uuid.uuid4().hex[:8]}"
        self.run_data = OptimizerRun(
            run_id=self.run_id,
            config=config,
            space=space,
            status=OptimizerStatus.INITIALIZED,
            created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        )

    def run(self) -> OptimizerRun:
        try:
            # 1. Candidate Generation
            self.run_data.status = OptimizerStatus.GENERATING_CANDIDATES
            generator = DeterministicGenerator(mode=self.config.search_mode)
            candidates = generator.generate(
                self.space, max_candidates=self.config.max_trials
            )

            # 2. Setup Backtest Config for Trials
            bt_config = BacktestConfig(
                symbol=self.config.symbol,
                interval=self.config.interval,
                start_time=datetime.datetime.fromtimestamp(
                    self.config.start_ts / 1000, datetime.timezone.utc
                )
                .isoformat()
                .replace("+00:00", "Z"),
                end_time=datetime.datetime.fromtimestamp(
                    self.config.end_ts / 1000, datetime.timezone.utc
                )
                .isoformat()
                .replace("+00:00", "Z"),
                feature_set=self.config.feature_set,
                strategy_set=self.config.strategy_family,
            )

            # 3. Trial Execution
            self.run_data.status = OptimizerStatus.RUNNING_TRIALS
            scorer = CompositeObjectiveScorer()
            guard_evaluator = StandardGuardEvaluator()
            runner = TrialRunner(scorer=scorer, guard_evaluator=guard_evaluator)

            for i, cand in enumerate(candidates):
                trial_id = f"{self.run_id}_t{i+1}"
                trial_config = TrialConfig(
                    trial_id=trial_id, run_id=self.run_id, candidate=cand
                )

                result = runner.run_trial(trial_config, self.space, bt_config)
                self.run_data.trials.append(result)

            # 4. Ranking
            self.run_data.status = OptimizerStatus.RANKING
            self.run_data.ranking = Ranker.rank_trials(
                self.run_data.trials, top_n=min(10, len(candidates))
            )

            # 5. Summarize
            successful = sum(1 for t in self.run_data.trials if not t.error_message)
            failed = sum(1 for t in self.run_data.trials if t.error_message)
            pruned = sum(
                1
                for t in self.run_data.trials
                if t.guard_report and t.guard_report.pruning_verdict.value != "keep"
            )

            best_exp = None
            if self.run_data.ranking:
                best_exp = self.run_data.ranking[0].expectancy

            self.run_data.summary = OptimizerSummary(
                run_id=self.run_id,
                symbol=self.config.symbol,
                interval=self.config.interval,
                strategy_family=self.config.strategy_family,
                total_trials=len(candidates),
                successful_trials=successful,
                failed_trials=failed,
                pruned_trials=pruned,
                status=OptimizerStatus.COMPLETED,
                best_expectancy=best_exp,
                created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            )

            self.run_data.status = OptimizerStatus.COMPLETED

        except Exception as e:
            self.run_data.status = OptimizerStatus.FAILED
            # Add error summary logic if needed
            raise e

        finally:
            self.run_data.completed_at = datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat()

        return self.run_data
