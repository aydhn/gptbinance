from typing import List, Dict, Any
from app.migration_plane.models import MigrationArtifactManifest

class ManifestBuilder:
    def build_manifest(self, migration_id: str, hash_value: str, lineage_refs: List[str], details: Dict[str, Any]) -> MigrationArtifactManifest:
         # Implementation for building manifests
        return MigrationArtifactManifest(
            migration_id=migration_id,
            hash_value=hash_value,
            lineage_refs=lineage_refs,
            details=details
        )
