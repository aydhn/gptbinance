import sys
import argparse
from app.learning_plane import register_cli_args as register_learning_args
from app.learning_plane import handle_cli as handle_learning_cli

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add scenario arguments (original logic converted to argparse)
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

    args = parser.parse_args()

    if args.command == "learning":
        handle_learning_cli(args)
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
