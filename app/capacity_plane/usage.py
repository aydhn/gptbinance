from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import UsageSnapshot

_usage_snapshots: Dict[str, List[UsageSnapshot]] = {}


def record_usage(
    resource_id: str,
    current_usage: float,
    peak_usage_1m: float,
    sustained_usage_5m: float,
    attribution: Dict[str, float] = None,
) -> UsageSnapshot:
    snap = UsageSnapshot(
        resource_id=resource_id,
        timestamp=datetime.now(timezone.utc),
        current_usage=current_usage,
        peak_usage_1m=peak_usage_1m,
        sustained_usage_5m=sustained_usage_5m,
        attribution=attribution or {},
    )
    if resource_id not in _usage_snapshots:
        _usage_snapshots[resource_id] = []
    _usage_snapshots[resource_id].append(snap)
    return snap


def get_latest_usage(resource_id: str) -> UsageSnapshot:
    snaps = _usage_snapshots.get(resource_id, [])
    if snaps:
        return snaps[-1]
    return UsageSnapshot(
        resource_id=resource_id,
        timestamp=datetime.now(timezone.utc),
        current_usage=0.0,
        peak_usage_1m=0.0,
        sustained_usage_5m=0.0,
    )
