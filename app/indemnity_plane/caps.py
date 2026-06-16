from app.indemnity_plane.models import CapRecord
def evaluate_caps(indemnity_id: str, is_bounded: bool) -> CapRecord:
    return CapRecord(indemnity_id=indemnity_id, is_bounded=is_bounded)
