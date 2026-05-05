from app.market_truth.models import KlineTruthReport


class KlineTruthEvaluator:
    def evaluate(
        self,
        symbol: str,
        interval: str,
        expected_close_time: int,
        actual_close_time: int,
        missing_bars: int,
    ) -> KlineTruthReport:
        is_aligned = abs(expected_close_time - actual_close_time) < 1000  # 1s tolerance
        return KlineTruthReport(
            symbol=symbol,
            interval=interval,
            is_aligned=is_aligned,
            missing_bars=missing_bars,
        )
