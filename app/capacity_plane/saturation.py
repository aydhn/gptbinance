from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import SaturationRecord
from app.capacity_plane.enums import SaturationSeverity

_saturation_records: Dict[str, List[SaturationRecord]] = {}


def record_saturation(
    resource_id: str,
    severity: SaturationSeverity,
    duration_seconds: float,
    blast_radius: List[str],
) -> SaturationRecord:
    rec = SaturationRecord(
        resource_id=resource_id,
        severity=severity,
        duration_seconds=duration_seconds,
        blast_radius=blast_radius,
        timestamp=datetime.now(timezone.utc),
    )
    if resource_id not in _saturation_records:
        _saturation_records[resource_id] = []
    _saturation_records[resource_id].append(rec)
    return rec


def list_saturation_records() -> List[SaturationRecord]:
    all_recs = []
    for recs in _saturation_records.values():
        all_recs.extend(recs)
    return all_recs
