from app.workflow_plane.runs import RunManager
from app.workflow_plane.models import RunWindow
from app.workflow_plane.enums import TriggerClass, WindowClass
from app.workflow_plane.exceptions import DuplicateRunError
from datetime import datetime, timezone
import pytest

def test_duplicate_run_rejection():
    mgr = RunManager()
    win = RunWindow(window_id="test-win", start_time=datetime.now(timezone.utc), end_time=datetime.now(timezone.utc), as_of_cut=datetime.now(timezone.utc), window_class=WindowClass.ROLLING)
    mgr.initiate_run("wf-1", win, TriggerClass.MANUAL)

    with pytest.raises(DuplicateRunError):
        mgr.initiate_run("wf-1", win, TriggerClass.MANUAL)
