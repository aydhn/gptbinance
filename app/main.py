import argparse
import sys
import json
import uuid
from datetime import datetime

from app.automation.storage import AutomationStorage
from app.automation.repository import AutomationRepository
from app.automation.execution import AutomationEngine
from app.automation.enums import JobType, ScheduleType, WorkflowType, TriggerType
from app.automation.models import JobDefinition, JobSchedule, WorkflowDefinition
from app.automation.jobs import (
    DataRefreshExecutor, FeatureRefreshExecutor, GovernanceRefreshExecutor,
    AnalyticsSummaryExecutor, HealthCheckExecutor, ReconciliationExecutor,
    BackupExecutor, ReadinessCheckExecutor, DriftCheckExecutor, PaperSmokeExecutor
)
from app.automation.workflows import create_nightly_research_workflow
from app.automation.triggers import is_due
from app.automation.history import get_last_run
from app.automation.reporting import generate_automation_summary

def main():
    parser = argparse.ArgumentParser(description="Trading System Automation Scheduler CLI")
    parser.add_argument("--register-job", action="store_true", help="Register a new job")
    parser.add_argument("--job-type", type=str, help="Job type enum value")
    parser.add_argument("--schedule", type=str, help="Schedule expression")

    parser.add_argument("--register-workflow", action="store_true", help="Register a new workflow")
    parser.add_argument("--workflow-type", type=str, help="Workflow type enum value")

    parser.add_argument("--list-jobs", action="store_true", help="List registered jobs")
    parser.add_argument("--list-workflows", action="store_true", help="List registered workflows")

    parser.add_argument("--run-due-jobs", action="store_true", help="Run due jobs")
    parser.add_argument("--run-job-now", action="store_true", help="Run job manually")
    parser.add_argument("--job-id", type=str, help="Job ID")

    parser.add_argument("--run-workflow-now", action="store_true", help="Run workflow manually")
    parser.add_argument("--workflow-id", type=str, help="Workflow ID")

    parser.add_argument("--pause-job", action="store_true", help="Pause a job")
    parser.add_argument("--resume-job", action="store_true", help="Resume a job")

    parser.add_argument("--show-automation-summary", action="store_true", help="Show summary")
    parser.add_argument("--show-run-history", action="store_true", help="Show history for a job")
    parser.add_argument("--show-next-runs", action="store_true", help="Show next runs")
    parser.add_argument("--show-failed-runs", action="store_true", help="Show failed runs")
    parser.add_argument("--automation-dry-run", action="store_true", help="Dry run workflow")

    args = parser.parse_args()

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
        JobType.PAPER_SMOKE: PaperSmokeExecutor()
    }

    engine = AutomationEngine(repository=repo, executors=executors)

    if args.register_job:
        job_type = JobType(args.job_type)
        job_id = f"job_{job_type.value}_{uuid.uuid4().hex[:8]}"
        schedule_obj = None
        if args.schedule:
            stype = ScheduleType.FIXED_TIME if "@" in args.schedule else ScheduleType.INTERVAL
            schedule_obj = JobSchedule(type=stype, expression=args.schedule)

        job = JobDefinition(
            id=job_id,
            type=job_type,
            name=f"{job_type.value} Task",
            schedule=schedule_obj
        )
        repo.save_job(job)
        print(f"Registered job: {job_id}")

    elif args.register_workflow:
        wf_type = WorkflowType(args.workflow_type)
        wf_id = f"wf_{wf_type.value}_{uuid.uuid4().hex[:8]}"

        if wf_type == WorkflowType.NIGHTLY_RESEARCH_REFRESH:
            wf = create_nightly_research_workflow(wf_id)
            if args.schedule:
                 stype = ScheduleType.FIXED_TIME if "@" in args.schedule else ScheduleType.INTERVAL
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
        print(f"Status: {run.status.value}, Rationale: {run.rationale}, Error: {run.error_message}")

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
             print(f"[{r.started_at}] {r.status.value} (Attempt: {r.attempt}, Duration: {r.duration_seconds}s)")

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

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
