import abc
from typing import Dict, Any


class ActivationCompilerBase(abc.ABC):
    @abc.abstractmethod
    def compile_intent(self, board_decision: Dict[str, Any]) -> Any:
        pass


class RolloutPlannerBase(abc.ABC):
    @abc.abstractmethod
    def build_plan(self, intent: Any) -> Any:
        pass


class ProbationEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, intent_id: str, metrics_data: Dict[str, Any]) -> Any:
        pass


class RevertPlannerBase(abc.ABC):
    @abc.abstractmethod
    def plan_revert(self, intent_id: str) -> Any:
        pass
