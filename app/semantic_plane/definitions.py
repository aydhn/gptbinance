from typing import Dict, List
from app.semantic_plane.models import CanonicalDefinitionRecord
from app.semantic_plane.exceptions import InvalidDefinitionError

class CanonicalDefinitionManager:
    def __init__(self, registry):
        self.registry = registry
        self.definitions: Dict[str, CanonicalDefinitionRecord] = {}

    def register_definition(self, definition: CanonicalDefinitionRecord):
        if not definition.authoritative_text:
            raise InvalidDefinitionError("Definition must have authoritative text")
        self.definitions[definition.definition_id] = definition
