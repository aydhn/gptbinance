from app.commitment_plane.models import CommitmentArtifactManifest, CommitmentObjectRef
from typing import List, Dict

class ManifestBuilder:
    @staticmethod
    def build_manifest(manifest_id: str, commitments: List[CommitmentObjectRef], hashes: Dict[str, str]) -> CommitmentArtifactManifest:
        return CommitmentArtifactManifest(
            manifest_id=manifest_id,
            commitments=commitments,
            hashes=hashes
        )
