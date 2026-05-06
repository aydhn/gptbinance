from uuid import uuid4
from app.identity.enums import (
    PrincipalType,
    CapabilityClass,
    TrustZone,
    AuthorizationVerdict,
)
from app.identity.models import PrincipalRecord, AuthorizationRequest
from app.identity.principals import principal_registry
from app.identity.capabilities import capability_registry
from app.identity.zones import zone_registry
from app.identity.proofs import proof_builder


def test_authorization_allow():
    p = PrincipalRecord(name="Authz User", principal_type=PrincipalType.HUMAN)
    principal_registry.register_principal(p)

    capability_registry.grant_capability(p.id, CapabilityClass.REQUEST_MIGRATION_APPLY)
    zone_registry.bind_zone(p.id, TrustZone.RUNTIME_SENSITIVE)

    req = AuthorizationRequest(
        principal_id=p.id,
        action="apply_migration",
        required_capabilities=[CapabilityClass.REQUEST_MIGRATION_APPLY],
        target_zone=TrustZone.RUNTIME_SENSITIVE,
    )

    proof = proof_builder.build_proof(req)
    assert proof.verdict == AuthorizationVerdict.ALLOW


def test_authorization_deny_missing_cap():
    p = PrincipalRecord(name="Authz User 2", principal_type=PrincipalType.HUMAN)
    principal_registry.register_principal(p)

    # Intentionally omitted capability grant
    zone_registry.bind_zone(p.id, TrustZone.RUNTIME_SENSITIVE)

    req = AuthorizationRequest(
        principal_id=p.id,
        action="apply_migration",
        required_capabilities=[CapabilityClass.REQUEST_MIGRATION_APPLY],
        target_zone=TrustZone.RUNTIME_SENSITIVE,
    )

    proof = proof_builder.build_proof(req)
    assert proof.verdict == AuthorizationVerdict.DENY
    assert "Principal lacks required capabilities." in proof.denial_reasons
