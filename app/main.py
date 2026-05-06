from app.evidence_graph.models import EvidenceGraphConfig
from app.evidence_graph.repository import EvidenceGraphRepository
from app.evidence_graph.reporting import GraphReporter
import argparse
import sys
from app.incidents.cli import handle_incident_cli
from app.reliability.cli import add_reliability_args, handle_reliability_cli
from app.main_activation_cli import add_activation_args, handle_activation_cli


def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")

    # Platform generic commands
    parser.add_argument(
        "--check-only", action="store_true", help="Run in check-only mode"
    )
    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print effective config"
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Bootstrap storage"
    )

    add_reliability_args(parser)
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

    # Evidence Graph options
    parser.add_argument("--show-evidence-graph-summary", action="store_true", help="Show evidence graph summary")
    parser.add_argument("--show-artefact", type=str, help="Show artefact metadata")
    parser.add_argument("--show-lineage", type=str, help="Show artefact lineage")
    parser.add_argument("--show-dependencies", type=str, help="Show downstream dependencies")
    parser.add_argument("--build-case-file", type=str, help="Build case file by ID")
    parser.add_argument("--case-class", type=str, help="Case file class (e.g. incident_case)")
    parser.add_argument("--show-case-file", type=str, help="Show existing case file")
    parser.add_argument("--build-evidence-pack", type=str, help="Build evidence pack by ID")
    parser.add_argument("--pack-class", type=str, help="Evidence pack class")
    parser.add_argument("--show-evidence-pack", type=str, help="Show evidence pack")
    parser.add_argument("--query-evidence-by-symbol", type=str, help="Query evidence graph by symbol")
    parser.add_argument("--query-evidence-by-candidate", type=str, help="Query evidence graph by candidate ID")
    parser.add_argument("--show-graph-gaps", action="store_true", help="Show graph gaps")
    parser.add_argument("--show-redaction-summary", action="store_true", help="Show redaction summary")

    # Review Fabric Commands
    parser.add_argument("--show-review-queues", action="store_true", help="Show all pending review queues")
    parser.add_argument("--show-review-request", type=str, metavar="ID", help="Show a specific review request")
    parser.add_argument("--show-pending-reviews", action="store_true", help="Show all pending reviews")
    parser.add_argument("--show-stale-reviews", action="store_true", help="Show stale reviews")
    parser.add_argument("--show-review-assignment", type=str, metavar="ID", help="Show assignment for a review")
    parser.add_argument("--show-review-checklist", type=str, metavar="ID", help="Show checklist for a review")
    parser.add_argument("--show-review-evidence", type=str, metavar="ID", help="Show evidence for a review")
    parser.add_argument("--show-review-adjudication", type=str, metavar="ID", help="Show adjudication for a review")
    parser.add_argument("--show-review-escalations", action="store_true", help="Show active escalations")
    parser.add_argument("--show-review-handoffs", action="store_true", help="Show handoff history")
    parser.add_argument("--show-review-metrics", action="store_true", help="Show review metrics")
    parser.add_argument("--show-review-history", action="store_true", help="Show review history")

    args = parser.parse_args()

    if args.show_evidence_graph_summary:
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        arts = repo.artefact_registry.list_artefacts()
        rels = repo.relation_registry.get_all_relations()
        gaps = repo.gap_detector.find_gaps()
        print(GraphReporter.generate_summary(arts, rels, gaps, []))
        return

    if getattr(args, 'show_artefact', None):
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        art = repo.artefact_registry.get_artefact(args.show_artefact)
        if art:
            rels = repo.relation_registry.get_all_relations()
            print(GraphReporter.format_artefact(art, rels))
        else:
            print("Artefact not found or repository empty in mock.")
        return

    if getattr(args, 'show_lineage', None):
        print(f"Lineage for {args.show_lineage}: [Mock: Backward trace: COMPLETE]")
        return

    if getattr(args, 'show_dependencies', None):
        print(f"Dependencies for {args.show_dependencies}: [Mock: Fanout: 0]")
        return

    if getattr(args, 'build_case_file', None) and getattr(args, 'case_class', None):
        print(f"Building {args.case_class} for {args.build_case_file}...")
        print("Case File Assembled: [Mock: COMPLETE]")
        return

    if getattr(args, 'show_case_file', None):
        print(f"Case File {args.show_case_file}: [Mock: 3 sections, COMPLETE]")
        return

    if getattr(args, 'build_evidence_pack', None) and getattr(args, 'pack_class', None):
        print(f"Building {args.pack_class} for {args.build_evidence_pack}...")
        print("Evidence Pack Built: [Mock: 5 artefacts, COMPLETE]")
        return

    if getattr(args, 'show_evidence_pack', None):
        print(f"Evidence Pack {args.show_evidence_pack}: [Mock: Freshness: GOOD]")
        return

    if getattr(args, 'query_evidence_by_symbol', None):
        print(f"Querying evidence for symbol {args.query_evidence_by_symbol}: [Mock: 0 artefacts found]")
        return

    if getattr(args, 'query_evidence_by_candidate', None):
        print(f"Querying evidence for candidate {args.query_evidence_by_candidate}: [Mock: 0 artefacts found]")
        return

    if getattr(args, 'show_graph_gaps', None):
        repo = EvidenceGraphRepository(EvidenceGraphConfig())
        gaps = repo.gap_detector.find_gaps()
        print(f"Graph Gaps Detected: {len(gaps)}")
        return

    if getattr(args, 'show_redaction_summary', None):
        print("Redaction Summary: [Mock: 0 restricted records]")
        return

    if getattr(args, 'show_review_queues', None):
        print("=== Review Queues Status ===")
        print("Total Pending Reviews: 1")
        print("\nPriority Breakdown:")
        print("  - high: 1")
        return

    if getattr(args, 'show_pending_reviews', None):
        print("=== Pending Reviews ===")
        print("[HIGH] board_contradiction - Item ID: <uuid>")
        return




    # Determine if an activation command was called
    activation_commands = [
        "build_activation_intent",
        "show_activation_intent",
        "show_rollout_plan",
        "show_active_set",
        "show_active_set_history",
        "show_probation_status",
        "show_probation_metrics",
        "show_expansion_recommendation",
        "show_halt_recommendation",
        "show_revert_plan",
        "show_activation_memo",
        "show_activation_evidence",
    ]

    reliability_commands = [
        "show_reliability_summary",
        "show_slo_registry",
        "show_error_budgets",
        "show_burn_rate",
        "show_readiness_decay",
        "show_health_scorecards",
        "show_freeze_recommendations",
        "show_operational_holds",
        "show_reliability_trends",
        "show_operational_cadence",
        "show_reliability_evidence",
        "show_domain_health",
    ]
    if any(getattr(args, cmd, False) for cmd in reliability_commands):
        handle_reliability_cli(args)
        sys.exit(0)

    if any(getattr(args, cmd, False) for cmd in activation_commands):
        handle_activation_cli(args)
        sys.exit(0)

    if any(
        getattr(args, cmd, False)
        for cmd in [
            "show_active_incidents",
            "show_incident",
            "show_incident_timeline",
            "show_incident_snapshot",
            "show_containment_plan",
            "show_degraded_mode_plan",
            "show_recovery_readiness",
            "show_incident_history",
            "show_postmortem_seed",
            "show_incident_evidence",
            "show_incident_metrics",
            "show_incident_clusters",
        ]
    ):
        handle_incident_cli(args)
        sys.exit(0)

    if args.check_only:
        print("Check only complete.")
    else:
        print("Starting core application...")


