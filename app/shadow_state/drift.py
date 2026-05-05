from typing import List
from app.shadow_state.models import ShadowTwinSnapshot, DriftFinding
from app.shadow_state.enums import ShadowDomain

from app.shadow_state.orders import detect_orders_drift
from app.shadow_state.positions import detect_positions_drift
from app.shadow_state.balances import detect_balances_drift
from app.shadow_state.modes import detect_modes_drift


class DriftDetector:
    """Base logic for detecting drift in a twin snapshot."""

    def detect_drift(
        self, twin: ShadowTwinSnapshot, domain: ShadowDomain
    ) -> List[DriftFinding]:
        if domain == ShadowDomain.ORDERS:
            return detect_orders_drift(twin)
        elif domain == ShadowDomain.POSITIONS:
            return detect_positions_drift(twin)
        elif domain == ShadowDomain.BALANCES:
            return detect_balances_drift(twin)
        elif domain == ShadowDomain.MODES:
            return detect_modes_drift(twin)
        return []
