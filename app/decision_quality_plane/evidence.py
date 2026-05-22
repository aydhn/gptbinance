from typing import Dict, Any

class DecisionEvidence:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("gameable_evidence"):
            return {"status": "caution", "reason": "best_option_claim_under_gameable_evidence"}
        return {"status": "ok"}
