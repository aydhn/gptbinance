from typing import Dict, Any

class Rollouts:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("anomaly_suppression"):
            return {"status": "anomaly", "reason": "rollout_success_under_suspicious_anomaly_suppression"}
        return {"status": "ok"}
