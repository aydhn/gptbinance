from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import LedgerDivergenceReport
from app.ledger_plane.enums import DivergenceSeverity

class DivergenceDetector:
    @staticmethod
    def report(severity: DivergenceSeverity, description: str, metadata: Dict[str, Any] = None) -> LedgerDivergenceReport:
        return LedgerDivergenceReport(
            id=str(uuid.uuid4()),
            severity=severity,
            description=description,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {}
        )
