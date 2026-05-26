# objections.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class ClaimObjectionRecord(BaseModel):
    objection_id: str
    claim_id: str
    objection_type: str # scope, valuation, priority, timeliness
    description: str
    lineage_refs: List[str]

class ClaimObjectionManager:
    def __init__(self):
        self.objections: Dict[str, ClaimObjectionRecord] = {}

    def object_to_claim(self, objection: ClaimObjectionRecord):
        self.objections[objection.objection_id] = objection

    def get_objection(self, objection_id: str) -> Optional[ClaimObjectionRecord]:
        return self.objections.get(objection_id)

    def list_objections(self) -> List[ClaimObjectionRecord]:
        return list(self.objections.values())
