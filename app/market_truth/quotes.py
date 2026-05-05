from app.market_truth.models import QuoteTruthReport
from app.market_truth.enums import FreshnessClass


class QuoteTruthEvaluator:
    def evaluate(
        self, symbol: str, bid: float, ask: float, freshness: FreshnessClass
    ) -> QuoteTruthReport:
        crossed = bid >= ask if bid > 0 and ask > 0 else False
        return QuoteTruthReport(
            symbol=symbol, freshness=freshness, crossed_suspicion=crossed
        )
