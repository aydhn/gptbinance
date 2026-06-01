from typing import Dict, Optional
from app.adaptation_plane.models import AdaptationRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidAdaptationObject

class ObjectsManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def create_object(self, adaptation: AdaptationRecord) -> None:
        """Create a new adaptation object and register it."""
        adaptation.status = "proposed"
        self.registry.register_adaptation(adaptation)

    def transition_status(self, adaptation_id: str, new_status: str) -> None:
        """Transition the lifecycle state of an adaptation object."""
        valid_statuses = ["proposed", "deployed", "verified", "failed"]
        if new_status not in valid_statuses:
            raise InvalidAdaptationObject(f"Invalid status: {new_status}")

        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidAdaptationObject(f"Adaptation {adaptation_id} not found.")

        adaptation.status = new_status
        self.registry.update_adaptation(adaptation_id, adaptation)

    def get_object(self, adaptation_id: str) -> Optional[AdaptationRecord]:
        return self.registry.get_adaptation(adaptation_id)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
