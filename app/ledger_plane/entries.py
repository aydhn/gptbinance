from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import LedgerEntry
from app.ledger_plane.enums import LedgerClass


class TypedLedgerEntryBuilder:
    @staticmethod
    def build(
        ledger_class: LedgerClass,
        asset: str,
        amount: float,
        account_scope: str,
        source_ref: str,
        metadata: Dict[str, Any] = None,
    ) -> LedgerEntry:
        return LedgerEntry(
            id=str(uuid.uuid4()),
            ledger_class=ledger_class,
            asset=asset,
            amount=amount,
            account_scope=account_scope,
            source_ref=source_ref,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {},
        )
