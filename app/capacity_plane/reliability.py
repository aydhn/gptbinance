from typing import Dict
from app.capacity_plane.saturation import list_saturation_records
from app.capacity_plane.enums import SaturationSeverity


def assess_capacity_reliability_impact() -> Dict[str, str]:
    sats = list_saturation_records()
    criticals = [
        s
        for s in sats
        if s.severity in (SaturationSeverity.CRITICAL, SaturationSeverity.EXHAUSTED)
    ]

    if criticals:
        return {"impact": "DEGRADED", "reason": "Critical saturation active."}
    return {"impact": "NONE", "reason": "No critical saturation."}
