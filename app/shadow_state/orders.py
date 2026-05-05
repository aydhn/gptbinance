from typing import List, Dict, Any
from app.shadow_state.models import ShadowTwinSnapshot, DriftFinding
from app.shadow_state.enums import ShadowDomain, DriftType, DriftSeverity
import uuid


def detect_orders_drift(twin: ShadowTwinSnapshot) -> List[DriftFinding]:
    """Detect open order divergence."""
    findings: List[DriftFinding] = []

    venue_orders = {
        o.client_order_id: o
        for o in twin.venue_truth.orders.orders
        if o.client_order_id
    }
    # Mock lookup from local belief
    local_active: Dict[str, Any] = {
        att.get("client_order_id", ""): att
        for att in twin.local_derived.active_attempts
    }

    for cid, venue_o in venue_orders.items():
        if cid not in local_active:
            findings.append(
                DriftFinding(
                    finding_id=f"fnd_{uuid.uuid4().hex[:8]}",
                    domain=ShadowDomain.ORDERS,
                    drift_type=DriftType.MISSING_LOCAL,
                    severity=DriftSeverity.WARNING,
                    description=f"Venue open order {str(cid)} not found in local active attempts",
                    venue_value=venue_o.model_dump(),
                    evidence_refs=[str(cid)],
                )
            )

    for cid_str, local_att in local_active.items():
        if not cid_str:
            continue
        if cid_str not in venue_orders:
            findings.append(
                DriftFinding(
                    finding_id=f"fnd_{uuid.uuid4().hex[:8]}",
                    domain=ShadowDomain.ORDERS,
                    drift_type=DriftType.MISSING_VENUE,
                    severity=DriftSeverity.CRITICAL,
                    description=f"Local active attempt {str(cid_str)} not found in venue open orders",
                    local_value=local_att,
                    evidence_refs=[str(cid_str)],
                )
            )

    return findings
