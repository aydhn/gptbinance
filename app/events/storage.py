from typing import Dict, List, Optional
from app.events.models import EventCalendarSnapshot, EventBlackoutWindow


class MemoryEventStorage:
    def __init__(self):
        self.snapshots: Dict[str, EventCalendarSnapshot] = {}
        self.blackouts: List[EventBlackoutWindow] = []

    def save_snapshot(self, snapshot: EventCalendarSnapshot):
        self.snapshots[snapshot.snapshot_id] = snapshot

    def get_latest_snapshot(self) -> Optional[EventCalendarSnapshot]:
        if not self.snapshots:
            return None
        return sorted(self.snapshots.values(), key=lambda s: s.timestamp)[-1]

    def save_blackout(self, blackout: EventBlackoutWindow):
        self.blackouts.append(blackout)

    def list_blackouts(self) -> List[EventBlackoutWindow]:
        return self.blackouts
