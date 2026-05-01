from typing import List, Optional
from app.automation.models import RunHistoryEntry, RunStatus


def get_last_success(
    history: List[RunHistoryEntry], job_id: str
) -> Optional[RunHistoryEntry]:
    """Get the last successful run for a job."""
    for entry in sorted(history, key=lambda e: e.started_at, reverse=True):
        if entry.job_id == job_id and entry.status == RunStatus.SUCCESS:
            return entry
    return None


def get_last_run(
    history: List[RunHistoryEntry], job_id: str
) -> Optional[RunHistoryEntry]:
    for entry in sorted(history, key=lambda e: e.started_at, reverse=True):
        if entry.job_id == job_id:
            return entry
    return None


def get_consecutive_failures(history: List[RunHistoryEntry], job_id: str) -> int:
    """Count consecutive failures since the last success."""
    count = 0
    for entry in sorted(history, key=lambda e: e.started_at, reverse=True):
        if entry.job_id != job_id:
            continue
        if entry.status == RunStatus.SUCCESS:
            break
        if entry.status == RunStatus.FAILED:
            count += 1
    return count
