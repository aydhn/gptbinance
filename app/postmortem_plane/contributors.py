COLLATERAL_CONTRIBUTORS = [
    "hidden_lien",
    "stale_valuation",
    "fake_segregation",
    "wrong_way_collateral",
    "deficiency_burial",
    "wrongful_liquidation"
]

# Phase 160: Waterfall Plane Integrations

WATERFALL_CONTRIBUTORS = [
    "hidden_seniority",
    "reserve_cosmetics",
    "disputed_claim_burial",
    "duplicate_allocation",
    "overdistribution",
    "clawback_gap"
]
# Escrow-plane contributors: fake_segregation, commingling, stale_evidence


# Phase 162: Netting Contributors
class NettingPostmortemContributor:
    categories = [
        "affiliate_laundering",
        "mutuality_failure",
        "stale_valuation",
        "stay_ignore",
        "double_offset",
        "residual_burial"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/postmortem_plane/contributors.py")
    return integration.evaluate_posture()
