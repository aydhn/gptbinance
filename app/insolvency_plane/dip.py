# dip.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class DIPSupportRecord(BaseModel):
    support_id: str
    provider: str
    amount: float
    status: str # approved, conditional, insufficient, defaulted
    lineage_refs: List[str]

class DIPSupportManager:
    def __init__(self):
        self.supports: Dict[str, DIPSupportRecord] = {}

    def register_dip_support(self, support: DIPSupportRecord):
        self.supports[support.support_id] = support

    def get_dip_support(self, support_id: str) -> Optional[DIPSupportRecord]:
        return self.supports.get(support_id)

    def list_dip_supports(self) -> List[DIPSupportRecord]:
        return list(self.supports.values())
