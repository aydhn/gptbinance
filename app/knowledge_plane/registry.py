from typing import List, Dict, Optional
from .models import KnowledgeObject
from .exceptions import InvalidKnowledgeObject
from .enums import KnowledgeClass

class CanonicalKnowledgeRegistry:
    def __init__(self):
        self._objects: Dict[str, KnowledgeObject] = {}

    def register(self, obj: KnowledgeObject):
        if not obj.knowledge_id:
            raise InvalidKnowledgeObject("knowledge_id is required.")
        if not obj.knowledge_class:
            raise InvalidKnowledgeObject("knowledge_class is required.")
        if obj.knowledge_class not in [c.value for c in KnowledgeClass]:
            raise InvalidKnowledgeObject(f"Invalid knowledge class: {obj.knowledge_class}")
        self._objects[obj.knowledge_id] = obj

    def get(self, knowledge_id: str) -> Optional[KnowledgeObject]:
        return self._objects.get(knowledge_id)

    def get_all(self) -> List[KnowledgeObject]:
        return list(self._objects.values())

    def get_by_class(self, knowledge_class: str) -> List[KnowledgeObject]:
        return [obj for obj in self._objects.values() if obj.knowledge_class == knowledge_class]

    def get_authoritative(self) -> List[KnowledgeObject]:
        return [obj for obj in self._objects.values() if obj.authoritative]
