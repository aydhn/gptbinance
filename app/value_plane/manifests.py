from typing import Dict, List, Optional
from app.value_plane.models import ValueArtifactManifest

class ManifestRegistry:
    def __init__(self):
        self._records: Dict[str, ValueArtifactManifest] = {}

    def register(self, record: ValueArtifactManifest):
        self._records[record.manifest_id] = record

    def get(self, record_id: str) -> Optional[ValueArtifactManifest]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueArtifactManifest]:
        return list(self._records.values())

manifest_registry = ManifestRegistry()
