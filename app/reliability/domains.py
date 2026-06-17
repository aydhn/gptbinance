class ReliabilityCollateralIntegrityDomain:
    name = "collateral_integrity"
    signals = ["stale_valuation", "hidden_lien", "wrong_way_collateral", "deficiency_burial"]

# Phase 160: Waterfall Plane Integrations

RELIABILITY_DOMAINS_WATERFALL = [
    "waterfall_integrity"
]
# Escrow-plane reliability: escrow_integrity connected to fake segregation and commingling inputs
