from app.workflow_plane.reruns import RerunManager
from app.workflow_plane.runs import RunManager
from app.workflow_plane.models import RunWindow
from app.workflow_plane.enums import TriggerClass, RunState, WindowClass
from datetime import datetime, timezone

def test_explicit_rerun_preserves_history():
    mgr = RunManager()
    rmgr = RerunManager(mgr)
    win = RunWindow(window_id="test-win", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)

    orig = mgr.initiate_run("wf-1", win, TriggerClass.MANUAL)
    new_run = rmgr.execute_rerun(orig.run_id, reason="Testing rerun", approver="admin")

    assert orig.state == RunState.RERUN_SUPERSEDED
    assert orig.superseded_by == new_run.run_id
    assert new_run.state == RunState.QUEUED
