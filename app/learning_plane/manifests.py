from app.learning_plane.models import LearningArtifactManifest
from app.learning_plane.storage import storage
import hashlib

class ManifestBuilder:
    def build(self, learning_id: str) -> LearningArtifactManifest:
        obj = storage.get_object(learning_id)
        if not obj:
            raise ValueError("Learning object not found")

        hashes = {}
        for sig_id in obj.signal_ids:
             hashes[f"signal_{sig_id}"] = hashlib.sha256(sig_id.encode()).hexdigest()

        for lesson_id in obj.lesson_ids:
             hashes[f"lesson_{lesson_id}"] = hashlib.sha256(lesson_id.encode()).hexdigest()

        manifest = LearningArtifactManifest(
            manifest_id=f"manifest_{learning_id}",
            learning_id=learning_id,
            hashes=hashes
        )
        storage.save_manifest(manifest)
        return manifest
