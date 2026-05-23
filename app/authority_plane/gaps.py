from typing import Dict, List, Optional
from .models import LegitimacyGapRecord

class GapsManager:
    """
    Exposes missing links in the authority chain preventing legitimacy.
    """
    def __init__(self):
        self.records: Dict[str, LegitimacyGapRecord] = {}

    def add_gap(self, gap_id: str, gap_type: str) -> LegitimacyGapRecord:
        record = LegitimacyGapRecord(gap_id, gap_type, [])
        self.records[gap_id] = record
        return record

    def get_no_valid(self) -> List[LegitimacyGapRecord]:
        return [r for r in self.records.values() if r.type == "NO_VALID"]

    def get_wrong_scope(self) -> List[LegitimacyGapRecord]:
        return [r for r in self.records.values() if r.type == "WRONG_SCOPE"]

    def get_expired(self) -> List[LegitimacyGapRecord]:
        return [r for r in self.records.values() if r.type == "EXPIRED"]

    def get_missing_ratification(self) -> List[LegitimacyGapRecord]:
        return [r for r in self.records.values() if r.type == "MISSING_RATIFICATION"]
