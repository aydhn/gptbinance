from app.indemnity_plane.models import SubrogationRecord
def evaluate_subrogation(indemnity_id: str, is_valid: bool) -> SubrogationRecord:
    return SubrogationRecord(indemnity_id=indemnity_id, is_valid=is_valid)
