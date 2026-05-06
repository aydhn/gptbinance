from typing import List, Optional
from uuid import UUID
from datetime import datetime, timezone

from app.identity.models import DelegationRecord
from app.identity.enums import DelegationClass, CapabilityClass
from app.identity.storage import identity_storage


class DelegationManager:
    # Some capabilities cannot be delegated
    NON_DELEGABLE = {
        CapabilityClass.FINALIZE_POSTMORTEM,
        CapabilityClass.REVIEW_BREAKGLASS,
    }

    def delegate(
        self,
        delegator_id: UUID,
        delegatee_id: UUID,
        capabilities: List[CapabilityClass],
        expires_at: datetime,
    ) -> Optional[DelegationRecord]:
        # Check non-delegable
        for cap in capabilities:
            if cap in self.NON_DELEGABLE:
                raise ValueError(f"Capability {cap.name} is non-delegable.")

        # In a real impl, ensure delegator actually HAS the capabilities they are delegating

        record = DelegationRecord(
            delegator_id=delegator_id,
            delegatee_id=delegatee_id,
            delegation_class=DelegationClass.STANDARD,
            capabilities=capabilities,
            granted_at=datetime.now(timezone.utc),
            expires_at=expires_at,
        )
        identity_storage.save_delegation(record)
        return record

    def list_all(self) -> List[DelegationRecord]:
        return identity_storage.get_all_delegations()


delegation_manager = DelegationManager()
