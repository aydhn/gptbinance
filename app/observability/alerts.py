COLLATERAL_ALERTS = [
    "hidden_lien_detected",
    "stale_valuation_detected",
    "fake_segregation_detected",
    "deficiency_detected",
    "wrongful_liquidation_detected",
    "collateral_review_required"
]

# Phase 160: Waterfall Plane Integrations

ALERT_TYPES_WATERFALL = [
    "hidden_seniority_detected",
    "reserve_cosmetics_detected",
    "disputed_claim_burial_detected",
    "overdistribution_detected",
    "clawback_gap_detected",
    "waterfall_review_required"
]
# Escrow-plane alerts: fake_segregation_detected, forged_instruction_detected


# Phase 162: Netting Alerts
class NettingAlerts:
    alerts = [
        "mutuality_failure_detected", "stale_valuation_detected",
        "stay_ignore_detected", "mistaken_setoff_detected",
        "residual_burial_detected", "netting_review_required"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/observability/alerts.py")
    return integration.evaluate_posture()
