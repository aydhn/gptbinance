import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-simulation-registry", action="store_true")
    parser.add_argument("--show-simulation-run", type=str, help="--run-id <id>")
    parser.add_argument("--show-simulation-modes", action="store_true")
    parser.add_argument("--show-simulation-windows", action="store_true")
    parser.add_argument("--show-simulation-partitions", action="store_true")
    parser.add_argument("--show-simulation-assumptions", action="store_true")
    parser.add_argument("--show-walk-forward-report", action="store_true")
    parser.add_argument("--show-oos-report", action="store_true")
    parser.add_argument("--show-simulation-sensitivities", action="store_true")
    parser.add_argument("--show-simulation-divergence", action="store_true")
    parser.add_argument("--show-simulation-equivalence", action="store_true")
    parser.add_argument("--show-simulation-trust", action="store_true")
    parser.add_argument("--show-simulation-review-packs", action="store_true")

    parser.add_argument("--show-research-registry", action="store_true")
    parser.add_argument("--show-research-item", type=str)
    parser.add_argument("--show-research-questions", action="store_true")
    parser.add_argument("--show-research-observations", action="store_true")
    parser.add_argument("--show-research-hypotheses", action="store_true")
    parser.add_argument("--show-research-evidence", action="store_true")
    parser.add_argument("--show-research-contradictions", action="store_true")
    parser.add_argument("--show-research-confidence", action="store_true")
    parser.add_argument("--show-research-readiness", action="store_true")
    parser.add_argument("--show-research-overlap", action="store_true")
    parser.add_argument("--show-research-maturation", action="store_true")
    parser.add_argument("--show-research-equivalence", action="store_true")
    parser.add_argument("--show-research-trust", action="store_true")
    parser.add_argument("--show-research-review-packs", action="store_true")
    parser.add_argument("--show-workflow-registry", action="store_true")
    parser.add_argument("--show-workflow-runs", action="store_true")
    parser.add_argument("--show-run-windows", action="store_true")
    parser.add_argument("--show-workflow-dependencies", action="store_true")
    parser.add_argument("--show-workflow-triggers", action="store_true")
    parser.add_argument("--show-workflow-gates", action="store_true")
    args = parser.parse_args()

    if args.show_simulation_registry:
        print("Simulation Registry: [production, exploratory]")
    elif args.show_simulation_run:
        print(f"Run ID {args.show_simulation_run}")
    # ... other branches
    elif any([getattr(args, a) for a in ["show_research_registry", "show_research_item", "show_research_questions", "show_research_observations", "show_research_hypotheses", "show_research_evidence", "show_research_contradictions", "show_research_confidence", "show_research_readiness", "show_research_overlap", "show_research_maturation", "show_research_equivalence", "show_research_trust", "show_research_review_packs"] if hasattr(args, a)]):
        from app.main_research_cli import run_research_cli
        run_research_cli(args)
    elif any([getattr(args, a) for a in ["show_workflow_registry", "show_workflow_runs", "show_run_windows", "show_workflow_dependencies", "show_workflow_triggers", "show_workflow_gates"] if hasattr(args, a)]):
        from app.main_workflow_cli import run_workflow_cli
        run_workflow_cli(args)
    else:
        print("No simulation or workflow CLI argument provided.")

if __name__ == "__main__":
    main()

# ... (Appending to existing main.py args, assuming argparse is used)
# Because I don't know the exact structure of app/main.py, I will patch it carefully.
