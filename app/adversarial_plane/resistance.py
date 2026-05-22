from typing import List, Optional
from app.adversarial_plane.models import ResistanceRecord

def create_resistance(resistance_id: str, resistance_level: str, sufficiency_notes: str, lineage_refs: Optional[List[str]] = None) -> ResistanceRecord:
    valid_levels = {"strong", "brittle", "bypassable", "layered"}
    if resistance_level not in valid_levels:
        raise ValueError(f"Invalid resistance level. Must be one of {valid_levels}")
    return ResistanceRecord(
        resistance_id=resistance_id,
        resistance_level=resistance_level,
        sufficiency_notes=sufficiency_notes,
        lineage_refs=lineage_refs or []
    )

class ResistanceManager:
    def __init__(self):
        self._resistances = {}

    def add_resistance(self, res: ResistanceRecord):
        self._resistances[res.resistance_id] = res

    def get_resistance(self, resistance_id: str) -> Optional[ResistanceRecord]:
        return self._resistances.get(resistance_id)

    def list_resistances(self) -> List[ResistanceRecord]:
        return list(self._resistances.values())
