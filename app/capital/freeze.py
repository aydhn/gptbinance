from datetime import datetime, timezone
from typing import List, Optional
from app.capital.models import CapitalFreezeState
from app.capital.enums import FreezeStatus


class FreezeManager:
    def __init__(self):
        self._current_state = CapitalFreezeState(status=FreezeStatus.INACTIVE)

    def get_state(self) -> CapitalFreezeState:
        return self._current_state

    def apply_freeze(
        self, reasons: List[str], prerequisites: List[str]
    ) -> CapitalFreezeState:
        self._current_state = CapitalFreezeState(
            status=FreezeStatus.ACTIVE,
            frozen_at=datetime.now(timezone.utc),
            reasons=reasons,
            thaw_prerequisites=prerequisites,
        )
        return self._current_state

    def request_thaw(self) -> CapitalFreezeState:
        if self._current_state.status == FreezeStatus.ACTIVE:
            self._current_state.status = FreezeStatus.THAW_PENDING
        return self._current_state

    def clear_freeze(self) -> CapitalFreezeState:
        self._current_state = CapitalFreezeState(status=FreezeStatus.INACTIVE)
        return self._current_state


freeze_manager = FreezeManager()
