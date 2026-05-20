from app.semantic_plane.registry import CanonicalSemanticRegistry

class TemporalSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def validate_admissibility_semantics(self, status: str) -> bool:
        valid_semantics = ["fresh", "stale", "expired", "admissible", "degraded_admissible"]
        return status in valid_semantics
