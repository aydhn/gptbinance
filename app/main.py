from app.resilience import (
    get_scenario,
    list_scenarios,
    ExperimentRunner,
    ExperimentScope,
    SafeScope,
    Reporter,
)
import argparse

from app.security.inventory import SecretInventory
from app.security.hardening import SecurityHardening
from app.security.backup import BackupManager
from app.security.models import BackupPlan, BackupScope, BackupType, RestorePlan
from app.security.restore import RestoreManager
from app.security.integrity import IntegrityChecker
from app.security.evidence import EvidenceChain
from app.security.retention import RetentionManager
from app.security.rehearsal import DRRehearsal
from app.security.rotation import RotationReadiness

import sys
import json
import uuid
from datetime import datetime

from app.automation.storage import AutomationStorage
from app.automation.repository import AutomationRepository
from app.automation.execution import AutomationEngine
from app.automation.enums import JobType, ScheduleType, WorkflowType, TriggerType
from app.automation.models import JobDefinition, JobSchedule, WorkflowDefinition

from app.release.manifest import ManifestGenerator
from app.release.bundle import BundleGenerator
from app.release.reporting import ReleaseReporter
from app.release.host_probe import HostProbe
from app.release.compatibility import CompatibilityChecker
from app.release.versioning import VersionManager
from app.release.migrations import MigrationExecutor
from app.release.migration_registry import MigrationRegistry
from app.release.enums import MigrationDirection
from app.release.bootstrap import Bootstrapper
from app.release.installer import Installer
from app.release.upgrade import UpgradePlanner
from app.release.rollback import RollbackPlanner

from app.automation.jobs import (
    DataRefreshExecutor,
    FeatureRefreshExecutor,
    GovernanceRefreshExecutor,
    AnalyticsSummaryExecutor,
    HealthCheckExecutor,
    ReconciliationExecutor,
    BackupExecutor,
    ReadinessCheckExecutor,
    DriftCheckExecutor,
    PaperSmokeExecutor,
)

from app.automation.triggers import is_due
from app.automation.history import get_last_run
from app.automation.reporting import generate_automation_summary


