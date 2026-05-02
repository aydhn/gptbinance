import argparse
import sys
from app.qualification.runner import QualificationRunner
from app.qualification.enums import QualificationProfile
from app.qualification.models import QualificationConfig
from app.qualification.repository import QualificationRepository
from app.qualification.reporting import (
    format_qualification_summary,
    format_traceability_matrix,
    format_scenario_results,
    format_forbidden_action_results,
    format_contract_verification,
    format_evidence_pack,
)


def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    parser.add_argument(
        "--run-qualification", action="store_true", help="Run a qualification suite"
    )
    parser.add_argument(
        "--run-qualification-dry-run",
        action="store_true",
        help="Dry-run a qualification suite",
    )
    parser.add_argument(
        "--qualification-profile", type=str, help="Qualification profile to use"
    )
    parser.add_argument(
        "--show-qualification-summary",
        action="store_true",
        help="Show summary for a run",
    )
    parser.add_argument(
        "--show-traceability-matrix",
        action="store_true",
        help="Show traceability matrix",
    )
    parser.add_argument(
        "--show-scenario-results",
        action="store_true",
        help="Show scenario results for a run",
    )
    parser.add_argument(
        "--show-forbidden-action-results",
        action="store_true",
        help="Show forbidden action results for a run",
    )
    parser.add_argument(
        "--show-contract-verification",
        action="store_true",
        help="Show contract verification for a run",
    )
    parser.add_argument(
        "--show-evidence-pack", action="store_true", help="Show evidence pack for a run"
    )
    parser.add_argument(
        "--show-certification-status",
        action="store_true",
        help="Show certification status for a run",
    )
    parser.add_argument(
        "--show-waivers", action="store_true", help="Show waivers for a run"
    )
    parser.add_argument("--run-id", type=str, help="Run ID for reporting commands")

    args = parser.parse_args()

    repo = QualificationRepository()

    if args.run_qualification or args.run_qualification_dry_run:
        if not args.qualification_profile:
            print("Error: --qualification-profile is required")
            sys.exit(1)

        try:
            profile = QualificationProfile(args.qualification_profile)
        except ValueError:
            print(
                f"Error: Invalid profile. Choose from {[e.value for e in QualificationProfile]}"
            )
            sys.exit(1)

        config = QualificationConfig(dry_run=args.run_qualification_dry_run)
        runner = QualificationRunner()
        print(
            f"Starting qualification run for profile {profile.value} (Dry Run: {config.dry_run})..."
        )
        run = runner.run(profile, config)
        repo.save_run(run)
        print(f"Qualification run completed. Run ID: {run.run_id}")
        print(
            f"Verdict: {run.verdict.verdict.value} | Recommendation: {run.verdict.go_no_go.value}"
        )
        sys.exit(0)

    if args.show_traceability_matrix:
        print(format_traceability_matrix())
        sys.exit(0)

    if args.run_id:
        run = repo.get_run(args.run_id)
        if not run:
            print(f"Error: Run {args.run_id} not found.")
            sys.exit(1)

        if args.show_qualification_summary:
            print(format_qualification_summary(run))
        elif args.show_scenario_results:
            print(format_scenario_results(run))
        elif args.show_forbidden_action_results:
            print(format_forbidden_action_results(run))
        elif args.show_contract_verification:
            print(format_contract_verification(run))
        elif args.show_evidence_pack:
            print(format_evidence_pack(run))
        elif args.show_certification_status:
            print(f"Profile: {run.profile.value}")
            print(f"Verdict: {run.verdict.verdict.value}")
            print(f"Recommendation: {run.verdict.go_no_go.value}")
        elif args.show_waivers:
            print("=== Active Waivers ===")
            print("Mock: No waivers registered for this run.")
    else:
        # Default behavior or no matching command
        parser.print_help()


if __name__ == "__main__":
    main()
