from datetime import datetime, timezone
from typing import List
from app.capacity_plane.models import CapacityDivergenceReport

_divergences: List[CapacityDivergenceReport] = []


def record_divergence(
    report_id: str, divergence_type: str, severity: str, blast_radius: List[str]
) -> CapacityDivergenceReport:
    rep = CapacityDivergenceReport(
        report_id=report_id,
        divergence_type=divergence_type,
        severity=severity,
        blast_radius=blast_radius,
        timestamp=datetime.now(timezone.utc),
    )
    _divergences.append(rep)
    return rep


def list_divergences() -> List[CapacityDivergenceReport]:
    return _divergences
