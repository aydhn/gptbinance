from app.indemnity_plane.models import PrejudiceRecord
def evaluate_prejudice(indemnity_id: str, has_prejudice: bool) -> PrejudiceRecord:
    return PrejudiceRecord(indemnity_id=indemnity_id, has_prejudice=has_prejudice)
