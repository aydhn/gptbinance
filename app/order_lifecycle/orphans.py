from app.order_lifecycle.models import OrphanOrderRecord, DeadLetterEvent
from app.order_lifecycle.enums import OrphanSeverity
from datetime import datetime, timezone
import uuid


class OrphanManager:
    def register_orphan(
        self, venue_order_id: str, severity: OrphanSeverity, notes: str
    ) -> OrphanOrderRecord:
        return OrphanOrderRecord(
            orphan_id=f"orph_{uuid.uuid4()}",
            venue_order_id=venue_order_id,
            severity=severity,
            timestamp=datetime.now(timezone.utc),
            remediation_notes=notes,
        )


# Phase 43
def evaluate_shadow_orphan_severity(self):
    pass
