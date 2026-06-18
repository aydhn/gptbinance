from typing import Dict, Any

class QualityManager:
    def __init__(self):
        pass

    def evaluate(self, context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "status": "evaluated",
            "warnings": [],
            "verdict": "PASSED"
        }
