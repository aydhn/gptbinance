from app.assurance_plane.models import SurveillanceFindingRecord

def create_finding(finding_id: str, assurance_id: str, finding_type: str, is_clean: bool) -> SurveillanceFindingRecord:
    return SurveillanceFindingRecord(
        finding_id=finding_id,
        assurance_id=assurance_id,
        finding_type=finding_type,
        is_clean=is_clean
    )
