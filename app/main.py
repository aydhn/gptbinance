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
    else:
        print(f"Command {cmd} acknowledged (Implementation stub).")

if __name__ == "__main__":
    main()
