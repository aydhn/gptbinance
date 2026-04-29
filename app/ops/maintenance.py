from datetime import datetime
from typing import List, Optional
from app.ops.models import MaintenanceWindow
from app.ops.enums import MaintenanceStatus
from app.ops.repository import OpsRepository
import uuid


class MaintenanceScheduler:
    def __init__(self, repository: OpsRepository):
        self.repository = repository

    def schedule_window(
        self,
        start_time: datetime,
        end_time: datetime,
        description: str,
        allowed_actions: List[str] = None,
    ) -> MaintenanceWindow:
        window = MaintenanceWindow(
            window_id=str(uuid.uuid4()),
            start_time=start_time,
            end_time=end_time,
            description=description,
            allowed_actions=allowed_actions or [],
        )
        self.repository.save_maintenance_window(window)
        return window

    def get_active_window(
        self, current_time: Optional[datetime] = None
    ) -> Optional[MaintenanceWindow]:
        now = current_time or datetime.utcnow()
        windows = self.repository.get_maintenance_windows()
        for window in windows:
            if window.status in (MaintenanceStatus.SCHEDULED, MaintenanceStatus.ACTIVE):
                if window.start_time <= now <= window.end_time:
                    return window
        return None

    def get_upcoming_windows(
        self, current_time: Optional[datetime] = None
    ) -> List[MaintenanceWindow]:
        now = current_time or datetime.utcnow()
        windows = self.repository.get_maintenance_windows()
        return [
            w
            for w in windows
            if w.status == MaintenanceStatus.SCHEDULED and w.start_time > now
        ]
