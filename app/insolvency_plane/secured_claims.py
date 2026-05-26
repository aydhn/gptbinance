# secured_claims.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import SecuredClaimRecord

class SecuredClaimManager:
    def __init__(self):
        self.secured_claims: Dict[str, SecuredClaimRecord] = {}

    def add_secured_claim(self, claim: SecuredClaimRecord):
        self.secured_claims[claim.claim_id] = claim

    def get_secured_claim(self, claim_id: str) -> Optional[SecuredClaimRecord]:
        return self.secured_claims.get(claim_id)

    def list_secured_claims(self) -> List[SecuredClaimRecord]:
        return list(self.secured_claims.values())
