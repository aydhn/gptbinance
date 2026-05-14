from typing import Dict, List
from app.capacity_plane.models import ExternalQuotaRecord

_external_quotas: Dict[str, ExternalQuotaRecord] = {}


def record_external_quota(
    quota_id: str,
    vendor: str,
    limit: float,
    used: float,
    window_seconds: int,
    exhaustion_posture: str,
) -> ExternalQuotaRecord:
    rec = ExternalQuotaRecord(
        quota_id=quota_id,
        vendor=vendor,
        limit=limit,
        used=used,
        window_seconds=window_seconds,
        exhaustion_posture=exhaustion_posture,
    )
    _external_quotas[quota_id] = rec
    return rec


def list_external_quotas() -> List[ExternalQuotaRecord]:
    return list(_external_quotas.values())
