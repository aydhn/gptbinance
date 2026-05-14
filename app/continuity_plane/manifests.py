from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityArtifactManifest

class ContinuityManifestBuilder:
    def __init__(self):
        self._manifests: Dict[str, ContinuityArtifactManifest] = {}

    def record_manifest(self, manifest: ContinuityArtifactManifest) -> None:
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[ContinuityArtifactManifest]:
        return self._manifests.get(manifest_id)
