from typing import Dict, Any

class PostmortemContributors:
    @staticmethod
    def classify(context: Dict[str, Any]) -> list:
        contributors = []
        if context.get("metric_gaming"): contributors.append("metric_gaming")
        if context.get("review_evasion"): contributors.append("review_evasion")
        return contributors
