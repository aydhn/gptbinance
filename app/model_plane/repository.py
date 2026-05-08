from typing import Optional
from app.model_plane.storage import ModelPlaneStorage
from app.model_plane.models import (
    ModelDefinition,
    ModelCheckpointRecord,
    InferenceManifest,
    InferenceContract,
)


class ModelPlaneRepository:
    def __init__(self, storage: ModelPlaneStorage):
        self.storage = storage

    def save_model(self, model: ModelDefinition) -> None:
        self.storage.save("models", model.model_id, model)

    def get_model(self, model_id: str) -> Optional[ModelDefinition]:
        try:
            return self.storage.load("models", model_id, ModelDefinition)
        except FileNotFoundError:
            return None

    def save_checkpoint(self, checkpoint: ModelCheckpointRecord) -> None:
        self.storage.save("checkpoints", checkpoint.checkpoint_id, checkpoint)

    def get_checkpoint(self, checkpoint_id: str) -> Optional[ModelCheckpointRecord]:
        try:
            return self.storage.load(
                "checkpoints", checkpoint_id, ModelCheckpointRecord
            )
        except FileNotFoundError:
            return None

    def save_manifest(self, manifest: InferenceManifest) -> None:
        self.storage.save("manifests", manifest.manifest_id, manifest)

    def save_contract(self, contract: InferenceContract) -> None:
        self.storage.save("contracts", contract.contract_id, contract)
