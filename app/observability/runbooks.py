COLLATERAL_RUNBOOKS = [
    "eligibility_revalidation",
    "valuation_refresh_review",
    "perfection_priority_review",
    "margin_deficiency_review",
    "liquidation_authority_review",
    "collateral_drift_cleanup_review"
]
# Escrow-plane runbooks: condition_revalidation, segregation_integrity_review


# Phase 162: Netting Runbooks
class NettingRunbooks:
    refs = [
        "mutuality_revalidation", "valuation_refresh_review",
        "stay_block_review", "closeout_amount_review",
        "mistaken_setoff_reversal_review", "netting_drift_cleanup_review"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/observability/runbooks.py")
    return integration.evaluate_posture()
