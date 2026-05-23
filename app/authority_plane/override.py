from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import OverrideAuthorityRecord
from .enums import OverrideClass

class OverrideManager:
    def __init__(self):
        self.records: Dict[str, OverrideAuthorityRecord] = {}

    def get_emergency(self) -> List[OverrideAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == OverrideClass.EMERGENCY]

    def get_scoped(self) -> List[OverrideAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == OverrideClass.SCOPED]

    def get_temporary(self) -> List[OverrideAuthorityRecord]:
        return [r for r in self.records.values() if r.class_type == OverrideClass.TEMPORARY]
