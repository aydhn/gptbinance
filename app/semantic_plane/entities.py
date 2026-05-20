from typing import List, Dict
from app.semantic_plane.models import EntityRecord

class EntityManager:
    def __init__(self, registry):
        self.registry = registry

    def register_entity(self, entity: EntityRecord):
        self.registry.register_entity(entity)

    def get_entities_with_boundary_notes(self) -> List[EntityRecord]:
        return [e for e in self.registry.entities.values() if e.boundary_notes]
