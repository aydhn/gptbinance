from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import QueueDepthRecord

_queue_records: Dict[str, QueueDepthRecord] = {}


def record_queue_depth(
    queue_id: str,
    size: int,
    oldest_message_age_seconds: float,
    drop_policy: str,
    starvation_surfaces: List[str],
) -> QueueDepthRecord:
    rec = QueueDepthRecord(
        queue_id=queue_id,
        size=size,
        oldest_message_age_seconds=oldest_message_age_seconds,
        drop_policy=drop_policy,
        starvation_surfaces=starvation_surfaces,
        timestamp=datetime.now(timezone.utc),
    )
    _queue_records[queue_id] = rec
    return rec


def list_queue_records() -> List[QueueDepthRecord]:
    return list(_queue_records.values())
