from app.allocation.storage import AllocationStorage
from app.allocation.models import AllocationManifest


class AllocationRepository:
    def __init__(self, storage: AllocationStorage):
        self.storage = storage

    def save_manifest(self, manifest: AllocationManifest):
        self.storage.save(f"manifest_{manifest.manifest_id}", manifest.model_dump())
        self.storage.save("latest_manifest", manifest.model_dump())

    def get_latest_manifest(self) -> AllocationManifest:
        data = self.storage.load("latest_manifest")
        if data:
            return AllocationManifest(**data)
        return None
