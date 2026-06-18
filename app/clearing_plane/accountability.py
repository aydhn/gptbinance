from typing import Dict, Any
from app.clearing_plane.exceptions import ClearingPlaneError

class AccountabilityManager:
    def __init__(self):
        self.records: Dict[str, Any] = {}

    def register(self, record_id: str, data: Dict[str, Any]) -> str:
        self.records[record_id] = data
        return record_id

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        if record_id not in self.records:
            raise ClearingPlaneError(f"Record {record_id} not found in accountability")
        return {"status": "evaluated", "record": self.records[record_id]}

    def get_proof_notes(self, record_id: str) -> str:
        return f"Proof notes for accountability {record_id}"
