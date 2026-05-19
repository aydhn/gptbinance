from typing import Dict, List, Optional
from app.federation_plane.models import FederationArtifactManifest
from app.federation_plane.exceptions import FederationPlaneError


class ManifestBuilder:
    def __init__(self):
        self._manifests: Dict[str, FederationArtifactManifest] = {}

    def build_manifest(self, manifest: FederationArtifactManifest):
        if not manifest.manifest_id:
            raise FederationPlaneError("Manifest ID required.")
        self._manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[FederationArtifactManifest]:
        return self._manifests.get(manifest_id)

    def list_manifests(self) -> List[FederationArtifactManifest]:
        return list(self._manifests.values())
