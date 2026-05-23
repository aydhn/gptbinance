from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import JointAuthorityRecord

class JointAuthorityManager:
    def __init__(self):
        self.records: Dict[str, JointAuthorityRecord] = {}

    def get_dual(self) -> List[JointAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "DUAL"]

    def get_multi(self) -> List[JointAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "MULTI"]

    def get_concurrent(self) -> List[JointAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "CONCURRENT"]

    def get_split(self) -> List[JointAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "SPLIT"]
