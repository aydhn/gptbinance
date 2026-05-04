from abc import ABC, abstractmethod
from typing import Dict, Any


class CapitalPolicyEngineBase(ABC):
    @abstractmethod
    def evaluate_policy(self, context: Dict[str, Any]) -> Any:
        pass


class EscalationEvaluatorBase(ABC):
    @abstractmethod
    def check_escalation_readiness(
        self, current_tier: str, target_tier: str, evidence: Any
    ) -> Any:
        pass


class BudgetEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_utilization(self, budget: Any, current_usage: Dict[str, float]) -> Any:
        pass


class PostureReporterBase(ABC):
    @abstractmethod
    def generate_snapshot(self) -> Any:
        pass
