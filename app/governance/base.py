from abc import ABC, abstractmethod
from typing import Any, Dict, List
from app.governance.models import (
    RefreshPlan,
    RefreshRun,
    RefreshResult,
    CandidateBundle,
    DecayReport,
    PromotionCandidateReport,
)


class BaseRefreshOrchestrator(ABC):
    @abstractmethod
    def run_refresh(self, run: RefreshRun) -> RefreshResult:
        pass


class BaseCandidateAssembler(ABC):
    @abstractmethod
    def assemble(self, refresh_run_id: str, refs: Dict[str, Any]) -> CandidateBundle:
        pass


class BaseDecayChecker(ABC):
    @abstractmethod
    def check_decay(self, active_bundle_id: str) -> List[DecayReport]:
        pass


class BasePromotionEvaluator(ABC):
    @abstractmethod
    def evaluate(self, bundle: CandidateBundle) -> PromotionCandidateReport:
        pass


class BaseBundleRegistry(ABC):
    @abstractmethod
    def register(self, bundle: CandidateBundle):
        pass

    @abstractmethod
    def get(self, bundle_id: str) -> CandidateBundle:
        pass
