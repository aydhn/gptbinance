from typing import List, Dict
from app.workflow_plane.exceptions import DependencyViolationError

class DependencyEvaluator:
    def __init__(self):
        self.must_run_after: Dict[str, List[str]] = {
            "model_inference": ["feature_refresh"],
            "allocation_cycle": ["model_inference", "risk_refresh"],
            "execution_cycle": ["allocation_cycle"]
        }

    def check_dependencies(self, job_id: str, completed_jobs: List[str]):
        required = self.must_run_after.get(job_id, [])
        for req in required:
            if req not in completed_jobs:
                raise DependencyViolationError(f"Job {job_id} requires {req} to complete first.")
