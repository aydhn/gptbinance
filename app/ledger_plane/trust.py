from datetime import datetime, timezone
import uuid
from typing import List, Dict, Any

from app.ledger_plane.models import LedgerTrustVerdict
from app.ledger_plane.enums import TrustVerdict


class TrustVerdictEngine:
    @staticmethod
    def evaluate(
        verdict: TrustVerdict, reasons: List[str], metadata: Dict[str, Any] = None
    ) -> LedgerTrustVerdict:
        return LedgerTrustVerdict(
            id=str(uuid.uuid4()),
            verdict=verdict,
            reasons=reasons,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {},
        )
