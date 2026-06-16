from typing import Dict, Any

class CollateralPolicyContext:
    @staticmethod
    def get_context(collateral_id: str, repo) -> Dict[str, Any]:
        return {
            "has_hidden_lien": repo.has_hidden_encumbrance(collateral_id),
            "is_stale_valuation": repo.is_valuation_stale(collateral_id),
            "is_fake_segregation": repo.has_fake_segregation(collateral_id)
        }
