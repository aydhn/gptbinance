from app.execution_plane.models import MarkoutReport
from app.performance_plane.components import ComponentRegistry
from app.performance_plane.enums import DragClass
from decimal import Decimal


class MarkoutEvaluator:
    @staticmethod
    def evaluate(
        spec_id: str,
        avg_fill_price: float,
        side: str,
        market_price_t_plus_n: float,
        window_ms: int,
    ) -> MarkoutReport:
        # Buy: favorable if market_price_t_plus_n > avg_fill_price
        # Sell: favorable if market_price_t_plus_n < avg_fill_price

        if avg_fill_price <= 0:
            return MarkoutReport(
                spec_id=spec_id,
                window_ms=window_ms,
                markout_bps=0.0,
                is_favorable=False,
                lineage_ref="invalid_fill_price",
            )

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
            lineage_ref="markout_v1",
        )

    @staticmethod
    def export_drag(report: MarkoutReport, volume: float, currency: str):
        if report.is_favorable:
            return None

        impact = (
            Decimal(str(volume))
            * Decimal(str(abs(report.markout_bps)))
            / Decimal("10000.0")
        )
        return ComponentRegistry.register_drag(
            drag_class=DragClass.MARKOUT,
            impact_value=-impact,
            currency=currency,
            lineage_refs=[report.spec_id],
        )
