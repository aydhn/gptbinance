from typing import Dict, Any

class EpistemicQuality:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        result = {"status": "ok"}
        if context.get("unsupported_certainty") or context.get("contradiction_burial"):
            result["status"] = "caution"
            result["reason"] = "epistemically_weak_but_strategically_convenient"
        return result
