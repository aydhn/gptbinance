class CollateralPostmortemEvidence:
    def export_canonical_refs(self, incident_id: str):
        return {"refs": ["collateral_objects", "liquidations", "deficiencies"]}
# Escrow-plane postmortem evidence: escrow objects, deposits, conditions exported
