from typing import Dict, List, Optional
from app.execution.live.models import OrderStateSnapshot
from app.execution.live.base import OrderStateStoreBase
from app.execution.live.enums import OrderLifecycleStatus


class InMemoryOrderStateStore(OrderStateStoreBase):
    def __init__(self):
        self._states: Dict[str, OrderStateSnapshot] = {}

    def save_state(self, snapshot: OrderStateSnapshot) -> None:
        self._states[snapshot.client_order_id] = snapshot

    def get_state(self, client_order_id: str) -> Optional[OrderStateSnapshot]:
        return self._states.get(client_order_id)

    def get_all_open_orders(self) -> List[OrderStateSnapshot]:
        return [state for state in self._states.values() if state.is_open]

    def get_by_exchange_id(
        self, exchange_order_id: str
    ) -> Optional[OrderStateSnapshot]:
        for state in self._states.values():
            if state.exchange_order_id == exchange_order_id:
                return state
        return None
