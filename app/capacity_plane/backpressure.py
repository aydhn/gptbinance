from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import BackpressureRecord

_backpressure_records: Dict[str, List[BackpressureRecord]] = {}


def record_backpressure(
    target_id: str,
    queue_growth_rate: float,
    consumer_lag: float,
    backlog_age_seconds: float,
) -> BackpressureRecord:
    rec = BackpressureRecord(
        target_id=target_id,
        queue_growth_rate=queue_growth_rate,
        consumer_lag=consumer_lag,
        backlog_age_seconds=backlog_age_seconds,
        timestamp=datetime.now(timezone.utc),
    )
    if target_id not in _backpressure_records:
        _backpressure_records[target_id] = []
    _backpressure_records[target_id].append(rec)
    return rec


def list_backpressure_records() -> List[BackpressureRecord]:
    all_recs = []
    for recs in _backpressure_records.values():
        all_recs.extend(recs)
    return all_recs
