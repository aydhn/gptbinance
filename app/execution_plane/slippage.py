from app.execution_plane.models import SlippageReport
from app.execution_plane.enums import SlippageSeverityClass

class SlippageEvaluator:
    @staticmethod
    def evaluate(spec_id: str, expected_price: float, avg_fill_price: float, side: str) -> SlippageReport:
        if expected_price <= 0:
            return SlippageReport(
                spec_id=spec_id, expected_slippage_bps=0.0, realized_slippage_bps=0.0,
                severity=SlippageSeverityClass.NONE, evidence_ref="invalid_expected_price"
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
            expected_slippage_bps=5.0, # Dummy expected
            realized_slippage_bps=realized_bps,
            severity=severity,
            evidence_ref="calc_v1"
        )
