from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.shadow_state.models import (
    VenueAccountSnapshot,
    LocalDerivedSnapshot,
    ConvergenceResult,
    RemediationPlan,
    ShadowTwinSnapshot,
)


class BaseSnapshotLoader(ABC):
    @abstractmethod
    def load_venue_snapshot(
        self, profile_id: str, workspace_id: str
    ) -> VenueAccountSnapshot:
        pass

    @abstractmethod
    def load_local_snapshot(
        self, profile_id: str, workspace_id: str
    ) -> LocalDerivedSnapshot:
        pass


class BaseConvergenceEvaluator(ABC):
    @abstractmethod
    def evaluate(self, twin: ShadowTwinSnapshot) -> Dict[str, ConvergenceResult]:
        pass


class BaseDriftClassifier(ABC):
    @abstractmethod
    def classify(self, findings: List[Any]) -> List[Any]:
        pass


class BaseRemediationPlanner(ABC):
    @abstractmethod
    def plan(
        self, run_id: str, results: Dict[str, ConvergenceResult]
    ) -> RemediationPlan:
        pass
