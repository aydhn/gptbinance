from app.indemnity_plane.models import AdvancementRecord
def evaluate_advancement(indemnity_id: str, is_valid: bool) -> AdvancementRecord:
    return AdvancementRecord(indemnity_id=indemnity_id, is_valid=is_valid)
