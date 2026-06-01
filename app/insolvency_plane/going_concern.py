# going_concern.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class GoingConcernRecord(BaseModel):
    concern_id: str
    description: str
    status: str # preserved, provisional, failed, misleading
    lineage_refs: List[str]

class GoingConcernManager:
    def __init__(self):
        self.concerns: Dict[str, GoingConcernRecord] = {}

    def register_going_concern(self, concern: GoingConcernRecord):
        self.concerns[concern.concern_id] = concern

    def get_going_concern(self, concern_id: str) -> Optional[GoingConcernRecord]:
        return self.concerns.get(concern_id)

    def list_going_concerns(self) -> List[GoingConcernRecord]:
        return list(self.concerns.values())

    # ADAPTATION PLANE INTEGRATION: going-concern repair adaptation-plane structural change and fitness refs ile canonical bağlansın
    # ADAPTATION PLANE INTEGRATION: going concern preserved treated corrected without adaptation basis explicit caution üretsin