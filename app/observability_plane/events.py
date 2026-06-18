COLLATERAL_EVENTS = [
    "collateral_posted",
    "valuation_refreshed",
    "haircut_applied",
    "lien_detected",
    "margin_call_issued",
    "deficiency_opened",
    "liquidation_triggered",
    "collateral_released"
]
# Escrow-plane events: escrow_opened, condition_registered, release_authorized, etc.

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/observability_plane/events.py")
    return integration.evaluate_posture()
