from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.adversarial_plane.models import AdversarialObject, AdversarialTrustVerdict

class AdversarialRegistryBase(ABC):
    @abstractmethod
    def register(self, obj: AdversarialObject) -> None:
        pass

    @abstractmethod
    def get(self, adversarial_id: str) -> AdversarialObject:
        pass

class ExploitEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context: Dict[str, Any]) -> str:
        pass

class ResistanceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context: Dict[str, Any]) -> str:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context: Dict[str, Any]) -> AdversarialTrustVerdict:
        pass
