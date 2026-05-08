from typing import Dict, Optional
from app.model_plane.models import UncertaintyRecord
from app.model_plane.enums import UncertaintyClass
from app.model_plane.exceptions import UncertaintyError


class UncertaintyManager:
    def __init__(self):
        self._records: Dict[str, UncertaintyRecord] = {}

    def store_record(self, record: UncertaintyRecord) -> None:
        if not record.record_id or not record.checkpoint_id:
            raise UncertaintyError("Invalid uncertainty record")
        self._records[record.record_id] = record

    def get_latest_for_checkpoint(
        self, checkpoint_id: str
    ) -> Optional[UncertaintyRecord]:
        records = [
            r for r in self._records.values() if r.checkpoint_id == checkpoint_id
        ]
        if not records:
            return None
        return sorted(records, key=lambda x: x.evaluated_at, reverse=True)[0]

    def check_low_confidence_gate(self, checkpoint_id: str) -> bool:
        """Returns True if the checkpoint uncertainty allows it to pass the gate"""
        record = self.get_latest_for_checkpoint(checkpoint_id)
        if not record:
            # Default to cautious and return False
            return False

        return record.uncertainty_class in [
            UncertaintyClass.HIGH_CONFIDENCE,
            UncertaintyClass.MODERATE_CONFIDENCE,
        ]
