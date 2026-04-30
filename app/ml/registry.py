from app.ml.models import ModelRegistryEntry
from app.ml.enums import RegistryStage, ModelStatus


class ModelRegistry:
    def __init__(self):
        self.entries = {}

    def register(self, entry: ModelRegistryEntry):
        self.entries[entry.run_id] = entry

    def get(self, run_id: str) -> ModelRegistryEntry:
        return self.entries.get(run_id)
