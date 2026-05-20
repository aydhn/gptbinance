from abc import ABC, abstractmethod
from app.semantic_plane.models import SemanticTrustVerdict, SemanticEquivalenceReport

class SemanticRegistryBase(ABC):
    @abstractmethod
    def register_term(self, term_record):
        pass

    @abstractmethod
    def register_metric(self, metric_record):
        pass

class InterpretationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, interpretation_record) -> bool:
        pass

class EquivalenceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, semantic_id: str) -> SemanticEquivalenceReport:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, semantic_id: str) -> SemanticTrustVerdict:
        pass
