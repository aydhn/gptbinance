import argparse

def main():
from .main_tradeoff_cli import add_tradeoff_args
from app.tradeoff_plane.cli_tradeoff_plane import handle_tradeoff_commands
    parser = argparse.ArgumentParser(description="Epistemic Plane CLI")
    parser.add_argument("--show-epistemic-registry", action="store_true")
    parser.add_argument("--show-epistemic-object", type=str, help="--epistemic-id <id>")
    parser.add_argument("--show-facts", action="store_true")
    parser.add_argument("--show-claims", action="store_true")
    parser.add_argument("--show-inferences", action="store_true")
    parser.add_argument("--show-hypotheses", action="store_true")
    parser.add_argument("--show-assumptions", action="store_true")
    parser.add_argument("--show-estimates", action="store_true")
    parser.add_argument("--show-evidence-items", action="store_true")
    parser.add_argument("--show-evidence-sets", action="store_true")
    parser.add_argument("--show-evidence-links", action="store_true")
    parser.add_argument("--show-evidence-sufficiency", action="store_true")
    parser.add_argument("--show-epistemic-confidence", action="store_true")
    parser.add_argument("--show-epistemic-uncertainty", action="store_true")
    parser.add_argument("--show-contradictions", action="store_true")
    parser.add_argument("--show-refutations", action="store_true")
    parser.add_argument("--show-unknowns", action="store_true")
    parser.add_argument("--show-knowability", action="store_true")
    parser.add_argument("--show-belief-revisions", action="store_true")
    parser.add_argument("--show-claim-lineage", action="store_true")
    parser.add_argument("--show-epistemic-readiness", action="store_true")
    parser.add_argument("--show-epistemic-forecast", action="store_true")
    parser.add_argument("--show-epistemic-debt", action="store_true")
    parser.add_argument("--show-epistemic-equivalence", action="store_true")
    parser.add_argument("--show-epistemic-trust", action="store_true")
    parser.add_argument("--show-epistemic-review-packs", action="store_true")
    add_tradeoff_args(parser)

    args = parser.parse_args()

    if handle_tradeoff_commands(args):
        return

    if args.show_epistemic_registry:
        print("[EPISTEMIC REGISTRY] - Showing canonical registry, families and markers.")
    elif args.show_epistemic_object:
        print(f"[EPISTEMIC OBJECT] {args.show_epistemic_object} - Showing claim class, evidence posture.")
    elif args.show_facts:
        print("[FACTS] - Showing observed/validated/stale facts.")
    elif args.show_claims:
        print("[CLAIMS] - Showing operational/policy/causal/eligibility claims.")
    elif args.show_inferences:
        print("[INFERENCES] - Showing inferences. Caveat: No inference==fact shortcut.")
    # Other print statements simulated for completeness
    elif args.show_epistemic_trust:
        print("[EPISTEMIC TRUST] - Showing trusted epistemic posture, blockers and caveats.")
    else:
        print("Epistemic Plane CLI Interface. Use --help to see commands.")

if __name__ == "__main__":
    main()
