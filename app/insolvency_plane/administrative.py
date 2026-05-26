# administrative.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class AdministrativeClaimRecord(BaseModel):
    claim_id: str
    admin_type: str # post_petition, necessary_operations, contested
    description: str
    lineage_refs: List[str]

class AdministrativeClaimManager:
    def __init__(self):
        self.admin_claims: Dict[str, AdministrativeClaimRecord] = {}

    def add_administrative_claim(self, claim: AdministrativeClaimRecord):
        self.admin_claims[claim.claim_id] = claim

    def get_administrative_claim(self, claim_id: str) -> Optional[AdministrativeClaimRecord]:
        return self.admin_claims.get(claim_id)

    def list_administrative_claims(self) -> List[AdministrativeClaimRecord]:
        return list(self.admin_claims.values())
