from abc import ABC, abstractmethod
from typing import Dict, Any

from app.remediation.models import (
    RemediationFindingRef,
    RemediationPack,
    ApplyResult,
    RollbackPlan,
)


class RecipeCompilerBase(ABC):
    @abstractmethod
    def compile_pack(self, finding: RemediationFindingRef) -> RemediationPack:
        pass


class PreflightEngineBase(ABC):
    @abstractmethod
    def run_preflight(self, pack: RemediationPack) -> Dict[str, Any]:
        pass


class ApplyExecutorBase(ABC):
    @abstractmethod
    def execute(self, pack: RemediationPack) -> ApplyResult:
        pass


class RollbackPlannerBase(ABC):
    @abstractmethod
    def plan_rollback(self, pack: RemediationPack) -> RollbackPlan:
        pass
