# unsecured_claims.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class UnsecuredClaimRecord(BaseModel):
    claim_id: str
    unsecured_type: str # general, deficiency, disputed
    description: str
    lineage_refs: List[str]

class UnsecuredClaimManager:
    def __init__(self):
        self.unsecured_claims: Dict[str, UnsecuredClaimRecord] = {}

    def add_unsecured_claim(self, claim: UnsecuredClaimRecord):
        self.unsecured_claims[claim.claim_id] = claim

    def get_unsecured_claim(self, claim_id: str) -> Optional[UnsecuredClaimRecord]:
        return self.unsecured_claims.get(claim_id)

    def list_unsecured_claims(self) -> List[UnsecuredClaimRecord]:
        return list(self.unsecured_claims.values())
