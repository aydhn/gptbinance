from typing import Optional
from app.position_plane.models import PositionState
from app.position_plane.storage import PositionStorage


class PositionRepository:
    def __init__(self, storage: PositionStorage):
        self.storage = storage

    def save_state(self, state: PositionState) -> None:
        self.storage.save_state(state)

    def get_latest_trusted_position(
        self, symbol: str, sleeve_id: str
    ) -> Optional[PositionState]:
        # Implementation depends on how we query storage, simple mock for now
        for state in self.storage._states.values():
            if (
                state.symbol == symbol
                and state.sleeve_id == sleeve_id
                and state.is_authoritative
            ):
                return state
        return None
