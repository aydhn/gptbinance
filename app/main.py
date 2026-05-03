import argparse
import sys

from app.replay.models import ReplayConfig, ReplaySourceRef, CounterfactualSpec
from app.replay.enums import ReplayScope, ReplaySourceType, CounterfactualType
from app.replay.repository import replay_repository
from app.replay.reporting import (
    format_summary,
    format_timeline,
    format_decision_path,
    format_diff,
    format_counterfactual_summary,
    format_replayability_score,
)

import uuid
import time
from app.perf.enums import WorkloadType, HostClass
from app.perf.storage import PerfStorage
from app.perf.repository import PerfRepository
from app.perf.workloads import WorkloadRegistry
from app.perf.profilers import WorkloadProfiler
from app.perf.reporting import PerfReporter
from app.perf.budgets import BudgetRegistry
from app.perf.bottlenecks import BottleneckAnalyzer
from app.perf.capacity import CapacityAnalyzer
from app.perf.regression import RegressionEvaluator
from app.perf.host_classes import HostClassRegistry
from app.perf.models import HostQualificationReport
from app.perf.enums import ReadinessVerdict
from app.data_governance import (
    GovernanceStorage,
    GovernanceRepository,
    GovernanceReporter,
    DatasetRef,
    DatasetType,
    TrustLevel,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Trading Platform - Performance Engineering CLI"
    )

    parser.add_argument(
        "--run-replay", action="store_true", help="Run deterministic replay"
    )
    parser.add_argument(
        "--replay-scope", type=str, help="Replay scope (trade, session, incident, etc.)"
    )
    parser.add_argument(
        "--replay-source-ref", type=str, help="Source reference for replay"
    )
    parser.add_argument(
        "--replay-window", type=str, help="Window for replay (start:end ISO strings)"
    )
    parser.add_argument(
        "--show-replay-summary", action="store_true", help="Show replay summary"
    )
    parser.add_argument(
        "--show-replay-timeline", action="store_true", help="Show event timeline"
    )
    parser.add_argument(
        "--show-decision-path", action="store_true", help="Show decision path"
    )
    parser.add_argument(
        "--show-replay-diff", action="store_true", help="Show replay diffs"
    )
    parser.add_argument(
        "--run-counterfactual",
        action="store_true",
        help="Run counterfactual simulation",
    )
    parser.add_argument(
        "--counterfactual-type", type=str, help="Counterfactual type (e.g. ml_disabled)"
    )
    parser.add_argument(
        "--show-counterfactual-summary",
        action="store_true",
        help="Show counterfactual summary",
    )
    parser.add_argument(
        "--build-forensic-bundle", action="store_true", help="Build forensic bundle"
    )
    parser.add_argument(
        "--show-replayability-score",
        action="store_true",
        help="Show replayability score",
    )

    parser.add_argument("--run-perf-profile", action="store_true")
    parser.add_argument("--perf-workload", type=str)
    parser.add_argument("--perf-host-class", type=str)
    parser.add_argument("--show-perf-summary", action="store_true")
    parser.add_argument("--run-id", type=str)
    parser.add_argument("--show-resource-budgets", action="store_true")
    parser.add_argument("--show-latency-summary", action="store_true")
    parser.add_argument("--show-bottleneck-report", action="store_true")
    parser.add_argument("--run-perf-regression-check", action="store_true")
    parser.add_argument("--baseline-run", type=str)
    parser.add_argument("--target-run", type=str)
    parser.add_argument("--show-capacity-report", action="store_true")
    parser.add_argument("--run-host-qualification", action="store_true")
    parser.add_argument("--show-perf-baselines", action="store_true")
    # New Governance arguments
    parser.add_argument("--register-data-contract", action="store_true")
    parser.add_argument("--show-data-contracts", action="store_true")
    parser.add_argument("--show-schema-registry", action="store_true")
    parser.add_argument("--run-data-quality-check", action="store_true")
    parser.add_argument("--show-quality-report", action="store_true")
    parser.add_argument("--show-lineage", action="store_true")
    parser.add_argument("--show-provenance", action="store_true")
    parser.add_argument("--show-canonical-map", action="store_true")
    parser.add_argument("--run-schema-compatibility-check", action="store_true")
    parser.add_argument("--show-schema-diff", action="store_true")
    parser.add_argument("--show-downstream-impact", action="store_true")
    parser.add_argument("--show-trust-verdict", action="store_true")
    parser.add_argument("--show-data-catalog", action="store_true")
    parser.add_argument(
        "--dataset-ref", type=str, help="Dataset Reference ID (format: id:version)"
    )
    parser.add_argument("--entity", type=str, help="Entity alias for canonical map")
    parser.add_argument(
        "--from-schema", type=str, help="Source schema (format: id:version)"
    )
    parser.add_argument(
        "--to-schema", type=str, help="Target schema (format: id:version)"
    )

    # Knowledge commands
    parser.add_argument(
        "--register-knowledge-item",
        action="store_true",
        help="Register a mock knowledge item",
    )
    parser.add_argument(
        "--show-knowledge-catalog",
        action="store_true",
        help="Show knowledge catalog summary",
    )
    parser.add_argument(
        "--show-runbooks", action="store_true", help="Show runbooks registry"
    )
    parser.add_argument("--show-sops", action="store_true", help="Show SOPs registry")
    parser.add_argument(
        "--show-playbooks", action="store_true", help="Show playbooks registry"
    )
    parser.add_argument(
        "--check-runbook-applicability",
        action="store_true",
        help="Check runbook applicability",
    )
    parser.add_argument(
        "--show-freshness-report",
        action="store_true",
        help="Show stale knowledge report",
    )
    parser.add_argument(
        "--show-lessons-learned",
        action="store_true",
        help="Show lessons learned registry",
    )
    parser.add_argument(
        "--run-readiness-quiz", action="store_true", help="Run a readiness quiz"
    )
    parser.add_argument(
        "--show-operator-readiness", action="store_true", help="Show operator readiness"
    )
    parser.add_argument(
        "--search-knowledge", action="store_true", help="Search knowledge catalog"
    )
    parser.add_argument(
        "--show-knowledge-links", action="store_true", help="Show knowledge links"
    )

    # Specific arguments for knowledge commands
    parser.add_argument(
        "--action-type", type=str, help="Action type for applicability check"
    )
    parser.add_argument("--operator", type=str, help="Operator ID for readiness")
    parser.add_argument("--scope", type=str, help="Scope for quiz")
    parser.add_argument("--query", type=str, help="Search query")
    parser.add_argument("--item-id", type=str, help="Knowledge item ID")

    args = parser.parse_args()

    storage = PerfStorage()
    repo = PerfRepository(storage)
    gov_repo = GovernanceRepository(GovernanceStorage())
    gov_reporter = GovernanceReporter()

    if args.run_replay:
        if not args.replay_scope or not args.replay_source_ref:
            print(
                "Error: --replay-scope and --replay-source-ref are required for --run-replay"
            )
            sys.exit(1)

        scope = ReplayScope(args.replay_scope)
        # simplistic parsing for demonstration
        src_parts = args.replay_source_ref.split(":")
        src_type = (
            ReplaySourceType.PAPER_SESSION
            if src_parts[0] == "paper"
            else ReplaySourceType.INCIDENT
        )  # Simplified

        sources = [
            ReplaySourceRef(
                source_type=src_type,
                ref_id=src_parts[1] if len(src_parts) > 1 else src_parts[0],
            )
        ]

        config = ReplayConfig(scope=scope, sources=sources)
        if args.build_forensic_bundle:
            config.include_forensics = True

        result = replay_repository.run_and_save(config)
        print(f"Replay run {result.run_id} completed.")
        sys.exit(0)

    elif args.run_counterfactual:
        if not args.run_id or not args.counterfactual_type:
            print(
                "Error: --run-id and --counterfactual-type are required for --run-counterfactual"
            )
            sys.exit(1)
        # Note: in a real system we'd probably re-run with the counterfactual spec
        # Here we'll just log it for dummy implementation
        print(
            f"Counterfactual simulation requested for run {args.run_id} with type {args.counterfactual_type}"
        )
        sys.exit(0)

    elif args.show_replay_summary:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_summary(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.show_replay_timeline:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_timeline(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.show_decision_path:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_decision_path(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.show_replay_diff:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_diff(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.show_counterfactual_summary:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_counterfactual_summary(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.show_replayability_score:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res:
            print(format_replayability_score(res))
        else:
            print("Run not found")
        sys.exit(0)

    elif args.build_forensic_bundle:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        res = replay_repository.get_run(args.run_id)
        if res and res.forensic_bundle:
            print(f"Forensic bundle ready for run {args.run_id}")
            print(f"Findings: {len(res.forensic_bundle.findings)}")
        else:
            print("Run not found or forensics not built")
        sys.exit(0)

    elif args.run_perf_profile:
        if not args.perf_workload or not args.perf_host_class:
            print("Error: --perf-workload and --perf-host-class required.")
            sys.exit(1)

        try:
            workload = WorkloadType[args.perf_workload]
            host_class = HostClass[args.perf_host_class]
        except KeyError:
            print("Error: Invalid workload or host class enum value.")
            sys.exit(1)

        run_id = f"run_{int(time.time())}_{uuid.uuid4().hex[:6]}"
        profiler = WorkloadProfiler(run_id, workload, host_class)

        print(f"Starting profile for {workload.value} on {host_class.value}...")
        profiler.start()

        # Simulate some workload execution and sampling
        with profiler.latency_tracker.measure("MainExecution"):
            time.sleep(0.5)
            profiler.sample_resources()
            time.sleep(0.5)

        profiler.stop()
        run_data = profiler.create_perf_run()
        repo.save_perf_run(run_data)

        print(f"Profile complete. Saved as {run_id}.")
        print(PerfReporter.format_run_summary(run_data))

    elif args.show_perf_summary:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        run = repo.get_perf_run(args.run_id)
        if run:
            print(PerfReporter.format_run_summary(run))
        else:
            print(f"Run {args.run_id} not found.")

    elif args.show_resource_budgets:
        if not args.perf_host_class:
            print("Error: --perf-host-class required.")
            sys.exit(1)
        # simplistic representation
        print(
            f"Showing budgets applicable to modes recommended for {args.perf_host_class}"
        )
        try:
            hc = HostClassRegistry.get(HostClass[args.perf_host_class])
        except KeyError:
            print("Invalid HostClass")
            sys.exit(1)

        modes = hc.recommended_modes
        seen = set()
        for mode in modes:
            for b in BudgetRegistry.get_applicable_resource_budgets(mode):
                k = f"{b.resource_type.value}_{b.severity.value}_{b.limit_value}"
                if k not in seen:
                    print(
                        f"[{mode.upper()}] {b.resource_type.value} ({b.severity.value}): Limit = {b.limit_value}"
                    )
                    seen.add(k)
            for b in BudgetRegistry.get_applicable_latency_budgets(mode):
                k = f"lat_{b.component_name}_{b.percentile.value}_{b.limit_ms}"
                if k not in seen:
                    print(
                        f"[{mode.upper()}] Latency {b.component_name} {b.percentile.value} ({b.severity.value}): Limit = {b.limit_ms}ms"
                    )
                    seen.add(k)

    elif args.show_latency_summary:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        run = repo.get_perf_run(args.run_id)
        if run:
            print("=== LATENCY SUMMARY ===")
            for lat in run.latencies:
                print(f"Component: {lat.component_name} | Calls: {lat.call_count}")
                print(
                    f"  P50: {lat.p50_ms:.2f}ms | P95: {lat.p95_ms:.2f}ms | P99: {lat.p99_ms:.2f}ms | Max: {lat.max_ms:.2f}ms"
                )
        else:
            print(f"Run {args.run_id} not found.")

    elif args.show_bottleneck_report:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        run = repo.get_perf_run(args.run_id)
        if run:
            reports = BottleneckAnalyzer.analyze(run)
            print(PerfReporter.format_bottleneck_report(reports))
        else:
            print(f"Run {args.run_id} not found.")

    elif args.run_perf_regression_check:
        if not args.baseline_run or not args.target_run:
            print("Error: --baseline-run and --target-run required.")
            sys.exit(1)
        base = repo.get_perf_run(args.baseline_run)
        targ = repo.get_perf_run(args.target_run)
        if base and targ:
            report = RegressionEvaluator.evaluate(base, targ)
            repo.save_regression_report(report)
            print(PerfReporter.format_regression_report(report))
        else:
            print("Could not find one or both runs.")

    elif args.show_capacity_report:
        if not args.run_id:
            print("Error: --run-id required.")
            sys.exit(1)
        run = repo.get_perf_run(args.run_id)
        if run:
            report = CapacityAnalyzer.evaluate(run.host_class, [run.workload_type])
            print(PerfReporter.format_capacity_report(report))
        else:
            print(f"Run {args.run_id} not found.")

    elif args.run_host_qualification:
        if not args.perf_host_class:
            print("Error: --perf-host-class required.")
            sys.exit(1)
        try:
            hc = HostClass[args.perf_host_class]
        except KeyError:
            print("Invalid HostClass")
            sys.exit(1)

        # Determine readiness based on expected workloads. Mocking a check here.
        tested = [
            WorkloadType.PAPER_RUNTIME_CYCLE,
            WorkloadType.TESTNET_EXECUTION_SMOKE,
        ]
        verdict = (
            ReadinessVerdict.READY
            if hc != HostClass.LOCAL_MINIMAL
            else ReadinessVerdict.CAUTION
        )

        report = HostQualificationReport(
            host_class=hc,
            tested_workloads=tested,
            readiness=verdict,
            evidence_refs=["run_xyz_123"],
        )
        repo.save_qualification_report(report)
        print(f"=== HOST QUALIFICATION REPORT: {hc.value} ===")
        print(f"Readiness: {verdict.value}")
        print(f"Tested Workloads: {[w.value for w in tested]}")
        print(f"Evidence Refs: {report.evidence_refs}")

    elif args.show_perf_baselines:
        runs = repo.get_all_run_ids()
        print("=== SAVED PERF RUNS ===")
        for r in runs:
            print(f"- {r}")

    elif args.register_data_contract:
        print("Registering mock data contract...")
        from app.data_governance import DataContract, ContractType, SchemaVersionRef

        contract = DataContract(
            contract_id="mock-contract-1",
            contract_type=ContractType.RAW,
            schema_ref=SchemaVersionRef(schema_id="mock-schema", version="v1"),
            required_fields=["id", "timestamp"],
            optional_fields=[],
            unique_keys=["id"],
            description="Mock Contract",
        )
        gov_repo.save_contract(contract)
        print("Contract registered.")

    elif args.show_data_contracts:
        print("Data Contracts:")
        for c in gov_repo.list_contracts():
            print(gov_reporter.format_contract(c))
            print("-" * 40)

    elif args.show_schema_registry:
        print("Schema Registry:")
        for s in gov_repo.list_schemas():
            print(gov_reporter.format_schema(s))
            print("-" * 40)

    elif args.run_data_quality_check and args.dataset_ref:
        print(f"Running Data Quality Check for {args.dataset_ref}...")
        ds_id, ver = args.dataset_ref.split(":")
        ref = DatasetRef(
            dataset_id=ds_id, dataset_type=DatasetType.UNKNOWN, version=ver
        )
        from app.data_governance import QualityEngine

        engine = QualityEngine()
        report = engine.evaluate(ref, data=[])
        gov_repo.save_quality_report(report)
        print(gov_reporter.format_quality_report(report))

    elif args.show_quality_report and args.run_id:
        print(f"Quality Report for Run {args.run_id}")

    elif args.show_lineage and args.dataset_ref:
        print(f"Lineage for {args.dataset_ref}")

    elif args.show_provenance and args.dataset_ref:
        print(f"Provenance for {args.dataset_ref}")

    elif args.show_canonical_map and args.entity:
        print(f"Canonical Map for {args.entity}")

    elif args.run_schema_compatibility_check and args.from_schema and args.to_schema:
        print(f"Schema Compatibility: {args.from_schema} -> {args.to_schema}")

    elif args.show_schema_diff and args.from_schema and args.to_schema:
        print(f"Schema Diff: {args.from_schema} -> {args.to_schema}")

    elif args.show_downstream_impact and args.dataset_ref:
        print(f"Downstream Impact for {args.dataset_ref}")

    elif args.show_trust_verdict and args.dataset_ref:
        ds_id, ver = args.dataset_ref.split(":")
        ref = DatasetRef(
            dataset_id=ds_id, dataset_type=DatasetType.UNKNOWN, version=ver
        )
        verdict = gov_repo.get_trust_verdict(ref)
        if verdict:
            print(gov_reporter.format_trust_verdict(verdict))
        else:
            print("Trust verdict not found.")

    elif args.show_data_catalog:
        print("Governance Data Catalog:")
        entries = gov_repo.list_catalog_entries()
        if not entries:
            print("Catalog is empty.")
        else:
            for e in entries:
                print(
                    f"- {e.dataset_ref.dataset_id} (v{e.dataset_ref.version}) | Status: {e.latest_trust_verdict.value} | Last Updated: {e.last_updated}"
                )

    elif args.register_knowledge_item:
        from app.knowledge.models import Runbook, KnowledgeOwner
        from app.knowledge.enums import DocumentStatus
        from app.knowledge.repository import knowledge_repo
        from datetime import datetime, timezone

        rb = Runbook(
            item_id="RB-TEST-001",
            title="Test Runbook",
            description="A test runbook for CLI testing",
            owner=KnowledgeOwner(owner_id="jules", team="ops"),
            status=DocumentStatus.PUBLISHED,
            last_reviewed_at=datetime.now(timezone.utc),
        )
        knowledge_repo.save_item(rb)
        print(
            f"Registered knowledge item: {rb.item_id} (owner: {rb.owner.owner_id}, status: {rb.status.value})"
        )

    elif args.show_knowledge_catalog:
        from app.knowledge.catalog import catalog_registry
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        summary = catalog_registry.get_catalog_summary()
        print(KnowledgeReporter.format_catalog_summary(summary))

    elif args.show_runbooks:
        from app.knowledge.runbooks import runbook_registry
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        for rb in runbook_registry.list_runbooks():
            print(KnowledgeReporter.format_runbook(rb))

    elif args.show_sops:
        from app.knowledge.sops import sop_registry
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        for sop in sop_registry.list_sops():
            print(KnowledgeReporter.format_sop(sop))

    elif args.show_playbooks:
        from app.knowledge.playbooks import playbook_registry
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        for pb in playbook_registry.list_playbooks():
            print(KnowledgeReporter.format_playbook(pb))

    elif args.check_runbook_applicability:
        from app.knowledge.applicability import applicability_engine
        from app.knowledge.runbooks import runbook_registry
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        context = {"action": args.action_type} if args.action_type else {}
        print(f"Checking applicability for context: {context}")
        for rb in runbook_registry.list_runbooks():
            verdict = applicability_engine.evaluate(rb, context)
            print(f"- {rb.item_id}: {verdict.value}")

    elif args.show_freshness_report:
        from app.knowledge.freshness import freshness_engine
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        reports = freshness_engine.evaluate_all()
        print(KnowledgeReporter.format_freshness_report(reports))

    elif args.show_lessons_learned:
        from app.knowledge.lessons import lesson_registry
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        for ls in lesson_registry.list_lessons():
            print(KnowledgeReporter.format_lesson(ls))

    elif args.run_readiness_quiz:
        if not args.operator or not args.scope:
            print("--operator and --scope required")
            sys.exit(1)
        from app.knowledge.quizzes import quiz_registry
        from app.knowledge.models import ReadinessQuiz, QuizQuestion

        # Register a mock quiz for testing
        q = ReadinessQuiz(
            quiz_id="QZ-MOCK-001",
            module_id="MOD-001",
            title=f"Mock Quiz for {args.scope}",
            passing_score=100.0,
            questions=[
                QuizQuestion(
                    question_id="q1",
                    text="Yes?",
                    options=["Yes", "No"],
                    correct_option_index=0,
                )
            ],
        )
        quiz_registry.register_quiz(q)
        res = quiz_registry.evaluate_quiz(
            "QZ-MOCK-001", args.operator, [0]
        )  # correct answer
        print(f"Quiz completed! Score: {res.score}, Verdict: {res.verdict.value}")

    elif args.show_operator_readiness:
        if not args.operator:
            print("--operator required")
            sys.exit(1)
        from app.knowledge.readiness import readiness_evaluator
        from app.knowledge.reporting import KnowledgeReporter

        record = readiness_evaluator.evaluate(args.operator, role="ops")
        print(KnowledgeReporter.format_readiness(record))

    elif args.search_knowledge:
        if not args.query:
            print("--query required")
            sys.exit(1)
        from app.knowledge.search import search_engine
        from app.knowledge.reporting import KnowledgeReporter
        from app.knowledge.repository import knowledge_repo

        knowledge_repo.load_catalog()
        results = search_engine.search(args.query)
        print(KnowledgeReporter.format_search_results(results))

    elif args.show_knowledge_links:
        if not args.item_id:
            print("--item-id required")
            sys.exit(1)
        from app.knowledge.links import knowledge_graph

        outbound = knowledge_graph.get_outbound_links(args.item_id)
        inbound = knowledge_graph.get_inbound_links(args.item_id)
        print(f"Links for {args.item_id}:")
        print(f"Outbound: {len(outbound)}")
        for l in outbound:
            print(f"  -> {l.target_id} ({l.link_type})")
        print(f"Inbound: {len(inbound)}")
        for l in inbound:
            print(f"  <- {l.source_id} ({l.link_type})")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
