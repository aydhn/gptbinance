from app.indemnity_plane.models import IndemnityComparisonRecord
def evaluate_comparisons(comparison_type: str, is_comparable: bool) -> IndemnityComparisonRecord:
    return IndemnityComparisonRecord(comparison_type=comparison_type, is_comparable=is_comparable)
