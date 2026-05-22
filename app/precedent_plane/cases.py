from app.precedent_plane.models import CaseRecord, HoldingRecord
from app.precedent_plane.enums import CaseClass
from typing import List

class CasesManager:
    def __init__(self):
        self.records: List[CaseRecord] = []

    def register_case(self, case: CaseRecord):
        if not case.case_id or not case.precedent_id:
            raise ValueError("Invalid case")
        self.records.append(case)
        return True

    def resolve_case(self, case_id: str):
        for r in self.records:
            if r.case_id == case_id:
                r.case_class = CaseClass.RESOLVED
                return r
        return None
