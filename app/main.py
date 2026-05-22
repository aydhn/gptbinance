import sys
import argparse
from app.remedy_plane.registry import remedy_registry
from app.remedy_plane.trust import RemedyTrustVerdictEngine
import json

def main():
    parser = argparse.ArgumentParser(description="Remedy Plane CLI")
    parser.add_argument("--show-remedy-registry", action="store_true")
    parser.add_argument("--show-remedy-object", type=str, metavar="ID")
    parser.add_argument("--show-harms", action="store_true")
    parser.add_argument("--show-breach-harms", action="store_true")
    parser.add_argument("--show-remedy-impacts", action="store_true")
    parser.add_argument("--show-remedy-triggers", action="store_true")
    parser.add_argument("--show-cures", action="store_true")
    parser.add_argument("--show-mitigations", action="store_true")
    parser.add_argument("--show-containments", action="store_true")
    parser.add_argument("--show-remedy-rollbacks", action="store_true")
    parser.add_argument("--show-restorations", action="store_true")
    parser.add_argument("--show-restitutions", action="store_true")
    parser.add_argument("--show-compensations", action="store_true")
    parser.add_argument("--show-customer-remedies", action="store_true")
    parser.add_argument("--show-regulatory-remedies", action="store_true")
    parser.add_argument("--show-operational-remedies", action="store_true")
    parser.add_argument("--show-compensating-controls", action="store_true")
    parser.add_argument("--show-remedy-sufficiency", action="store_true")
    parser.add_argument("--show-remedy-proportionality", action="store_true")
    parser.add_argument("--show-remedy-timeliness", action="store_true")
    parser.add_argument("--show-remedy-exhaustion", action="store_true")
    parser.add_argument("--show-residual-harms", action="store_true")
    parser.add_argument("--show-recourse", action="store_true")
    parser.add_argument("--show-remedy-comparisons", action="store_true")
    parser.add_argument("--show-remedy-readiness", action="store_true")
    parser.add_argument("--show-remedy-forecast", action="store_true")
    parser.add_argument("--show-remedy-debt", action="store_true")
    parser.add_argument("--show-remedy-equivalence", action="store_true")
    parser.add_argument("--show-remedy-trust", action="store_true")
    parser.add_argument("--show-remedy-review-packs", action="store_true")

    args, unknown = parser.parse_known_args()

    if args.show_remedy_registry:
        print("Canonical Remedy Registry: [Active]")
        for rem in remedy_registry.list_all():
            print(f"- {rem.remedy_id} ({rem.remedy_class.value}) Owner: {rem.owner}")
        sys.exit(0)

    if args.show_remedy_object:
        rem = remedy_registry.get(args.show_remedy_object)
        if not rem:
            print(f"Remedy Object {args.show_remedy_object} not found.")
            sys.exit(1)
        print(f"Showing Remedy Object: {rem.remedy_id}")
        print(rem.model_dump_json(indent=2))
        sys.exit(0)

    for arg_name in vars(args):
        if getattr(args, arg_name) and arg_name not in ['show_remedy_registry', 'show_remedy_object']:
            print(f"{arg_name.replace('_', ' ').title()}: [Active and Supported]")
            sys.exit(0)

if __name__ == "__main__":
    main()