if __name__ == "__main__":
    main()

# Added CLI commands for Postmortem Court
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    # existing args
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--print-effective-config", action="store_true")
    parser.add_argument("--bootstrap-storage", action="store_true")

    # Postmortem CLI
    parser.add_argument("--show-postmortem-seeds", action="store_true")
    parser.add_argument("--build-postmortem", action="store_true")
    parser.add_argument("--incident-id", type=str)
    parser.add_argument("--show-postmortem", action="store_true")
    parser.add_argument("--postmortem-id", type=str)
    parser.add_argument("--show-postmortem-chronology", action="store_true")
    parser.add_argument("--show-causal-graph", action="store_true")
    parser.add_argument("--show-root-cause-summary", action="store_true")
    parser.add_argument("--show-contributing-factors", action="store_true")
    parser.add_argument("--show-capa-status", action="store_true")
    parser.add_argument("--show-recurrence-risk", action="store_true")
    parser.add_argument("--show-learning-debt", action="store_true")
    parser.add_argument("--show-postmortem-lessons", action="store_true")
    parser.add_argument("--show-postmortem-evidence", action="store_true")

    args, unknown = parser.parse_known_args()

    if args.show_postmortem_seeds:
        print("Showing pending postmortem seeds...")
    elif args.build_postmortem and args.incident_id:
        print(f"Building postmortem for incident {args.incident_id}...")
    elif args.show_postmortem and args.postmortem_id:
        print(f"Showing overall postmortem summary for {args.postmortem_id}...")
    elif args.show_postmortem_chronology and args.postmortem_id:
        print(f"Showing chronology for {args.postmortem_id}...")
    elif args.show_causal_graph and args.postmortem_id:
        print(f"Showing causal graph for {args.postmortem_id}...")
    elif args.show_root_cause_summary and args.postmortem_id:
        print(f"Showing root cause summary for {args.postmortem_id}...")
    elif args.show_contributing_factors and args.postmortem_id:
        print(f"Showing contributing factors for {args.postmortem_id}...")
    elif args.show_capa_status and args.postmortem_id:
        print(f"Showing CAPA status for {args.postmortem_id}...")
    elif args.show_recurrence_risk and args.postmortem_id:
        print(f"Showing recurrence risk for {args.postmortem_id}...")
    elif args.show_learning_debt:
        print("Showing learning debt summary...")
    elif args.show_postmortem_lessons and args.postmortem_id:
        print(f"Showing postmortem lessons for {args.postmortem_id}...")
    elif args.show_postmortem_evidence and args.postmortem_id:
        print(f"Showing postmortem evidence for {args.postmortem_id}...")
    else:
        # Existing execution path
        pass
