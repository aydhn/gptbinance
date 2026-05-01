from datetime import datetime, timezone, timedelta
from typing import Optional
import re

from app.automation.models import JobSchedule
from app.automation.enums import ScheduleType
from app.automation.exceptions import ScheduleParseError


def get_next_run(
    schedule: JobSchedule, last_run_at: Optional[datetime] = None
) -> Optional[datetime]:
    """Calculate the next run time based on the schedule."""
    now = datetime.now(timezone.utc)

    if schedule.type == ScheduleType.MANUAL:
        return None

    if schedule.type == ScheduleType.INTERVAL:
        try:
            seconds = int(schedule.expression)
        except ValueError:
            raise ScheduleParseError(
                f"Invalid interval expression: {schedule.expression}"
            )

        if not last_run_at:
            return now

        return last_run_at + timedelta(seconds=seconds)

    if schedule.type == ScheduleType.FIXED_TIME:
        # e.g., "daily@02:30"
        match = re.match(r"(daily)@(\d{2}):(\d{2})", schedule.expression)
        if match:
            freq, hour, minute = match.groups()
            hour = int(hour)
            minute = int(minute)

            # Simple UTC fixed time for now
            target_today = now.replace(
                hour=hour, minute=minute, second=0, microsecond=0
            )

            if not last_run_at:
                if target_today > now:
                    return target_today
                else:
                    return target_today + timedelta(days=1)

            if now > target_today and last_run_at < target_today:
                return target_today
            elif now <= target_today and last_run_at < target_today - timedelta(days=1):
                return target_today
            elif now > target_today:
                return target_today + timedelta(days=1)
            else:
                return target_today

        raise ScheduleParseError(
            f"Unsupported fixed time expression: {schedule.expression}"
        )

    raise ScheduleParseError(f"Unsupported schedule type: {schedule.type}")
