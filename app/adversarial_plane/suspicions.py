from typing import List, Optional
from app.adversarial_plane.models import SuspicionRecord
from app.adversarial_plane.enums import SuspicionClass

def create_suspicion(suspicion_id: str, suspicion_class: SuspicionClass, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> SuspicionRecord:
    return SuspicionRecord(
        suspicion_id=suspicion_id,
        suspicion_class=suspicion_class,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class SuspicionManager:
    def __init__(self):
        self._suspicions = {}

    def add_suspicion(self, susp: SuspicionRecord):
        self._suspicions[susp.suspicion_id] = susp

    def get_suspicion(self, suspicion_id: str) -> Optional[SuspicionRecord]:
        return self._suspicions.get(suspicion_id)

    def list_suspicions(self) -> List[SuspicionRecord]:
        return list(self._suspicions.values())
