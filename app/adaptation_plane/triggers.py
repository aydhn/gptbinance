from typing import Optional
from app.adaptation_plane.models import AdaptationTriggerRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidAdaptationObject

class TriggersManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def attach_trigger(self, adaptation_id: str, trigger: AdaptationTriggerRecord) -> None:
        """Attach a trigger to an existing adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidAdaptationObject(f"Adaptation {adaptation_id} not found.")

        # Historical truth overwrite koruması
        if adaptation.trigger:
            raise InvalidAdaptationObject("Trigger already exists for this adaptation. Historical overwrite is forbidden.")

        adaptation.trigger = trigger
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
