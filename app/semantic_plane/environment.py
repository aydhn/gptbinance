from app.semantic_plane.registry import CanonicalSemanticRegistry

class EnvironmentSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def check_environment_semantics(self, env_label: str) -> str:
        # Prevent vague 'prod-like' labels without underlying semantics
        if env_label.lower() in ["prod-like", "staging-ish", "pre-prod"]:
            return "caution: ambiguous environment label detected. Lacks canonical meaning."
        return "trusted"
