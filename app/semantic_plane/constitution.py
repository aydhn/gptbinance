from app.semantic_plane.registry import CanonicalSemanticRegistry

class ConstitutionSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def evaluate_verdict_semantics(self, verdict_label: str) -> bool:
        # Blocker/caution taxonomy semantics must align with semantic plane definitions
        if verdict_label not in ["blocker", "caution", "review_required", "pass"]:
            return False
        return True
