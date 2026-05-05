from app.market_truth.models import MarkPriceTruthReport
from app.market_truth.enums import FreshnessClass


class MarkPriceTruthEvaluator:
    def evaluate(self, symbol: str, freshness: FreshnessClass) -> MarkPriceTruthReport:
        stale_caution = freshness in [FreshnessClass.STALE, FreshnessClass.BROKEN]
        return MarkPriceTruthReport(
            symbol=symbol, freshness=freshness, stale_caution=stale_caution
        )
