from typing import Optional
from datetime import datetime, timezone
from app.automation.models import JobDefinition
from app.automation.schedules import get_next_run


def is_due(job: JobDefinition, last_run_at: Optional[datetime]) -> bool:
    if not job.schedule or job.schedule.type == "manual":
        return False

    next_run = get_next_run(job.schedule, last_run_at)
    if not next_run:
        return False

    now = datetime.now(timezone.utc)
    return now >= next_run
