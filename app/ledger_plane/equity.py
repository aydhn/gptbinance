from datetime import datetime, timezone
import uuid
from typing import Dict, Any

from app.ledger_plane.models import EquityView
from app.ledger_plane.enums import EquityClass

class EquityViewBuilder:
    @staticmethod
    def build(account_scope: str, equity_class: EquityClass, total_value: float, currency: str, metadata: Dict[str, Any] = None) -> EquityView:
        return EquityView(
            id=str(uuid.uuid4()),
            account_scope=account_scope,
            equity_class=equity_class,
            total_value=total_value,
            currency=currency,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {}
        )
