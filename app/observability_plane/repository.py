from typing import Any
from .storage import ObservabilityStorageEngine

class ObservabilityRepository:
    def __init__(self, storage: ObservabilityStorageEngine):
        self.storage = storage

    def save_manifest(self, manifest: Any) -> None:
        self.storage.write(f"manifest_{manifest.manifest_id}", manifest)

    def get_manifest(self, manifest_id: str) -> Any:
        return self.storage.read(f"manifest_{manifest_id}")
