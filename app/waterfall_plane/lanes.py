from app.waterfall_plane.models import ClaimLaneRecord

def register_lane(lane_id: str, lane_type: str) -> ClaimLaneRecord:
    return ClaimLaneRecord(lane_id=lane_id, lane_type=lane_type)
