from typing import Optional
from app.adaptation_plane.models import CorrectivePackageRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidAdaptationObject

class PackagesManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def create_package(self, adaptation_id: str, package: CorrectivePackageRecord) -> None:
        """Create a new corrective package for an adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidAdaptationObject(f"Adaptation {adaptation_id} not found.")

        # Historical truth overwrite koruması
        if adaptation.corrective_package:
            raise InvalidAdaptationObject("Corrective Package already exists for this adaptation.")

        adaptation.corrective_package = package
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
