from typing import List, Optional
from uuid import UUID
from datetime import datetime, timezone

from app.identity.enums import AuthorizationVerdict, CapabilityClass, TrustZone
from app.identity.models import (
    AuthorizationRequest,
    AuthorizationDecision,
    AuthorizationProof,
)
from app.identity.storage import identity_storage
from app.identity.principals import principal_registry
from app.identity.capabilities import capability_registry
from app.identity.zones import zone_registry
from app.identity.policies import policy_engine


class AuthorizationEngine:
    def evaluate(self, request: AuthorizationRequest) -> AuthorizationDecision:
        reasons = []

        principal = principal_registry.resolve_principal(request.principal_id)
        if not principal:
            return AuthorizationDecision(
                verdict=AuthorizationVerdict.DENY, reasons=["Principal not found."]
            )

        # 1. Policy Hard Blocks
        blocks = policy_engine.check_hard_blocks(principal, request.target_zone)
        if blocks:
            return AuthorizationDecision(
                verdict=AuthorizationVerdict.DENY, reasons=blocks
            )

        # 2. Zone Check
        if not zone_registry.is_in_zone(request.principal_id, request.target_zone):
            reasons.append(
                f"Principal not bound to required trust zone: {request.target_zone.name}"
            )
            return AuthorizationDecision(
                verdict=AuthorizationVerdict.DENY, reasons=reasons
            )

        # 3. Capability Check
        if not capability_registry.evaluate(
            request.principal_id, request.required_capabilities
        ):
            reasons.append("Principal lacks required capabilities.")
            return AuthorizationDecision(
                verdict=AuthorizationVerdict.DENY, reasons=reasons
            )

        # Note: In a full impl, we would also check scopes, session validity, SoD here.

        return AuthorizationDecision(
            verdict=AuthorizationVerdict.ALLOW, reasons=["All checks passed."]
        )


authorization_engine = AuthorizationEngine()
