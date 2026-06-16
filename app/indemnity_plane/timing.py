from app.indemnity_plane.models import NoticeTimingRecord
def evaluate_timing(indemnity_id: str, is_timely: bool) -> NoticeTimingRecord:
    return NoticeTimingRecord(indemnity_id=indemnity_id, is_timely=is_timely)
