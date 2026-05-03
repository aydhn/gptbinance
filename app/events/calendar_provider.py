from datetime import datetime, timezone
from typing import List
from app.events.base import CalendarProviderBase
from app.events.models import EventRecord, EventCalendarSnapshot
from app.events.sources import DummyMacroCalendarAdapter
from app.events.normalization import DefaultEventNormalizer
import uuid


class DefaultCalendarProvider(CalendarProviderBase):
    def __init__(self):
        self.sources = [DummyMacroCalendarAdapter()]
        self.normalizer = DefaultEventNormalizer()

    def get_calendar(
        self, start_time: datetime, end_time: datetime
    ) -> List[EventRecord]:
        raw_events = []
        for src in self.sources:
            raw_events.extend(src.fetch_events())

        events = self.normalizer.normalize(raw_events)
        return [e for e in events if start_time <= e.timestamp <= end_time]

    def get_snapshot(self) -> EventCalendarSnapshot:
        events = self.get_calendar(
            datetime.min.replace(tzinfo=timezone.utc),
            datetime.max.replace(tzinfo=timezone.utc),
        )
        return EventCalendarSnapshot(
            snapshot_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            events=events,
        )
