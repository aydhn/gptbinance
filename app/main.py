import argparse
import sys
from app.interpretation_plane.registry import CanonicalInterpretationRegistry
from app.interpretation_plane.models import InterpretationObject, TextRecord, TextUnitClass, InterpretationClass
from app.obligation_plane.registry import CanonicalObligationRegistry

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")

    # Interpretation Plane Commands
    parser.add_argument("--show-interpretation-registry", action="store_true")
    parser.add_argument("--show-interpretation-object", action="store_true")
    parser.add_argument("--interpretation-id", type=str)
    parser.add_argument("--show-texts", action="store_true")
    parser.add_argument("--show-terms", action="store_true")
    parser.add_argument("--show-clauses", action="store_true")
    parser.add_argument("--show-phrases", action="store_true")
    parser.add_argument("--show-readings", action="store_true")
    parser.add_argument("--show-ambiguities", action="store_true")
    parser.add_argument("--show-canonical-meanings", action="store_true")
    parser.add_argument("--show-interpretation-trust", action="store_true")

    for arg in [
        "--show-textual-readings", "--show-contextual-readings", "--show-purposive-readings",
        "--show-restrictive-readings", "--show-expansive-readings", "--show-glosses",
        "--show-clarifications", "--show-reinterpretations", "--show-interpretation-conflicts",
        "--show-beneficiary-safe-constructions", "--show-interpretation-hierarchy",
        "--show-interpretation-scopes", "--show-interpretation-drift", "--show-interpretation-comparisons",
        "--show-interpretation-readiness", "--show-interpretation-forecast", "--show-interpretation-debt",
        "--show-interpretation-equivalence", "--show-interpretation-review-packs"
    ]:
        parser.add_argument(arg, action="store_true")

    # Obligation Plane Commands
    parser.add_argument("--show-obligation-registry", action="store_true")
    parser.add_argument("--show-obligation-object", action="store_true")
    parser.add_argument("--obligation-id", type=str)
    parser.add_argument("--show-obligations", action="store_true")
    parser.add_argument("--show-duties", action="store_true")
    parser.add_argument("--show-requirements", action="store_true")
    parser.add_argument("--show-prohibitions", action="store_true")
    parser.add_argument("--show-forbearance", action="store_true")
    parser.add_argument("--show-obligation-triggers", action="store_true")
    parser.add_argument("--show-trigger-conditions", action="store_true")
    parser.add_argument("--show-trigger-activations", action="store_true")
    parser.add_argument("--show-deadlines", action="store_true")
    parser.add_argument("--show-due-windows", action="store_true")
    parser.add_argument("--show-recurrence", action="store_true")
    parser.add_argument("--show-escalation-duties", action="store_true")
    parser.add_argument("--show-nonwaivable-duties", action="store_true")
    parser.add_argument("--show-suspensions", action="store_true")
    parser.add_argument("--show-obligation-waivers", action="store_true")
    parser.add_argument("--show-excuses", action="store_true")
    parser.add_argument("--show-impossibility", action="store_true")
    parser.add_argument("--show-substitute-performance", action="store_true")
    parser.add_argument("--show-duty-breaches", action="store_true")
    parser.add_argument("--show-overdue-duties", action="store_true")
    parser.add_argument("--show-discharges", action="store_true")
    parser.add_argument("--show-residual-duties", action="store_true")
    parser.add_argument("--show-beneficiary-safe-completions", action="store_true")
    parser.add_argument("--show-obligation-comparisons", action="store_true")
    parser.add_argument("--show-obligation-readiness", action="store_true")
    parser.add_argument("--show-obligation-forecast", action="store_true")
    parser.add_argument("--show-obligation-debt", action="store_true")
    parser.add_argument("--show-obligation-equivalence", action="store_true")
    parser.add_argument("--show-obligation-trust", action="store_true")
    parser.add_argument("--show-obligation-review-packs", action="store_true")

    # Enforcement Plane Commands
    parser.add_argument("--show-enforcement-registry", action="store_true")
    parser.add_argument("--show-enforcement-object", action="store_true")
    parser.add_argument("--enforcement-id", type=str)
    parser.add_argument("--show-enforcements", action="store_true")
    parser.add_argument("--show-interventions", action="store_true")
    parser.add_argument("--show-holds", action="store_true")
    parser.add_argument("--show-blocks", action="store_true")
    parser.add_argument("--show-quarantines", action="store_true")
    parser.add_argument("--show-enforcement-suspensions", action="store_true")
    parser.add_argument("--show-disablements", action="store_true")
    parser.add_argument("--show-kill-switches", action="store_true")
    parser.add_argument("--show-rollbacks", action="store_true")
    parser.add_argument("--show-reversals", action="store_true")
    parser.add_argument("--show-sanctions", action="store_true")
    parser.add_argument("--show-rate-limit-enforcement", action="store_true")
    parser.add_argument("--show-gate-enforcement", action="store_true")
    parser.add_argument("--show-compensating-restrictions", action="store_true")
    parser.add_argument("--show-enforcement-triggers", action="store_true")
    parser.add_argument("--show-trigger-evidence", action="store_true")
    parser.add_argument("--show-enforcement-scope", action="store_true")
    parser.add_argument("--show-enforcement-proportionality", action="store_true")
    parser.add_argument("--show-due-process", action="store_true")
    parser.add_argument("--show-enforcement-appeals", action="store_true")
    parser.add_argument("--show-enforcement-reviews", action="store_true")
    parser.add_argument("--show-lift-criteria", action="store_true")
    parser.add_argument("--show-enforcement-expiry", action="store_true")
    parser.add_argument("--show-reenable", action="store_true")
    parser.add_argument("--show-residual-restrictions", action="store_true")
    parser.add_argument("--show-beneficiary-safe-enforcement", action="store_true")
    parser.add_argument("--show-enforcement-comparisons", action="store_true")
    parser.add_argument("--show-enforcement-readiness", action="store_true")
    parser.add_argument("--show-enforcement-forecast", action="store_true")
    parser.add_argument("--show-enforcement-debt", action="store_true")
    parser.add_argument("--show-enforcement-equivalence", action="store_true")
    parser.add_argument("--show-enforcement-trust", action="store_true")
    parser.add_argument("--show-enforcement-review-packs", action="store_true")

    args = parser.parse_args()

    interp_registry = CanonicalInterpretationRegistry()
    mock_obj = InterpretationObject(
        interpretation_id="interp_001",
        interp_class=InterpretationClass.CONTRACT_CLAUSE,
        texts={"txt1": TextRecord("txt1", "Company may terminate at will", TextUnitClass.CLAUSE, "contract_v1")}
    )
    interp_registry.register(mock_obj)

    if args.show_interpretation_registry:
        print("\n--- Canonical Interpretation Registry ---")
        for obj in interp_registry.get_all():
            print(f"- ID: {obj.interpretation_id} | Class: {obj.interp_class.name}")
        sys.exit(0)

    if args.show_interpretation_trust:
        print("\n--- Interpretation Trust Verdicts ---")
        for obj in interp_registry.get_all():
            trust = obj.get_trust_report()
            print(f"ID: {obj.interpretation_id} -> Verdict: {trust.verdict.name}")
            if trust.blockers:
                print(f"  Blockers: {trust.blockers}")
        sys.exit(0)

    if args.show_texts:
        print("\n--- Interpretation Texts ---")
        for obj in interp_registry.get_all():
            for t in obj.texts.values():
                print(f"[{obj.interpretation_id}] Text: {t.content} (Source: {t.source_ref})")
        sys.exit(0)

    if args.show_obligation_registry:
        print("\n--- Canonical Obligation Registry ---")
        # Logic to be implemented...
        sys.exit(0)

    # Enforcement Plane output handling
    if args.show_enforcement_registry:
        print("\n--- Enforcement Registry (Canonical & Typed) ---")
        sys.exit(0)

    if args.show_enforcement_object and args.enforcement_id:
        print(f"\n--- Enforcement Object Details: {args.enforcement_id} ---")
        sys.exit(0)

    if args.show_enforcements:
        print("\n--- Active/Expired/Lifted/Disputed Enforcements ---")
        sys.exit(0)

    if args.show_interventions:
        print("\n--- Preventive/Corrective/Containment/Coercive Interventions ---")
        sys.exit(0)

    if args.show_holds:
        print("\n--- Temporary/Review/Beneficiary-Protective/Indefinite-Risk Holds ---")
        sys.exit(0)

    if args.show_blocks:
        print("\n--- Hard/Scoped/Soft/Block-with-Review Records ---")
        sys.exit(0)

    if args.show_quarantines:
        print("\n--- Data/Actor/Environment/Customer-Impact Quarantines ---")
        sys.exit(0)

    if args.show_enforcement_suspensions:
        print("\n--- Temporary/Conditional/Punitive-Looking/Invalid Suspensions ---")
        sys.exit(0)

    if args.show_disablements:
        print("\n--- Capability/Feature/Actor/Federated Disablements ---")
        sys.exit(0)

    if args.show_kill_switches:
        print("\n--- Emergency/Scoped/Cascading Kill-Switch Records ---")
        sys.exit(0)

    if args.show_rollbacks:
        print("\n--- Config/Release/Migration Rollbacks ---")
        sys.exit(0)

    if args.show_reversals:
        print("\n--- Action/State/Authorization/Partial Reversals ---")
        sys.exit(0)

    if args.show_sanctions:
        print("\n--- Formal/Provisional/Behavior/Partner Sanctions ---")
        sys.exit(0)

    if args.show_rate_limit_enforcement:
        print("\n--- Abuse Throttling/Safety/Fairness-Preserving Rate Limits ---")
        sys.exit(0)

    if args.show_gate_enforcement:
        print("\n--- Precondition/Approval/Review/Release Gates ---")
        sys.exit(0)

    if args.show_compensating_restrictions:
        print("\n--- Temporary/Scoped/Beneficiary-Protective Restrictions ---")
        sys.exit(0)

    if args.show_enforcement_triggers:
        print("\n--- Obligation/Rights/Liability/Risk Triggers ---")
        sys.exit(0)

    if args.show_trigger_evidence:
        print("\n--- Authoritative/Weak/Conflicting/Stale Trigger Evidence ---")
        sys.exit(0)

    if args.show_enforcement_scope:
        print("\n--- Actor/Tenant/Environment/Beneficiary Scopes ---")
        sys.exit(0)

    if args.show_enforcement_proportionality:
        print("\n--- Proportionate/Under/Over/Discriminatory-Looking Enforcement Posture ---")
        sys.exit(0)

    if args.show_due_process:
        print("\n--- Pre-review/Post-review/Notice-and-appeal/Emergency-bypass-with-debt Postures ---")
        sys.exit(0)

    if args.show_enforcement_appeals:
        print("\n--- Valid/Pending/Denied/Granted Appeals ---")
        sys.exit(0)

    if args.show_enforcement_reviews:
        print("\n--- Mandatory/Recurring/Lift/Contested Reviews ---")
        sys.exit(0)

    if args.show_lift_criteria:
        print("\n--- Explicit/Partial/Blocked/Premature Lift Records ---")
        sys.exit(0)

    if args.show_enforcement_expiry:
        print("\n--- Time-bound/Expired/Auto-expiring/Stale Active Restrictions ---")
        sys.exit(0)

    if args.show_reenable:
        print("\n--- Safe/Staged/Conditional/Invalid Re-enable Posture ---")
        sys.exit(0)

    if args.show_residual_restrictions:
        print("\n--- Residual Customer/System/Review-Duty Restrictions ---")
        sys.exit(0)

    if args.show_beneficiary_safe_enforcement:
        print("\n--- Rights-Preserving/Notice-Safe/Proportional Beneficiary-Safe Enforcement Lines ---")
        sys.exit(0)

    if args.show_enforcement_comparisons:
        print("\n--- Block vs Hold, Quarantine vs Suspension, Rollback vs Reversal, Local vs Federated Comparisons ---")
        sys.exit(0)

    if args.show_enforcement_readiness:
        print("\n--- Trigger Clarity, Proportionality Rigor, Due-Process Discipline, Reversibility Hygiene, Residual Visibility ---")
        sys.exit(0)

    if args.show_enforcement_forecast:
        print("\n--- Indefinite Hold, Unblock Drift, Appeal Backlog, Over-enforcement, Review Lapse Forecasts ---")
        sys.exit(0)

    if args.show_enforcement_debt:
        print("\n--- Shadow Enforcement, Indefinite Hold, Due-Process Bypass, Unblock Laundering, Beneficiary-Harmful Enforcement Debt ---")
        sys.exit(0)

    if args.show_enforcement_equivalence:
        print("\n--- Replay/Paper/Probation/Live Equivalence Verdict and Blockers ---")
        sys.exit(0)

    if args.show_enforcement_trust:
        print("\n--- Trusted Enforcement Posture Verdicts, Blockers, Caveats ---")
        sys.exit(0)

    if args.show_enforcement_review_packs:
        print("\n--- Trigger/Intervention/Sanction/Appeal/Lift/Residual Review Packs ---")
        sys.exit(0)

if __name__ == "__main__":
    main()
