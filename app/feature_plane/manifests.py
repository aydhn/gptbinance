from typing import Dict, Optional
from app.feature_plane.models import FeatureManifest


class ManifestManager:
    def __init__(self):
        self._manifests: Dict[str, FeatureManifest] = {}

    def store(self, manifest: FeatureManifest):
        self._manifests[manifest.manifest_id] = manifest

    def get(self, manifest_id: str) -> Optional[FeatureManifest]:
        return self._manifests.get(manifest_id)
