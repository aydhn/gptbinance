from typing import Dict, Optional
from datetime import datetime
from app.strategies.enums import SignalDirection
from app.strategies.models import StrategyStateSnapshot


class StrategyStateManager:
    """
    Manages the internal state of strategies across evaluations.
    This acts as an in-memory cache for the duration of the run.
    Future phases can persist this to a database.
    """

    def __init__(self):
        # strategy_name_symbol -> StrategyStateSnapshot
        self._states: Dict[str, StrategyStateSnapshot] = {}

    def _generate_key(self, strategy_name: str, symbol: str) -> str:
        return f"{strategy_name}::{symbol}"

    def get_state(
        self, strategy_name: str, symbol: str
    ) -> Optional[StrategyStateSnapshot]:
        key = self._generate_key(strategy_name, symbol)
        return self._states.get(key)

    def save_state(self, snapshot: StrategyStateSnapshot):
        key = self._generate_key(snapshot.strategy_name, snapshot.symbol)
        self._states[key] = snapshot

    def update_last_signal(
        self,
        strategy_name: str,
        symbol: str,
        timestamp: datetime,
        direction: SignalDirection,
    ):
        key = self._generate_key(strategy_name, symbol)

        if key not in self._states:
            self._states[key] = StrategyStateSnapshot(
                strategy_name=strategy_name, symbol=symbol
            )

        self._states[key].last_signal_time = timestamp
        self._states[key].last_direction = direction

    def get_last_direction(
        self, strategy_name: str, symbol: str
    ) -> Optional[SignalDirection]:
        state = self.get_state(strategy_name, symbol)
        return state.last_direction if state else None
