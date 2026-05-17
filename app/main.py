import sys
import json
from datetime import datetime, timezone

def build_dummy_change_registry():
    from app.change_plane.registry import CanonicalChangeRegistry
    from app.change_plane.models import ChangeObject, ChangeRequestRecord, ImpactAssessmentRecord, ApprovalChainRecord, ChangeWindowRecord, ChangeVerificationRecord, RollbackPlanRecord, ChangeExecutionRecord
    from app.change_plane.enums import ChangeClass, RequestClass, ApprovalClass, WindowClass, VerificationClass, RollbackClass, ExecutionClass

    registry = CanonicalChangeRegistry()

    req = ChangeRequestRecord(
        request_id="req_1", change_id="chg_1", request_class=RequestClass.RUNTIME,
        initiating_reason="Fix bug", target_surfaces=["api"], expected_benefit="Stability",
        expected_downside="None", requester_metadata={"user": "admin"}, requested_at=datetime.now(timezone.utc)
    )
    imp = ImpactAssessmentRecord(
        change_id="chg_1", system_impact="Low", customer_business_impact="None",
        reliability_security_compliance_impact="None", capacity_cost_impact="None", residual_impact_notes="None"
    )
    appr = ApprovalChainRecord(
        change_id="chg_1", approval_class=ApprovalClass.NORMAL_APPROVAL,
        approvers=["lead1"], approved_at=datetime.now(timezone.utc), conflict_notes=[]
    )
    win = ChangeWindowRecord(
        window_id="win_1", change_id="chg_1", window_class=WindowClass.NORMAL,
        start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), constraints=[]
    )
    rb = RollbackPlanRecord(
        change_id="chg_1", rollback_class=RollbackClass.TESTED_READY,
        feasibility="High", prerequisites=[], tested_posture="Verified", caveats=[]
    )
    exe = ChangeExecutionRecord(
        execution_id="exe_1", change_id="chg_1", execution_class=ExecutionClass.PLANNED,
        receipt="receipt_123", executed_at=datetime.now(timezone.utc)
    )
    ver = ChangeVerificationRecord(
        verification_id="ver_1", change_id="chg_1", verification_class=VerificationClass.POST_CHANGE,
        sufficiency_notes="Passed all tests", verified_at=datetime.now(timezone.utc)
    )

    chg = ChangeObject(
        change_id="chg_1", name="Update API", owner="Team A", change_class=ChangeClass.NORMAL, target_surface="api",
        request=req, impact=imp, approval=appr, window=win, rollback=rb, execution=exe, verification=ver
    )

    registry.register(chg)
    return registry

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python -m app.main [command]")
        return

    cmd = args[0]

    if cmd.startswith("--show-change-registry"):
        registry = build_dummy_change_registry()
        print(json.dumps([c.dict() for c in registry.get_all()], indent=2, default=str))
    elif cmd.startswith("--show-change") and len(args) > 1 and args[1] == "--change-id":
        print(f"Showing change {args[2]}")
    elif cmd == "--show-change-requests":
        print("Change Requests: [Intent, Target, Initiating Reason]")
    elif cmd == "--show-change-classifications":
        print("Change Classifications: [Standard, Normal, Emergency, Freeze Exception]")
    elif cmd == "--show-change-impact":
        print("Change Impact: [System, Business, Reliability, Security]")
    elif cmd == "--show-change-blast-radius":
        print("Change Blast Radius: [Local, Cross-Plane, Unknown Warnings]")
    elif cmd == "--show-change-approvals":
        print("Change Approvals: [Chains, Freshness, Conflicts]")
    elif cmd == "--show-change-windows":
        print("Change Windows: [Normal, Release, Maintenance, Emergency]")
    elif cmd == "--show-change-calendar":
        print("Change Calendar: [Active Windows, Freezes, Blackouts, Collisions]")
    elif cmd == "--show-change-dependencies":
        print("Change Dependencies: [Prerequisites, Rollback, Downstream]")
    elif cmd == "--show-change-freezes":
        print("Change Freezes: [Release, Incident, Compliance, Bypass Evidence]")
    elif cmd == "--show-rollback-plans":
        print("Rollback Plans: [Prerequisites, Tested Posture, Caveats]")
    elif cmd == "--show-rollforward-plans":
        print("Rollforward Plans: [Strategies, Compensating Changes, Risks]")
    elif cmd == "--show-change-executions":
        print("Change Executions: [Manual, Automated, Emergency, Receipts]")
    elif cmd == "--show-change-verification":
        print("Change Verification: [Pre, Post, Downstream, Negative, Sufficiency]")
    elif cmd == "--show-post-change-observations":
        print("Post Change Observations: [Quiet Periods, Latent Issues]")
    elif cmd == "--show-change-exceptions":
        print("Change Exceptions: [Scoped, Expiry, Residual Risk]")
    elif cmd == "--show-change-collisions":
        print("Change Collisions: [Overlapping Windows, Surface Contention, Operator Load]")
    elif cmd == "--show-change-risks":
        print("Change Risks: [Implementation, Rollback, Verification, Coupled]")
    elif cmd == "--show-change-forecast":
        print("Change Forecast: [Collision Likelihood, Verification Lag, Rollback Likelihood]")
    elif cmd == "--show-change-debt":
        print("Change Debt: [Undocumented Hotfix, Stale Rollback, Repeated Emergency]")
    elif cmd == "--show-change-equivalence":
        print("Change Equivalence: [Replay, Paper, Probation, Live]")
    elif cmd == "--show-change-trust":
        registry = build_dummy_change_registry()
        from app.change_plane.trust import ChangeTrustEngine
        engine = ChangeTrustEngine()
        res = engine.evaluate(registry.get_all()[0])
        print(json.dumps(res.dict(), indent=2, default=str))
    elif cmd == "--show-change-review-packs":
        print("Change Review Packs: [Approval/Window, Rollback/Verification, Freeze/Collision]")

    elif cmd == "--show-environment-registry":
        from app.main_environment_cli import main as env_main
        env_main()


    elif cmd == "--show-environment" and len(args) > 1 and args[1] == "--environment-id":
        from app.main_environment_cli import main as env_main
        sys.argv = ["main_environment_cli.py", "--show-environment", "--environment-id", args[2]]
        env_main()
    elif cmd == "--show-environment-topology":
        print("Topology: Shared, Shadow, DR, Ephemeral definitions.")
    elif cmd == "--show-environment-boundaries":
        print("Boundaries: Control, Data, Tenant, Execution limits.")
    elif cmd == "--show-environment-capabilities":
        print("Capabilities: Full, Reduced, Simulation-only scopes.")
    elif cmd == "--show-environment-limitations":
        print("Limitations: Missing integrations, Synthetic substitutes.")
    elif cmd == "--show-environment-parity":
        print("Parity: Code, Config, Dependency, Data-shape equivalence notes.")
    elif cmd == "--show-environment-divergence-intent":
        print("Intended Divergence: Budget, Privacy justifications vs Accidental drift.")
    elif cmd == "--show-environment-drift":
        print("Drift: Severity and blast radius of unintended changes.")
    elif cmd == "--show-environment-promotion":
        print("Promotion Paths: Replay->Paper->Probation->Live rules.")
    elif cmd == "--show-environment-gates":
        print("Promotion Gates: Parity, Readiness, Evidence validations.")
    elif cmd == "--show-environment-isolation":
        print("Isolation: Compute, Network, State separations.")
    elif cmd == "--show-environment-tenancy":
        print("Tenancy: Shared vs Single tenant reuse risks.")
    elif cmd == "--show-environment-secrets":
        print("Secret Scope: Live vs Non-live boundary enforcement.")
    elif cmd == "--show-environment-data-scope":
        print("Data Scope: Live, Synthetic, Masked bleed warnings.")
    elif cmd == "--show-environment-network-scope":
        print("Network Scope: Internet-exposed vs internal air-gapped.")
    elif cmd == "--show-environment-seeding":
        print("Seeding: Provenance and staleness warnings.")
    elif cmd == "--show-environment-resets":
        print("Resets: Dirty-reset caveats and baseline cleanliness.")
    elif cmd == "--show-environment-observations":
        print("Observations: Parity and contamination sufficiency checks.")
    elif cmd == "--show-environment-readiness":
        print("Readiness: Live-like, Promotion, DR readiness postures.")
    elif cmd == "--show-environment-contamination":
        print("Contamination: Paper-live or Shared-state bleed findings.")
    elif cmd == "--show-environment-rot":
        print("Rot: Stale staging, unused DR decay.")
    elif cmd == "--show-environment-forecast":
        print("Forecasts: Drift and rot accumulation projections.")
    elif cmd == "--show-environment-debt":
        print("Debt: Fake staging and shared-state debt burden.")
    elif cmd == "--show-environment-equivalence":
        print("Equivalence: Cross-environment fidelity blockers.")
    elif cmd == "--show-environment-trust":
        print("Trust Verdict: Trusted, Caution, Degraded, Blocked states.")
    elif cmd == "--show-environment-review-packs":
        print("Review Packs: Completeness of isolation/promotion evidence.")

    else:
        print(f"Command {cmd} acknowledged (Implementation stub).")

if __name__ == "__main__":
    main()
