from abc import ABC, abstractmethod
from typing import Any, Dict
from app.release_plane.models import ReleaseCandidate, CompatibilityReport, RolloutPlan, ReleaseTrustVerdict

class CanonicalReleaseRegistryBase(ABC):
    @abstractmethod
    def register(self, release_def: Any) -> None:
        pass

    @abstractmethod
    def get(self, release_id: str) -> Any:
        pass

class CompatibilityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, candidate: ReleaseCandidate, target_env: Any) -> CompatibilityReport:
        pass

class RolloutEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, candidate: ReleaseCandidate) -> RolloutPlan:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, candidate: ReleaseCandidate, compatibility: CompatibilityReport, rollout: RolloutPlan) -> ReleaseTrustVerdict:
        pass

class ReleaseFormatterBase(ABC):
    @abstractmethod
    def format_output(self, data: Any) -> Dict[str, Any]:
        pass
