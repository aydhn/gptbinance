import sys
import argparse

from app.learning_plane import register_cli_args as register_learning_args
from app.learning_plane import handle_cli as handle_learning_cli


def handle_federation_cli(args):
    # Mapping args to simple prints for CLI
    for action in vars(args):
        if getattr(args, action) and action != "command":
            print(f"Handling --{action.replace('_', '-')}")
            return
    print("Federation Plane CLI Base")



def print_provenance_registry():
    print("Provenance Registry:")

def print_provenance_object(provenance_id: str):
    if provenance_id:
        print(f"Provenance Object {provenance_id}")
    else:
        print(f"Object {provenance_id} not found.")

def handle_provenance_cli(args):
    if getattr(args, "show_provenance_registry", False):
        print_provenance_registry()
        return
    if getattr(args, "show_provenance_object", False):
        if args.provenance_id:
            print_provenance_object(args.provenance_id)
        else:
            print("Missing --provenance-id")
        return
    for action in vars(args):
        if getattr(args, action) and action not in ["command", "provenance_id"]:
            print(f"Handling --{action.replace('_', '-')}")
            return
    print("Provenance Plane CLI Base")


def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add scenario arguments (original logic converted to argparse)

    provenance_parser = subparsers.add_parser("provenance")
    provenance_parser.add_argument("--show-provenance-registry", action="store_true")
    provenance_parser.add_argument("--show-provenance-object", action="store_true")
    provenance_parser.add_argument("--provenance-id", type=str, help="ID of the provenance object")
    provenance_parser.add_argument("--show-sources", action="store_true")
    provenance_parser.add_argument("--show-provenance-inputs", action="store_true")
    provenance_parser.add_argument("--show-transformations", action="store_true")
    provenance_parser.add_argument("--show-derived-artifacts", action="store_true")
    provenance_parser.add_argument("--show-feature-lineage", action="store_true")
    provenance_parser.add_argument("--show-model-influence", action="store_true")
    provenance_parser.add_argument("--show-config-influence", action="store_true")
    provenance_parser.add_argument("--show-decision-lineage", action="store_true")
    provenance_parser.add_argument("--show-approval-lineage", action="store_true")
    provenance_parser.add_argument("--show-action-lineage", action="store_true")
    provenance_parser.add_argument("--show-side-effects", action="store_true")
    provenance_parser.add_argument("--show-outcome-lineage", action="store_true")
    provenance_parser.add_argument("--show-contributions", action="store_true")
    provenance_parser.add_argument("--show-attribution", action="store_true")
    provenance_parser.add_argument("--show-causal-confidence", action="store_true")
    provenance_parser.add_argument("--show-chain-of-custody", action="store_true")
    provenance_parser.add_argument("--show-custody-gaps", action="store_true")
    provenance_parser.add_argument("--show-responsibility", action="store_true")
    provenance_parser.add_argument("--show-explainability", action="store_true")
    provenance_parser.add_argument("--show-provenance-comparisons", action="store_true")
    provenance_parser.add_argument("--show-provenance-readiness", action="store_true")
    provenance_parser.add_argument("--show-provenance-forecast", action="store_true")
    provenance_parser.add_argument("--show-provenance-debt", action="store_true")
    provenance_parser.add_argument("--show-provenance-equivalence", action="store_true")
    provenance_parser.add_argument("--show-provenance-trust", action="store_true")
    provenance_parser.add_argument("--show-provenance-review-packs", action="store_true")

    scenario_parser = subparsers.add_parser("scenario")
    scenario_parser.add_argument("--show-scenario-registry", action="store_true")
    scenario_parser.add_argument("--show-scenario", action="store_true")
    scenario_parser.add_argument("--show-scenario-taxonomy", action="store_true")
    scenario_parser.add_argument("--show-scenarios", action="store_true")
    scenario_parser.add_argument("--show-scenario-baselines", action="store_true")
    scenario_parser.add_argument("--show-scenario-assumptions", action="store_true")
    scenario_parser.add_argument("--show-scenario-shocks", action="store_true")
    scenario_parser.add_argument("--show-scenario-interventions", action="store_true")
    scenario_parser.add_argument("--show-scenario-branches", action="store_true")
    scenario_parser.add_argument("--show-scenario-timelines", action="store_true")
    scenario_parser.add_argument("--show-scenario-counterfactuals", action="store_true")
    scenario_parser.add_argument("--show-scenario-cascades", action="store_true")
    scenario_parser.add_argument("--show-second-order-effects", action="store_true")
    scenario_parser.add_argument("--show-scenario-outcomes", action="store_true")
    scenario_parser.add_argument("--show-scenario-robustness", action="store_true")
    scenario_parser.add_argument("--show-scenario-fragility", action="store_true")
    scenario_parser.add_argument("--show-recovery-credibility", action="store_true")
    scenario_parser.add_argument("--show-policy-stress", action="store_true")
    scenario_parser.add_argument("--show-constitutional-stress", action="store_true")
    scenario_parser.add_argument("--show-scenario-comparisons", action="store_true")
    scenario_parser.add_argument("--show-scenario-forecast", action="store_true")
    scenario_parser.add_argument("--show-scenario-debt", action="store_true")
    scenario_parser.add_argument("--show-scenario-readiness", action="store_true")
    scenario_parser.add_argument("--show-scenario-equivalence", action="store_true")
    scenario_parser.add_argument("--show-scenario-trust", action="store_true")
    scenario_parser.add_argument("--show-scenario-review-packs", action="store_true")

    # Add learning plane arguments
    register_learning_args(subparsers)

    # Add federation plane arguments
    federation_parser = subparsers.add_parser("federation")
    federation_parser.add_argument("--show-federation-registry", action="store_true")
    federation_parser.add_argument("--show-federation", action="store_true")
    federation_parser.add_argument("--federation-id", type=str)
    federation_parser.add_argument("--show-federation-taxonomy", action="store_true")
    federation_parser.add_argument("--show-federations", action="store_true")
    federation_parser.add_argument("--show-domains", action="store_true")
    federation_parser.add_argument("--show-tenants", action="store_true")
    federation_parser.add_argument("--show-trust-boundaries", action="store_true")
    federation_parser.add_argument("--show-authority-boundaries", action="store_true")
    federation_parser.add_argument("--show-shared-services", action="store_true")
    federation_parser.add_argument(
        "--show-federation-dependencies", action="store_true"
    )
    federation_parser.add_argument("--show-delegated-authority", action="store_true")
    federation_parser.add_argument("--show-portability", action="store_true")
    federation_parser.add_argument("--show-evidence-translation", action="store_true")
    federation_parser.add_argument("--show-global-local-rules", action="store_true")
    federation_parser.add_argument("--show-federation-conflicts", action="store_true")
    federation_parser.add_argument("--show-federated-blast-radius", action="store_true")
    federation_parser.add_argument("--show-tenant-isolation", action="store_true")
    federation_parser.add_argument("--show-shared-risks", action="store_true")
    federation_parser.add_argument("--show-partner-federation", action="store_true")
    federation_parser.add_argument("--show-federated-verdicts", action="store_true")
    federation_parser.add_argument(
        "--show-federation-observations", action="store_true"
    )
    federation_parser.add_argument("--show-federation-forecast", action="store_true")
    federation_parser.add_argument("--show-federation-debt", action="store_true")
    federation_parser.add_argument("--show-federation-readiness", action="store_true")
    federation_parser.add_argument("--show-federation-equivalence", action="store_true")
    federation_parser.add_argument("--show-federation-trust", action="store_true")
    federation_parser.add_argument(
        "--show-federation-review-packs", action="store_true"
    )

    args = parser.parse_args()

    if args.command == "learning":
        handle_learning_cli(args)

    elif args.command == "provenance":
        handle_provenance_cli(args)

        handle_learning_cli(args)
    elif args.command == "federation":
        handle_federation_cli(args)
    elif args.command == "scenario":
        for action in vars(args):
            if getattr(args, action) and action != "command":
                print(f"Handling --{action.replace('_', '-')}")
                return
        print("Scenario CLI Base")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

# CLI Integration
from app.autonomy_plane.cli import main as autonomy_cli_main
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("--show"):
        autonomy_cli_main(sys.argv[1:])
