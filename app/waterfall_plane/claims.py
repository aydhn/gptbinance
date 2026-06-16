from typing import Optional
from app.waterfall_plane.models import ClaimRecord
from app.waterfall_plane.enums import ClaimClass

def register_claim(claim_id: str, waterfall_id: str, claim_class: ClaimClass, amount: float) -> ClaimRecord:
    return ClaimRecord(
        claim_id=claim_id,
        waterfall_id=waterfall_id,
        claim_class=claim_class,
        amount=amount
    )
