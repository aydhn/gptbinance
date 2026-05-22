from typing import Dict, Any

class ReliabilityDomain:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "exploit_normalization": context.get("exploit_normalization"),
            "review_theater": context.get("review_theater")
        }
