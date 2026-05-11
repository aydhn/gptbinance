from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
from app.compliance_plane.models import ComplianceTrustVerdict, AuditReadinessReport


class RequirementRegistryBase(ABC):
    @abstractmethod
    def register_requirement(self, requirement: Any) -> None:
        pass

    @abstractmethod
    def get_requirement(self, req_id: str) -> Optional[Any]:
        pass


class ControlEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_control(self, control_id: str) -> bool:
        pass


class AuditReadinessEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_readiness(self, scope: Dict[str, Any]) -> AuditReadinessReport:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self) -> ComplianceTrustVerdict:
        pass
