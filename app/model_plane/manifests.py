from typing import Dict, Optional, List
from app.model_plane.models import InferenceManifest, InferenceManifestEntry
from app.model_plane.exceptions import ModelPlaneError


class InferenceManifestBuilder:
    def __init__(self):
        self._manifests: Dict[str, InferenceManifest] = {}

    def store_manifest(self, manifest: InferenceManifest) -> None:
        if not manifest.manifest_id:
            raise ModelPlaneError("Manifest ID is required.")
        if not manifest.entries:
            raise ModelPlaneError("Manifest must have at least one entry.")
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[InferenceManifest]:
        return self._manifests.get(manifest_id)

    def list_manifests(self) -> List[InferenceManifest]:
        return list(self._manifests.values())
