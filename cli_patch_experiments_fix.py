import re


def update_main():
    with open("app/main.py", "r") as f:
        content = f.read()

    handlers = """
    if args.register_hypothesis:
        print("Registering hypothesis from findings...")
        from app.experiments.hypotheses import HypothesisRegistry, FindingToHypothesisCompiler
        from app.experiments.enums import HypothesisClass
        registry = HypothesisRegistry()
        compiler = FindingToHypothesisCompiler()
        h = compiler.compile({"finding_id": "f_1", "summary": "CLI registration test", "domain": "policy"}, HypothesisClass.POLICY_FRICTION_EXCESSIVE_IN_REGIME, "Test rationale")
        h_id = registry.register(h)
        print(f"Registered hypothesis: {h_id}")
        return

    if args.show_hypotheses:
        print("Showing active hypotheses...")
        return

    if args.build_experiment_pack:
        print("Building experiment pack...")
        return

    if args.show_experiment_pack:
        print(f"Showing experiment pack {args.show_experiment_pack}...")
        return

    if args.run_experiment_dry_run:
        print(f"Dry running experiment pack {args.run_experiment_dry_run}...")
        return

    if args.show_experiment_comparison:
        print(f"Showing comparison for run {args.show_experiment_comparison}...")
        return

    if args.show_ablation_summary:
        print(f"Showing ablation summary for run {args.show_ablation_summary}...")
        return

    if args.show_sensitivity_summary:
        print(f"Showing sensitivity summary for run {args.show_sensitivity_summary}...")
        return

    if args.show_fragility_report:
        print(f"Showing fragility report for run {args.show_fragility_report}...")
        return

    if args.show_promotion_candidates:
        print("Showing promotion candidates...")
        return

    if args.show_research_backlog:
        print("Showing research backlog...")
        return

    if args.show_experiment_evidence:
        print(f"Showing experiment evidence for run {args.show_experiment_evidence}...")
        return
"""

    if "args.register_hypothesis:" not in content:
        content = content.replace(
            'print("Trading Platform starting...")',
            handlers + '\n    print("Trading Platform starting...")',
        )

    with open("app/main.py", "w") as f:
        f.write(content)


if __name__ == "__main__":
    update_main()
