from typing import List
from uuid import UUID
from datetime import datetime, timezone
from app.identity.enums import CapabilityClass
from app.identity.models import CapabilityGrant
from app.identity.base import CapabilityEvaluatorBase
from app.identity.storage import identity_storage


class CapabilityRegistry(CapabilityEvaluatorBase):
    def grant_capability(
        self, principal_id: UUID, capability: CapabilityClass, granted_by: UUID = None
    ) -> None:
        grant = CapabilityGrant(
            principal_id=principal_id,
            capability=capability,
            granted_at=datetime.now(timezone.utc),
            granted_by=granted_by,
        )
        identity_storage.save_capability_grant(grant)

    def evaluate(
        self, principal_id: UUID, required_capabilities: List[CapabilityClass]
    ) -> bool:
        grants = identity_storage.get_capabilities(principal_id)
        granted_caps = {g.capability for g in grants}
        return all(req in granted_caps for req in required_capabilities)

    def list_all_capabilities(self) -> List[CapabilityClass]:
        return list(CapabilityClass)


capability_registry = CapabilityRegistry()
