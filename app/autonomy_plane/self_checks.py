from typing import Dict, Any

class SelfChecks:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        if context.get("self_check_gaming"):
            return {"status": "caution", "reason": "self_check_passed_but_easy_to_game"}
        return {"status": "ok"}
