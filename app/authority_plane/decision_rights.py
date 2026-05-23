from typing import Dict, List, Optional
from .models import DecisionRightRecord
from .enums import DecisionRightClass

class DecisionRightsManager:
    """
    Defines explicit decision boundaries: approve, deny, conditionally approve, recommend.
    """
    def __init__(self):
        self.rights: Dict[str, DecisionRightRecord] = {}

    def _add_right(self, right_id: str, authority_id: str, rclass: DecisionRightClass, ambiguity_notes: List[str] = None) -> DecisionRightRecord:
        record = DecisionRightRecord(right_id, authority_id, rclass, ambiguity_notes or [], [])
        self.rights[right_id] = record
        return record

    def add_approve(self, right_id: str, authority_id: str, ambiguity_notes: List[str] = None) -> DecisionRightRecord:
        return self._add_right(right_id, authority_id, DecisionRightClass.APPROVE, ambiguity_notes)

    def add_deny(self, right_id: str, authority_id: str, ambiguity_notes: List[str] = None) -> DecisionRightRecord:
        return self._add_right(right_id, authority_id, DecisionRightClass.DENY, ambiguity_notes)

    def add_conditionally_approve(self, right_id: str, authority_id: str, ambiguity_notes: List[str] = None) -> DecisionRightRecord:
        return self._add_right(right_id, authority_id, DecisionRightClass.CONDITIONALLY_APPROVE, ambiguity_notes)

    def add_recommend_only(self, right_id: str, authority_id: str, ambiguity_notes: List[str] = None) -> DecisionRightRecord:
        return self._add_right(right_id, authority_id, DecisionRightClass.RECOMMEND_ONLY, ambiguity_notes)

    def get_by_id(self, right_id: str) -> Optional[DecisionRightRecord]:
        return self.rights.get(right_id)
