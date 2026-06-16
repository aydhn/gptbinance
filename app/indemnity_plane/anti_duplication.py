from app.indemnity_plane.models import AntiDuplicationRecord
def evaluate_anti_duplication(indemnity_id: str, is_clean: bool) -> AntiDuplicationRecord:
    return AntiDuplicationRecord(indemnity_id=indemnity_id, is_clean=is_clean)
