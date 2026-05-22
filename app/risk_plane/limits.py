from typing import Dict, Any

class RiskLimits:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("exposure_understatement"):
            return {"status": "caution", "reason": "risk_number_improved_under_exploitable_metric_semantics"}
        return {"status": "ok"}
