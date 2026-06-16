from app.indemnity_plane.models import IndemnifiedClaimRecord
def record_claim(indemnity_id: str, claim_type: str) -> IndemnifiedClaimRecord:
    return IndemnifiedClaimRecord(indemnity_id=indemnity_id, claim_type=claim_type)
