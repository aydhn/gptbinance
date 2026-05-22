from typing import Dict, List, Optional
from app.adversarial_plane.models import AdversarialObject
from app.adversarial_plane.base import AdversarialRegistryBase
from app.adversarial_plane.exceptions import InvalidAdversarialObjectError

class CanonicalAdversarialRegistry(AdversarialRegistryBase):
    def __init__(self):
        self._registry: Dict[str, AdversarialObject] = {}

    def register(self, obj: AdversarialObject) -> None:
        if not obj.adversarial_id:
            raise InvalidAdversarialObjectError("Adversarial object must have an ID.")
        self._registry[obj.adversarial_id] = obj

    def get(self, adversarial_id: str) -> Optional[AdversarialObject]:
        return self._registry.get(adversarial_id)

    def list_all(self) -> List[AdversarialObject]:
        return list(self._registry.values())

    def get_by_class(self, adv_class: str) -> List[AdversarialObject]:
        return [obj for obj in self._registry.values() if obj.adversarial_class == adv_class]
