class CollateralPolicyEvaluator:
    def evaluate_high_risk_action(self, collateral_id: str, repo):
        if repo.has_hidden_encumbrance(collateral_id):
            return {"decision": "DENY", "reason": "hidden_encumbrance"}
        if repo.is_valuation_stale(collateral_id):
            return {"decision": "REVIEW", "reason": "stale_valuation"}
        return {"decision": "ALLOW"}
# Escrow-plane policy: evidence obligations, fake segregation/stale evidence deny decisions
