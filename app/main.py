import argparse
from app.assurance_plane.registry import AssuranceRegistry
from app.assurance_plane.repository import AssuranceRepository

def main():
    parser = argparse.ArgumentParser(description="Assurance Plane CLI")
    parser.add_argument("--show-accountability-registry", action="store_true")
    parser.add_argument("--show-accountability-object", action="store_true")
    parser.add_argument("--show-accountable-subjects", action="store_true")
    parser.add_argument("--show-scapegoating-risk", action="store_true")
    parser.add_argument("--show-accountability-trust", action="store_true")
    parser.add_argument("--show-accountability-debt", action="store_true")
    parser.add_argument("--show-accountability-comparisons", action="store_true")
    parser.add_argument("--breach-id", type=str)
    parser.add_argument("--accountability-id", type=str)

    parser.add_argument("--show-assurance-registry", action="store_true", help="Show canonical Assurance Registry")
    parser.add_argument("--show-assurance-object", action="store_true", help="Show assurance object")
    parser.add_argument("--assurance-id", type=str, help="Assurance ID")
    parser.add_argument("--show-assurances", action="store_true", help="Show assurances")
    parser.add_argument("--show-assurance-claims", action="store_true", help="Show assurance claims")
    parser.add_argument("--show-assurance-scope", action="store_true", help="Show assurance scopes")
    parser.add_argument("--show-assurance-cases", action="store_true", help="Show assurance cases")
    parser.add_argument("--show-evidence-packs", action="store_true", help="Show evidence packs")
    parser.add_argument("--show-evidence-items", action="store_true", help="Show evidence items")
    parser.add_argument("--show-sufficiency", action="store_true", help="Show evidence sufficiency")
    parser.add_argument("--show-contradictions", action="store_true", help="Show contradictions")
    parser.add_argument("--show-caveats", action="store_true", help="Show caveats")
    parser.add_argument("--show-certifications", action="store_true", help="Show certifications")
    parser.add_argument("--show-attestations", action="store_true", help="Show attestations")
    parser.add_argument("--show-independent-review", action="store_true", help="Show independent reviews")
    parser.add_argument("--show-surveillance-cycles", action="store_true", help="Show surveillance cycles")
    parser.add_argument("--show-surveillance-findings", action="store_true", help="Show surveillance findings")
    parser.add_argument("--show-expiry", action="store_true", help="Show expiries")
    parser.add_argument("--show-revocation-triggers", action="store_true", help="Show revocation triggers")
    parser.add_argument("--show-assurance-downgrades", action="store_true", help="Show downgrades")
    parser.add_argument("--show-assurance-comparisons", action="store_true", help="Show comparisons")
    parser.add_argument("--show-assurance-readiness", action="store_true", help="Show readiness evaluations")
    parser.add_argument("--show-assurance-forecast", action="store_true", help="Show forecast")
    parser.add_argument("--show-assurance-debt", action="store_true", help="Show assurance debt")
    parser.add_argument("--show-assurance-equivalence", action="store_true", help="Show equivalence")
    parser.add_argument("--show-assurance-trust", action="store_true", help="Show trust verdicts")
    parser.add_argument("--show-assurance-review-packs", action="store_true", help="Show review packs")


    parser.add_argument("--show-incentive-registry", action="store_true", help="Show canonical Incentive Registry")
    parser.add_argument("--show-incentive-object", action="store_true")
    parser.add_argument("--incentive-id", type=str)
    parser.add_argument("--show-incentives", action="store_true")
    parser.add_argument("--show-incentive-subjects", action="store_true")
    parser.add_argument("--show-behavioral-targets", action="store_true")
    parser.add_argument("--show-incentive-levers", action="store_true")
    parser.add_argument("--show-rewards", action="store_true")
    parser.add_argument("--show-reward-formulas", action="store_true")
    parser.add_argument("--show-delayed-rewards", action="store_true")
    parser.add_argument("--show-penalties", action="store_true")
    parser.add_argument("--show-penalty-triggers", action="store_true")
    parser.add_argument("--show-friction-controls", action="store_true")
    parser.add_argument("--show-clawbacks", action="store_true")
    parser.add_argument("--show-escalation-incentives", action="store_true")
    parser.add_argument("--show-surveillance-incentives", action="store_true")
    parser.add_argument("--show-shared-incentives", action="store_true")
    parser.add_argument("--show-incentive-conflicts", action="store_true")
    parser.add_argument("--show-moral-hazard", action="store_true")
    parser.add_argument("--show-externalities", action="store_true")
    parser.add_argument("--show-gaming-signals", action="store_true")
    parser.add_argument("--show-incentive-reviews", action="store_true")
    parser.add_argument("--show-incentive-recalibration", action="store_true")
    parser.add_argument("--show-incentive-comparisons", action="store_true")
    parser.add_argument("--show-incentive-readiness", action="store_true")
    parser.add_argument("--show-incentive-forecast", action="store_true")
    parser.add_argument("--show-incentive-debt", action="store_true")
    parser.add_argument("--show-incentive-equivalence", action="store_true")
    parser.add_argument("--show-incentive-trust", action="store_true")
    parser.add_argument("--show-incentive-review-packs", action="store_true")

    args = parser.parse_args()

    if args.show_assurance_registry:
        print("[CLI] Initializing and displaying canonical Assurance Registry...")
    elif args.show_assurance_object and args.assurance_id:
        print(f"[CLI] Showing details for Assurance ID: {args.assurance_id}")
    elif args.show_assurance_trust:
        print(f"[CLI] Evaluating Trust Verdict for Assurance IDs...")

    elif args.show_incentive_registry:
        print("[CLI] Initializing and displaying canonical Incentive Registry...")
    elif args.show_incentive_object and args.incentive_id:
        print(f"[CLI] Showing details for Incentive ID: {args.incentive_id}")
    elif args.show_incentive_trust:
        print(f"[CLI] Evaluating Trust Verdict for Incentive IDs...")
    else:
        print("[CLI] Assurance Plane Governance CLI available. Use --help for commands.")

if __name__ == "__main__":
    main()
