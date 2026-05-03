from abc import ABC, abstractmethod
from typing import Dict, Any


class ScenarioRunnerBase(ABC):
    @abstractmethod
    def run_scenario(self, scenario, context: Dict[str, Any]):
        pass


class ShockEngineBase(ABC):
    @abstractmethod
    def apply_shocks(self, state: Dict[str, Any], shocks: list) -> Dict[str, Any]:
        pass


class LossEstimatorBase(ABC):
    @abstractmethod
    def estimate_loss(self, shocked_state: Dict[str, Any], position: Dict[str, Any]):
        pass


class BudgetEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, losses: float, profile: str):
        pass
