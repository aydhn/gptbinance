from typing import Dict, Any
from app.clearing_plane.exceptions import InvalidDefaultWaterfallError

class DefaultsManager:
    def __init__(self):
        self.records: Dict[str, Dict[str, Any]] = {}

    def register(self, record_id: str, data: Dict[str, Any]) -> str:
        self.records[record_id] = data
        return record_id

    def evaluate_default_declaration(self, record_id: str) -> Dict[str, Any]:
        record = self.records.get(record_id, {})
        is_formal_declaration = record.get("formally_declared", False)
        has_hedge_plan = record.get("hedge_plan_ready", False)

        if not is_formal_declaration or not has_hedge_plan:
            raise InvalidDefaultWaterfallError(f"Opaque default posture for {record_id}.")

        return {"status": "default_declared_cleanly", "record": self.records[record_id]}

    def evaluate(self, record_id: str) -> Dict[str, Any]:
        return self.evaluate_default_declaration(record_id)
