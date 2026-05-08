from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import LedgerEquivalenceReport
from app.ledger_plane.enums import EquivalenceVerdict


class EquivalenceEvaluator:
    @staticmethod
    def evaluate(
        verdict: EquivalenceVerdict, description: str, metadata: Dict[str, Any] = None
    ) -> LedgerEquivalenceReport:
        return LedgerEquivalenceReport(
            id=str(uuid.uuid4()),
            verdict=verdict,
            description=description,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {},
        )
