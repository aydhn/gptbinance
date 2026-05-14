from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import FairnessReport
from app.capacity_plane.enums import FairnessClass

_fairness_reports: Dict[str, FairnessReport] = {}


def report_fairness(
    target_id: str,
    fairness_class: FairnessClass,
    dominance_indicators: Dict[str, float],
    starvation_warnings: List[str],
) -> FairnessReport:
    rec = FairnessReport(
        target_id=target_id,
        fairness_class=fairness_class,
        dominance_indicators=dominance_indicators,
        starvation_warnings=starvation_warnings,
        timestamp=datetime.now(timezone.utc),
    )
    _fairness_reports[target_id] = rec
    return rec


def list_fairness_reports() -> List[FairnessReport]:
    return list(_fairness_reports.values())
