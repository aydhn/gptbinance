from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import ReviewAuthorityRecord

class ReviewManager:
    def __init__(self):
        self.records: Dict[str, ReviewAuthorityRecord] = {}

    def get_mandatory(self) -> List[ReviewAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "MANDATORY"]

    def get_optional(self) -> List[ReviewAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "OPTIONAL"]

    def get_review_only(self) -> List[ReviewAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "REVIEW_ONLY"]
