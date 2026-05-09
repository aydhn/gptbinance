from app.workflow_plane.models import ScheduleDefinition

class ScheduleRegistry:
    def __init__(self):
        self._schedules = {}

    def register(self, schedule: ScheduleDefinition):
        self._schedules[schedule.schedule_id] = schedule
