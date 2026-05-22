from typing import List, Optional
from app.adversarial_plane.models import PoisoningRecord
from app.adversarial_plane.enums import PoisoningClass

def create_poisoning(poisoning_id: str, poisoning_class: PoisoningClass, proof_notes: str, lineage_refs: Optional[List[str]] = None) -> PoisoningRecord:
    return PoisoningRecord(
        poisoning_id=poisoning_id,
        poisoning_class=poisoning_class,
        proof_notes=proof_notes,
        lineage_refs=lineage_refs or []
    )

class PoisoningManager:
    def __init__(self):
        self._poisoning_records = {}

    def add_poisoning(self, poi: PoisoningRecord):
        self._poisoning_records[poi.poisoning_id] = poi

    def get_poisoning(self, poisoning_id: str) -> Optional[PoisoningRecord]:
        return self._poisoning_records.get(poisoning_id)

    def list_poisoning_records(self) -> List[PoisoningRecord]:
        return list(self._poisoning_records.values())
