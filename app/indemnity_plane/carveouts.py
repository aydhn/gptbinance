from app.indemnity_plane.models import CarveOutRecord
def evaluate_carveout(indemnity_id: str, is_clear: bool) -> CarveOutRecord:
    return CarveOutRecord(indemnity_id=indemnity_id, is_clear=is_clear)
