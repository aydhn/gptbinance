from .models import FundingBurdenOverlay
from .enums import FundingBurdenClass

class FundingAnalyzer:
    def analyze(self, symbol: str) -> FundingBurdenOverlay:
        return FundingBurdenOverlay(symbol=symbol, expected_drag_usd_per_day=0.0, burden_class=FundingBurdenClass.NEGLIGIBLE)
