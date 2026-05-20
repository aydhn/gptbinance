from app.semantic_plane.registry import CanonicalSemanticRegistry

class ReadinessManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def aggregate_semantic_readiness(self) -> dict:
        total_terms = len(self.registry.terms)
        conflicts = len(self.registry.conflicts)

        # Simplified readiness logic
        readiness_score = 100
        if conflicts > 0:
            readiness_score -= (conflicts * 10)

        return {
            "status": "Ready" if readiness_score > 80 else "Review Required",
            "score": max(0, readiness_score),
            "total_terms": total_terms,
            "unresolved_conflicts": conflicts
        }
