import argparse
from datetime import datetime, timezone, timedelta
from app.identity_plane.models import (
    PrincipalDefinition,
    CapabilityDefinition,
    RoleDefinition,
    GrantRecord,
    ScopeGrant,
    AuthSession,
    SessionProvenance,
)
from app.identity_plane.enums import PrincipalClass, CapabilityRiskClass, SessionClass
from app.identity_plane.registry import CanonicalPrincipalRegistry
from app.identity_plane.authorization import AuthorizationEngine
from app.identity_plane.trust import IdentityTrustVerdictEngine


def setup_mock_identity():
    reg = CanonicalPrincipalRegistry()
    reg.register_principal(
        PrincipalDefinition(
            principal_id="admin_user_1", principal_class=PrincipalClass.HUMAN_OPERATOR
        )
    )
    reg.register_principal(
        PrincipalDefinition(
            principal_id="deploy_bot",
            principal_class=PrincipalClass.SERVICE_RUNTIME,
            owner_id="admin_user_1",
        )
    )

    reg.register_capability(
        CapabilityDefinition(
            capability_id="execute_trade",
            risk_class=CapabilityRiskClass.HIGH,
            description="Execute live trades",
        )
    )
    reg.register_role(
        RoleDefinition(role_id="trader_role", capabilities=["execute_trade"])
    )

    reg.add_grant(
        GrantRecord(
            grant_id="g1",
            principal_id="admin_user_1",
            role_or_capability_id="trader_role",
            is_role=True,
            scopes=[ScopeGrant(environment="live", resource_pattern="*")],
        )
    )

    authz = AuthorizationEngine(reg)
    session = AuthSession(
        session_id="sess_123",
        principal_id="admin_user_1",
        session_class=SessionClass.INTERACTIVE,
        provenance=SessionProvenance(
            originating_principal_id="admin_user_1", auth_method="mfa", trigger_chain=[]
        ),
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )
    authz.register_session(session)
    return reg, authz


def main():
    parser = argparse.ArgumentParser(
        description="Trading Platform CLI (Identity Plane)"
    )
    parser.add_argument("--show-principal-registry", action="store_true")
    parser.add_argument("--show-auth-sessions", action="store_true")
    parser.add_argument(
        "--show-identity-trust", type=str, help="Principal ID to check trust for"
    )
    args = parser.parse_args()

    reg, authz = setup_mock_identity()

    if args.show_principal_registry:
        print("=== CANONICAL PRINCIPAL REGISTRY ===")
        for p in reg.principals.values():
            print(
                f"- {p.principal_id} [{p.principal_class.value}] (Owner: {p.owner_id}, State: {p.state.value})"
            )

    if args.show_auth_sessions:
        print("=== ACTIVE AUTH SESSIONS ===")
        for s in authz.active_sessions.values():
            print(
                f"- Session: {s.session_id} | Principal: {s.principal_id} | Active: {s.is_active}"
            )
            print(
                f"  Provenance: {s.provenance.auth_method} via {s.provenance.originating_principal_id}"
            )

    if args.show_identity_trust:
        trust_engine = IdentityTrustVerdictEngine(reg, authz)
        verdict = trust_engine.evaluate_trust(args.show_identity_trust)
        print("=== IDENTITY TRUST VERDICT ===")
        print(f"Principal: {verdict.principal_id}")
        print(f"Verdict: {verdict.verdict.value.upper()}")
        print(f"Blockers: {verdict.blockers}")
        print(f"Caveats: {verdict.caveats}")


if __name__ == "__main__":
    main()
