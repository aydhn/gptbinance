# Simplified CLI extensions for integration into app/main.py
import argparse
import sys
import json
from app.activation.repository import activation_repo
from app.activation.reporting import ActivationReporter
from app.activation.intents import IntentCompiler
from app.activation.plans import RolloutPlanner


def handle_activation_cli(args):
    if args.build_activation_intent:
        # Mock board decision for CLI demonstration
        board_decision = {
            "decision": "CONDITIONAL_GO",
            "candidate_id": args.candidate_id or "cand-123",
            "decision_id": "board-456",
            "activation_class": "canary_limited",
            "scope": {"allowed_symbols": ["BTCUSDT"], "ttl_seconds": 3600},
        }
        compiler = IntentCompiler()
        try:
            intent = compiler.compile_intent(board_decision)
            activation_repo.save_intent(intent)
            print(f"Created Intent: {intent.intent_id}")
            print(ActivationReporter.format_intent(intent))

            # Auto-generate a plan for convenience
            planner = RolloutPlanner()
            plan = planner.build_plan(intent)
            activation_repo.save_plan(plan)

        except Exception as e:
            print(f"Error building intent: {e}")

    elif args.show_activation_intent:
        intent = activation_repo.get_intent(args.intent_id)
        if intent:
            print(ActivationReporter.format_intent(intent))
        else:
            print(f"Intent {args.intent_id} not found.")

    elif args.show_rollout_plan:
        plan = activation_repo.get_plan(args.intent_id)
        if plan:
            print(ActivationReporter.format_plan(plan))
        else:
            print(f"Plan for intent {args.intent_id} not found.")

    elif args.show_probation_status:
        status = activation_repo.get_probation_status(args.intent_id)
        if status:
            print(ActivationReporter.format_probation(status))
        else:
            print(f"Probation status for intent {args.intent_id} not found.")

    elif args.show_expansion_recommendation:
        print(
            f"Showing expansion recommendation for intent {args.intent_id} (mocked for CLI)..."
        )

    elif args.show_halt_recommendation:
        print(
            f"Showing halt recommendation for intent {args.intent_id} (mocked for CLI)..."
        )

    elif args.show_revert_plan:
        print(f"Showing revert plan for intent {args.intent_id} (mocked for CLI)...")

    elif args.show_active_set:
        print("Showing current active sets (mocked for CLI)...")

    elif args.show_active_set_history:
        print("Showing active set history (mocked for CLI)...")

    else:
        print("Command executed. Use specific flags to see more details.")


def add_activation_args(parser):
    group = parser.add_argument_group("Staged Activation Controller")
    group.add_argument("--build-activation-intent", action="store_true")
    group.add_argument("--candidate-id", type=str)
    group.add_argument("--show-activation-intent", action="store_true")
    group.add_argument("--intent-id", type=str)
    group.add_argument("--show-rollout-plan", action="store_true")
    group.add_argument("--show-active-set", action="store_true")
    group.add_argument("--show-active-set-history", action="store_true")
    group.add_argument("--show-probation-status", action="store_true")
    group.add_argument("--show-probation-metrics", action="store_true")
    group.add_argument("--show-expansion-recommendation", action="store_true")
    group.add_argument("--show-halt-recommendation", action="store_true")
    group.add_argument("--show-revert-plan", action="store_true")
    group.add_argument("--show-activation-memo", action="store_true")
    group.add_argument("--show-activation-evidence", action="store_true")
