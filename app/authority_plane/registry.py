from typing import Dict, List, Optional
# pylint: disable=unused-import
# flake8: noqa
from .base import AuthorityRegistryBase
from .models import AuthorityObject
from .exceptions import InvalidAuthorityObjectError

class CanonicalAuthorityRegistry(AuthorityRegistryBase):
    """
    Canonical authority registry explicitly separating facts, claims,
    and ensuring robust authority object tracking.
    """
    def __init__(self):
        self._registry: Dict[str, AuthorityObject] = {}
        self.families = [
            "release_approval_authority", "migration_acceptance_authority",
            "security_exception_authority", "compliance_attestation_authority",
            "customer_promise_authority", "finality_verdict_authority",
            "remedy_sufficiency_authority", "autonomy_override_authority",
            "federated_decision_authority", "contractual_acceptance_authority",
            "constitutional_override_authority", "cross_plane_binding_authority"
        ]

    def register(self, authority: AuthorityObject) -> str:
        if not authority.authority_id:
            raise InvalidAuthorityObjectError("Authority must have an explicit ID")
        if authority.authority_id in self._registry:
            raise InvalidAuthorityObjectError("Authority ID already exists")

        self._registry[authority.authority_id] = authority
        return authority.authority_id

    def get(self, authority_id: str) -> AuthorityObject:
        if authority_id not in self._registry:
            raise InvalidAuthorityObjectError(f"Authority {authority_id} not found in canonical registry")
        return self._registry[authority_id]

    def list_all(self) -> List[AuthorityObject]:
        return list(self._registry.values())

    def find_by_owner(self, owner: str) -> List[AuthorityObject]:
        return [obj for obj in self._registry.values() if obj.owner == owner]
