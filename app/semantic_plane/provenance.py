from app.semantic_plane.registry import CanonicalSemanticRegistry

class ProvenanceSemanticManager:
    def __init__(self, registry: CanonicalSemanticRegistry):
        self.registry = registry

    def check_attribution_semantics(self, claim_type: str) -> str:
        # Differentiate primary cause vs contributing factor semantics
        if claim_type not in ["primary_cause", "contributing_factor"]:
             return "Caution: Provenance claim uses ambiguous attribution semantics."
        return "trusted"
