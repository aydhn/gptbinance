from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import ThrottlingRecord
from app.capacity_plane.enums import ThrottlingClass, WorkloadClass

_throttling_records: Dict[str, ThrottlingRecord] = {}


def record_throttling(
    throttle_id: str,
    target_id: str,
    throttle_class: ThrottlingClass,
    affected_workloads: List[WorkloadClass],
    trigger_history: List[str],
) -> ThrottlingRecord:
    rec = ThrottlingRecord(
        throttle_id=throttle_id,
        target_id=target_id,
        throttle_class=throttle_class,
        affected_workloads=affected_workloads,
        trigger_history=trigger_history,
        timestamp=datetime.now(timezone.utc),
    )
    _throttling_records[throttle_id] = rec
    return rec


def list_throttling_records() -> List[ThrottlingRecord]:
    return list(_throttling_records.values())
