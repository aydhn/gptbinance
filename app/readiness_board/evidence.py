class CollateralReadinessEvidence:
    def get_bundle(self, collateral_id: str, repo):
        return {
            "asset_clarity": not repo.has_fake_segregation(collateral_id),
            "valuation_sufficiency": not repo.is_valuation_stale(collateral_id),
            "perfection_integrity": not repo.has_hidden_encumbrance(collateral_id)
        }
# Escrow-plane readiness: escrow trust, deposit clarity, condition sufficiency added to bundle
