
from datetime import datetime, timezone
from app.events.storage import MemoryEventStorage
from app.events.repository import EventRepository
from app.events.models import EventCalendarSnapshot


def test_event_storage_and_repository():
    storage = MemoryEventStorage()
    repo = EventRepository(storage)

    snap = EventCalendarSnapshot(
        snapshot_id="s1", timestamp=datetime.now(timezone.utc), events=[]
    )
    storage.save_snapshot(snap)

    retrieved = repo.get_current_calendar()
    assert retrieved.snapshot_id == "s1"
