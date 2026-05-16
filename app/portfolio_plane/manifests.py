from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioArtifactManifest
from app.portfolio_plane.exceptions import PortfolioStorageError

class ManifestManager:
    def __init__(self):
        self._manifests: Dict[str, PortfolioArtifactManifest] = {}

    def register(self, manifest: PortfolioArtifactManifest):
        if manifest.manifest_id in self._manifests:
            raise PortfolioStorageError(f"Manifest {manifest.manifest_id} already exists")
        self._manifests[manifest.manifest_id] = manifest

    def get(self, manifest_id: str) -> Optional[PortfolioArtifactManifest]:
        return self._manifests.get(manifest_id)

    def get_all(self) -> Dict[str, PortfolioArtifactManifest]:
        return self._manifests.copy()
