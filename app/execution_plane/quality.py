from app.execution_plane.models import SlippageReport, MarkoutReport, FillQualityReport
from app.execution_plane.enums import FillQualityClass, SlippageSeverityClass
from app.performance_plane.enums import DragClass
from app.performance_plane.components import ComponentRegistry
from decimal import Decimal


class ExecutionQualityEngine:
    @staticmethod
    def synthesize(
        fill_report: FillQualityReport,
        slippage_report: SlippageReport,
        markout_report: MarkoutReport,
    ) -> dict:
        score = 100

        if fill_report.quality_class in [
            FillQualityClass.POOR,
            FillQualityClass.UNACCEPTABLE,
        ]:
            score -= 40
        elif fill_report.quality_class == FillQualityClass.DEGRADED:
            score -= 20

        if slippage_report.severity == SlippageSeverityClass.CRITICAL:
            score -= 50
        elif slippage_report.severity == SlippageSeverityClass.ELEVATED:
            score -= 20

        if not markout_report.is_favorable and markout_report.markout_bps < -10.0:
            score -= 10

        overall_verdict = "healthy"
        if score < 50:
            overall_verdict = "degraded"
        if score < 20:
            overall_verdict = "critical_failure"

        return {
            "score": score,
            "overall_verdict": overall_verdict,
            "fill_quality": fill_report.quality_class.value,
            "slippage_severity": slippage_report.severity.value,
            "markout_is_favorable": markout_report.is_favorable,
        }

    @staticmethod
    def export_performance_drags(
        fill_report: FillQualityReport,
        slippage_report: SlippageReport,
        markout_report: MarkoutReport,
        volume: Decimal,
        currency: str,
    ):
        drags = []
        # Calculate impact approximations based on volume and bps
        if slippage_report.realized_slippage_bps > 0:
            slip_impact = (
                volume
                * Decimal(str(slippage_report.realized_slippage_bps))
                / Decimal("10000.0")
            )
            drags.append(
                ComponentRegistry.register_drag(
                    drag_class=DragClass.SLIPPAGE,
                    impact_value=-slip_impact,
                    currency=currency,
                    lineage_refs=[slippage_report.spec_id],
                )
            )

        if not markout_report.is_favorable:
            markout_impact = (
                volume
                * Decimal(str(abs(markout_report.markout_bps)))
                / Decimal("10000.0")
            )
            drags.append(
                ComponentRegistry.register_drag(
                    drag_class=DragClass.MARKOUT,
                    impact_value=-markout_impact,
                    currency=currency,
                    lineage_refs=[markout_report.spec_id],
                )
            )

        return drags
