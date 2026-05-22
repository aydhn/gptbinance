from typing import Dict, Any

class AssuranceTesting:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("review_poisoning") or context.get("sample_gaming"):
            return {"status": "caution", "reason": "test_passed_but_adversarially_weak_evidence"}
        return {"status": "ok"}
