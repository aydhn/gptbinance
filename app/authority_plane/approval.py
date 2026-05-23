from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import ApprovalAuthorityRecord

class ApprovalManager:
    def __init__(self):
        self.records: Dict[str, ApprovalAuthorityRecord] = {}

    def get_binding(self) -> List[ApprovalAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "BINDING"]

    def get_scoped(self) -> List[ApprovalAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "SCOPED"]

    def get_quorum(self) -> List[ApprovalAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "QUORUM"]

    def get_delegated(self) -> List[ApprovalAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "DELEGATED"]
