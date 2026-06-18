from typing import Dict, Any, List
from app.clearing_plane.exceptions import InvalidNovationError

class NovationManager:
    def __init__(self):
        self.records: Dict[str, Dict[str, Any]] = {}

    def register(self, record_id: str, data: Dict[str, Any]) -> str:
        self.records[record_id] = data
        return record_id

    def verify_strict_novation(self, record_id: str) -> bool:
        record = self.records.get(record_id)
        if not record:
            return False

        is_accepted_by_ccp = record.get("accepted_by_ccp", False)
        has_bilateral_residue = record.get("has_bilateral_residue", True)

        if is_accepted_by_ccp and not has_bilateral_residue:
            return True
        return False

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        if not self.verify_strict_novation(record_id):
            raise InvalidNovationError(f"Fake novation detected for {record_id}. Trade accepted but bilateral exposure remains.")
        return {"status": "strict_novation_clean", "record": self.records[record_id]}
