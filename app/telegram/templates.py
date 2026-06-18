COLLATERAL_TEMPLATES = {
    "hidden_lien_detected": "⚠️ HIDDEN LIEN DETECTED\nCollateral ID: {id}\nAction Required: Immediate review of priority perfection.",
    "stale_valuation_detected": "⚠️ STALE VALUATION\nCollateral ID: {id}\nHaircuts and advance rates may be compromised."
}
# Escrow-plane telegram templates: escrow manifest ready, fake segregation detected


# Phase 162: Netting Notification Templates
NETTING_TEMPLATES = {
    "netting_manifest_ready": "Netting manifest is ready.",
    "mutuality_failure_detected": "Mutuality failure detected.",
    "stale_valuation_detected": "Stale valuation detected.",
    "mistaken_setoff_detected": "Mistaken setoff detected.",
    "netting_review_required": "Netting review required.",
    "netting_summary_digest": "Netting summary digest."
}

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/telegram/templates.py")
    return integration.evaluate_posture()
