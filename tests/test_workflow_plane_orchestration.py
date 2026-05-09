from app.workflow_plane.orchestration import WorkflowOrchestrator
from app.workflow_plane.dependencies import DependencyEvaluator
from app.workflow_plane.gates import WorkflowGateEvaluator
from app.workflow_plane.models import WorkflowRun, RunWindow, JobContract
from app.workflow_plane.enums import TriggerClass, RunState, WindowClass, JobClass
from datetime import datetime, timezone

def test_orchestrator():
    deps = DependencyEvaluator()
    gates = WorkflowGateEvaluator()
    orch = WorkflowOrchestrator(deps, gates)

    win = RunWindow(window_id="test", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)
    run = WorkflowRun(
        run_id="r1", workflow_id="w1", window=win, trigger_class=TriggerClass.MANUAL,
        state=RunState.READY, started_at=datetime.now(timezone.utc)
    )

    jobs = [
        JobContract(job_id="feature_refresh", job_class=JobClass.FEATURE_BUILD, description="t", is_idempotent=True, mutability_class="append", recoverability_class="auto", required_trust_inputs=[])
    ]

    ready_jobs = orch.orchestrate(run, jobs)
    assert len(ready_jobs) == 1
    assert ready_jobs[0].job_id == "feature_refresh"
