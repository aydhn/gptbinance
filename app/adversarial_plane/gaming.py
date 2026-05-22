from typing import List, Optional
from app.adversarial_plane.models import GamingRecord
from app.adversarial_plane.enums import GamingClass

def create_gaming(gaming_id: str, gaming_class: GamingClass, caveats: str, lineage_refs: Optional[List[str]] = None) -> GamingRecord:
    return GamingRecord(
        gaming_id=gaming_id,
        gaming_class=gaming_class,
        caveats=caveats,
        lineage_refs=lineage_refs or []
    )

class GamingManager:
    def __init__(self):
        self._gaming_records = {}

    def add_gaming(self, gam: GamingRecord):
        self._gaming_records[gam.gaming_id] = gam

    def get_gaming(self, gaming_id: str) -> Optional[GamingRecord]:
        return self._gaming_records.get(gaming_id)

    def list_gaming_records(self) -> List[GamingRecord]:
        return list(self._gaming_records.values())
