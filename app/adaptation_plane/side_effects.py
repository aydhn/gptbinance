from typing import List
from app.adaptation_plane.models import SideEffectRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import AdaptationPlaneError

class SideEffectsManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def register_side_effect(self, adaptation_id: str, side_effect: SideEffectRecord) -> None:
        """Register a new side effect for an adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise AdaptationPlaneError(f"Adaptation {adaptation_id} not found.")

        existing_ids = [se.side_effect_id for se in adaptation.side_effects]
        if side_effect.side_effect_id in existing_ids:
            raise AdaptationPlaneError(f"Side effect {side_effect.side_effect_id} already exists.")

        adaptation.side_effects.append(side_effect)
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
