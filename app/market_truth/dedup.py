from app.market_truth.models import DedupRecord
from app.market_truth.enums import DedupVerdict
from typing import Set


class DuplicateDetector:
    def __init__(self):
        self.seen_events: Set[str] = set()

    def check_event(self, event_fingerprint: str) -> DedupRecord:
        if event_fingerprint in self.seen_events:
            return DedupRecord(
                event_id=event_fingerprint, verdict=DedupVerdict.DUPLICATE
            )
        self.seen_events.add(event_fingerprint)
        return DedupRecord(event_id=event_fingerprint, verdict=DedupVerdict.UNIQUE)
