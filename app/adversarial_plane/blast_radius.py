from typing import List, Optional
from app.adversarial_plane.models import BlastRadiusRecord

def create_blast_radius(blast_radius_id: str, radius_level: str, hidden_notes: str, lineage_refs: Optional[List[str]] = None) -> BlastRadiusRecord:
    valid_levels = {"local", "federated", "delayed", "hidden"}
    if radius_level not in valid_levels:
        raise ValueError(f"Invalid radius level. Must be one of {valid_levels}")
    return BlastRadiusRecord(
        blast_radius_id=blast_radius_id,
        radius_level=radius_level,
        hidden_notes=hidden_notes,
        lineage_refs=lineage_refs or []
    )

class BlastRadiusManager:
    def __init__(self):
        self._blast_radii = {}

    def add_blast_radius(self, br: BlastRadiusRecord):
        self._blast_radii[br.blast_radius_id] = br

    def get_blast_radius(self, blast_radius_id: str) -> Optional[BlastRadiusRecord]:
        return self._blast_radii.get(blast_radius_id)

    def list_blast_radii(self) -> List[BlastRadiusRecord]:
        return list(self._blast_radii.values())
