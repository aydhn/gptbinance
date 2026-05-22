from typing import Dict, Any

class Approvals:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("approval_laundering") or context.get("stale_approval_masking"):
            return {"status": "caution", "reason": "approval_present_but_adversarially_weak"}
        return {"status": "ok"}
