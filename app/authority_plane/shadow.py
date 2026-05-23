from typing import Dict, List, Optional
from .models import ShadowAuthorityRecord

class ShadowManager:
    """
    Highlights informal or title-inflated authority usage avoiding real mandates.
    """
    def __init__(self):
        self.records: Dict[str, ShadowAuthorityRecord] = {}

    def add_shadow(self, s_id: str, stype: str, findings: List[str] = None) -> ShadowAuthorityRecord:
        record = ShadowAuthorityRecord(s_id, stype, findings or [], [])
        self.records[s_id] = record
        return record

    def get_informal(self) -> List[ShadowAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "INFORMAL"]

    def get_title_mismatch(self) -> List[ShadowAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "TITLE_MISMATCH"]

    def get_influence(self) -> List[ShadowAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "INFLUENCE"]
