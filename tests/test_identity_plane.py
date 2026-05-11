import pytest
from datetime import datetime, timezone, timedelta
from app.identity_plane.models import (
    PrincipalDefinition, CapabilityDefinition, AuthSession, SessionProvenance,
    ElevationRecord, ImpersonationRecord, GrantRecord, ScopeGrant
)
from app.identity_plane.enums import PrincipalClass, CapabilityRiskClass, SessionClass, TrustVerdict, ElevationClass, ImpersonationClass
from app.identity_plane.registry import CanonicalPrincipalRegistry
from app.identity_plane.authorization import AuthorizationEngine
from app.identity_plane.trust import IdentityTrustVerdictEngine

def test_principal_registry():
    reg = CanonicalPrincipalRegistry()

    # Must fail without owner
    from app.identity_plane.exceptions import InvalidPrincipalDefinition
    with pytest.raises(InvalidPrincipalDefinition):
        reg.register_principal(PrincipalDefinition(principal_id="bot1", principal_class=PrincipalClass.SERVICE_RUNTIME))

    # Success
    reg.register_principal(PrincipalDefinition(principal_id="bot1", principal_class=PrincipalClass.SERVICE_RUNTIME, owner_id="human1"))
    assert "bot1" in reg.principals

def test_authorization_and_elevation():
    reg = CanonicalPrincipalRegistry()
    reg.register_principal(PrincipalDefinition(principal_id="u1", principal_class=PrincipalClass.HUMAN_OPERATOR))
    reg.add_grant(GrantRecord(grant_id="g1", principal_id="u1", role_or_capability_id="read_only", is_role=False, scopes=[ScopeGrant(environment="live", resource_pattern="*")]))

    authz = AuthorizationEngine(reg)
    session = AuthSession(
        session_id="s1", principal_id="u1", session_class=SessionClass.INTERACTIVE,
        provenance=SessionProvenance(originating_principal_id="u1", auth_method="pwd", trigger_chain=[]),
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
    )
    authz.register_session(session)

    # Base capability works
    assert authz.evaluate("s1", "read_only", "live").is_allowed == True
    # Missing capability fails
    assert authz.evaluate("s1", "execute_trade", "live").is_allowed == False

    # JIT Elevation
    authz.add_elevation(ElevationRecord(
        record_id="e1", session_id="s1", elevation_class=ElevationClass.JUST_IN_TIME, granted_capabilities=["execute_trade"],
        approved_by="admin2", justification="incident_response", expires_at=datetime.now(timezone.utc) + timedelta(minutes=15)
    ))

    # After elevation, capability works
    assert authz.evaluate("s1", "execute_trade", "live").is_allowed == True

def test_impersonation_blockers():
    reg = CanonicalPrincipalRegistry()
    reg.register_principal(PrincipalDefinition(principal_id="u1", principal_class=PrincipalClass.HUMAN_OPERATOR))
    reg.register_principal(PrincipalDefinition(principal_id="target_admin", principal_class=PrincipalClass.HUMAN_OPERATOR))
    reg.add_grant(GrantRecord(grant_id="g1", principal_id="target_admin", role_or_capability_id="super_admin", is_role=False, scopes=[ScopeGrant(environment="live", resource_pattern="*")]))

    authz = AuthorizationEngine(reg)
    session = AuthSession(
        session_id="s1", principal_id="u1", session_class=SessionClass.INTERACTIVE,
        provenance=SessionProvenance(originating_principal_id="u1", auth_method="pwd", trigger_chain=[]),
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
    )
    authz.register_session(session)

    # Without impersonation, cannot act as super_admin
    assert authz.evaluate("s1", "super_admin", "live").is_allowed == False

    # Legitimate audited impersonation
    authz.add_impersonation(ImpersonationRecord(
        record_id="imp1", session_id="s1", impersonation_class=ImpersonationClass.APPROVED_ADMIN, target_principal_id="target_admin",
        approved_by="security_officer", justification="break_glass", expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)
    ))

    # After valid impersonation, can act as target
    assert authz.evaluate("s1", "super_admin", "live").is_allowed == True

def test_trust_verdict():
    reg = CanonicalPrincipalRegistry()
    reg.register_principal(PrincipalDefinition(principal_id="u1", principal_class=PrincipalClass.HUMAN_OPERATOR))

    # Add a stale grant
    reg.add_grant(GrantRecord(
        grant_id="g_stale", principal_id="u1", role_or_capability_id="old_role", is_role=False,
        scopes=[ScopeGrant(environment="live", resource_pattern="*")],
        expires_at=datetime.now(timezone.utc) - timedelta(days=1)
    ))

    authz = AuthorizationEngine(reg)
    trust_engine = IdentityTrustVerdictEngine(reg, authz)

    verdict = trust_engine.evaluate_trust("u1")
    assert verdict.verdict == TrustVerdict.DEGRADED
    assert "Stale grant detected" in verdict.caveats[0]
