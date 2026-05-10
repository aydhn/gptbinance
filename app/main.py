import argparse
import sys
from app.policy_plane.registry import registry
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    parser.add_argument("--show-policy-registry", action="store_true")
    parser.add_argument("--show-policy", action="store_true")
    parser.add_argument("--policy-id", type=str)
    parser.add_argument("--show-policy-rules", action="store_true")
    parser.add_argument("--show-policy-invariants", action="store_true")
    parser.add_argument("--show-policy-obligations", action="store_true")
    parser.add_argument("--show-policy-subjects-actions-resources", action="store_true")
    parser.add_argument("--show-policy-contexts", action="store_true")
    parser.add_argument("--show-policy-evaluations", action="store_true")
    parser.add_argument("--show-policy-precedence", action="store_true")
    parser.add_argument("--show-policy-conflicts", action="store_true")
    parser.add_argument("--show-policy-exceptions", action="store_true")
    parser.add_argument("--show-policy-waivers", action="store_true")
    parser.add_argument("--show-policy-debt", action="store_true")
    parser.add_argument("--show-policy-coverage", action="store_true")
    parser.add_argument("--show-policy-equivalence", action="store_true")
    parser.add_argument("--show-policy-trust", action="store_true")
    parser.add_argument("--show-policy-review-packs", action="store_true")

    args, unknown = parser.parse_known_args()

    if args.show_policy_registry:
        print("Canonical Policy Registry:")
        for p in registry.list_policies():
            print(f" - {p.policy_id} ({p.policy_class.name})")
        sys.exit(0)

    if args.show_policy and args.policy_id:
        p = registry.get_policy(args.policy_id)
        if p:
            print(f"Policy: {p.policy_id}")
            print(f"Class: {p.policy_class.name}")
            print(f"Rules: {len(p.rules)}")
            print(f"Invariants: {len(p.invariants)}")
            print(f"Obligations: {len(p.obligations)}")
        else:
            print("Policy not found")
        sys.exit(0)

    if args.show_policy_trust:
        from app.policy_plane.trust import evaluate_system_trust
        trust = evaluate_system_trust()
        print(f"System Trust Verdict: {trust.verdict.name}")
        for k, v in trust.factors.items():
            print(f" - {k}: {v}")
        sys.exit(0)

    # Default message if no matching flag
    print("Welcome to Trading Platform CLI. Use --help for options.")

if __name__ == "__main__":
    main()
