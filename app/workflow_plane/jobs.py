from app.workflow_plane.models import JobContract

class JobRegistry:
    def __init__(self):
        self._jobs = {}
    def register(self, job: JobContract):
        self._jobs[job.job_id] = job
    def get(self, job_id: str) -> JobContract:
        return self._jobs.get(job_id)

job_registry = JobRegistry()

class WorkflowJobMigrationRef:
    def source_target_expectations(self, prechecks=None):
        pass
