from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.ops.models import MaintenanceWindow


class MaintenanceScheduler:
    def __init__(self, repo):
        self.repo = repo

    def schedule_window(self, start: datetime, end: datetime, reason: str):
        self.repo.save_maintenance_window(
            MaintenanceWindow(
                window_id="test", start_time=start, end_time=end, description=reason
            )
        )
