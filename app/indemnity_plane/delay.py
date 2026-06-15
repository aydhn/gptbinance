from app.indemnity_plane.models import ReimbursementDelayRecord
def evaluate_delay(indemnity_id: str, has_delay: bool) -> ReimbursementDelayRecord:
    return ReimbursementDelayRecord(indemnity_id=indemnity_id, has_delay=has_delay)
