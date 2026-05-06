from typing import List, Optional
from uuid import UUID
from datetime import datetime, timezone

from app.identity.models import BreakGlassRecord
from app.identity.enums import BreakglassClass
from app.identity.storage import identity_storage


class BreakglassManager:
    def activate(
        self, principal_id: UUID, reason: str, bg_class: BreakglassClass
    ) -> BreakGlassRecord:
        record = BreakGlassRecord(
            principal_id=principal_id,
            breakglass_class=bg_class,
            reason=reason,
            activated_at=datetime.now(timezone.utc),
        )
        identity_storage.save_breakglass(record)
        # In a real system, this triggers IMMEDIATE high-severity alerts
        return record

    def review(self, record_id: UUID, reviewed_by: UUID) -> bool:
        record = identity_storage.breakglass_records.get(record_id)
        if not record:
            return False

        record.reviewed_at = datetime.now(timezone.utc)
        # Also log reviewed_by, store findings, etc.
        return True

    def list_all(self) -> List[BreakGlassRecord]:
        return identity_storage.get_all_breakglass()


breakglass_manager = BreakglassManager()