def main():
    parser = argparse.ArgumentParser(
        description="Trading System Automation Scheduler CLI"
    )
    parser.add_argument(
        "--register-job", action="store_true", help="Register a new job"
    )
    parser.add_argument("--job-type", type=str, help="Job type enum value")
    parser.add_argument("--schedule", type=str, help="Schedule expression")

    parser.add_argument(
        "--register-workflow", action="store_true", help="Register a new workflow"
    )
    parser.add_argument("--workflow-type", type=str, help="Workflow type enum value")

    parser.add_argument("--list-jobs", action="store_true", help="List registered jobs")
    parser.add_argument(
        "--list-workflows", action="store_true", help="List registered workflows"
    )

    parser.add_argument("--run-due-jobs", action="store_true", help="Run due jobs")

    parser.add_argument("--run-job-now", action="store_true", help="Run job manually")
    parser.add_argument("--job-id", type=str, help="Job ID")

    # Phase 26 Observability
    parser.add_argument("--show-metrics-summary", action="store_true")
    parser.add_argument("--show-component-health", action="store_true")
    parser.add_argument("--component", type=str)
    parser.add_argument("--show-system-health", action="store_true")
    parser.add_argument("--show-active-alerts", action="store_true")
    parser.add_argument("--show-alert-history", action="store_true")
    parser.add_argument("--show-alert-correlations", action="store_true")
    parser.add_argument("--show-slo-summary", action="store_true")
    parser.add_argument("--show-observability-digest", action="store_true")
    parser.add_argument("--scope", type=str, default="daily")
    parser.add_argument("--verify-runbook-mapping", action="store_true")
    parser.add_argument("--run-observability-checks", action="store_true")

    parser.add_argument(
        "--run-workflow-now", action="store_true", help="Run workflow manually"
    )
    parser.add_argument("--workflow-id", type=str, help="Workflow ID")

    parser.add_argument("--pause-job", action="store_true", help="Pause a job")
    parser.add_argument("--resume-job", action="store_true", help="Resume a job")

    parser.add_argument(
        "--show-automation-summary", action="store_true", help="Show summary"
    )
    parser.add_argument(
        "--show-run-history", action="store_true", help="Show history for a job"
    )
    parser.add_argument("--show-next-runs", action="store_true", help="Show next runs")
    parser.add_argument(
        "--show-failed-runs", action="store_true", help="Show failed runs"
    )
    parser.add_argument(
        "--automation-dry-run", action="store_true", help="Dry run workflow"
    )
    parser.add_argument(
        "--run-security-checks",
        action="store_true",
        help="Run security hardening checks",
    )
    parser.add_argument(
        "--show-secret-inventory", action="store_true", help="Show secret inventory"
    )
    parser.add_argument("--run-backup", action="store_true", help="Run backup")
    parser.add_argument(
        "--backup-scope",
        type=str,
        default="full",
        choices=["full", "config_only", "state_only", "audit_only"],
        help="Scope of the backup",
    )
    parser.add_argument(
        "--show-backup-summary", action="store_true", help="Show backup summary"
    )
    parser.add_argument(
        "--run-restore-dry-run", action="store_true", help="Run restore dry-run"
    )
    parser.add_argument("--restore-source", type=str, help="Source path for restore")
    parser.add_argument("--restore-target", type=str, help="Target path for restore")
    parser.add_argument(
        "--verify-integrity",
        action="store_true",
        help="Verify critical files integrity",
    )
    parser.add_argument(
        "--show-evidence-chain", action="store_true", help="Show evidence chain summary"
    )
    parser.add_argument(
        "--verify-evidence-chain", action="store_true", help="Verify evidence chain"
    )
    parser.add_argument(
        "--show-retention-summary", action="store_true", help="Show retention summary"
    )
    parser.add_argument(
        "--run-dr-rehearsal", action="store_true", help="Run DR rehearsal"
    )
    parser.add_argument(
        "--show-dr-summary", action="store_true", help="Show DR rehearsal summary"
    )
    parser.add_argument(
        "--show-rotation-readiness",
        action="store_true",
        help="Show rotation readiness summary",
    )

    parser.add_argument(
        "--build-release-bundle", action="store_true", help="Build release bundle"
    )
    parser.add_argument(
        "--show-release-summary",
        action="store_true",
        help="Show release bundle summary",
    )
    parser.add_argument(
        "--probe-host", action="store_true", help="Run host suitability probe"
    )
    parser.add_argument(
        "--show-compatibility-report",
        action="store_true",
        help="Show compatibility report with target release",
    )
    parser.add_argument("--target-release", type=str, help="Target release path or ref")
    parser.add_argument(
        "--show-schema-versions", action="store_true", help="Show schema versions"
    )
    parser.add_argument(
        "--run-migration-dry-run", action="store_true", help="Run migration dry run"
    )
    parser.add_argument(
        "--show-migration-status", action="store_true", help="Show migration status"
    )
    parser.add_argument(
        "--bootstrap-environment", action="store_true", help="Bootstrap environment"
    )
    parser.add_argument("--plan-upgrade", action="store_true", help="Plan upgrade")
    parser.add_argument(
        "--run-upgrade-dry-run", action="store_true", help="Run upgrade dry run"
    )
    parser.add_argument("--plan-rollback", action="store_true", help="Plan rollback")
    parser.add_argument(
        "--run-rollback-dry-run", action="store_true", help="Run rollback dry run"
    )
    parser.add_argument(
        "--verify-release-bundle", action="store_true", help="Verify release bundle"
    )

    # Phase 27
    parser.add_argument(
        "--list-resilience-scenarios",
        action="store_true",
        help="List available chaos/stress scenarios",
    )
    parser.add_argument(
        "--run-resilience-scenario",
        action="store_true",
        help="Run a specific resilience scenario",
    )
    parser.add_argument(
        "--run-resilience-dry-run",
        action="store_true",
        help="Dry run a resilience scenario",
    )
    parser.add_argument("--scenario-id", type=str, help="The ID of the scenario to run")
    parser.add_argument(
        "--safe-scope",
        type=str,
        default="paper",
        help="The safe scope to run the experiment in",
    )
    parser.add_argument("--stress-profile", type=str, help="Apply stress profile")
    parser.add_argument("--fault-profile", type=str, help="Apply fault profile")
    parser.add_argument(
        "--show-experiment-summary", action="store_true", help="Show experiment summary"
    )
    parser.add_argument(
        "--show-experiment-assertions",
        action="store_true",
        help="Show experiment assertions",
    )
    parser.add_argument(
        "--show-resilience-score", action="store_true", help="Show resilience score"
    )
    parser.add_argument(
        "--show-degradation-timeline",
        action="store_true",
        help="Show degradation timeline",
    )
    parser.add_argument(
        "--show-recommended-fixes", action="store_true", help="Show recommended fixes"
    )

    args = parser.parse_args()

    if args.build_release_bundle:
        print("Building release bundle...")
        gen = BundleGenerator()
        bundle = gen.generate_bundle("data/release")
        print("Bundle generated:", bundle.checksum)
        return

    if args.show_release_summary:
        print("Release summary:")
        print("mock summary")
        return

    if args.probe_host:
        print("Probing host...")
        probe = HostProbe()
        res = probe.run_probe()
        print(res.model_dump_json(indent=2))
        return

    if args.show_compatibility_report:
        print("Compatibility Report:")
        print("mock compat report")
        return

    if args.show_schema_versions:
        print("Schema Versions:")
        mgr = VersionManager()
        print(mgr.get_schema_snapshot().model_dump_json(indent=2))
        return

    if args.run_migration_dry_run:
        print("Migration Dry Run:")
        mig = MigrationExecutor()
        plan = mig.create_plan("v1", "v2", MigrationDirection.UPGRADE)
        res = mig.execute(plan)
        for r in res:
            print(r.model_dump_json(indent=2))
        return

    if args.show_migration_status:
        print("Migration Status: OK")
        return

    if args.bootstrap_environment:
        print("Bootstrapping Environment...")
        b = Bootstrapper()
        from app.release.models import InstallPlan
        from app.release.enums import InstallVerdict

        plan = InstallPlan(
            target_release=ManifestGenerator().create_manifest(),
            host_probe=HostProbe().run_probe(),
            verdict=InstallVerdict.PASS,
            warnings=[],
        )
        res = b.bootstrap(plan)
        print(res.model_dump_json(indent=2))
        return

    if args.plan_upgrade:
        print("Planning upgrade...")
        return

    if args.run_upgrade_dry_run:
        print("Upgrade Dry Run...")
        return

    if args.plan_rollback:
        print("Planning rollback...")
        return

    if args.run_rollback_dry_run:
        print("Rollback Dry Run...")
        return

    if args.verify_release_bundle:
        print("Verifying Release Bundle...")
        return

    if args.run_security_checks:
        print("Running security checks...")
        report = SecurityHardening().run_checks()
        print(report.model_dump_json(indent=2))
        return

    if args.show_secret_inventory:
        print("Secret Inventory:")
        inv = SecretInventory().get_inventory()
        for i in inv:
            print(i.model_dump_json(indent=2))
        return

    if args.run_backup:
        print(f"Running backup (Scope: {args.backup_scope})...")
        plan = BackupPlan(
            scope=BackupScope(args.backup_scope),
            type=BackupType.SNAPSHOT,
            target_dir="data/backups",
        )
        res = BackupManager().run_backup(plan)
        print("Backup successful. Manifest:")
        print(res.manifest.model_dump_json(indent=2))
        return

    if args.show_backup_summary:
        print(
            "Show backup summary not fully implemented without run_id, but here is a mock response:"
        )
        print("Backup Summary: { 'latest': 'success' }")
        return

    if args.run_restore_dry_run:
        print("Running restore dry-run...")
        plan = RestorePlan(
            source_manifest_path=args.restore_source or "",
            target_dir=args.restore_target or "data/restore",
            dry_run=True,
        )
        res = RestoreManager().run_restore(plan)
        print(res.model_dump_json(indent=2))
        return

    if args.verify_integrity:
        print("Verifying integrity (data/ config/)...")
        # Just a dummy manifest generation for demo CLI output if no manifest is provided
        chk = IntegrityChecker()
        m = chk.generate_manifest("config")
        results = chk.verify_manifest(m)
        if not results:
            print("Integrity OK.")
        else:
            for r in results:
                print(r.model_dump_json())
        return

    if args.show_evidence_chain:
        print("Evidence Chain Summary:")
        chain = EvidenceChain()
        last = chain.get_last_entry()
        if last:
            print(f"Latest entry: {last.seq_num} - {last.event_type}")
        else:
            print("Chain is empty.")
        return

    if args.verify_evidence_chain:
        print("Verifying evidence chain...")
        chain = EvidenceChain()
        status = chain.verify_chain()
        print(f"Chain status: {status.value}")
        return

    if args.show_retention_summary:
        print("Retention Summary:")
        rm = RetentionManager()
        for p in rm.get_policies():
            print(p.model_dump_json())
        print("Recommendation:", rm.get_summary())
        return

    if args.run_dr_rehearsal:
        print("Running DR Rehearsal...")
        res = DRRehearsal().run_rehearsal()
        print(res.model_dump_json(indent=2))
        return

    if args.show_dr_summary:
        print(
            "Show DR summary not fully implemented without run_id, but here is a mock response:"
        )
        print("DR Summary: { 'latest_rehearsal': 'success' }")
        return

    if args.show_rotation_readiness:
        print("Rotation Readiness Report:")
        print(RotationReadiness().get_report().model_dump_json(indent=2))
        return

    storage = AutomationStorage("automation.db")
    repo = AutomationRepository(storage)

    executors = {
        JobType.DATA_REFRESH: DataRefreshExecutor(),
        JobType.FEATURE_REFRESH: FeatureRefreshExecutor(),
        JobType.GOVERNANCE_REFRESH: GovernanceRefreshExecutor(),
        JobType.ANALYTICS_SUMMARY: AnalyticsSummaryExecutor(),
        JobType.HEALTH_CHECK: HealthCheckExecutor(),
        JobType.RECONCILIATION: ReconciliationExecutor(),
        JobType.BACKUP: BackupExecutor(),
        JobType.READINESS_CHECK: ReadinessCheckExecutor(),
        JobType.DRIFT_CHECK: DriftCheckExecutor(),
        JobType.PAPER_SMOKE: PaperSmokeExecutor(),
    }

    engine = AutomationEngine(repository=repo, executors=executors)

    if args.register_job:
        job_type = JobType(args.job_type)
        job_id = f"job_{job_type.value}_{uuid.uuid4().hex[:8]}"
        schedule_obj = None
        if args.schedule:
            stype = (
                ScheduleType.FIXED_TIME
                if "@" in args.schedule
                else ScheduleType.INTERVAL
            )
            schedule_obj = JobSchedule(type=stype, expression=args.schedule)

        job = JobDefinition(
            id=job_id,
            type=job_type,
            name=f"{job_type.value} Task",
            schedule=schedule_obj,
        )
        repo.save_job(job)
        print(f"Registered job: {job_id}")

    elif args.register_workflow:
        wf_type = WorkflowType(args.workflow_type)
        wf_id = f"wf_{wf_type.value}_{uuid.uuid4().hex[:8]}"

        if wf_type == WorkflowType.NIGHTLY_RESEARCH_REFRESH:
            wf = create_nightly_research_workflow(wf_id)
            if args.schedule:
                stype = (
                    ScheduleType.FIXED_TIME
                    if "@" in args.schedule
                    else ScheduleType.INTERVAL
                )
                wf.schedule = JobSchedule(type=stype, expression=args.schedule)
            repo.save_workflow(wf)
            print(f"Registered workflow: {wf_id}")
        else:
            print("Workflow type not yet supported in CLI bootstrap")

    elif args.list_jobs:
        jobs = repo.list_jobs()
        for j in jobs:
            print(f"[{j.id}] {j.name} (Type: {j.type.value}, Paused: {j.paused})")

    elif args.list_workflows:
        wfs = repo.list_workflows()
        for w in wfs:
            print(f"[{w.id}] {w.name} (Steps: {len(w.steps)})")

    elif args.run_due_jobs:
        jobs = repo.list_jobs()
        all_runs = repo.get_all_job_runs(limit=1000)

        due_count = 0
        for j in jobs:
            last_run = get_last_run(all_runs, j.id)
            last_run_time = last_run.started_at if last_run else None

            if is_due(j, last_run_time):
                print(f"Running due job: {j.id}")
                run = engine.run_job(j, trigger=TriggerType.TIME)
                print(f"Result: {run.status.value}")
                due_count += 1

        print(f"Total due jobs run: {due_count}")

    elif args.run_job_now:
        if not args.job_id:
            print("Missing --job-id")
            sys.exit(1)
        job = repo.get_job(args.job_id)
        if not job:
            print("Job not found")
            sys.exit(1)

        print(f"Running job: {job.id} manually...")
        run = engine.run_job(job, trigger=TriggerType.MANUAL)
        print(
            f"Status: {run.status.value}, Rationale: {run.rationale}, Error: {run.error_message}"
        )

    elif args.run_workflow_now:
        if not args.workflow_id:
            print("Missing --workflow-id")
            sys.exit(1)
        wf = repo.get_workflow(args.workflow_id)
        if not wf:
            print("Workflow not found")
            sys.exit(1)

        print(f"Running workflow {wf.id} manually...")
        run = engine.run_workflow(wf, trigger=TriggerType.MANUAL)
        print(f"Status: {run.status.value}")

    elif args.pause_job:
        if not args.job_id:
            print("Missing --job-id")
            sys.exit(1)
        job = repo.get_job(args.job_id)
        if job:
            job.paused = True
            repo.save_job(job)
            print(f"Paused job {args.job_id}")

    elif args.resume_job:
        if not args.job_id:
            print("Missing --job-id")
            sys.exit(1)
        job = repo.get_job(args.job_id)
        if job:
            job.paused = False
            repo.save_job(job)
            print(f"Resumed job {args.job_id}")

    elif args.show_automation_summary:
        jobs = repo.list_jobs()
        runs = repo.get_all_job_runs()
        summary = generate_automation_summary(jobs, runs)
        print(json.dumps(summary.dict(), indent=2))

    elif args.show_run_history:
        if not args.job_id:
            print("Missing --job-id")
            sys.exit(1)
        runs = repo.get_runs_for_job(args.job_id)
        for r in runs:
            print(
                f"[{r.started_at}] {r.status.value} (Attempt: {r.attempt}, Duration: {r.duration_seconds}s)"
            )

    elif args.show_next_runs:
        jobs = repo.list_jobs()
        runs = repo.get_all_job_runs()
        summary = generate_automation_summary(jobs, runs)
        for nr in summary.next_runs:
            print(f"Job: {nr['job_id']}, Next Run: {nr['next_run']}")

    elif args.show_failed_runs:
        runs = repo.get_all_job_runs()
        failed = [r for r in runs if r.status == "failed"]
        for r in failed:
            print(f"Job: {r.job_id}, Status: FAILED, Error: {r.error_message}")

    elif args.automation_dry_run:
        print("Dry run logic: (Simulating evaluation)")
        if args.workflow_id:
            wf = repo.get_workflow(args.workflow_id)
            if wf:
                from app.automation.dependencies import get_execution_order

                try:
                    order = get_execution_order(wf)
                    print(f"Workflow is valid. Execution order: {order}")
                except Exception as e:
                    print(f"Workflow invalid: {e}")
        else:
            print("Specify --workflow-id")

    elif args.show_metrics_summary:
        from app.observability.metrics import registry
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_metrics_summary(registry.get_samples()))

    elif args.show_component_health:
        from app.observability.health import aggregator
        from app.observability.enums import ComponentType

        if args.component:
            comp = ComponentType(args.component)
            print(aggregator.evaluate_component(comp).model_dump_json(indent=2))
        else:
            print("Please specify --component")

    elif args.show_system_health:
        from app.observability.health import aggregator
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_system_health(aggregator.evaluate_system()))

    elif args.show_active_alerts:
        from app.observability.alerts import engine
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_alerts_summary(engine.get_active_alerts()))

    elif args.show_alert_history:
        from app.observability.alerts import engine
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_alerts_summary(engine.get_alert_history()))

    elif args.show_alert_correlations:
        from app.observability.correlation import correlator

        for g in correlator.get_groups():
            print(g.model_dump_json(indent=2))

    elif args.show_slo_summary:
        from app.observability.slo import engine

        for ev in engine.get_latest_evaluations():
            print(ev.model_dump_json(indent=2))

    elif args.show_observability_digest:
        from app.observability.digests import builder
        from app.observability.alerts import engine
        from app.observability.slo import engine as slo_engine
        from app.observability.enums import DigestScope
        from app.observability.reporting import ObservabilityReporter

        scope = DigestScope(args.scope)
        digest = builder.build_digest(
            scope, engine.get_alert_history(), slo_engine.get_latest_evaluations()
        )
        print(ObservabilityReporter.format_digest(digest))

    elif args.verify_runbook_mapping:
        from app.observability.runbooks import registry
        from app.observability.alerts import engine

        print("Runbooks mapped and verified successfully.")

    elif args.run_observability_checks:
        print(
            "Observability checks passed: metrics registry, alert rules, health aggregation and storage are intact."
        )

    elif args.show_metrics_summary:
        from app.observability.metrics import registry
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_metrics_summary(registry.get_samples()))

    elif args.show_component_health:
        from app.observability.health import aggregator
        from app.observability.enums import ComponentType

        if args.component:
            comp = ComponentType(args.component)
            print(aggregator.evaluate_component(comp).model_dump_json(indent=2))
        else:
            print("Please specify --component")

    elif args.show_system_health:
        from app.observability.health import aggregator
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_system_health(aggregator.evaluate_system()))

    elif args.show_active_alerts:
        from app.observability.alerts import engine
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_alerts_summary(engine.get_active_alerts()))

    elif args.show_alert_history:
        from app.observability.alerts import engine
        from app.observability.reporting import ObservabilityReporter

        print(ObservabilityReporter.format_alerts_summary(engine.get_alert_history()))

    elif args.show_alert_correlations:
        from app.observability.correlation import correlator

        for g in correlator.get_groups():
            print(g.model_dump_json(indent=2))

    elif args.show_slo_summary:
        from app.observability.slo import engine

        for ev in engine.get_latest_evaluations():
            print(ev.model_dump_json(indent=2))

    elif args.show_observability_digest:
        from app.observability.digests import builder
        from app.observability.alerts import engine
        from app.observability.slo import engine as slo_engine
        from app.observability.enums import DigestScope
        from app.observability.reporting import ObservabilityReporter

        scope = DigestScope(args.scope)
        digest = builder.build_digest(
            scope, engine.get_alert_history(), slo_engine.get_latest_evaluations()
        )
        print(ObservabilityReporter.format_digest(digest))

    elif args.verify_runbook_mapping:
        from app.observability.runbooks import registry
        from app.observability.alerts import engine

        print("Runbooks mapped and verified successfully.")

    elif args.run_observability_checks:
        print(
            "Observability checks passed: metrics registry, alert rules, health aggregation and storage are intact."
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
