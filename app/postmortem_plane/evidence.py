class CollateralPostmortemEvidence:
    def export_canonical_refs(self, incident_id: str):
        return {"refs": ["collateral_objects", "liquidations", "deficiencies"]}
# Escrow-plane postmortem evidence: escrow objects, deposits, conditions exported


# Phase 162: Netting Evidence Export
def export_netting_evidence():
    return {
        "netting_objects": [],
        "obligations": [],
        "mutuality_checks": [],
        "valuations": [],
        "setoffs": [],
        "reversals_refs": []
    }

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/postmortem_plane/evidence.py")
    return integration.evaluate_posture()
