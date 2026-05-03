from typing import List
from datetime import datetime
from app.events.models import EventBlackoutWindow
from app.events.enums import BlackoutType


class BlackoutManager:
    def __init__(self):
        self.blackouts: List[EventBlackoutWindow] = []

    def add_manual_blackout(
        self, start: datetime, end: datetime, reason: str
    ) -> EventBlackoutWindow:
        import uuid

        bo = EventBlackoutWindow(
            blackout_id=str(uuid.uuid4()),
            start_time=start,
            end_time=end,
            blackout_type=BlackoutType.MANUAL,
            reason=reason,
        )
        self.blackouts.append(bo)
        return bo

    def get_active_blackouts(self, now: datetime) -> List[EventBlackoutWindow]:
        return [b for b in self.blackouts if b.start_time <= now <= b.end_time]
