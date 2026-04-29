from abc import ABC, abstractmethod
from typing import List, Dict, Any
from app.optimizer.models import (
    SearchSpace,
    ParameterCandidate,
    TrialResult,
    ObjectiveScore,
    OptimizationGuardReport,
    OptimizerRun,
    TrialConfig,
    TrialMetrics,
)


class BaseGenerator(ABC):
    @abstractmethod
    def generate(
        self, space: SearchSpace, max_candidates: int
    ) -> List[ParameterCandidate]:
        pass


class BaseScorer(ABC):
    @abstractmethod
    def score(self, metrics: TrialMetrics) -> ObjectiveScore:
        pass


class BaseGuardEvaluator(ABC):
    @abstractmethod
    def evaluate(self, trial_id: str, metrics: TrialMetrics) -> OptimizationGuardReport:
        pass


class BaseTrialRunner(ABC):
    @abstractmethod
    def run_trial(
        self, config: TrialConfig, space: SearchSpace, bt_config: Any
    ) -> TrialResult:
        pass


class BaseOptimizerEngine(ABC):
    @abstractmethod
    def run(self) -> OptimizerRun:
        pass
