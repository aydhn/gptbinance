from typing import Dict, Any

class SemanticDrift:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        result = {"status": "ok"}
        if context.get("threshold_reinterpretation") or context.get("alias_laundering"):
            result["status"] = "blocker"
            result["reason"] = "semantic_drift_with_exploit_incentive"
        return result
