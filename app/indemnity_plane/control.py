from app.indemnity_plane.models import DefenseControlRecord
def evaluate_control(indemnity_id: str, is_clean: bool) -> DefenseControlRecord:
    return DefenseControlRecord(indemnity_id=indemnity_id, is_clean=is_clean)
