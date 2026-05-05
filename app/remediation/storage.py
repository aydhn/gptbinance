from typing import Dict, List
from app.remediation.models import RemediationPack, RemediationDebtRecord


class RemediationStorage:
    def __init__(self):
        self._packs: Dict[str, RemediationPack] = {}
        self._debts: Dict[str, RemediationDebtRecord] = {}

    def save_pack(self, pack: RemediationPack):
        self._packs[pack.pack_id] = pack

    def get_pack(self, pack_id: str) -> RemediationPack:
        return self._packs.get(pack_id)

    def list_packs(self) -> List[RemediationPack]:
        return list(self._packs.values())

    def save_debt(self, debt: RemediationDebtRecord):
        self._debts[debt.debt_id] = debt

    def get_debts(self) -> List[RemediationDebtRecord]:
        return list(self._debts.values())
