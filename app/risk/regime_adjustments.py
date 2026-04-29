from app.risk.enums import RegimeRiskMode


class RegimeAdjuster:
    def get_multiplier(self, mode: RegimeRiskMode) -> float:
        if mode == RegimeRiskMode.CAUTION:
            return 0.5
        elif mode == RegimeRiskMode.RESTRICTIVE:
            return 0.25
        return 1.0
