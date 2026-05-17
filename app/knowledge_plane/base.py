from abc import ABC, abstractmethod

class KnowledgeRegistryBase(ABC):
    @abstractmethod
    def register(self, obj): pass
    @abstractmethod
    def get(self, knowledge_id: str): pass

class ApplicabilityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, knowledge_id: str, context: dict) -> bool: pass

class FreshnessEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, knowledge_id: str) -> str: pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, knowledge_id: str) -> dict: pass
