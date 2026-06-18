from typing import Dict, Any
from .models import NettingSubjectRecord

class SubjectManager:
    def __init__(self):
        self.subjects: Dict[str, NettingSubjectRecord] = {}

    def register_subject(self, data: Dict[str, Any]) -> NettingSubjectRecord:
        sub = NettingSubjectRecord(**data)
        self.subjects[sub.subject_id] = sub
        return sub
