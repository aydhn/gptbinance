class MarketTruthVerdict:
    def get_truthfulness(self, symbol: str) -> bool:
        # Market truth posture -> allocation clipping/defer/reject input
        return True

class MarketTruthContext:
    """Provides staleness and freshness surfaces for execution trust."""
    @staticmethod
    def get_truth_verdict(symbol: str) -> dict:
        # Stub
        return {"is_fresh": True, "stale_quotes": False, "thin_liquidity": False}
