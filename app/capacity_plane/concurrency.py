from typing import Dict, List
from app.capacity_plane.models import ConcurrencyLimit

_concurrency_limits: Dict[str, ConcurrencyLimit] = {}


def set_concurrency_limit(
    limit_id: str,
    scope: str,
    max_concurrent: int,
    current_concurrent: int,
    saturation_notes: str = "",
) -> ConcurrencyLimit:
    # no infinite concurrency default
    if max_concurrent <= 0:
        max_concurrent = 1  # very safe default
        saturation_notes = "Forced default due to infinite or invalid config"

    limit = ConcurrencyLimit(
        limit_id=limit_id,
        scope=scope,
        max_concurrent=max_concurrent,
        current_concurrent=current_concurrent,
        saturation_notes=saturation_notes,
    )
    _concurrency_limits[limit_id] = limit
    return limit


def list_concurrency_limits() -> List[ConcurrencyLimit]:
    return list(_concurrency_limits.values())
