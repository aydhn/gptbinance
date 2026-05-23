from typing import Dict, List, Optional
from .models import RatificationRecord
from .enums import RatificationClass

class RatificationManager:
    """
    Distinguishes valid from insufficient or abusive post-hoc ratifications.
    No ratification==original authority shortcut allowed.
    """
    def __init__(self):
        self.records: Dict[str, RatificationRecord] = {}

    def add_ratification(self, rat_id: str, rclass: RatificationClass, cautions: List[str] = None) -> RatificationRecord:
        record = RatificationRecord(rat_id, rclass, cautions or [], [])
        self.records[rat_id] = record
        return record

    def get_valid(self) -> List[RatificationRecord]:
        return [r for r in self.records.values() if r.class_type == RatificationClass.VALID]

    def get_insufficient(self) -> List[RatificationRecord]:
        return [r for r in self.records.values() if r.class_type == RatificationClass.INSUFFICIENT]

    def get_post_hoc(self) -> List[RatificationRecord]:
        return [r for r in self.records.values() if r.class_type == RatificationClass.POST_HOC]
