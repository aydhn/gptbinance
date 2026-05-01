from datetime import datetime, timezone, timedelta
from app.automation.models import JobSchedule
from app.automation.enums import ScheduleType
from app.automation.schedules import get_next_run


def test_interval_schedule():
    sched = JobSchedule(type=ScheduleType.INTERVAL, expression="3600")
    now = datetime.now(timezone.utc)

    # First run
    next_run = get_next_run(sched, None)
    assert next_run is not None

    # Subsequent run
    last_run = now - timedelta(seconds=1800)
    next_run = get_next_run(sched, last_run)
    assert next_run == last_run + timedelta(seconds=3600)


def test_fixed_time_schedule():
    sched = JobSchedule(type=ScheduleType.FIXED_TIME, expression="daily@14:30")
    now = datetime.now(timezone.utc)
    target_today = now.replace(hour=14, minute=30, second=0, microsecond=0)

    # If target today is in future
    if target_today > now:
        next_run = get_next_run(sched, None)
        assert next_run == target_today
