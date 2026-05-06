import argparse
import sys
from app.incidents.cli import handle_incident_cli
from app.main_activation_cli import add_activation_args, handle_activation_cli

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")

    # Platform generic commands
    parser.add_argument("--check-only", action="store_true", help="Run in check-only mode")
    parser.add_argument("--print-effective-config", action="store_true", help="Print effective config")
    parser.add_argument("--bootstrap-storage", action="store_true", help="Bootstrap storage")

    add_activation_args(parser)

    parser.add_argument("--show-active-incidents", action="store_true")
    parser.add_argument("--show-incident", type=str, metavar="ID")
    parser.add_argument("--show-incident-timeline", type=str, metavar="ID")
    parser.add_argument("--show-incident-snapshot", type=str, metavar="ID")
    parser.add_argument("--show-containment-plan", type=str, metavar="ID")
    parser.add_argument("--show-degraded-mode-plan", type=str, metavar="ID")
    parser.add_argument("--show-recovery-readiness", type=str, metavar="ID")
    parser.add_argument("--show-incident-history", action="store_true")
    parser.add_argument("--show-postmortem-seed", type=str, metavar="ID")
    parser.add_argument("--show-incident-evidence", type=str, metavar="ID")
    parser.add_argument("--show-incident-metrics", action="store_true")
    parser.add_argument("--show-incident-clusters", action="store_true")

    args = parser.parse_args()

    # Determine if an activation command was called
    activation_commands = [
        "build_activation_intent", "show_activation_intent", "show_rollout_plan",
        "show_active_set", "show_active_set_history", "show_probation_status",
        "show_probation_metrics", "show_expansion_recommendation",
        "show_halt_recommendation", "show_revert_plan", "show_activation_memo",
        "show_activation_evidence"
    ]

    if any(getattr(args, cmd, False) for cmd in activation_commands):
        handle_activation_cli(args)
        sys.exit(0)


    if any(getattr(args, cmd, False) for cmd in ['show_active_incidents', 'show_incident', 'show_incident_timeline', 'show_incident_snapshot', 'show_containment_plan', 'show_degraded_mode_plan', 'show_recovery_readiness', 'show_incident_history', 'show_postmortem_seed', 'show_incident_evidence', 'show_incident_metrics', 'show_incident_clusters']):
        handle_incident_cli(args)
        sys.exit(0)


    if args.check_only:
        print("Check only complete.")
    else:
        print("Starting core application...")

if __name__ == "__main__":
    main()
