from app.indemnity_plane.models import PartialIndemnityRecord
def evaluate_partials(indemnity_id: str, is_bounded: bool) -> PartialIndemnityRecord:
    return PartialIndemnityRecord(indemnity_id=indemnity_id, is_bounded=is_bounded)
