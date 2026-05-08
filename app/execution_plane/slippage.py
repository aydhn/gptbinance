from app.execution_plane.models import SlippageReport
from app.execution_plane.enums import SlippageSeverityClass
from app.performance_plane.components import ComponentRegistry
from app.performance_plane.enums import DragClass
from decimal import Decimal


class SlippageEvaluator:
    @staticmethod
    def evaluate(
        spec_id: str, expected_price: float, avg_fill_price: float, side: str
    ) -> SlippageReport:
        if expected_price <= 0:
            return SlippageReport(
                spec_id=spec_id,
                expected_slippage_bps=0.0,
                realized_slippage_bps=0.0,
                severity=SlippageSeverityClass.NONE,
                evidence_ref="invalid_expected_price",
            )

        diff = expected_price - avg_fill_price
        # For buy: higher fill price = adverse slippage
        # For sell: lower fill price = adverse slippage
        if side.lower() == "buy":
            slippage_pct = -diff / expected_price
        else:
            slippage_pct = diff / expected_price

        realized_bps = slippage_pct * 10000.0

        severity = SlippageSeverityClass.NONE
        if realized_bps > 50:
            severity = SlippageSeverityClass.CRITICAL
        elif realized_bps > 20:
            severity = SlippageSeverityClass.ELEVATED
        elif realized_bps > 5:
            severity = SlippageSeverityClass.MILD

        return SlippageReport(
            spec_id=spec_id,
            expected_slippage_bps=5.0,  # Dummy expected
            realized_slippage_bps=realized_bps,
            severity=severity,
            evidence_ref="calc_v1",
        )

    @staticmethod
    def export_drag(report: SlippageReport, volume: float, currency: str):
        impact = (
            Decimal(str(volume))
            * Decimal(str(report.realized_slippage_bps))
            / Decimal("10000.0")
        )
        return ComponentRegistry.register_drag(
            drag_class=DragClass.SLIPPAGE,
            impact_value=-impact,
            currency=currency,
            lineage_refs=[report.spec_id],
        )
