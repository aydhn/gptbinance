from typing import List, Optional
from app.adversarial_plane.models import CircumventionRecord

def create_circumvention(circumvention_id: str, bypass_type: str, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> CircumventionRecord:
    valid_types = {"control", "policy", "constitutional", "scope"}
    if bypass_type not in valid_types:
        raise ValueError(f"Invalid bypass type. Must be one of {valid_types}")
    return CircumventionRecord(
        circumvention_id=circumvention_id,
        bypass_type=bypass_type,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class CircumventionManager:
    def __init__(self):
        self._circumventions = {}

    def add_circumvention(self, circ: CircumventionRecord):
        self._circumventions[circ.circumvention_id] = circ

    def get_circumvention(self, circumvention_id: str) -> Optional[CircumventionRecord]:
        return self._circumventions.get(circumvention_id)

    def list_circumventions(self) -> List[CircumventionRecord]:
        return list(self._circumventions.values())
