from abc import ABC, abstractmethod
from app.decision_quality_plane.models import DecisionManifest

class DecisionRegistryBase(ABC):
    @abstractmethod
    def register(self, manifest: DecisionManifest):
        pass

class EpistemicEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, manifest: DecisionManifest):
        pass
