from abc import ABC, abstractmethod
from typing import Dict, Any, List

class CandidateCompilerBase(ABC):
    @abstractmethod
    def compile(self, intent: Any) -> Any:
        pass

class OrderSpecBuilderBase(ABC):
    @abstractmethod
    def build(self, candidate: Any, venue: Any) -> Any:
        pass

class RoutingEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, candidate: Any) -> Any:
        pass

class QualityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, execution_data: Any) -> Any:
        pass
