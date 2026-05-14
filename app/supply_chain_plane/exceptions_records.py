from typing import Dict, Optional, List
from app.supply_chain_plane.models import SupplyChainExceptionRecord


class ExceptionRegistry:
    def __init__(self):
        self._exceptions: Dict[str, SupplyChainExceptionRecord] = {}

    def register_exception(self, exception: SupplyChainExceptionRecord) -> None:
        self._exceptions[exception.exception_id] = exception

    def get_exception(self, exception_id: str) -> Optional[SupplyChainExceptionRecord]:
        return self._exceptions.get(exception_id)

    def get_exceptions_for_component(
        self, component_id: str
    ) -> List[SupplyChainExceptionRecord]:
        return [
            e
            for e in self._exceptions.values()
            if e.component_ref.component_id == component_id
        ]
