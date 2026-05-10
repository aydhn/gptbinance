from typing import Dict, Optional
from app.incident_plane.models import IncidentManifest

class IncidentRepository:
    def __init__(self):
        self._store: Dict[str, IncidentManifest] = {}

    def save(self, manifest: IncidentManifest):
        self._store[manifest.incident_id] = manifest

    def get_manifest(self, incident_id: str) -> Optional[IncidentManifest]:
        return self._store.get(incident_id)
