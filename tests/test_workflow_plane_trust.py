from app.workflow_plane.trust import WorkflowTrustEvaluator
from app.workflow_plane.models import WorkflowRun, RunWindow, GateCheckResult
from app.workflow_plane.enums import RunState, TrustVerdict, TriggerClass, GateClass, WindowClass
from datetime import datetime, timezone

def test_trust_evaluation():
    evaluator = WorkflowTrustEvaluator()
    win = RunWindow(window_id="test", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)

    run1 = WorkflowRun(
        run_id="r1", workflow_id="w1", window=win, trigger_class=TriggerClass.MANUAL,
        state=RunState.COMPLETED, started_at=datetime.now(timezone.utc),
        gate_results=[GateCheckResult(gate_class=GateClass.DATA_TRUST, passed=True, rationale="ok")]
    )
    assert evaluator.evaluate(run1).verdict == TrustVerdict.TRUSTED

    run2 = WorkflowRun(
        run_id="r2", workflow_id="w1", window=win, trigger_class=TriggerClass.MANUAL,
        state=RunState.COMPLETED, started_at=datetime.now(timezone.utc),
        gate_results=[GateCheckResult(gate_class=GateClass.DATA_TRUST, passed=True, bypassed=True, rationale="bypassed")]
    )
    assert evaluator.evaluate(run2).verdict == TrustVerdict.CAUTION

    run3 = WorkflowRun(
        run_id="r3", workflow_id="w1", window=win, trigger_class=TriggerClass.MANUAL,
        state=RunState.FAILED, started_at=datetime.now(timezone.utc)
    )
    assert evaluator.evaluate(run3).verdict == TrustVerdict.BLOCKED
