from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from app.identity.models import (
    PrincipalRecord,
    AuthorizationProof,
    AuthorizationRequest,
)
from app.identity.enums import CapabilityClass


class PrincipalResolverBase(ABC):
    @abstractmethod
    def resolve_principal(self, principal_id: UUID) -> Optional[PrincipalRecord]:
        pass


class CapabilityEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(
        self, principal_id: UUID, required_capabilities: List[CapabilityClass]
    ) -> bool:
        pass


class SessionValidatorBase(ABC):
    @abstractmethod
    def validate_session(self, session_id: UUID) -> bool:
        pass


class AuthorizationProofBuilderBase(ABC):
    @abstractmethod
    def build_proof(self, request: AuthorizationRequest) -> AuthorizationProof:
        pass
