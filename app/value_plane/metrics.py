from typing import Dict, Any

class ValueMetrics:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("reported_value_inflation"):
            return {"status": "caution", "reason": "value_gain_under_gaming_suspicion"}
        return {"status": "ok"}
