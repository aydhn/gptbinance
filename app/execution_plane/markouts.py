from app.execution_plane.models import MarkoutReport

class MarkoutEvaluator:
    @staticmethod
    def evaluate(spec_id: str, avg_fill_price: float, side: str, market_price_t_plus_n: float, window_ms: int) -> MarkoutReport:
        # Buy: favorable if market_price_t_plus_n > avg_fill_price
        # Sell: favorable if market_price_t_plus_n < avg_fill_price

        if avg_fill_price <= 0:
            return MarkoutReport(spec_id=spec_id, window_ms=window_ms, markout_bps=0.0, is_favorable=False, lineage_ref="invalid_fill_price")

        diff = market_price_t_plus_n - avg_fill_price
        if side.lower() == "buy":
             markout_pct = diff / avg_fill_price
        else:
             markout_pct = -diff / avg_fill_price

        markout_bps = markout_pct * 10000.0
        is_favorable = markout_bps > 0

        return MarkoutReport(
            spec_id=spec_id,
            window_ms=window_ms,
            markout_bps=markout_bps,
            is_favorable=is_favorable,
            lineage_ref="markout_v1"
        )
