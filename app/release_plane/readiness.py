from typing import Dict, Any

class ReleaseReadiness:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("canary_theater") or context.get("rollout_masking"):
            return {"status": "blocker", "reason": "release_ready_under_exploitable_canary_semantics"}
        return {"status": "ok"}
