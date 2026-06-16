from app.indemnity_plane.models import IndemnifiedSubjectRecord
def record_subject(indemnity_id: str, subject_type: str) -> IndemnifiedSubjectRecord:
    return IndemnifiedSubjectRecord(indemnity_id=indemnity_id, subject_type=subject_type)
