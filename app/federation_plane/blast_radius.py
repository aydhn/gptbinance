from typing import Dict, List, Optional
from app.federation_plane.models import BlastRadiusRecord
from app.federation_plane.exceptions import FederationPlaneError


class BlastRadiusManager:
    def __init__(self):
        self._records: Dict[str, BlastRadiusRecord] = {}

    def register(self, record: BlastRadiusRecord):
        if not record.blast_id:
            raise FederationPlaneError("No invisible shared fallout allowed.")
        self._records[record.blast_id] = record

    def get_blast_radius(self, blast_id: str) -> Optional[BlastRadiusRecord]:
        return self._records.get(blast_id)

    def list_blast_radii(self) -> List[BlastRadiusRecord]:
        return list(self._records.values())
