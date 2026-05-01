from typing import Dict, List, Optional
import uuid
from datetime import datetime, timezone

from app.automation.models import (
    JobDefinition,
    JobRun,
    JobRunContext,
    RunStatus,
    PreconditionAction,
    WorkflowDefinition,
    WorkflowRun,
)
from app.automation.enums import JobType, TriggerType
from app.automation.exceptions import DuplicateRunError
from app.automation.idempotency import generate_run_key
from app.automation.preconditions import (
    evaluate_all_preconditions,
    aggregate_precondition_verdict,
    MaintenancePrecondition,
    QuietHoursPrecondition,
    IncidentPrecondition,
)
from app.automation.base import JobExecutorBase
from app.automation.retries import evaluate_retry, RetryVerdict


class AutomationEngine:
    def __init__(
        self, repository, executors: Dict[JobType, JobExecutorBase], notifier=None
    ):
        self.repository = repository
        self.executors = executors
        self.notifier = notifier

    def _create_preconditions(self) -> List:
        # In a real app, inject actual status from ops/incidents layer
        # For phase 23, we mock the status retrieval
        # e.g., is_maintenance = ops.is_maintenance_active()
        return [
            QuietHoursPrecondition(),
            MaintenancePrecondition(is_maintenance_active=False),
            IncidentPrecondition(has_active_incident=False),
        ]

    def run_job(
        self,
        job_def: JobDefinition,
        trigger: TriggerType,
        scheduled_time_str: str = "",
        manual_inputs: Optional[dict] = None,
    ) -> JobRun:
        if job_def.paused and trigger != TriggerType.MANUAL:
            run = JobRun(
                id=str(uuid.uuid4()),
                job_id=job_def.id,
                job_type=job_def.type,
                status=RunStatus.SKIPPED,
                context=JobRunContext(trigger_type=trigger, run_key=""),
                rationale="Job is paused",
            )
            self.repository.save_run(run)
            return run

        inputs = {**job_def.inputs, **(manual_inputs or {})}
        run_key = generate_run_key(job_def.id, inputs, scheduled_time_str)

        # Duplicate run check
        existing_run = self.repository.get_run_by_key(run_key)
        if existing_run and existing_run.status in [
            RunStatus.SUCCESS,
            RunStatus.RUNNING,
        ]:
            if trigger == TriggerType.MANUAL:
                # Force rerun possible? For now, raise or return existing
                raise DuplicateRunError(
                    f"Run with key {run_key} already exists and is {existing_run.status.value}"
                )
            else:
                return existing_run

        context = JobRunContext(trigger_type=trigger, run_key=run_key)

        # Evaluate Preconditions
        checks = evaluate_all_preconditions(
            job_def, context, self._create_preconditions()
        )
        verdict = aggregate_precondition_verdict(checks)

        rationale = "; ".join(
            [c.result.rationale for c in checks if not c.result.passed]
        )

        if verdict == PreconditionAction.BLOCK:
            run = JobRun(
                id=str(uuid.uuid4()),
                job_id=job_def.id,
                job_type=job_def.type,
                status=RunStatus.BLOCKED,
                context=context,
                rationale=rationale,
            )
            self.repository.save_run(run)
            return run
        elif verdict == PreconditionAction.DEFER:
            run = JobRun(
                id=str(uuid.uuid4()),
                job_id=job_def.id,
                job_type=job_def.type,
                status=RunStatus.DEFERRED,
                context=context,
                rationale=rationale,
            )
            self.repository.save_run(run)
            return run
        elif verdict == PreconditionAction.SKIP:
            run = JobRun(
                id=str(uuid.uuid4()),
                job_id=job_def.id,
                job_type=job_def.type,
                status=RunStatus.SKIPPED,
                context=context,
                rationale=rationale,
            )
            self.repository.save_run(run)
            return run

        # Execute
        run = JobRun(
            id=str(uuid.uuid4()),
            job_id=job_def.id,
            job_type=job_def.type,
            status=RunStatus.RUNNING,
            context=context,
            started_at=datetime.now(timezone.utc),
        )
        self.repository.save_run(run)

        executor = self.executors.get(job_def.type)
        if not executor:
            run.status = RunStatus.FAILED
            run.error_message = f"No executor found for type {job_def.type}"
            run.completed_at = datetime.now(timezone.utc)
            self.repository.save_run(run)
            return run

        attempt = 1
        while attempt <= max(1, job_def.retry_policy.max_attempts):
            run.attempt = attempt
            try:
                artifacts = executor.execute(job_def, context)
                run.artifacts = artifacts
                run.status = RunStatus.SUCCESS
                run.completed_at = datetime.now(timezone.utc)
                if run.started_at:
                    run.duration_seconds = (
                        run.completed_at - run.started_at
                    ).total_seconds()
                self.repository.save_run(run)
                return run
            except Exception as e:
                error_msg = str(e)
                error_class = e.__class__.__name__
                run.error_message = f"{error_class}: {error_msg}"

                retry_verdict = evaluate_retry(
                    job_def.retry_policy, attempt, error_class
                )

                if retry_verdict == RetryVerdict.RETRY:
                    attempt += 1
                    # In real async engine, we'd schedule the retry after backoff
                    # Here we simulate the loop
                    continue
                else:
                    run.status = RunStatus.FAILED
                    run.completed_at = datetime.now(timezone.utc)
                    if run.started_at:
                        run.duration_seconds = (
                            run.completed_at - run.started_at
                        ).total_seconds()
                    self.repository.save_run(run)

                    if self.notifier:
                        self.notifier.notify(f"Job {job_def.name} failed: {error_msg}")

                    return run

        # Fallback if loop exits without returning
        run.status = RunStatus.FAILED
        run.completed_at = datetime.now(timezone.utc)
        self.repository.save_run(run)
        return run

    def run_workflow(
        self, workflow_def: WorkflowDefinition, trigger: TriggerType
    ) -> WorkflowRun:
        from app.automation.dependencies import get_execution_order

        run = WorkflowRun(
            id=str(uuid.uuid4()),
            workflow_id=workflow_def.id,
            status=RunStatus.RUNNING,
            started_at=datetime.now(timezone.utc),
        )
        self.repository.save_workflow_run(run)

        try:
            order = get_execution_order(workflow_def)
        except Exception:
            run.status = RunStatus.FAILED
            run.completed_at = datetime.now(timezone.utc)
            self.repository.save_workflow_run(run)
            return run

        step_map = {step.id: step for step in workflow_def.steps}

        for step_id in order:
            step = step_map[step_id]
            # Check dependencies
            deps_ok = True
            for dep_id in step.dependencies:
                dep_run_id = run.step_runs.get(dep_id)
                if not dep_run_id:
                    deps_ok = False
                    break
                dep_run = self.repository.get_run(dep_run_id)
                if dep_run.status != RunStatus.SUCCESS:
                    deps_ok = False
                    break

            if not deps_ok:
                run.status = RunStatus.FAILED
                run.completed_at = datetime.now(timezone.utc)
                self.repository.save_workflow_run(run)
                return run

            job_def = self.repository.get_job(step.job_id)
            if not job_def:
                run.status = RunStatus.FAILED
                run.completed_at = datetime.now(timezone.utc)
                self.repository.save_workflow_run(run)
                return run

            job_run = self.run_job(job_def, trigger)
            run.step_runs[step_id] = job_run.id
            self.repository.save_workflow_run(run)

            if job_run.status != RunStatus.SUCCESS:
                run.status = RunStatus.FAILED
                run.completed_at = datetime.now(timezone.utc)
                self.repository.save_workflow_run(run)
                return run

        run.status = RunStatus.SUCCESS
        run.completed_at = datetime.now(timezone.utc)
        self.repository.save_workflow_run(run)
        return run
