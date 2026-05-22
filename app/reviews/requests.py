from typing import Dict, Any

class ReviewRequests:
    @staticmethod
    def get_classes() -> List[str]:
        return [
            "adversarial_integrity_review",
            "exploit_surface_review",
            "gaming_review"
        ]
