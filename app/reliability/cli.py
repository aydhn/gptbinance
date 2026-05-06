from app.reliability.reporting import ReliabilityReporter
from app.reliability.repository import repository
from app.reliability.domains import domain_registry
from app.reliability.slos import slo_registry


def add_reliability_args(parser):
    parser.add_argument(
        "--show-reliability-summary",
        action="store_true",
        help="Show overall operational readiness summary",
    )
    parser.add_argument(
        "--show-slo-registry", action="store_true", help="Show active SLO definitions"
    )
    parser.add_argument(
        "--show-error-budgets",
        action="store_true",
        help="Show per-domain error budgets",
    )
    parser.add_argument(
        "--show-burn-rate",
        action="store_true",
        help="Show short/long window burn rates",
    )
    parser.add_argument(
        "--show-readiness-decay",
        action="store_true",
        help="Show readiness decay contributors",
    )
    parser.add_argument(
        "--show-health-scorecards", action="store_true", help="Show domain scorecards"
    )
    parser.add_argument(
        "--show-freeze-recommendations",
        action="store_true",
        help="Show change freeze recommendations",
    )
    parser.add_argument(
        "--show-operational-holds",
        action="store_true",
        help="Show operational hold recommendations",
    )
    parser.add_argument(
        "--show-reliability-trends",
        action="store_true",
        help="Show reliability degradation patterns",
    )
    parser.add_argument(
        "--show-operational-cadence",
        action="store_true",
        help="Show operational cadence artifacts",
    )
    parser.add_argument(
        "--show-reliability-evidence",
        action="store_true",
        help="Show reliability evidence bundle refs",
    )
    parser.add_argument(
        "--show-domain-health",
        type=str,
        metavar="DOMAIN",
        help="Show specific domain health summary",
    )


def handle_reliability_cli(args):
    if args.show_reliability_summary:
        print("Showing overall operational readiness summary...")
    elif args.show_slo_registry:
        print(ReliabilityReporter.format_slos(slo_registry.list_all()))
    elif args.show_error_budgets:
        print("Showing error budgets...")
    elif args.show_burn_rate:
        print("Showing burn rates...")
    elif args.show_readiness_decay:
        print("Showing readiness decay...")
    elif args.show_health_scorecards:
        print(ReliabilityReporter.format_scorecards(repository.get_latest_scorecards()))
    elif args.show_freeze_recommendations:
        print(
            ReliabilityReporter.format_freeze(repository.get_freeze_recommendations())
        )
    elif args.show_operational_holds:
        print("Showing operational holds...")
    elif args.show_reliability_trends:
        print("Showing reliability trends...")
    elif args.show_operational_cadence:
        print(ReliabilityReporter.format_cadence(repository.get_cadence_artifacts()))
    elif args.show_reliability_evidence:
        print("Showing reliability evidence...")
    elif args.show_domain_health:
        print(f"Showing health for domain: {args.show_domain_health}...")
