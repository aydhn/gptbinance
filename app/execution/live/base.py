from abc import ABC, abstractmethod
from typing import List, Optional
from app.execution.live.models import (
    ExecutionRequest,
    ExecutionResult,
    CancelRequest,
    CancelResult,
    ReplaceRequest,
    OrderStateSnapshot,
    ReconciliationReport,
)


class OrderRouterBase(ABC):
    @abstractmethod
    async def submit_order(self, request: ExecutionRequest) -> ExecutionResult:
        pass

    @abstractmethod
    async def cancel_order(self, request: CancelRequest) -> CancelResult:
        pass

    @abstractmethod
    async def replace_order(self, request: ReplaceRequest) -> ExecutionResult:
        pass


class OrderStateStoreBase(ABC):
    @abstractmethod
    def save_state(self, snapshot: OrderStateSnapshot) -> None:
        pass

    @abstractmethod
    def get_state(self, client_order_id: str) -> Optional[OrderStateSnapshot]:
        pass

    @abstractmethod
    def get_all_open_orders(self) -> List[OrderStateSnapshot]:
        pass


class ReconciliationEngineBase(ABC):
    @abstractmethod
    async def run_reconciliation(self) -> ReconciliationReport:
        pass
