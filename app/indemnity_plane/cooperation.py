from app.indemnity_plane.models import CooperationRecord
def evaluate_cooperation(indemnity_id: str, is_valid: bool) -> CooperationRecord:
    return CooperationRecord(indemnity_id=indemnity_id, is_valid=is_valid)
