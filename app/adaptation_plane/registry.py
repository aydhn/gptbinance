from typing import Dict, List, Optional
from app.adaptation_plane.models import AdaptationRecord
from app.adaptation_plane.enums import AdaptationClass
from app.adaptation_plane.exceptions import InvalidAdaptationObject

class RegistryManager:
    def __init__(self):
        self.adaptations: Dict[str, AdaptationRecord] = {}

    def register_adaptation(self, adaptation: AdaptationRecord) -> None:
        """Register a new adaptation into the canonical registry."""
        if not adaptation.adaptation_id:
            raise InvalidAdaptationObject("Adaptation ID must be specified.")

        if adaptation.adaptation_id in self.adaptations:
            raise InvalidAdaptationObject(f"Adaptation {adaptation.adaptation_id} already exists.")

        if not isinstance(adaptation.class_type, AdaptationClass):
            raise InvalidAdaptationObject(f"Invalid adaptation class: {adaptation.class_type}")

        self.adaptations[adaptation.adaptation_id] = adaptation

    def get_adaptation(self, adaptation_id: str) -> Optional[AdaptationRecord]:
        return self.adaptations.get(adaptation_id)

    def list_adaptations(self, class_type: Optional[AdaptationClass] = None) -> List[AdaptationRecord]:
        if class_type:
            return [a for a in self.adaptations.values() if a.class_type == class_type]
        return list(self.adaptations.values())

    def update_adaptation(self, adaptation_id: str, updated_record: AdaptationRecord) -> None:
        if adaptation_id not in self.adaptations:
            raise InvalidAdaptationObject(f"Adaptation {adaptation_id} not found.")

        # Historical truth overwrite koruması: ID ve Class değişemez
        existing = self.adaptations[adaptation_id]
        if existing.adaptation_id != updated_record.adaptation_id:
            raise InvalidAdaptationObject("Cannot overwrite adaptation ID.")
        if existing.class_type != updated_record.class_type:
            raise InvalidAdaptationObject("Cannot overwrite adaptation class.")

        self.adaptations[adaptation_id] = updated_record

    def evaluate(self, *args, **kwargs):
        return "evaluated"
