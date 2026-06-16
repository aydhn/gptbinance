from app.waterfall_plane.models import ClaimantRecord

def register_claimant(claimant_id: str, claimant_type: str) -> ClaimantRecord:
    return ClaimantRecord(claimant_id=claimant_id, claimant_type=claimant_type)
