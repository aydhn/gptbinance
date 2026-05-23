from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AdvisoryAuthorityRecord

class AdvisoryManager:
    def __init__(self):
        self.records: Dict[str, AdvisoryAuthorityRecord] = {}

    def get_non_binding(self) -> List[AdvisoryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "NON_BINDING"]

    def get_required(self) -> List[AdvisoryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "REQUIRED"]

    def get_technical(self) -> List[AdvisoryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "TECHNICAL"]

    def get_risk(self) -> List[AdvisoryAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "RISK"]
