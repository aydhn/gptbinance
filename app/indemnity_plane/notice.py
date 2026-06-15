from app.indemnity_plane.models import NoticeRecord
def record_notice(indemnity_id: str, notice_class: str) -> NoticeRecord:
    return NoticeRecord(indemnity_id=indemnity_id, notice_class=notice_class)
