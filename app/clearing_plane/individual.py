from typing import Dict, Any
from app.clearing_plane.exceptions import InvalidSegregationPostureError

class IndividualManager:
    def __init__(self):
        self.records: Dict[str, Dict[str, Any]] = {}

    def register(self, record_id: str, data: Dict[str, Any]) -> str:
        self.records[record_id] = data
        return record_id

    def verify_clean_segregation(self, record_id: str) -> bool:
        record = self.records.get(record_id, {})
        fellow_customer_risk = record.get("fellow_customer_risk", True)
        beneficiary_verified = record.get("beneficiary_verified", False)
        return beneficiary_verified and not fellow_customer_risk

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        if not self.verify_clean_segregation(record_id):
            raise InvalidSegregationPostureError(f"Fake individual segregation for {record_id}.")
        return {"status": "individual_segregation_clean", "record": self.records[record_id]}
