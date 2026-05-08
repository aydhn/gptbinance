from typing import Dict, Optional
from datetime import datetime, timezone, timedelta
from app.model_plane.base import CalibrationEvaluatorBase
from app.model_plane.models import CalibrationRecord
from app.model_plane.enums import CalibrationClass
from app.model_plane.exceptions import CalibrationError


class CalibrationManager(CalibrationEvaluatorBase):
    def __init__(self, stale_threshold_days: int = 7):
        self._records: Dict[str, CalibrationRecord] = {}
        self.stale_threshold_days = stale_threshold_days

    def store_record(self, record: CalibrationRecord) -> None:
        if not record.record_id or not record.checkpoint_id:
            raise CalibrationError("Invalid calibration record")
        self._records[record.record_id] = record

    def get_latest_for_checkpoint(
        self, checkpoint_id: str
    ) -> Optional[CalibrationRecord]:
        records = [
            r for r in self._records.values() if r.checkpoint_id == checkpoint_id
        ]
        if not records:
            return None
        return sorted(records, key=lambda x: x.evaluated_at, reverse=True)[0]

    def evaluate_calibration(self, checkpoint_id: str) -> CalibrationRecord:
        record = self.get_latest_for_checkpoint(checkpoint_id)
        if not record:
            raise CalibrationError(
                f"No calibration record found for checkpoint {checkpoint_id}"
            )
        return record

    def check_calibration_freshness(self, record: CalibrationRecord) -> bool:
        now = datetime.now(timezone.utc)
        age = now - record.evaluated_at
        is_stale = age > timedelta(days=self.stale_threshold_days)
        record.is_stale = is_stale
        return is_stale
