from app.ledger.models import LedgerEvent, LedgerEventSource
from app.ledger.enums import SourceSystem, LedgerEntryType
from datetime import datetime, timezone
import uuid


class EventFactory:
    @staticmethod
    def create_fill_event(
        asset: str, amount: float, price: float, side: str
    ) -> LedgerEvent:
        return LedgerEvent(
            event_id=str(uuid.uuid4()),
            type=LedgerEntryType.TRADE_SETTLEMENT,
            source=LedgerEventSource(
                system=SourceSystem.INTERNAL_ENGINE,
                event_id=f"fill_{uuid.uuid4()}",
                timestamp=datetime.now(timezone.utc),
            ),
            amount=amount,
            asset=asset,
            metadata={"price": price, "side": side},
        )
