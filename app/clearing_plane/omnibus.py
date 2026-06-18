from typing import Dict, Any
from app.clearing_plane.exceptions import InvalidSegregationPostureError

class OmnibusManager:
    def __init__(self):
        self.records: Dict[str, Dict[str, Any]] = {}

    def register(self, record_id: str, data: Dict[str, Any]) -> str:
        self.records[record_id] = data
        return record_id

    def check_for_contamination(self, record_id: str) -> bool:
        record = self.records.get(record_id, {})
        has_house_money = record.get("contains_house_funds", False)
        is_portability_tested = record.get("portability_tested", False)
        return has_house_money or not is_portability_tested

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        if self.check_for_contamination(record_id):
            raise InvalidSegregationPostureError(f"Omnibus theater / Contamination detected for {record_id}.")
        return {"status": "omnibus_segregation_clean", "record": self.records[record_id]}
