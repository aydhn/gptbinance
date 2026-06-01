from typing import List, Optional
from app.adaptation_plane.models import CountermeasureRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidCountermeasure

class CountermeasuresManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def add_countermeasure(self, adaptation_id: str, countermeasure: CountermeasureRecord) -> None:
        """Add a countermeasure to a corrective package of an adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidCountermeasure(f"Adaptation {adaptation_id} not found.")

        if not adaptation.corrective_package:
            raise InvalidCountermeasure("Cannot add countermeasure without an existing Corrective Package.")

        # Duplicate kontrolü
        existing_ids = [cm.countermeasure_id for cm in adaptation.corrective_package.countermeasures]
        if countermeasure.countermeasure_id in existing_ids:
            raise InvalidCountermeasure(f"Countermeasure {countermeasure.countermeasure_id} already exists.")

        adaptation.corrective_package.countermeasures.append(countermeasure)
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
