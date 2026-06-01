from typing import Optional
from app.adaptation_plane.models import FitnessRestorationRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidFitnessRestoration

class FitnessManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def restore_fitness(self, adaptation_id: str, fitness: FitnessRestorationRecord) -> None:
        """Register fitness restoration state for an adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidFitnessRestoration(f"Adaptation {adaptation_id} not found.")

        if not adaptation.verification:
            raise InvalidFitnessRestoration("Cannot claim fitness restored without a Verification Window.")

        if adaptation.fitness:
            raise InvalidFitnessRestoration("Fitness restoration already recorded. Historical overwrite forbidden.")

        adaptation.fitness = fitness

        # Fitness restoration status update
        adaptation.status = "verified"
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
