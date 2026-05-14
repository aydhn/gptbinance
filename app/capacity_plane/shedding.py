from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import SheddingRecord
from app.capacity_plane.enums import SheddingClass

_shedding_records: Dict[str, SheddingRecord] = {}


def record_shedding(
    shed_id: str, target_id: str, shed_class: SheddingClass, verification_notes: str
) -> SheddingRecord:
    rec = SheddingRecord(
        shed_id=shed_id,
        target_id=target_id,
        shed_class=shed_class,
        verification_notes=verification_notes,
        timestamp=datetime.now(timezone.utc),
    )
    _shedding_records[shed_id] = rec
    return rec


def list_shedding_records() -> List[SheddingRecord]:
    return list(_shedding_records.values())
