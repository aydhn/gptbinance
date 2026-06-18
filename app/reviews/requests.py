COLLATERAL_REVIEW_CLASSES = [
    "collateral_integrity_review",
    "asset_eligibility_review",
    "valuation_haircut_review",
    "perfection_priority_review",
    "margin_liquidation_review",
    "beneficiary_collateral_review"
]
# Escrow-plane reviews: escrow_integrity_review, deposit_condition_review


# Phase 162: Netting Reviews
class NettingReviews:
    classes = [
        "netting_integrity_review", "obligation_mutuality_review",
        "valuation_closeout_review", "setoff_reversal_review",
        "insolvency_netting_review", "beneficiary_balance_review"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/reviews/requests.py")
    return integration.evaluate_posture()
