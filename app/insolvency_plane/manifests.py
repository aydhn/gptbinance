# manifests.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyArtifactManifest

class InsolvencyManifestManager:
    def __init__(self):
        self.manifests: Dict[str, InsolvencyArtifactManifest] = {}

    def register_manifest(self, manifest: InsolvencyArtifactManifest):
        self.manifests[manifest.manifest_id] = manifest

    def get_manifest(self, manifest_id: str) -> Optional[InsolvencyArtifactManifest]:
        return self.manifests.get(manifest_id)

    def list_manifests(self) -> List[InsolvencyArtifactManifest]:
        return list(self.manifests.values())
