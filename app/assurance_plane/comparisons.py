from app.assurance_plane.models import AssuranceComparisonRecord

def create_comparison(comp_id: str, src_id: str, tgt_id: str, notes: str) -> AssuranceComparisonRecord:
    return AssuranceComparisonRecord(
        comparison_id=comp_id,
        source_assurance_id=src_id,
        target_assurance_id=tgt_id,
        notes=notes
    )
