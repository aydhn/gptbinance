from app.workflow_plane.receipts import ReceiptManager
from app.workflow_plane.models import WorkflowRun, RunWindow
from app.workflow_plane.enums import TriggerClass, RunState, WindowClass
from datetime import datetime, timezone

def test_receipt_manager():
    mgr = ReceiptManager()
    win = RunWindow(window_id="test", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)
    run = WorkflowRun(
        run_id="r1", workflow_id="w1", window=win, trigger_class=TriggerClass.MANUAL,
        state=RunState.COMPLETED, started_at=datetime.now(timezone.utc)
    )
    receipt = mgr.issue_receipt(run, "operator")
    assert "completed successfully" in receipt.completion_summary
