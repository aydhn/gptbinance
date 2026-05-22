from typing import Dict, Any

class TemporalReordering:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        result = {"status": "ok"}
        if context.get("harmful_reorder") or context.get("stale_as_fresh"):
            result["status"] = "caution"
            result["reason"] = "benign_looking_but_exploitable_reorder"
        return result
