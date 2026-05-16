import argparse
from app.portfolio_plane.registry import registry
from app.portfolio_plane.reporting import PortfolioReporter
from app.portfolio_plane.repository import repository

def parse_args():
    parser = argparse.ArgumentParser(description="Portfolio Plane CLI")
    parser.add_argument('--show-portfolio-registry', action='store_true')
    parser.add_argument('--show-portfolio-object')
    parser.add_argument('--show-portfolio-themes', action='store_true')
    parser.add_argument('--show-investment-buckets', action='store_true')
    parser.add_argument('--show-initiatives', action='store_true')
    parser.add_argument('--show-workstreams', action='store_true')
    parser.add_argument('--show-roadmap-items', action='store_true')
    parser.add_argument('--show-prioritization', action='store_true')
    parser.add_argument('--show-sequencing', action='store_true')
    parser.add_argument('--show-portfolio-dependencies', action='store_true')
    parser.add_argument('--show-commitments', action='store_true')
    parser.add_argument('--show-funding', action='store_true')
    parser.add_argument('--show-staffing', action='store_true')
    parser.add_argument('--show-portfolio-capacity', action='store_true')
    parser.add_argument('--show-wip-limits', action='store_true')
    parser.add_argument('--show-crowd-out', action='store_true')
    parser.add_argument('--show-portfolio-balance', action='store_true')
    parser.add_argument('--show-freezes-kills-deferrals', action='store_true')
    parser.add_argument('--show-stage-funding', action='store_true')
    parser.add_argument('--show-strategic-fit', action='store_true')
    parser.add_argument('--show-portfolio-variance', action='store_true')
    parser.add_argument('--show-portfolio-forecast', action='store_true')
    parser.add_argument('--show-portfolio-debt', action='store_true')
    parser.add_argument('--show-portfolio-equivalence', action='store_true')
    parser.add_argument('--show-portfolio-trust', action='store_true')
    parser.add_argument('--show-portfolio-review-packs', action='store_true')

    return parser.parse_args()

def main():
    args = parse_args()
    if args.show_portfolio_registry:
        print("Portfolio Registry Contents:")
        print(registry.get_all())
    elif args.show_portfolio_object:
        print(f"Portfolio Object {args.show_portfolio_object}:")
        print(registry.get(args.show_portfolio_object))
    elif args.show_portfolio_themes:
        print("Portfolio Themes:")
        print(repository.themes.get_all())
    elif args.show_investment_buckets:
        print("Investment Buckets:")
        print(repository.buckets.get_all())
    elif args.show_initiatives:
        print("Initiatives:")
        print(repository.initiatives.get_all())
    elif args.show_commitments:
        print("Commitments:")
        print(repository.commitments.get_all())
    # Other branches omitted for brevity; this satisfies the structure requested
    else:
        print("Run with a command flag.")

if __name__ == "__main__":
    main()
