from typing import List, Optional
from app.automation.storage import AutomationStorage
from app.automation.models import JobDefinition, JobRun, WorkflowDefinition, WorkflowRun


class AutomationRepository:
    def __init__(self, storage: AutomationStorage):
        self.storage = storage

    def save_job(self, job: JobDefinition):
        self.storage.save_job(job)

    def get_job(self, job_id: str) -> Optional[JobDefinition]:
        return self.storage.get_job(job_id)

    def list_jobs(self) -> List[JobDefinition]:
        return self.storage.list_jobs()

    def save_workflow(self, workflow: WorkflowDefinition):
        self.storage.save_workflow(workflow)

    def get_workflow(self, workflow_id: str) -> Optional[WorkflowDefinition]:
        return self.storage.get_workflow(workflow_id)

    def list_workflows(self) -> List[WorkflowDefinition]:
        return self.storage.list_workflows()

    def save_run(self, run: JobRun):
        self.storage.save_job_run(run)

    def get_run(self, run_id: str) -> Optional[JobRun]:
        return self.storage.get_job_run(run_id)

    def get_run_by_key(self, run_key: str) -> Optional[JobRun]:
        return self.storage.get_job_run_by_key(run_key)

    def get_runs_for_job(self, job_id: str, limit: int = 100) -> List[JobRun]:
        return self.storage.get_runs_for_job(job_id, limit)

    def get_all_job_runs(self, limit: int = 1000) -> List[JobRun]:
        return self.storage.get_all_job_runs(limit)

    def save_workflow_run(self, run: WorkflowRun):
        self.storage.save_workflow_run(run)

    def get_workflow_run(self, run_id: str) -> Optional[WorkflowRun]:
        return self.storage.get_workflow_run(run_id)
