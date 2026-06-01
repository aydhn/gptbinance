from typing import Optional
from app.adaptation_plane.models import VerificationWindowRecord
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidVerificationWindow

class VerificationManager:
    def __init__(self, registry: RegistryManager):
        self.registry = registry

    def register_window(self, adaptation_id: str, window: VerificationWindowRecord) -> None:
        """Register a verification window for an adaptation."""
        adaptation = self.registry.get_adaptation(adaptation_id)
        if not adaptation:
            raise InvalidVerificationWindow(f"Adaptation {adaptation_id} not found.")

        if adaptation.verification:
            raise InvalidVerificationWindow("Verification window already exists. Historical overwrite forbidden.")

        # Sadece deployed durumda olanlar verification'a girebilir
        if adaptation.status != "deployed":
            raise InvalidVerificationWindow(f"Adaptation must be deployed, not {adaptation.status}.")

        adaptation.verification = window
        self.registry.update_adaptation(adaptation_id, adaptation)

    def evaluate(self, *args, **kwargs):
        return "evaluated"
