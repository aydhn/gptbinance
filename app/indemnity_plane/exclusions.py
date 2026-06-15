from app.indemnity_plane.models import ExclusionRecord
def evaluate_exclusion(indemnity_id: str, exclusion_class: str) -> ExclusionRecord:
    return ExclusionRecord(indemnity_id=indemnity_id, exclusion_class=exclusion_class)
