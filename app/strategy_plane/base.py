from abc import ABC, abstractmethod
from typing import Optional, List
from app.strategy_plane.models import (
    StrategyDefinition,
    StrategyFitReport,
    StrategyEquivalenceReport,
    StrategyTrustVerdict,
)
from app.strategy_plane.enums import LifecycleState


class BaseStrategyRegistry(ABC):
    @abstractmethod
    def register(self, definition: StrategyDefinition) -> None:
        pass

    @abstractmethod
    def get(self, strategy_id: str) -> Optional[StrategyDefinition]:
        pass

    @abstractmethod
    def list_all(self) -> List[StrategyDefinition]:
        pass


class BaseLifecycleEvaluator(ABC):
    @abstractmethod
    def transition(
        self,
        strategy_id: str,
        new_state: LifecycleState,
        reason: str,
        evidence_refs: List[str] = None,
    ):
        pass

    @abstractmethod
    def get_current_state(self, strategy_id: str) -> LifecycleState:
        pass


class BaseFitEvaluator(ABC):
    @abstractmethod
    def evaluate_fit(
        self, strategy_id: str, regime_context: str, execution_context: str
    ) -> StrategyFitReport:
        pass


class BaseTrustEvaluator(ABC):
    @abstractmethod
    def evaluate(
        self,
        strategy: StrategyDefinition,
        lifecycle_state: LifecycleState,
        equivalence_report: StrategyEquivalenceReport = None,
        decay_report=None,
        overlap_report=None,
    ) -> StrategyTrustVerdict:
        pass
