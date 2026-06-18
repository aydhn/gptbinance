COLLATERAL_CAPABILITIES = [
    "inspect_collateral_manifest",
    "review_assets_eligibility_and_haircuts",
    "review_liens_perfection_and_priority",
    "review_calls_deficiencies_and_liquidations",
    "review_wrong_way_and_fake_segregation_risks"
]
# Escrow-plane capabilities: inspect_escrow_manifest, review_deposits_conditions_and_agents


# Phase 162: Netting Capabilities
class NettingCapabilities:
    caps = [
        "inspect_netting_manifest",
        "review_counterparties_capacities_and_obligations",
        "review_mutuality_maturity_and_setoff_rights",
        "review_valuations_closeouts_and_residuals",
        "review_affiliate_laundering_and_hidden_residual_risks"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/identity/capabilities.py")
    return integration.evaluate_posture()
