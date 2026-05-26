# claims.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import ClaimRecord
from app.insolvency_plane.enums import ClaimClass

class ClaimManager:
    def __init__(self):
        self.claims: Dict[str, ClaimRecord] = {}

    def file_claim(self, claim: ClaimRecord):
        self.claims[claim.claim_id] = claim

    def get_claim(self, claim_id: str) -> Optional[ClaimRecord]:
        return self.claims.get(claim_id)

    def list_claims(self) -> List[ClaimRecord]:
        return list(self.claims.values())

    def get_claims_by_estate(self, estate_id: str) -> List[ClaimRecord]:
        return [c for c in self.claims.values() if c.estate_id == estate_id]
