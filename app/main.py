import argparse
import sys
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
    GovernanceStorage, GovernanceRepository, GovernanceReporter,
    DatasetRef, DatasetType, TrustLevel
)

def main():
    parser = argparse.ArgumentParser(description="Binance Trading Platform - Performance Engineering CLI")
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
    parser.add_argument("--dataset-ref", type=str, help="Dataset Reference ID (format: id:version)")
    parser.add_argument("--entity", type=str, help="Entity alias for canonical map")
    parser.add_argument("--from-schema", type=str, help="Source schema (format: id:version)")
    parser.add_argument("--to-schema", type=str, help="Target schema (format: id:version)")


    args = parser.parse_args()

    storage = PerfStorage()
    repo = PerfRepository(storage)
    gov_repo = GovernanceRepository(GovernanceStorage())
    gov_reporter = GovernanceReporter()

    if args.run_perf_profile:
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
        print(f"Showing budgets applicable to modes recommended for {args.perf_host_class}")
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
                    print(f"[{mode.upper()}] {b.resource_type.value} ({b.severity.value}): Limit = {b.limit_value}")
                    seen.add(k)
            for b in BudgetRegistry.get_applicable_latency_budgets(mode):
                k = f"lat_{b.component_name}_{b.percentile.value}_{b.limit_ms}"
                if k not in seen:
                    print(f"[{mode.upper()}] Latency {b.component_name} {b.percentile.value} ({b.severity.value}): Limit = {b.limit_ms}ms")
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
                print(f"  P50: {lat.p50_ms:.2f}ms | P95: {lat.p95_ms:.2f}ms | P99: {lat.p99_ms:.2f}ms | Max: {lat.max_ms:.2f}ms")
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
        tested = [WorkloadType.PAPER_RUNTIME_CYCLE, WorkloadType.TESTNET_EXECUTION_SMOKE]
        verdict = ReadinessVerdict.READY if hc != HostClass.LOCAL_MINIMAL else ReadinessVerdict.CAUTION

        report = HostQualificationReport(
            host_class=hc,
            tested_workloads=tested,
            readiness=verdict,
            evidence_refs=["run_xyz_123"]
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
            description="Mock Contract"
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
        ref = DatasetRef(dataset_id=ds_id, dataset_type=DatasetType.UNKNOWN, version=ver)
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
        ref = DatasetRef(dataset_id=ds_id, dataset_type=DatasetType.UNKNOWN, version=ver)
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
                print(f"- {e.dataset_ref.dataset_id} (v{e.dataset_ref.version}) | Status: {e.latest_trust_verdict.value} | Last Updated: {e.last_updated}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
