class VolatilityAdjuster:
    def get_multiplier(self, volatility_ratio: float) -> float:
        """
        volatility_ratio: e.g., current_atr / historical_atr.
        If current is very high (ratio > 1.5), we shrink size.
        """
        if volatility_ratio > 2.0:
            return 0.5
        elif volatility_ratio > 1.5:
            return 0.75
        elif volatility_ratio < 0.5:
            return 1.25  # Slightly relax if very quiet, though usually we want to stay conservative
        return 1.0
