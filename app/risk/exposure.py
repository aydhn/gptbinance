from typing import List, Dict
from datetime import datetime
from app.risk.models import ExposureSnapshot
from app.backtest.models import PositionState
from app.backtest.enums import PositionSide


class ExposureCalculator:
    def calculate(
        self, positions: List[PositionState], equity: float, timestamp: datetime
    ) -> ExposureSnapshot:
        symbol_exp: Dict[str, float] = {}
        strategy_exp: Dict[str, float] = {}
        long_exp = 0.0
        short_exp = 0.0

        for pos in positions:
            if pos.side == PositionSide.FLAT or pos.quantity == 0:
                continue

            notional = (
                pos.quantity * pos.entry_price
            )  # Using entry for simplicity, current price would be better if passed

            if pos.symbol not in symbol_exp:
                symbol_exp[pos.symbol] = 0.0
            symbol_exp[pos.symbol] += notional

            # Future: add strategy exposure tracking here when PositionState supports strategy source

            if pos.side == PositionSide.LONG:
                long_exp += notional
            elif pos.side == PositionSide.SHORT:
                short_exp += notional

        return ExposureSnapshot(
            timestamp=timestamp,
            symbol_exposures=symbol_exp,
            strategy_exposures=strategy_exp,
            total_long_exposure=long_exp,
            total_short_exposure=short_exp,
            total_gross_exposure=long_exp + short_exp,
            total_equity=equity,
        )
