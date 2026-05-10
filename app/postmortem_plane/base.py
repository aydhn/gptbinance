from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from app.postmortem_plane.models import (
    PostmortemDefinition,
    PostmortemTrustVerdict,
    CausalChain,
    CorrectiveAction,
    PreventiveAction,
    RemediationDebtRecord,
    RecurrenceRecord
)

class PostmortemRegistryBase(ABC):
    @abstractmethod
    def register_postmortem(self, postmortem: PostmortemDefinition) -> str:
        pass

    @abstractmethod
    def get_postmortem(self, postmortem_id: str) -> Optional[PostmortemDefinition]:
        pass

    @abstractmethod
    def list_postmortems(self, filters: Dict[str, Any] = None) -> List[PostmortemDefinition]:
        pass

class CausalEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_chain(self, chain: CausalChain) -> bool:
        pass

class RemediationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_actions(self, corrective: List[CorrectiveAction], preventive: List[PreventiveAction]) -> bool:
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, postmortem: PostmortemDefinition) -> PostmortemTrustVerdict:
        pass
