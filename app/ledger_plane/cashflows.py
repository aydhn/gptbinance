from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import CashflowRecord
from app.ledger_plane.enums import CashflowClass

class CashflowBuilder:
    @staticmethod
    def build(cashflow_class: CashflowClass, asset: str, amount: float, account_scope: str, direction: str, metadata: Dict[str, Any] = None) -> CashflowRecord:
        return CashflowRecord(
            id=str(uuid.uuid4()),
            cashflow_class=cashflow_class,
            asset=asset,
            amount=amount,
            account_scope=account_scope,
            direction=direction,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {}
        )
