from typing import List
from app.shadow_state.models import ShadowTwinSnapshot, DriftFinding


def detect_balances_drift(twin: ShadowTwinSnapshot) -> List[DriftFinding]:
    findings: List[DriftFinding] = []
    return findings
