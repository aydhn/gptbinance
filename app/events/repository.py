from app.events.storage import MemoryEventStorage
from app.events.models import EventCalendarSnapshot


class EventRepository:
    def __init__(self, storage: MemoryEventStorage):
        self.storage = storage

    def get_current_calendar(self) -> EventCalendarSnapshot:
        snap = self.storage.get_latest_snapshot()
        if not snap:
            raise ValueError("No calendar snapshot found")
        return snap
