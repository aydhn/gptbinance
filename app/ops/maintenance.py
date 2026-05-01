from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class MaintenanceWindow(BaseModel):
    start_time: datetime
    end_time: datetime
    reason: str

class MaintenanceScheduler:
    def __init__(self, repo):
        self.repo = repo

    def schedule_window(self, start: datetime, end: datetime, reason: str):
        self.repo.save_maintenance_window(MaintenanceWindow(start_time=start, end_time=end, reason=reason))
