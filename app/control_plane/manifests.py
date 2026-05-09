import uuid
from app.control_plane.models import ControlArtifactManifest


class ManifestBuilder:
    def build_manifest(
        self, action_id: str, receipt_id: str, hashes: dict
    ) -> ControlArtifactManifest:
        return ControlArtifactManifest(
            manifest_id=f"MNF-{uuid.uuid4().hex[:8]}",
            action_id=action_id,
            receipt_id=receipt_id,
            hashes=hashes,
        )
