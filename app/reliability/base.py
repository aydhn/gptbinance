from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.reliability.models import (
    SLODefinition,
    ErrorBudget,
    BurnRateReport,
    HealthScorecard,
    OperationalCadenceArtifact,
)


class SLOEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, slo: SLODefinition, metrics: Dict[str, Any]) -> float:
        pass


class BudgetEngineBase(ABC):
    @abstractmethod
    def calculate_consumption(
        self, budget: ErrorBudget, current_value: float, target_value: float
    ) -> float:
        pass


class ScorecardBuilderBase(ABC):
    @abstractmethod
    def build_scorecard(
        self, domain_name: str, metrics: Dict[str, Any]
    ) -> HealthScorecard:
        pass


class CadenceArtifactBuilderBase(ABC):
    @abstractmethod
    def build_artifact(self, artifact_type: str) -> OperationalCadenceArtifact:
        pass
