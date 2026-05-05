from typing import List
from app.shadow_state.models import ShadowTwinSnapshot, DriftFinding
from app.shadow_state.enums import ShadowDomain, DriftType, DriftSeverity
import uuid


def detect_positions_drift(twin: ShadowTwinSnapshot) -> List[DriftFinding]:
    """Detect position divergence between venue and crossbook posture."""
    findings = []

    venue_pos = {p.symbol: p for p in twin.venue_truth.positions.positions}
    local_pos = twin.local_derived.crossbook_posture.get("positions", {})

    for sym, vp in venue_pos.items():
        if sym not in local_pos:
            findings.append(
                DriftFinding(
                    finding_id=f"fnd_{uuid.uuid4().hex[:8]}",
                    domain=ShadowDomain.POSITIONS,
                    drift_type=DriftType.MISSING_LOCAL,
                    severity=DriftSeverity.BLOCKER,
                    description=f"Venue position {sym} not recognized by local crossbook",
                    venue_value=vp.model_dump(),
                    evidence_refs=[sym],
                )
            )
        elif vp.size != local_pos[sym].get("size"):
            findings.append(
                DriftFinding(
                    finding_id=f"fnd_{uuid.uuid4().hex[:8]}",
                    domain=ShadowDomain.POSITIONS,
                    drift_type=DriftType.VALUE_MISMATCH,
                    severity=DriftSeverity.CRITICAL,
                    description=f"Position size mismatch for {sym}",
                    venue_value=vp.size,
                    local_value=local_pos[sym].get("size"),
                    magnitude=abs(vp.size - local_pos[sym].get("size", 0)),
                    evidence_refs=[sym],
                )
            )

    return findings
