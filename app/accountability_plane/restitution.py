
from app.accountability_plane.exceptions import RestitutionGapError
from app.accountability_plane.models import RestitutionBurdenRecord

class RestitutionManager:
    def __init__(self):
        self._store = {}

    def assign_restitution(self, restitution_id: str, breach_ref: str) -> RestitutionBurdenRecord:
        record = RestitutionBurdenRecord(
            restitution_id=restitution_id,
            breach_ref=breach_ref,
            is_resolved=False
        )
        self._store[restitution_id] = record
        return record

    def mark_resolved(self, restitution_id: str, evidence: str):
        record = self._store.get(restitution_id)
        if not record:
            raise RestitutionGapError("Cannot resolve unknown restitution.")
        if not evidence:
            raise RestitutionGapError("Cannot resolve restitution without evidence.")
        record.is_resolved = True
        return record
