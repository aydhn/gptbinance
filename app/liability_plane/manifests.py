import uuid
from typing import Dict
from app.liability_plane.models import LiabilityArtifactManifest
from app.liability_plane.repository import LiabilityRepository

class ManifestManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def create_manifest(self, liability_id: str, hashes: Dict[str, str]) -> LiabilityArtifactManifest:
        return LiabilityArtifactManifest(
            manifest_id=str(uuid.uuid4()),
            liability_id=liability_id,
            hashes=hashes
        )
