from app.ml.models import ModelRegistryEntry
from app.ml.enums import RegistryStage, ModelStatus


class ModelRegistry:
    def __init__(self):
        self.entries = {}

    def register(self, entry: ModelRegistryEntry):
        self.entries[entry.run_id] = entry

    def get(self, run_id: str) -> ModelRegistryEntry:
        return self.entries.get(run_id)

    # Phase 21 additions
    def get_stage_refs(self, stage: str) -> list:
        # Mock for returning models linked to a stage
        return []

    # Phase 22 Analytics hook
    def get_analytics_refs(self) -> dict:
        return {
            "active_models": self.entries,
            "drift_reports": [],  # Mock
            "calibration_refs": [],  # Mock
        }
