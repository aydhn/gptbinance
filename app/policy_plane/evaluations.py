from typing import Dict, Any

class PolicyEvaluations:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("exploitable_review_path") or context.get("hidden_gaming_incentive"):
            return {"status": "deny", "reason": "adversarial_obligations_failed"}
        return {"status": "allow"}
