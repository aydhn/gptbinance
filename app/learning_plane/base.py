from abc import ABC, abstractmethod
from typing import Dict, Any, List

from app.learning_plane.models import LearningObject, LearningTrustVerdict

class LearningRegistryBase(ABC):
    @abstractmethod
    def register_object(self, obj: LearningObject) -> None:
        pass

    @abstractmethod
    def get_object(self, learning_id: str) -> LearningObject:
        pass

class FindingEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, finding_id: str) -> Dict[str, Any]:
        pass

class HardeningEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, action_id: str) -> Dict[str, Any]:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, learning_id: str) -> LearningTrustVerdict:
        pass
