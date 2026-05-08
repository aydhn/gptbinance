from app.execution_plane.models import SlippageReport, MarkoutReport, FillQualityReport
from app.execution_plane.enums import FillQualityClass, SlippageSeverityClass

class ExecutionQualityEngine:
    @staticmethod
    def synthesize(fill_report: FillQualityReport, slippage_report: SlippageReport, markout_report: MarkoutReport) -> dict:
        score = 100

        if fill_report.quality_class in [FillQualityClass.POOR, FillQualityClass.UNACCEPTABLE]:
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
            "markout_is_favorable": markout_report.is_favorable
        }
