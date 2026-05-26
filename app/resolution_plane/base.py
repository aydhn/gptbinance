from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from app.resolution_plane.models import ResolutionObject, ResolutionTrustVerdict

class ResolutionRegistryBase(ABC):
    @abstractmethod
    def register_resolution(self, resolution: ResolutionObject) -> None:
        pass

    @abstractmethod
    def get_resolution(self, resolution_id: str) -> Optional[ResolutionObject]:
        pass

class ContinuityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_continuity(self, resolution_id: str) -> Dict[str, Any]:
        pass

class TransferEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_transfer(self, resolution_id: str) -> Dict[str, Any]:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, resolution_id: str) -> ResolutionTrustVerdict:
        pass
