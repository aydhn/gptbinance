from abc import ABC, abstractmethod
from typing import Dict, Any, List


class HypothesisCompilerBase(ABC):
    @abstractmethod
    def compile(self, findings: List[Dict[str, Any]]) -> Dict[str, Any]:
        pass


class ExperimentRunnerBase(ABC):
    @abstractmethod
    def run(self, pack_id: str) -> str:
        pass


class ComparisonEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, run_id: str) -> Dict[str, Any]:
        pass


class PromotionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, comparison_results: Dict[str, Any], fragility_results: Dict[str, Any]
    ) -> str:
        pass
