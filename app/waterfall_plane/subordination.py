from app.waterfall_plane.models import SubordinationRecord

def register_subordination(subordination_id: str, subordinated_to: str) -> SubordinationRecord:
    return SubordinationRecord(subordination_id=subordination_id, subordinated_to=subordinated_to)
