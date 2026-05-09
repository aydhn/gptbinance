from app.workflow_plane.registry import registry
from app.workflow_plane.runs import RunManager

class WorkflowReporter:
    def __init__(self, run_manager: RunManager):
        self.registry = registry
        self.run_manager = run_manager

    def print_registry(self):
        print("=== CANONICAL WORKFLOW REGISTRY ===")
        for wf in self.registry.get_all():
            print(f"- [{wf.workflow_class.upper()}] {wf.workflow_id} | Critical: {wf.critical}")
            print(f"  Objective: {wf.objective}")
            for job in wf.jobs:
                print(f"    * Job: {job.job_id} ({job.mutability_class})")

    def print_runs(self):
        print("=== WORKFLOW RUNS ===")
        for run in self.run_manager.get_all_runs():
            print(f"- Run ID: {run.run_id} | WF: {run.workflow_id} | State: {run.state.value}")
            print(f"  Window: {run.window.start_time} to {run.window.end_time}")
            if run.superseded_by:
                print(f"  [!] Superseded by: {run.superseded_by}")
