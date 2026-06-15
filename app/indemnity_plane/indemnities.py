from app.indemnity_plane.models import IndemnityRecord
def record_indemnity(indemnity_id: str, state: str) -> IndemnityRecord:
    return IndemnityRecord(indemnity_id=indemnity_id, state=state)
