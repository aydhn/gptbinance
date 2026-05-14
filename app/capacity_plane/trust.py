from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import CapacityTrustVerdictModel
from app.capacity_plane.enums import CapacityTrustVerdict
from app.capacity_plane.isolation import check_live_isolation
from app.capacity_plane.reliability import assess_capacity_reliability_impact


def evaluate_capacity_trust() -> CapacityTrustVerdictModel:
    factors = {}
    blockers = []
    caveats = []

    if not check_live_isolation():
        blockers.append("Live isolation breached.")
        factors["isolation"] = "FAILED"
    else:
        factors["isolation"] = "PASSED"

    rel = assess_capacity_reliability_impact()
    if rel["impact"] == "DEGRADED":
        caveats.append(f"Reliability impact: {rel['reason']}")
        factors["reliability"] = "DEGRADED"
    else:
        factors["reliability"] = "PASSED"

    verdict = CapacityTrustVerdict.TRUSTED
    if blockers:
        verdict = CapacityTrustVerdict.BLOCKED
    elif caveats:
        verdict = CapacityTrustVerdict.CAUTION

    return CapacityTrustVerdictModel(
        verdict_id=f"tv_{int(datetime.now(timezone.utc).timestamp())}",
        verdict=verdict,
        factors=factors,
        blockers=blockers,
        caveats=caveats,
        timestamp=datetime.now(timezone.utc),
    )
