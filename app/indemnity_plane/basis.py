from app.indemnity_plane.models import IndemnityBasisRecord
def evaluate_basis(indemnity_id: str, is_sufficient: bool) -> IndemnityBasisRecord:
    return IndemnityBasisRecord(indemnity_id=indemnity_id, is_sufficient=is_sufficient)
