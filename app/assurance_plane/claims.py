from app.assurance_plane.models import AssuranceClaimRecord
from app.assurance_plane.enums import ClaimClass

def create_claim(claim_id: str, assurance_id: str, claim_class: ClaimClass, description: str) -> AssuranceClaimRecord:
    return AssuranceClaimRecord(
        claim_id=claim_id,
        assurance_id=assurance_id,
        claim_class=claim_class,
        description=description
    )
