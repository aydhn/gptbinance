from app.indemnity_plane.models import CoverageRecord
def evaluate_coverage(indemnity_id: str, coverage_class: str) -> CoverageRecord:
    return CoverageRecord(indemnity_id=indemnity_id, coverage_class=coverage_class)
