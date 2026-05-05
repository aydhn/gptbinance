import argparse
from app.migrations.reporting import ReportingEngine
from app.migrations.models import MigrationPlan
from datetime import datetime
from app.migrations.registry import migration_registry
from app.migrations.domains import MigrationDomain
from datetime import datetime, timezone
import json

from app.policy_kernel.evaluation import evaluate_policy
from app.policy_kernel.context import assemble_policy_context
from app.policy_kernel.evidence import assemble_evidence_bundle
from app.policy_kernel.storage import get_decision, get_conflicts
from app.policy_kernel.rules import list_rules
from app.policy_kernel.invariants import list_invariants
from app.policy_kernel.waivers import list_active_waivers
from app.policy_kernel.drift import list_drifts
from app.policy_kernel.gaps import list_gaps
from app.policy_kernel.reporting import generate_policy_audit_summary
from app.policy_kernel.proofs import generate_decision_proof


def parse_args():
    parser = argparse.ArgumentParser(description="Trading Platform Core")
    # Migration Fabric CLI commands
    parser.add_argument("--build-migration-plan", action="store_true", help="Build a plan for pending migrations")
    parser.add_argument("--show-migration-plan", type=str, help="Show steps for a given plan-id")
    parser.add_argument("--show-migration-compatibility", type=str, help="Show compatibility verdict for a plan-id")
    parser.add_argument("--show-migration-matrix", action="store_true", help="Show active compatibility matrix")
    parser.add_argument("--run-migration-preflight", type=str, help="Run preflight checks for a plan-id")
    parser.add_argument("--run-migration-dry-run", type=str, help="Run dry-run simulation for a plan-id")
    parser.add_argument("--request-migration-apply", type=str, help="Request migration apply for a plan-id")
    parser.add_argument("--show-migration-rollback-plan", type=str, help="Show rollback plan for a plan-id")
    parser.add_argument("--show-migration-rollforward-plan", type=str, help="Show rollforward plan for a plan-id")
    parser.add_argument("--show-migration-verification", type=str, help="Show verification results for a plan-id")
    parser.add_argument("--show-migration-debt", action="store_true", help="Show migration debt summary")
    parser.add_argument("--show-migration-evidence", type=str, help="Show migration evidence bundle for a plan-id")

    parser.add_argument("--check-only", action="store_true", help="Run checks only")
    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print config"
    )
    parser.add_argument("--bootstrap-storage", action="store_true", help="Bootstrap db")

    # Policy Kernel CLI Commands
    parser.add_argument(
        "--evaluate-policy",
        action="store_true",
        help="Evaluate unified policy for current context",
    )
    parser.add_argument(
        "--show-policy-decision",
        action="store_true",
        help="Show policy decision for a run ID",
    )
    parser.add_argument(
        "--show-policy-proof",
        action="store_true",
        help="Show policy proof for a run ID",
    )
    parser.add_argument(
        "--show-policy-conflicts",
        action="store_true",
        help="Show policy conflicts for a run ID",
    )
    parser.add_argument(
        "--show-policy-invariants",
        action="store_true",
        help="Show active invariants registry",
    )
    parser.add_argument(
        "--show-policy-rules", action="store_true", help="Show normal rules registry"
    )
    parser.add_argument(
        "--show-policy-waivers", action="store_true", help="Show active waivers"
    )
    parser.add_argument(
        "--show-policy-drift",
        action="store_true",
        help="Show declared vs actual enforcement drift summary",
    )
    parser.add_argument(
        "--show-policy-gaps",
        action="store_true",
        help="Show missing invariant coverage and stale rules",
    )
    parser.add_argument(
        "--run-policy-audit",
        action="store_true",
        help="Run full policy constitution audit",
    )
    parser.add_argument(
        "--run-invariant-check",
        action="store_true",
        help="Only run non-bypassable invariant evaluation",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        help="Run ID for decision/proof commands",
        default="mock-decision",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.evaluate_policy:
        ctx = assemble_policy_context(
            "mock_action", "workspace_1", "profile_1", "paper"
        )
        ev = assemble_evidence_bundle(workspace_refs={"ok": True})
        decision = evaluate_policy("mock_action", ctx, ev)
        print("=== UNIFIED POLICY EVALUATION ===")
        print(f"Action: {decision.action_type}")
        print(f"Final Verdict: {decision.final_verdict.name}")
        print(f"Reasoning: {decision.reasoning}")
        print("Winning Rules:", decision.winning_rules)
        return

    if args.show_policy_decision:
        decision = get_decision(args.run_id)
        if decision:
            print(f"Decision for {args.run_id}: {decision.final_verdict.name}")
        else:
            print("Decision not found.")
        return

    if args.show_policy_proof:
        decision = get_decision(args.run_id)
        if decision:
            print(generate_decision_proof(decision))
        else:
            print("Decision not found for proof generation.")
        return

    if args.show_policy_conflicts:
        conflicts = get_conflicts(args.run_id)
        print(f"Found {len(conflicts)} conflicts for {args.run_id}.")
        for c in conflicts:
            print(f"- {c.conflict_class.name}: {c.resolution_notes}")
        return

    if args.show_policy_invariants:
        print("=== POLICY INVARIANTS ===")
        for inv in list_invariants():
            print(f"[{inv.domain.name}] {inv.rule_id} - {inv.severity.name}")
            print(f"  Rationale: {inv.rationale}")
        return

    if args.show_policy_rules:
        print("=== POLICY RULES ===")
        for rule in list_rules():
            print(
                f"[{rule.domain.name}] {rule.rule_id} - {rule.severity.name} (Waivable: {rule.is_waivable})"
            )
            print(f"  Rationale: {rule.rationale}")
        return

    if args.show_policy_waivers:
        print("=== ACTIVE WAIVERS ===")
        for w in list_active_waivers():
            print(
                f"{w.waiver_id} -> Rule: {w.rule_id} [Scope: {w.scope}] Expires: {w.expires_at.isoformat()}"
            )
        return

    if args.show_policy_drift:
        print("=== POLICY DRIFT ===")
        for d in list_drifts():
            print(
                f"[{d.severity.name}] {d.module_name}: Expected {d.declared_verdict.name}, Actual {d.actual_verdict.name}"
            )
        return

    if args.show_policy_gaps:
        print("=== POLICY GAPS ===")
        for g in list_gaps():
            print(f"[{g.severity.name}] Domain {g.domain.name}: {g.description}")
        return

    if args.run_policy_audit:
        print(generate_policy_audit_summary())
        return

    if args.run_invariant_check:
        ctx = assemble_policy_context(
            "mock_action", "workspace_1", "profile_1", "paper"
        )
        ev = assemble_evidence_bundle(workspace_refs={"ok": True})
        decision = evaluate_policy("mock_action", ctx, ev)
        print("=== INVARIANT CHECK RESULTS ===")
        print(f"Result: {decision.final_verdict.name}")
        for r in decision.winning_rules:
            print(f"Active rule: {r}")
        return

    print("Platform core starting...")


if __name__ == "__main__":
    main()
