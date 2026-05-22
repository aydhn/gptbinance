from app.precedent_plane.models import ConflictRecord
from app.precedent_plane.enums import ConflictClass
from typing import List

class ConflictsManager:
    def __init__(self):
        self.records: List[ConflictRecord] = []

    def register_conflict(self, precedent_id_a: str, precedent_id_b: str, conflict_class: ConflictClass, proof_notes: str):
        record = ConflictRecord(
            conflict_id=f"C-{len(self.records)+1}",
            precedent_id_a=precedent_id_a,
            precedent_id_b=precedent_id_b,
            conflict_class=conflict_class,
            proof_notes=proof_notes
        )
        self.records.append(record)
        return record

    def get_unresolved_conflicts(self):
        return [c for c in self.records if not c.resolved]
