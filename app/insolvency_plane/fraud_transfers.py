# fraud_transfers.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class FraudLikeTransferRecord(BaseModel):
    transfer_id: str
    description: str
    intent_status: str # suspicious, insider, contested
    lineage_refs: List[str]

class FraudTransferManager:
    def __init__(self):
        self.transfers: Dict[str, FraudLikeTransferRecord] = {}

    def register_fraud_transfer(self, transfer: FraudLikeTransferRecord):
        self.transfers[transfer.transfer_id] = transfer

    def get_fraud_transfer(self, transfer_id: str) -> Optional[FraudLikeTransferRecord]:
        return self.transfers.get(transfer_id)

    def list_fraud_transfers(self) -> List[FraudLikeTransferRecord]:
        return list(self.transfers.values())
