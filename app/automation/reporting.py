from typing import List
from app.automation.models import (
    AutomationSummary,
    JobDefinition,
    RunHistoryEntry,
    RunStatus,
)
from app.automation.history import get_last_run
from app.automation.schedules import get_next_run


def generate_automation_summary(
    jobs: List[JobDefinition], history: List[RunHistoryEntry]
) -> AutomationSummary:
    paused = sum(1 for j in jobs if j.paused)

    next_runs = []
    recent_failures = 0

    for j in jobs:
        last = get_last_run(history, j.id)

        # Count recent failures
        if last and last.status == RunStatus.FAILED:
            recent_failures += 1

        next_r = None
        if j.schedule:
            last_dt = last.started_at if last else None
            next_r = get_next_run(j.schedule, last_dt)

        next_runs.append(
            {
                "job_id": j.id,
                "name": j.name,
                "paused": j.paused,
                "next_run": next_r.isoformat() if next_r else None,
                "last_status": last.status.value if last else None,
            }
        )

    # Sort next runs by time
    valid_next_runs = [nr for nr in next_runs if nr["next_run"] is not None]

    def get_sort_key(item: dict) -> str:
        val = item.get("next_run")
        return str(val) if val is not None else ""

    next_runs_sorted = sorted(valid_next_runs, key=get_sort_key)

    return AutomationSummary(
        total_jobs=len(jobs),
        due_jobs=0,  # Computed at execution time usually
        paused_jobs=paused,
        recent_failures=recent_failures,
        next_runs=next_runs_sorted,
    )
