from typing import Optional
from app.adaptation_plane.models import RootCauseHypothesisRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidRootCauseHypothesis

class HypothesesManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def attach_hypothesis(self, adaptation_id: str, hypothesis: RootCauseHypothesisRecord) -> None:
        """Attach a root cause hypothesis to an existing adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidRootCauseHypothesis(f"Adaptation {adaptation_id} not found.")

        # Historical truth overwrite koruması
        if adaptation.hypothesis:
            raise InvalidRootCauseHypothesis("Hypothesis already exists for this adaptation. Historical overwrite is forbidden.")

        adaptation.hypothesis = hypothesis
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
