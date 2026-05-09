from app.workflow_plane.models import WorkflowRun, JobContract
from app.workflow_plane.dependencies import DependencyEvaluator
from app.workflow_plane.gates import WorkflowGateEvaluator
from app.workflow_plane.enums import RunState
from typing import List

class WorkflowOrchestrator:
    def __init__(self, dependencies: DependencyEvaluator, gates: WorkflowGateEvaluator):
        self.dependencies = dependencies
        self.gates = gates

    def orchestrate(self, run: WorkflowRun, available_jobs: List[JobContract]) -> List[JobContract]:
        # Returns jobs ready to be executed
        gate_results = self.gates.evaluate(run)
        if any(not g.passed for g in gate_results):
            run.state = RunState.GATED_WAIT
            return []

        completed_job_ids = [j.job_id for j in run.job_runs if j.state == RunState.COMPLETED]
        ready_jobs = []
        for job in available_jobs:
            if job.job_id in completed_job_ids:
                continue
            try:
                self.dependencies.check_dependencies(job.job_id, completed_job_ids)
                ready_jobs.append(job)
            except Exception:
                pass

        if not ready_jobs and len(completed_job_ids) == len(available_jobs):
            run.state = RunState.COMPLETED

        return ready_jobs
