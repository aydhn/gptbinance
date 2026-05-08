from pydantic import BaseModel


class VolatilityRegimeState(BaseModel):
    symbol: str
    realized_volatility: float
    stressed_band_multiplier: float
    is_noisy_tape: bool


def adjust_limit_by_volatility(
    base_limit: float, regime: VolatilityRegimeState
) -> float:
    # Tighten risk limit if volatility is extremely high
    if regime.stressed_band_multiplier > 1.5:
        return base_limit * 0.5
    return base_limit
