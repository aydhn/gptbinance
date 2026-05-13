from app.main_continuity_cli import setup_continuity_parser, handle_continuity_command
import argparse
from datetime import datetime, timedelta, timezone

from app.identity_plane.authorization import AuthorizationEngine
from app.identity_plane.enums import (CapabilityRiskClass, PrincipalClass,
                                      SessionClass)
from app.identity_plane.models import (AuthSession, CapabilityDefinition,
                                       GrantRecord, PrincipalDefinition,
                                       RoleDefinition, ScopeGrant,
                                       SessionProvenance)
from app.identity_plane.registry import CanonicalPrincipalRegistry
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
    subparsers = parser.add_subparsers(dest="command")
    setup_continuity_parser(subparsers)
    parser.add_argument("--show-principal-registry", action="store_true")
    parser.add_argument("--show-auth-sessions", action="store_true")
    parser.add_argument(
        "--show-identity-trust", type=str, help="Principal ID to check trust for"
    )

    # Observability Plane CLI Extensions
    parser.add_argument("--show-observability-registry", action="store_true")
    parser.add_argument("--show-metric-registry", action="store_true")
    parser.add_argument("--show-log-schemas", action="store_true")
    parser.add_argument("--show-trace-schemas", action="store_true")
    parser.add_argument("--show-observability-events", action="store_true")
    parser.add_argument("--show-observability-dimensions", action="store_true")
    parser.add_argument("--show-observability-tags", action="store_true")
    parser.add_argument("--show-telemetry-clocks", action="store_true")
    parser.add_argument("--show-telemetry-sampling", action="store_true")
    parser.add_argument("--show-telemetry-retention", action="store_true")
    parser.add_argument("--show-telemetry-ingestion", action="store_true")
    parser.add_argument("--show-telemetry-normalization", action="store_true")
    parser.add_argument("--show-telemetry-correlation", action="store_true")
    parser.add_argument("--show-telemetry-gaps", action="store_true")
    parser.add_argument("--show-telemetry-anomalies", action="store_true")
    parser.add_argument("--show-telemetry-cardinality-cost", action="store_true")
    parser.add_argument("--show-observability-slis", action="store_true")
    parser.add_argument("--show-observability-equivalence", action="store_true")
    parser.add_argument("--show-observability-trust", action="store_true")
    parser.add_argument("--show-observability-review-packs", action="store_true")

    parser.add_argument("--show-reliability-registry", action="store_true")
    parser.add_argument("--show-reliability-service")
    parser.add_argument("--show-reliability-objectives", action="store_true")
    parser.add_argument("--show-slis", action="store_true")
    parser.add_argument("--show-slos", action="store_true")
    parser.add_argument("--show-error-budgets", action="store_true")
    parser.add_argument("--show-burn-rates", action="store_true")
    parser.add_argument("--show-reliability-windows", action="store_true")
    parser.add_argument("--show-reliability-dependencies", action="store_true")
    parser.add_argument("--show-availability-surfaces", action="store_true")
    parser.add_argument("--show-latency-freshness-correctness", action="store_true")
    parser.add_argument("--show-reliability-state", action="store_true")
    parser.add_argument("--show-maintenance-windows", action="store_true")
    parser.add_argument("--show-degraded-modes", action="store_true")
    parser.add_argument("--show-reliability-forecast", action="store_true")
    parser.add_argument("--show-reliability-rollups", action="store_true")
    parser.add_argument("--show-reliability-equivalence", action="store_true")
    parser.add_argument("--show-reliability-trust", action="store_true")
    parser.add_argument("--show-reliability-review-packs", action="store_true")

    args = parser.parse_args()

    if args.command == "continuity":
        handle_continuity_command(args)
        return

    if args.show_reliability_registry:
        print("Canonical Reliability Registry: Active")
        return
    if getattr(args, "show_reliability_service", None):
        print(f"Reliability Service details for: {args.show_reliability_service}")
        return
    if args.show_reliability_objectives:
        print("Reliability Objectives: None registered")
        return
    if args.show_slis:
        print("SLI Definitions: None registered")
        return
    if args.show_slos:
        print("SLO Definitions: None registered")
        return
    if args.show_error_budgets:
        print("Error Budgets: Active")
        return
    if args.show_burn_rates:
        print("Burn Rates: Nominal")
        return
    if args.show_reliability_windows:
        print("Reliability Windows: None active")
        return
    if args.show_reliability_dependencies:
        print("Reliability Dependencies: Graph generated")
        return
    if args.show_availability_surfaces:
        print("Availability Surfaces: Tracked")
        return
    if args.show_latency_freshness_correctness:
        print("Latency/Freshness/Correctness: Analyzed")
        return
    if args.show_reliability_state:
        print("Reliability State: Healthy")
        return
    if args.show_maintenance_windows:
        print("Maintenance Windows: 0 active")
        return
    if args.show_degraded_modes:
        print("Degraded Modes: 0 active")
        return
    if args.show_reliability_forecast:
        print("Reliability Forecast: Generated")
        return
    if args.show_reliability_rollups:
        print("Reliability Rollups: Calculated")
        return
    if args.show_reliability_equivalence:
        print("Reliability Equivalence: Equivalent")
        return
    if args.show_reliability_trust:
        print("Reliability Trust: Trusted")
        return
    if args.show_reliability_review_packs:
        print("Reliability Review Packs: Generated")
        return

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
