from app.semantic_plane.registry import CanonicalSemanticRegistry

class ContractSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def verify_payload_semantics(self, field_names: list[str]) -> list[str]:
        # Identify syntactically compatible but semantically undefined payload fields
        cautions = []
        registered_term_names = [t.name for t in self.registry.terms.values()]
        for field in field_names:
            if field not in registered_term_names:
                cautions.append(f"Caution: Contract field '{field}' lacks canonical semantic definition.")
        return cautions
