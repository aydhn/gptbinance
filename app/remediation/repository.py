from typing import List
from app.remediation.models import RemediationPack, RemediationDebtRecord
from app.remediation.storage import RemediationStorage


class RemediationRepository:
    def __init__(self):
        self.storage = RemediationStorage()

    def save_pack(self, pack: RemediationPack):
        self.storage.save_pack(pack)

    def get_pack(self, pack_id: str) -> RemediationPack:
        return self.storage.get_pack(pack_id)

    def get_active_debt(self) -> List[RemediationDebtRecord]:
        # Filter for active debts
        return self.storage.get_debts()
