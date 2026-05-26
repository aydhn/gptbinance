# priority_claims.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import PriorityClaimRecord

class PriorityClaimManager:
    def __init__(self):
        self.priority_claims: Dict[str, PriorityClaimRecord] = {}

    def add_priority_claim(self, claim: PriorityClaimRecord):
        self.priority_claims[claim.claim_id] = claim

    def get_priority_claim(self, claim_id: str) -> Optional[PriorityClaimRecord]:
        return self.priority_claims.get(claim_id)

    def list_priority_claims(self) -> List[PriorityClaimRecord]:
        return list(self.priority_claims.values())
