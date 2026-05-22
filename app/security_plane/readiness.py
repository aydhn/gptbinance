from typing import Dict, Any

class SecurityReadiness:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("low_cost_circumvention"):
            return {"status": "caution", "reason": "secure_posture_under_low_cost_circumvention"}
        return {"status": "ok"}
