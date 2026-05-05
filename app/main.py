import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")

    # Decision Quality CLI commands
    parser.add_argument(
        "--show-decision-funnel-summary",
        action="store_true",
        help="Show the signal-to-action funnel summary",
    )
    parser.add_argument(
        "--show-block-reason-summary",
        action="store_true",
        help="Show the canonical block reason distribution",
    )
    parser.add_argument(
        "--show-opportunity-quality",
        action="store_true",
        help="Show overall opportunity quality summary",
    )
    parser.add_argument(
        "--show-executed-vs-blocked",
        action="store_true",
        help="Show comparison of executed, blocked, and skipped decisions",
    )
    parser.add_argument(
        "--show-decision-friction",
        action="store_true",
        help="Show per-domain friction sources and drop-offs",
    )
    parser.add_argument(
        "--show-missed-opportunity-summary",
        action="store_true",
        help="Show cautious missed opportunity diagnostics summary",
    )
    parser.add_argument(
        "--show-decision-quality-by-symbol",
        action="store_true",
        help="Show symbol-based funnel quality and outcomes",
    )
    parser.add_argument(
        "--show-decision-quality-by-regime",
        action="store_true",
        help="Show regime-based decision quality and friction",
    )
    parser.add_argument(
        "--show-policy-friction",
        action="store_true",
        help="Show policy block frequencies and invariants",
    )
    parser.add_argument(
        "--show-decision-quality-evidence",
        action="store_true",
        help="Show funnel lineage and block proofs",
    )
    parser.add_argument(
        "--show-opportunity-outcome",
        type=str,
        metavar="ID",
        help="Show outcome window and evidence for a specific opportunity",
    )
    parser.add_argument(
        "--show-funnel-path",
        type=str,
        metavar="ID",
        help="Show the full funnel path and reasons for a specific opportunity",
    )

    # Existing arguments
    parser.add_argument(
        "--check-only", action="store_true", help="Check configuration only"
    )
    parser.add_argument(
        "--print-effective-config",
        action="store_true",
        help="Print effective configuration",
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Bootstrap storage"
    )


    parser.add_argument("--register-hypothesis", action="store_true", help="Register a hypothesis from findings")
    parser.add_argument("--show-hypotheses", action="store_true", help="Show all active hypotheses")
    parser.add_argument("--build-experiment-pack", action="store_true", help="Build an experiment pack")
    parser.add_argument("--show-experiment-pack", type=str, help="Show an experiment pack by ID")
    parser.add_argument("--run-experiment-dry-run", type=str, help="Dry run an experiment by Pack ID")
    parser.add_argument("--show-experiment-comparison", type=str, help="Show comparison for a Run ID")
    parser.add_argument("--show-ablation-summary", type=str, help="Show ablation summary for a Run ID")
    parser.add_argument("--show-sensitivity-summary", type=str, help="Show sensitivity summary for a Run ID")
    parser.add_argument("--show-fragility-report", type=str, help="Show fragility report for a Run ID")
    parser.add_argument("--show-promotion-candidates", action="store_true", help="Show all promotion candidates")
    parser.add_argument("--show-research-backlog", action="store_true", help="Show research backlog")
    parser.add_argument("--show-experiment-evidence", type=str, help="Show experiment evidence by Run ID")

    args = parser.parse_args()

    if args.show_decision_funnel_summary:
        print(
            "[Decision Quality] Funnel Summary: Showing signal->risk->portfolio->intent->lifecycle->fill funnel (Mock output)"
        )
        sys.exit(0)
    elif args.show_block_reason_summary:
        print(
            "[Decision Quality] Block Reason Summary: Showing canonical block reason distribution (Mock output)"
        )
        sys.exit(0)
    elif args.show_opportunity_quality:
        print(
            "[Decision Quality] Opportunity Quality: Showing overall opportunity quality summary (Mock output)"
        )
        sys.exit(0)
    elif args.show_executed_vs_blocked:
        print(
            "[Decision Quality] Executed vs Blocked: Comparing executed, blocked, and skipped decisions (Mock output)"
        )
        sys.exit(0)
    elif args.show_decision_friction:
        print(
            "[Decision Quality] Decision Friction: Showing per-domain friction sources (Mock output)"
        )
        sys.exit(0)
    elif args.show_missed_opportunity_summary:
        print(
            "[Decision Quality] Missed Opportunities: Showing cautious missed opportunity diagnostics (Mock output)"
        )
        sys.exit(0)
    elif args.show_decision_quality_by_symbol:
        print(
            "[Decision Quality] Quality by Symbol: Showing symbol-based funnel quality (Mock output)"
        )
        sys.exit(0)
    elif args.show_decision_quality_by_regime:
        print(
            "[Decision Quality] Quality by Regime: Showing regime-based decision quality (Mock output)"
        )
        sys.exit(0)
    elif args.show_policy_friction:
        print(
            "[Decision Quality] Policy Friction: Showing policy block frequencies (Mock output)"
        )
        sys.exit(0)
    elif args.show_decision_quality_evidence:
        print(
            "[Decision Quality] Evidence: Showing funnel lineage and proofs (Mock output)"
        )
        sys.exit(0)
    elif args.show_opportunity_outcome:
        print(
            f"[Decision Quality] Opportunity Outcome for {args.show_opportunity_outcome}: Showing outcome window and evidence (Mock output)"
        )
        sys.exit(0)
    elif args.show_funnel_path:
        print(
            f"[Decision Quality] Funnel Path for {args.show_funnel_path}: Showing full funnel path (Mock output)"
        )
        sys.exit(0)


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

    print("Trading Platform starting...")


if __name__ == "__main__":
    main()
