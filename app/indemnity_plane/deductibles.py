from app.indemnity_plane.models import DeductibleRecord
def evaluate_deductibles(indemnity_id: str, has_deductible: bool) -> DeductibleRecord:
    return DeductibleRecord(indemnity_id=indemnity_id, has_deductible=has_deductible)
