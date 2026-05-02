from typing import Dict, Any, Optional
from datetime import datetime
from decimal import Decimal
from app.execution.live.models import OrderLifecycleEvent, UserStreamEvent
from app.execution.live.enums import OrderLifecycleStatus, UserStreamEventType


class ExecutionParser:
    """Parses raw exchange payloads into domain events."""

    @staticmethod
    def parse_user_stream_event(payload: Dict[str, Any]) -> Optional[UserStreamEvent]:
        event_type = payload.get("e")
        if event_type == "executionReport":
            return UserStreamEvent(
                event_type=UserStreamEventType.EXECUTION_REPORT,
                timestamp=datetime.utcfromtimestamp(payload.get("E", 0) / 1000.0),
                raw_data=payload,
            )
        elif event_type == "outboundAccountPosition":
            return UserStreamEvent(
                event_type=UserStreamEventType.ACCOUNT_UPDATE,
                timestamp=datetime.utcfromtimestamp(payload.get("E", 0) / 1000.0),
                raw_data=payload,
            )
        elif event_type == "balanceUpdate":
            return UserStreamEvent(
                event_type=UserStreamEventType.BALANCE_UPDATE,
                timestamp=datetime.utcfromtimestamp(payload.get("E", 0) / 1000.0),
                raw_data=payload,
            )
        return UserStreamEvent(
            event_type=UserStreamEventType.UNKNOWN,
            timestamp=datetime.utcnow(),
            raw_data=payload,
        )

    @staticmethod
    def parse_execution_report(payload: Dict[str, Any]) -> OrderLifecycleEvent:
        """Parses a Binance executionReport into an OrderLifecycleEvent."""
        status_map = {
            "NEW": OrderLifecycleStatus.ACKNOWLEDGED,
            "PARTIALLY_FILLED": OrderLifecycleStatus.PARTIALLY_FILLED,
            "FILLED": OrderLifecycleStatus.FILLED,
            "CANCELED": OrderLifecycleStatus.CANCELED,
            "REJECTED": OrderLifecycleStatus.REJECTED,
            "EXPIRED": OrderLifecycleStatus.EXPIRED,
        }
        raw_status = payload.get("X", "UNKNOWN")
        status = status_map.get(raw_status, OrderLifecycleStatus.UNKNOWN)

        return OrderLifecycleEvent(
            client_order_id=payload.get("c", ""),
            status=status,
            timestamp=datetime.utcfromtimestamp(payload.get("E", 0) / 1000.0),
            details={
                "exchange_order_id": str(payload.get("i", "")),
                "symbol": payload.get("s", ""),
                "filled_qty": Decimal(payload.get("z", "0")),
                "last_filled_qty": Decimal(payload.get("l", "0")),
                "last_filled_price": Decimal(payload.get("L", "0")),
                "average_price": (
                    Decimal(payload.get("p", "0")) if "p" in payload else None
                ),
            },
        )
