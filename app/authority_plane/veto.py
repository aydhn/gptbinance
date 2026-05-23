from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import VetoAuthorityRecord
from .enums import VetoClass

class VetoManager:
    def __init__(self):
        self.records: Dict[str, VetoAuthorityRecord] = {}

    def get_hard(self) -> List[VetoAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == VetoClass.HARD]

    def get_scoped(self) -> List[VetoAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == VetoClass.SCOPED]

    def get_suspensive(self) -> List[VetoAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == VetoClass.SUSPENSIVE]

    def get_advisory_signal(self) -> List[VetoAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == VetoClass.ADVISORY_SIGNAL]
