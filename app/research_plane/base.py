from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from app.research_plane.models import (
    ResearchItem,
    ResearchQuestion,
    ResearchHypothesis,
    EvidenceBundle,
    ContradictionRecord,
    ConfidenceAssessment,
    ResearchReadinessRecord,
    ResearchInvalidationRecord,
    ResearchOverlapReport,
    ResearchMaturationReport,
    ResearchEquivalenceReport,
    ResearchTrustVerdict,
    ResearchArtifactManifest,
)


class ResearchRegistryBase(ABC):
    @abstractmethod
    def register_item(self, item: ResearchItem) -> None:
        pass

    @abstractmethod
    def get_item(self, research_id: str) -> Optional[ResearchItem]:
        pass

    @abstractmethod
    def update_item(self, item: ResearchItem) -> None:
        pass

    @abstractmethod
    def list_items(self) -> List[ResearchItem]:
        pass


class EvidenceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_bundle(
        self, bundle: EvidenceBundle, hypothesis: ResearchHypothesis
    ) -> Dict[str, str]:
        pass


class ReadinessEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_readiness(self, item: ResearchItem) -> ResearchReadinessRecord:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, item: ResearchItem) -> ResearchTrustVerdict:
        pass
