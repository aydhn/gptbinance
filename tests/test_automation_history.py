from datetime import datetime, timezone, timedelta
from app.automation.models import RunHistoryEntry
from app.automation.enums import RunStatus
from app.automation.history import get_last_success, get_consecutive_failures


def test_get_last_success():
    now = datetime.now(timezone.utc)
    history = [
        RunHistoryEntry(
            run_id="1",
            job_id="job1",
            status=RunStatus.FAILED,
            started_at=now,
            attempt=1,
            error=None,
            duration_seconds=1.0,
        ),
        RunHistoryEntry(
            run_id="2",
            job_id="job1",
            status=RunStatus.SUCCESS,
            started_at=now - timedelta(minutes=5),
            attempt=1,
            error=None,
            duration_seconds=1.0,
        ),
    ]

    ls = get_last_success(history, "job1")
    assert ls is not None
    assert ls.run_id == "2"


def test_consecutive_failures():
    now = datetime.now(timezone.utc)
    history = [
        RunHistoryEntry(
            run_id="1",
            job_id="job1",
            status=RunStatus.FAILED,
            started_at=now,
            attempt=1,
            error=None,
            duration_seconds=1.0,
        ),
        RunHistoryEntry(
            run_id="2",
            job_id="job1",
            status=RunStatus.FAILED,
            started_at=now - timedelta(minutes=5),
            attempt=1,
            error=None,
            duration_seconds=1.0,
        ),
        RunHistoryEntry(
            run_id="3",
            job_id="job1",
            status=RunStatus.SUCCESS,
            started_at=now - timedelta(minutes=10),
            attempt=1,
            error=None,
            duration_seconds=1.0,
        ),
    ]

    fails = get_consecutive_failures(history, "job1")
    assert fails == 2
