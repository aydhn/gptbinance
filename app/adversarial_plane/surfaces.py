from typing import List, Optional
from app.adversarial_plane.models import AttackSurfaceRecord
from app.adversarial_plane.enums import SurfaceClass

def create_attack_surface(surface_id: str, surface_class: SurfaceClass, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> AttackSurfaceRecord:
    return AttackSurfaceRecord(
        surface_id=surface_id,
        surface_class=surface_class,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class AttackSurfaceManager:
    def __init__(self):
        self._surfaces = {}

    def add_surface(self, surf: AttackSurfaceRecord):
        self._surfaces[surf.surface_id] = surf

    def get_surface(self, surface_id: str) -> Optional[AttackSurfaceRecord]:
        return self._surfaces.get(surface_id)

    def list_surfaces(self) -> List[AttackSurfaceRecord]:
        return list(self._surfaces.values())
