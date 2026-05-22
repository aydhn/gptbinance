from typing import Dict, Any

class Waivers:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("waiver_farming"):
            return {"status": "blocker", "reason": "waiver_granted_under_exploit_pattern"}
        return {"status": "ok"}
