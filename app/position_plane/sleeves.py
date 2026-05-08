from typing import List, Dict
from app.position_plane.models import PositionState


class SleeveManager:
    @staticmethod
    def aggregate_by_sleeve(
        states: List[PositionState],
    ) -> Dict[str, List[PositionState]]:
        sleeve_map = {}
        for state in states:
            sleeve_map.setdefault(state.sleeve_id, []).append(state)
        return sleeve_map

    @staticmethod
    def aggregate_symbol_across_sleeves(
        states: List[PositionState], symbol: str
    ) -> List[PositionState]:
        return [state for state in states if state.symbol == symbol]
