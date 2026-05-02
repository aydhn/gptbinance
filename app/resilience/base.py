from abc import ABC, abstractmethod
from app.resilience.models import (
    ExperimentDefinition,
    ExperimentRun,
    ExperimentScope,
    FaultInjectionSpec,
    StressSpec,
    AssertionSpec,
    AssertionResult,
    ResilienceScore,
    ExperimentSummary,
)


class BaseFaultInjector(ABC):
    @abstractmethod
    async def inject(self, spec: FaultInjectionSpec, run_id: str) -> None:
        pass

    @abstractmethod
    async def cleanup(self, spec: FaultInjectionSpec, run_id: str) -> None:
        pass


class BaseStressGenerator(ABC):
    @abstractmethod
    async def apply_stress(self, spec: StressSpec, run_id: str) -> None:
        pass

    @abstractmethod
    async def remove_stress(self, spec: StressSpec, run_id: str) -> None:
        pass


class BaseAssertionEvaluator(ABC):
    @abstractmethod
    async def evaluate(self, spec: AssertionSpec, run_id: str) -> AssertionResult:
        pass


class BaseResilienceScorer(ABC):
    @abstractmethod
    def calculate_score(self, summary: ExperimentSummary) -> ResilienceScore:
        pass


class BaseExperimentRunner(ABC):
    @abstractmethod
    async def run_experiment(
        self, definition: ExperimentDefinition, scope: ExperimentScope
    ) -> ExperimentRun:
        pass
