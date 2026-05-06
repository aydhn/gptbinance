from typing import List, Dict
from uuid import UUID
from app.identity.enums import TrustZone, CapabilityClass, PrincipalStatus
from app.identity.models import PrincipalRecord


class IdentityPolicyEngine:
    """
    Enforces high-level invariants that must not be violated, regardless of specific capability checks.
    """

    def check_hard_blocks(
        self, principal: PrincipalRecord, target_zone: TrustZone
    ) -> List[str]:
        blocks = []
        if principal.status == PrincipalStatus.SUSPENDED:
            blocks.append("Principal is suspended.")

        if principal.status == PrincipalStatus.REVIEW_ONLY and target_zone in [
            TrustZone.RUNTIME_SENSITIVE,
            TrustZone.RELEASE_CONTROLLED,
        ]:
            blocks.append("REVIEW_ONLY principal cannot access operational zones.")

        return blocks


policy_engine = IdentityPolicyEngine()
