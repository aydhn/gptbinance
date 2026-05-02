from typing import Optional
from .models import LiquidationSnapshot, MaintenanceMarginSnapshot
from .enums import LiquidationProximity, MarginCallSeverity


class LiquidationApproxModel:
    """
    Approximate model for calculating liquidation distances and maintenance margins.
    Does not perfectly mimic exchange internals, but provides conservative bounds.
    """

    def __init__(self, maintenance_margin_rate: float = 0.005):
        self.maintenance_margin_rate = maintenance_margin_rate

    def calculate_liquidation_snapshot(
        self,
        symbol: str,
        current_price: float,
        entry_price: float,
        position_size: float,
        margin_balance: float,
        is_long: bool,
    ) -> LiquidationSnapshot:
        if position_size == 0 or margin_balance <= 0:
            return LiquidationSnapshot(
                symbol=symbol,
                current_price=current_price,
                liquidation_price=None,
                distance_pct=1.0,
                proximity=LiquidationProximity.SAFE,
            )

        position_notional = abs(position_size) * entry_price

        # Approximate: Margin = Notional * Maintenance_Rate
        # Liquidation when Margin Balance drops to Maintenance Margin
        # PNL = +/- (Current - Entry) * Size
        # Target: Margin_Balance + PNL <= Notional * Maintenance_Rate

        mm_req = position_notional * self.maintenance_margin_rate
        buffer = margin_balance - mm_req

        if buffer <= 0:
            return LiquidationSnapshot(
                symbol=symbol,
                current_price=current_price,
                liquidation_price=current_price,
                distance_pct=0.0,
                proximity=LiquidationProximity.DANGER,
            )

        if is_long:
            # Drop in price causes loss
            price_drop = buffer / abs(position_size)
            liq_price = max(0, entry_price - price_drop)
            distance = (
                (current_price - liq_price) / current_price if current_price > 0 else 0
            )
        else:
            # Rise in price causes loss
            price_rise = buffer / abs(position_size)
            liq_price = entry_price + price_rise
            distance = (
                (liq_price - current_price) / current_price if current_price > 0 else 0
            )

        proximity = LiquidationProximity.SAFE
        if distance < 0.05:
            proximity = LiquidationProximity.DANGER
        elif distance < 0.15:
            proximity = LiquidationProximity.WARNING

        return LiquidationSnapshot(
            symbol=symbol,
            current_price=current_price,
            liquidation_price=liq_price,
            distance_pct=distance,
            proximity=proximity,
        )
