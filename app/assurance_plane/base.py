from abc import ABC, abstractmethod
from typing import List, Optional
from app.assurance_plane.models import AssuranceObject, AssuranceTrustVerdict, AssuranceRecord

class AssuranceRegistryBase(ABC):
    @abstractmethod
    def register_assurance(self, obj: AssuranceObject) -> None:
        pass

    @abstractmethod
    def get_assurance(self, assurance_id: str) -> Optional[AssuranceRecord]:
        pass

class SufficiencyEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, claim_id: str, pack_id: str) -> str:
        pass

class SurveillanceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, assurance_id: str) -> str:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, assurance_id: str) -> AssuranceTrustVerdict:
        pass
