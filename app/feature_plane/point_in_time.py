from app.feature_plane.models import PointInTimeCheckResult
from app.feature_plane.exceptions import PointInTimeViolationError
from datetime import datetime


class PointInTimeValidator:
    def validate(
        self, manifest_id: str, as_of_time: datetime
    ) -> PointInTimeCheckResult:
        # Dummy validation for now
        return PointInTimeCheckResult(
            manifest_id=manifest_id,
            as_of_time=as_of_time,
            is_valid=True,
            blockers=[],
            leakage_hints=[],
        )
