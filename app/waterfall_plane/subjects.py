from app.waterfall_plane.models import WaterfallSubjectRecord

def register_subject(subject_id: str, subject_type: str) -> WaterfallSubjectRecord:
    return WaterfallSubjectRecord(subject_id=subject_id, subject_type=subject_type)
