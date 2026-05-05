from typing import List
from app.shadow_state.models import ShadowTwinSnapshot, DriftFinding
from app.shadow_state.enums import ShadowDomain, DriftType, DriftSeverity
import uuid


def detect_modes_drift(twin: ShadowTwinSnapshot) -> List[DriftFinding]:
    findings = []
    venue_modes = twin.venue_truth.modes
    local_modes = twin.local_derived.account_mode_belief

    if venue_modes.futures_position_mode != local_modes.get("futures_position_mode"):
        findings.append(
            DriftFinding(
                finding_id=f"fnd_{uuid.uuid4().hex[:8]}",
                domain=ShadowDomain.MODES,
                drift_type=DriftType.MODE_MISMATCH,
                severity=DriftSeverity.BLOCKER,
                description="Futures position mode mismatch",
                venue_value=venue_modes.futures_position_mode,
                local_value=local_modes.get("futures_position_mode"),
            )
        )

    return findings
