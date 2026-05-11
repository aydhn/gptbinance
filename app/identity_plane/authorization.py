from datetime import datetime, timezone
from typing import Set, Dict, List
from app.identity_plane.models import AuthSession, ElevationRecord, ImpersonationRecord, AuthzEvaluationRecord
from app.identity_plane.registry import CanonicalPrincipalRegistry

class AuthorizationEngine:
    def __init__(self, registry: CanonicalPrincipalRegistry):
        self.registry = registry
        self.active_sessions: Dict[str, AuthSession] = {}
        self.elevations: Dict[str, ElevationRecord] = {}
        self.impersonations: Dict[str, ImpersonationRecord] = {}
        self.revocations: Set[str] = set()

    def register_session(self, session: AuthSession):
        self.active_sessions[session.session_id] = session

    def add_elevation(self, elevation: ElevationRecord):
        self.elevations[elevation.session_id] = elevation

    def add_impersonation(self, impersonation: ImpersonationRecord):
        self.impersonations[impersonation.session_id] = impersonation

    def revoke_principal(self, principal_id: str):
        self.revocations.add(principal_id)

    def evaluate(self, session_id: str, required_capability: str, environment: str) -> AuthzEvaluationRecord:
        deny_reasons = []
        session = self.active_sessions.get(session_id)

        if not session:
            return AuthzEvaluationRecord(session_id=session_id, capability=required_capability, environment=environment, is_allowed=False, deny_reasons=["Session not found"])

        if not session.is_active:
            deny_reasons.append("Session is inactive")
        elif session.expires_at < datetime.now(timezone.utc):
            session.is_active = False
            deny_reasons.append("Session expired")

        effective_principal = session.principal_id

        impersonation = self.impersonations.get(session_id)
        if impersonation and impersonation.expires_at > datetime.now(timezone.utc):
            effective_principal = impersonation.target_principal_id

        if effective_principal in self.revocations:
            deny_reasons.append("Principal is revoked")

        principal_def = self.registry.principals.get(effective_principal)
        if not principal_def or principal_def.state != "active":
            deny_reasons.append(f"Principal {effective_principal} is not active")

        caps = set()
        if not deny_reasons:
            caps = set(self.registry.get_principal_capabilities(effective_principal, environment))
            elevation = self.elevations.get(session_id)
            if elevation and elevation.expires_at > datetime.now(timezone.utc):
                caps.update(elevation.granted_capabilities)

            if required_capability not in caps:
                deny_reasons.append(f"Missing capability: {required_capability}")

        is_allowed = len(deny_reasons) == 0
        return AuthzEvaluationRecord(
            session_id=session_id,
            capability=required_capability,
            environment=environment,
            is_allowed=is_allowed,
            deny_reasons=deny_reasons
        )
