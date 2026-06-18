COLLATERAL_ARTEFACT_FAMILIES = ["collateral_objects", "liquidations", "haircuts", "perfections"]
COLLATERAL_RELATIONS = ["collateralized_under", "pledged_by", "perfected_under", "valued_under", "liquidated_under", "released_under", "diverged_collateral_from"]
# Escrow-plane artefacts: escrow objects, conditions, instructions as artefact family


# Phase 162: Netting Artefacts
class NettingEvidenceArtefact:
    families = [
        "netting_objects", "nettings", "subjects", "counterparties", "capacities",
        "obligations", "sets", "eligibility", "mutuality", "maturity",
        "due_payable", "contingent", "disputed", "stayed", "conversion",
        "valuation", "closeout", "setoff_rights", "contractual", "statutory", "equitable",
        "payment_netting", "settlement_netting", "closeout_netting", "novation",
        "cross_product", "insolvency", "stay_blocks", "partials", "residuals",
        "mistaken_setoff", "reversal", "anti_duplication", "gross_legs",
        "comparisons", "equivalence", "trust_reports"
    ]
    relations = [
        "netted_under", "setoff_under", "closeout_under", "reversed_under",
        "valued_under", "residual_under", "diverged_netting_from"
    ]

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/evidence_graph/artefacts.py")
    return integration.evaluate_posture()
