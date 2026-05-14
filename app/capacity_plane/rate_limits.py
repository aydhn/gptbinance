from typing import Dict, List
from app.capacity_plane.models import RateLimitRecord

_rate_limits: Dict[str, RateLimitRecord] = {}


def record_rate_limit(
    limit_id: str,
    target: str,
    rate: float,
    window_type: str,
    budget_usage_ratio: float,
    retry_budget_linked: bool,
) -> RateLimitRecord:
    rec = RateLimitRecord(
        limit_id=limit_id,
        target=target,
        rate=rate,
        window_type=window_type,
        budget_usage_ratio=budget_usage_ratio,
        retry_budget_linked=retry_budget_linked,
    )
    _rate_limits[limit_id] = rec
    return rec


def list_rate_limits() -> List[RateLimitRecord]:
    return list(_rate_limits.values())
