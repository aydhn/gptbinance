from typing import Dict, Any

class ChangeVerification:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("verification_theater"):
            return {"status": "caution", "reason": "verified_claim_under_exploitable_shortcut"}
        return {"status": "ok"}
