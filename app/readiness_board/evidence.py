from typing import Dict, Any

class ReadinessEvidence:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("critical_adversarial_integrity_failures"):
            return {"status": "blocker", "reason": "critical_adversarial_integrity_failures"}
        return {"status": "ready"}
