from app.indemnity_plane.models import FailedIndemnityRecord
def evaluate_failed(indemnity_id: str, has_failure: bool) -> FailedIndemnityRecord:
    return FailedIndemnityRecord(indemnity_id=indemnity_id, has_failure=has_failure)
