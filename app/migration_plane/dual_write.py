from datetime import datetime, timezone
from app.migration_plane.models import DualWriteRecord

class DualWriteManager:
    def start_dual_write(self, migration_id: str, expiry: datetime) -> DualWriteRecord:
        # Implementation for dual write
        return DualWriteRecord(
            migration_id=migration_id,
            start_time=datetime.now(timezone.utc),
            expiry=expiry,
            divergence_detected=False
        )
