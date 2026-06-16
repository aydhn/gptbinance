from app.indemnity_plane.models import RecoupmentRecord
def evaluate_recoupment(indemnity_id: str, is_valid: bool) -> RecoupmentRecord:
    return RecoupmentRecord(indemnity_id=indemnity_id, is_valid=is_valid)
