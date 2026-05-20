# Stub for manifests logic
from app.semantic_plane.models import SemanticArtifactManifest
import hashlib

class ManifestBuilder:
    def build(self, semantic_id: str) -> SemanticArtifactManifest:
        h = hashlib.sha256(semantic_id.encode()).hexdigest()
        return SemanticArtifactManifest(
            manifest_id=f"man_{semantic_id}",
            semantic_id=semantic_id,
            hash=h
        )
