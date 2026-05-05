from app.market_truth.models import TradeTruthReport


class TradeTruthEvaluator:
    def evaluate(
        self, symbol: str, is_monotonic: bool, silence_ms: float, max_silence: float
    ) -> TradeTruthReport:
        return TradeTruthReport(
            symbol=symbol,
            trade_continuity=is_monotonic,
            stale_silence=(silence_ms > max_silence),
        )
