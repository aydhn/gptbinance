# subordination.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class SubordinatedClaimRecord(BaseModel):
    claim_id: str
    subordination_type: str # contractual, structural, equitable, invalid
    description: str
    lineage_refs: List[str]

class SubordinationManager:
    def __init__(self):
        self.subordinated_claims: Dict[str, SubordinatedClaimRecord] = {}

    def add_subordinated_claim(self, claim: SubordinatedClaimRecord):
        self.subordinated_claims[claim.claim_id] = claim

    def get_subordinated_claim(self, claim_id: str) -> Optional[SubordinatedClaimRecord]:
        return self.subordinated_claims.get(claim_id)

    def list_subordinated_claims(self) -> List[SubordinatedClaimRecord]:
        return list(self.subordinated_claims.values())
