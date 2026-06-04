
from typing import List, Optional
from app.renewal_plane.models import RenewalCriteriaRecord, CriteriaClass

class CriteriaManager:
    def __init__(self):
        self.criteria = []

    def add_criteria(self, c_id: str, c_class: CriteriaClass):
        self.criteria.append(RenewalCriteriaRecord(criteria_id=c_id, criteria_class=c_class))

    def evaluate_all(self) -> bool:
        return all(c.criteria_class == CriteriaClass.SUFFICIENT_CRITERIA for c in self.criteria)
