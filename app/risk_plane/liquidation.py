from .models import LiquidationProximityState
from .enums import LiquidationClass


def calculate_liquidation_proximity(
    mark_price: float, liquidation_price: float, stale_mark: bool
) -> LiquidationProximityState:
    if mark_price <= 0 or liquidation_price <= 0:
        return LiquidationProximityState(
            liquidation_class=LiquidationClass.SAFE,
            proximity_ratio=1.0,
            conservative_buffer=1.0,
            stale_mark_caution=stale_mark,
            proof_notes=["No liquidation price available or valid."],
        )

    # Assume long for simplicity in ratio calculation here; abstract logic
    distance = abs(mark_price - liquidation_price) / mark_price

    if distance < 0.02:
        liq_class = LiquidationClass.CRITICAL
    elif distance < 0.05:
        liq_class = LiquidationClass.PROXIMITY
    elif distance < 0.10:
        liq_class = LiquidationClass.WARNING
    else:
        liq_class = LiquidationClass.SAFE

    buffer = distance * 0.8 if stale_mark else distance

    return LiquidationProximityState(
        liquidation_class=liq_class,
        proximity_ratio=distance,
        conservative_buffer=buffer,
        stale_mark_caution=stale_mark,
        proof_notes=[f"Distance: {distance*100:.2f}%. Buffer: {buffer*100:.2f}%"],
    )
