from datetime import datetime, timezone
from app.identity_plane.models import IdentityTrustVerdictDetails
from app.identity_plane.enums import TrustVerdict, PrincipalClass
from app.identity_plane.registry import CanonicalPrincipalRegistry
from app.identity_plane.authorization import AuthorizationEngine

class IdentityTrustVerdictEngine:
    def __init__(self, registry: CanonicalPrincipalRegistry, authz: AuthorizationEngine):
        self.registry = registry
        self.authz = authz

    def evaluate_trust(self, principal_id: str) -> IdentityTrustVerdictDetails:
        blockers = []
        caveats = []

        principal = self.registry.principals.get(principal_id)
        if not principal:
            return IdentityTrustVerdictDetails(principal_id=principal_id, verdict=TrustVerdict.BLOCKED, blockers=["Principal not found"], caveats=[])

        if principal.state != "active":
            blockers.append(f"Principal state is {principal.state}")

        if principal.principal_class == PrincipalClass.SERVICE_RUNTIME and not principal.owner_id:
            blockers.append("Orphan service account detected (no owner)")

        if principal_id in self.authz.revocations:
            blockers.append("Principal is revoked")

        now = datetime.now(timezone.utc)
        for grant in self.registry.grants:
            if grant.principal_id == principal_id and grant.expires_at and grant.expires_at < now:
                caveats.append(f"Stale grant detected: {grant.grant_id}")

        if blockers:
            return IdentityTrustVerdictDetails(principal_id=principal_id, verdict=TrustVerdict.BLOCKED, blockers=blockers, caveats=caveats)
        elif caveats:
            return IdentityTrustVerdictDetails(principal_id=principal_id, verdict=TrustVerdict.DEGRADED, blockers=blockers, caveats=caveats)

        return IdentityTrustVerdictDetails(principal_id=principal_id, verdict=TrustVerdict.TRUSTED, blockers=[], caveats=[])
