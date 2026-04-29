"""Paper order book management."""
import logging
from typing import Dict, List, Optional
from datetime import datetime

from .models import PaperOrder, PaperOrderIntent, PaperOrderStatus
from .exceptions import PaperOrderLifecycleError

logger = logging.getLogger(__name__)


class PaperOrderBook:
    def __init__(self):
        self.orders: Dict[str, PaperOrder] = {}

    def add_from_intent(self, intent: PaperOrderIntent, order_id: str) -> PaperOrder:
        if order_id in self.orders:
            raise PaperOrderLifecycleError(f"Order ID {order_id} already exists.")

        order = PaperOrder(
            order_id=order_id,
            intent_id=intent.intent_id,
            symbol=intent.symbol,
            side=intent.side,
            qty=intent.qty,
            status=PaperOrderStatus.CREATED,
            created_at=datetime.utcnow(),
        )
        self.orders[order_id] = order
        return order

    def update_status(
        self, order_id: str, new_status: PaperOrderStatus, **kwargs
    ) -> PaperOrder:
        if order_id not in self.orders:
            raise PaperOrderLifecycleError(f"Order {order_id} not found.")

        order = self.orders[order_id]

        # Simple state machine validation
        terminal_states = {
            PaperOrderStatus.FILLED,
            PaperOrderStatus.CANCELLED,
            PaperOrderStatus.REJECTED,
            PaperOrderStatus.EXPIRED,
        }
        if order.status in terminal_states:
            raise PaperOrderLifecycleError(
                f"Cannot update terminal order {order_id} from {order.status} to {new_status}"
            )

        order.status = new_status

        if new_status == PaperOrderStatus.ACCEPTED:
            order.accepted_at = datetime.utcnow()
        elif new_status == PaperOrderStatus.FILLED:
            order.filled_at = datetime.utcnow()
            order.fill_price = kwargs.get("fill_price")
            order.fill_assumption = kwargs.get("fill_assumption")
            order.fees = kwargs.get("fees", 0.0)
        elif new_status == PaperOrderStatus.REJECTED:
            order.rejection_reason = kwargs.get("rejection_reason")

        return order

    def get_open_orders(self, symbol: Optional[str] = None) -> List[PaperOrder]:
        open_states = {
            PaperOrderStatus.CREATED,
            PaperOrderStatus.QUEUED,
            PaperOrderStatus.ACCEPTED,
            PaperOrderStatus.PARTIALLY_FILLED,
        }
        return [
            o
            for o in self.orders.values()
            if o.status in open_states and (symbol is None or o.symbol == symbol)
        ]

    def get_all(self) -> List[PaperOrder]:
        return list(self.orders.values())
