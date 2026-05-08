from decimal import Decimal
from typing import List, Dict

from app.position_plane.models import PositionState, PositionExposureView
from app.position_plane.enums import Side


class ExposureCalculator:
    @staticmethod
    def calculate_exposures(
        states: List[PositionState], mark_prices: Dict[str, Decimal]
    ) -> PositionExposureView:
        if not states:
            return PositionExposureView(
                symbol="aggregate",
                gross_exposure=Decimal("0"),
                net_directional_exposure=Decimal("0"),
                hedge_adjusted_exposure=Decimal("0"),
                residual_directional_exposure=Decimal("0"),
                base_currency="MIXED",
                quote_currency="MIXED",
                caveats=["No positions to calculate exposure."],
            )

        symbol = states[0].symbol  # assuming single symbol aggregation for now
        gross_exp = Decimal("0")
        net_exp = Decimal("0")

        for state in states:
            mark_price = mark_prices.get(state.symbol, state.average_entry_price)
            if mark_price == Decimal("0"):
                continue

            notional = state.quantity * mark_price
            gross_exp += notional
            if state.side == Side.LONG:
                net_exp += notional
            elif state.side == Side.SHORT:
                net_exp -= notional

        hedge_adjusted = min(
            gross_exp, abs(net_exp)
        )  # simple heuristic, requires proper hedge overlay logic
        residual = abs(net_exp)

        return PositionExposureView(
            symbol=symbol,
            gross_exposure=gross_exp,
            net_directional_exposure=net_exp,
            hedge_adjusted_exposure=hedge_adjusted,
            residual_directional_exposure=residual,
            base_currency=symbol.split("USDT")[0] if "USDT" in symbol else "BASE",
            quote_currency="USDT" if "USDT" in symbol else "QUOTE",
        )
