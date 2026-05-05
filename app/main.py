import argparse
from datetime import datetime, timezone

from app.remediation.models import RemediationFindingRef
from app.remediation.compiler import RemediationCompiler
from app.remediation.blast_radius import BlastRadiusAnalyzer
from app.remediation.simulation import DryRunEngine
from app.remediation.apply import ApplyExecutor
from app.remediation.verification import VerificationEngine
from app.remediation.debt import DebtGovernance
from app.remediation.preflight import PreflightEngine
from app.remediation.rollback import RollbackPlanner
from app.remediation.reporting import RemediationReporter


def main():
    parser = argparse.ArgumentParser(
        description="Trading Platform Remediation Orchestration CLI"
    )
    parser.add_argument(
        "--build-remediation-pack",
        type=str,
        help="Finding ID to build pack for",
        metavar="FINDING_ID",
    )
    parser.add_argument("--show-remediation-pack", type=str, help="Show pack details")
    parser.add_argument(
        "--show-remediation-blast-radius",
        type=str,
        help="Show blast radius for pack ID",
    )
    parser.add_argument(
        "--run-remediation-preflight", type=str, help="Run preflight checks"
    )
    parser.add_argument(
        "--run-remediation-dry-run", type=str, help="Simulate pack apply"
    )
    parser.add_argument(
        "--request-remediation-apply",
        type=str,
        help="Apply or generate request for pack",
    )
    parser.add_argument(
        "--show-remediation-apply-history",
        action="store_true",
        help="Show apply history",
    )
    parser.add_argument(
        "--show-remediation-verification", type=str, help="Show verification for pack"
    )
    parser.add_argument(
        "--show-remediation-debt",
        action="store_true",
        help="Show outstanding remediation debt",
    )
    parser.add_argument(
        "--show-remediation-rollback-plan", type=str, help="Show rollback plan for pack"
    )
    parser.add_argument(
        "--show-remediation-evidence", type=str, help="Show evidence for pack"
    )
    parser.add_argument(
        "--show-remediation-conflicts", type=str, help="Show conflicts for pack"
    )

    args = parser.parse_args()

    # Mock finding for demonstration
    mock_finding = RemediationFindingRef(
        finding_id=args.build_remediation_pack or "FND-999",
        source_domain="order_lifecycle",
        severity="high",
        detected_at=datetime.now(timezone.utc),
        context={"symbol": "BTCUSDT", "issue": "orphan_order_detected"},
    )

    compiler = RemediationCompiler()
    analyzer = BlastRadiusAnalyzer()
    simulator = DryRunEngine()
    executor = ApplyExecutor()
    verifier = VerificationEngine()
    debt_gov = DebtGovernance()
    preflight = PreflightEngine()
    rollback = RollbackPlanner()
    reporter = RemediationReporter()

    if args.build_remediation_pack:
        pack = compiler.compile_pack(mock_finding)
        print(reporter.format_pack_summary(pack))

    elif args.show_remediation_pack:
        pack = compiler.compile_pack(mock_finding)
        print(reporter.format_pack_summary(pack))

    elif args.show_remediation_blast_radius:
        pack = compiler.compile_pack(mock_finding)
        report = analyzer.analyze(pack)
        print(reporter.format_blast_radius(report))

    elif args.run_remediation_preflight:
        pack = compiler.compile_pack(mock_finding)
        report = preflight.run_preflight(pack)
        print(f"\n=== PREFLIGHT REPORT ===")
        print(f"Passed: {report['passed']}")
        if report["blockers"]:
            print(f"Blockers: {report['blockers']}")
        if report["warnings"]:
            print(f"Warnings: {report['warnings']}")
        print("======================\n")

    elif args.run_remediation_dry_run:
        pack = compiler.compile_pack(mock_finding)
        res = simulator.simulate(pack)
        print(reporter.format_simulation(res))

    elif args.request_remediation_apply:
        pack = compiler.compile_pack(mock_finding)
        res = executor.execute(pack)
        print("\n=== APPLY OUTCOME ===")
        print(f"Mode Used: {res.mode_used.value}")
        if res.generated_request_id:
            print(f"Action: GENERATED APPROVAL REQUEST [{res.generated_request_id}]")
            print(f"Reason: {res.error_message}")
        else:
            print("Action: DIRECT SAFE APPLY COMPLETED")
            print(
                f"Before/After Snapshots: {res.before_snapshot_ref} -> {res.after_snapshot_ref}"
            )

        verdict = verifier.verify(pack)
        print(f"\nPost-Apply Verification: {verdict.verdict.value} - {verdict.details}")
        print("=====================\n")

    elif args.show_remediation_apply_history:
        print("\n=== APPLY HISTORY ===")
        print("Mock: No history available in mock state.")
        print("=====================\n")

    elif args.show_remediation_verification:
        pack = compiler.compile_pack(mock_finding)
        verdict = verifier.verify(pack)
        print(f"\n=== VERIFICATION ===")
        print(f"Verdict: {verdict.verdict.value}")
        print(f"Details: {verdict.details}")
        print("====================\n")

    elif args.show_remediation_debt:
        debts = debt_gov.assess_debt([mock_finding])
        print("\n=== REMEDIATION DEBT GOVERNANCE ===")
        for d in debts:
            print(
                f"Debt ID: {d.debt_id} | Sev: {d.severity.value} | Aging: {d.aging_days} days | Qual Blocker: {d.is_qualification_blocker}"
            )
        print("===================================\n")

    elif args.show_remediation_rollback_plan:
        pack = compiler.compile_pack(mock_finding)
        plan = rollback.plan_rollback(pack)
        print("\n=== ROLLBACK PLAN ===")
        print(f"Eligible: {plan.is_eligible}")
        if not plan.is_eligible:
            print(f"Reason: {plan.reason_if_not_eligible}")
        else:
            print(f"Steps: {plan.steps}")
        print("=====================\n")

    elif args.show_remediation_evidence:
        print("\n=== EVIDENCE ===")
        print("Mock: Fetching evidence bundle for pack...")
        print("Contains: Finding Ref, Pack Manifest, Apply Result, Verification Result")
        print("================\n")

    elif args.show_remediation_conflicts:
        print("\n=== CONFLICTS ===")
        print("Mock: No conflicting packs found in active registry.")
        print("=================\n")


if __name__ == "__main__":
    main()
