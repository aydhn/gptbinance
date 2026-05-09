from app.workflow_plane.backfills import BackfillManager
from app.workflow_plane.runs import RunManager
from app.workflow_plane.models import RunWindow
from app.workflow_plane.exceptions import BackfillContaminationError
from app.workflow_plane.enums import WindowClass
from datetime import datetime, timezone, timedelta
import pytest

def test_backfill_initiation():
    mgr = BackfillManager(RunManager())
    now = datetime.now(timezone.utc)
    w1 = RunWindow(window_id="w1", start_time=now-timedelta(days=2), end_time=now-timedelta(days=1), as_of_cut=now, window_class=WindowClass.BACKFILL)
    w2 = RunWindow(window_id="w2", start_time=now-timedelta(days=1), end_time=now, as_of_cut=now, window_class=WindowClass.BACKFILL)

    b = mgr.initiate_backfill("wf-1", w1, w2, "Missing data")
    assert b.workflow_id == "wf-1"

def test_backfill_contamination_guard():
    mgr = BackfillManager(RunManager())
    now = datetime.now(timezone.utc)
    w1 = RunWindow(window_id="w1", start_time=now-timedelta(days=1), end_time=now, as_of_cut=now, window_class=WindowClass.BACKFILL)
    w2 = RunWindow(window_id="w2", start_time=now-timedelta(days=2), end_time=now-timedelta(days=1), as_of_cut=now, window_class=WindowClass.BACKFILL)

    with pytest.raises(BackfillContaminationError):
        mgr.initiate_backfill("wf-1", w1, w2, "Invalid order")
