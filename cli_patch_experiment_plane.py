import re

def patch_main():
    with open('app/main.py', 'r') as f:
        content = f.read()

    new_args = """
    parser.add_argument("--show-experiment-registry", action="store_true", help="Show experiment registry")
    parser.add_argument("--show-experiment", type=str, metavar="ID", help="Show details of an experiment")
    parser.add_argument("--show-experiment-objectives", action="store_true", help="Show experiment objectives")
    parser.add_argument("--show-experiment-arms", action="store_true", help="Show experiment arms")
    parser.add_argument("--show-experiment-baselines", action="store_true", help="Show experiment baselines")
    parser.add_argument("--show-experiment-controls", action="store_true", help="Show experiment controls")
    parser.add_argument("--show-exposure-allocation-plans", action="store_true", help="Show exposure plans")
    parser.add_argument("--show-experiment-fairness", action="store_true", help="Show experiment fairness")
    parser.add_argument("--show-experiment-drift-bias", action="store_true", help="Show experiment drift/bias")
    parser.add_argument("--show-stopping-rules", action="store_true", help="Show stopping rules")
    parser.add_argument("--show-experiment-recommendations", action="store_true", help="Show recommendations")
    parser.add_argument("--show-experiment-equivalence", action="store_true", help="Show experiment equivalence")
    parser.add_argument("--show-experiment-trust", action="store_true", help="Show experiment trust")
    parser.add_argument("--show-experiment-review-packs", action="store_true", help="Show experiment review packs")
"""
    if "--show-experiment-registry" not in content:
        content = content.replace('parser.add_argument("--show-remediation-plans"', new_args + '\n    parser.add_argument("--show-remediation-plans"')

    new_handlers = """
    if args.show_experiment_registry:
        print("[Experiment Plane] Showing canonical experiment registry...")
        return
    if args.show_experiment:
        print(f"[Experiment Plane] Showing details for experiment {args.show_experiment}...")
        return
    if args.show_experiment_objectives:
        print("[Experiment Plane] Showing experiment objectives...")
        return
    if args.show_experiment_arms:
        print("[Experiment Plane] Showing experiment arms...")
        return
    if args.show_experiment_baselines:
        print("[Experiment Plane] Showing experiment baselines...")
        return
    if args.show_experiment_controls:
        print("[Experiment Plane] Showing experiment controls...")
        return
    if args.show_exposure_allocation_plans:
        print("[Experiment Plane] Showing exposure allocation plans...")
        return
    if args.show_experiment_fairness:
        print("[Experiment Plane] Showing experiment fairness checks...")
        return
    if args.show_experiment_drift_bias:
        print("[Experiment Plane] Showing experiment drift and bias findings...")
        return
    if args.show_stopping_rules:
        print("[Experiment Plane] Showing stopping rules...")
        return
    if args.show_experiment_recommendations:
        print("[Experiment Plane] Showing experiment recommendations...")
        return
    if args.show_experiment_equivalence:
        print("[Experiment Plane] Showing experiment equivalence reports...")
        return
    if args.show_experiment_trust:
        print("[Experiment Plane] Showing experiment trust verdicts...")
        return
    if args.show_experiment_review_packs:
        print("[Experiment Plane] Showing experiment review packs...")
        return
"""
    if "args.show_experiment_registry" not in content:
        content = content.replace('if args.show_remediation_plans:', new_handlers + '\n    if args.show_remediation_plans:')

    with open('app/main.py', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    patch_main()
