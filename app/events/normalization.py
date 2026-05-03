from typing import List, Dict, Any
from datetime import datetime
from app.events.base import EventNormalizerBase
from app.events.models import EventRecord
from app.events.enums import (
    EventCategory,
    EventSeverity,
    EventConfidence,
    EventFreshness,
)


class DefaultEventNormalizer(EventNormalizerBase):
    def normalize(self, raw_events: List[Dict[str, Any]]) -> List[EventRecord]:
        normalized = []
        for raw in raw_events:
            # Basit bir eşleme, normalde daha akıllı olabilir
            try:
                timestamp = datetime.fromisoformat(
                    raw.get("time", datetime.now().isoformat())
                )
            except ValueError:
                timestamp = datetime.now()

            record = EventRecord(
                event_id=raw.get("id", "unknown"),
                source_id="default_source",
                title=raw.get("title", "Unknown Event"),
                category=EventCategory.OTHER,
                severity=EventSeverity.MEDIUM
                if raw.get("importance") != "High"
                else EventSeverity.HIGH,
                confidence=EventConfidence.MEDIUM,
                timestamp=timestamp,
                freshness=EventFreshness.FRESH,
            )
            normalized.append(record)
        return normalized
