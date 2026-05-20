from typing import Dict, List, Optional
from app.semantic_plane.models import TermRecord
from app.semantic_plane.enums import TermClass

class TermManager:
    def __init__(self, registry):
        self.registry = registry

    def register_term(self, term: TermRecord):
        self.registry.register_term(term)

    def get_canonical_terms(self) -> List[TermRecord]:
        return [t for t in self.registry.terms.values() if t.term_class == TermClass.CANONICAL]

    def check_for_overloaded_terms(self) -> List[TermRecord]:
        return [t for t in self.registry.terms.values() if t.term_class == TermClass.OVERLOADED]
