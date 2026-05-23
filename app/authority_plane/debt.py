from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityDebtRecord

class DebtManager:
    def __init__(self):
        self.records: Dict[str, AuthorityDebtRecord] = {}

    def get_shadow_authority(self) -> List[AuthorityDebtRecord]:
        return [r for r in self.records.values() if r.type == "SHADOW_AUTHORITY"]

    def get_delegation_leakage(self) -> List[AuthorityDebtRecord]:
        return [r for r in self.records.values() if r.type == "DELEGATION_LEAKAGE"]

    def get_emergency_overuse(self) -> List[AuthorityDebtRecord]:
        return [r for r in self.records.values() if r.type == "EMERGENCY_OVERUSE"]

    def get_ratification_laundering(self) -> List[AuthorityDebtRecord]:
        return [r for r in self.records.values() if r.type == "RATIFICATION_LAUNDERING"]

    def get_missing_sod(self) -> List[AuthorityDebtRecord]:
        return [r for r in self.records.values() if r.type == "MISSING_SOD"]
