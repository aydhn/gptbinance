from app.indemnity_plane.models import ConsentConflictRecord
def evaluate_conflicts(indemnity_id: str, has_conflict: bool) -> ConsentConflictRecord:
    return ConsentConflictRecord(indemnity_id=indemnity_id, has_conflict=has_conflict)
