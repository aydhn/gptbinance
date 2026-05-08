
from app.position_plane.models import (
    PositionState,
    PositionExposureView,
    PositionPnLBreakdown,
    PositionDivergenceReport,
    PositionTrustVerdict,
)


class PositionReporter:
    @staticmethod
    def format_state(state: PositionState) -> str:
        return f"Position[{state.symbol}]: {state.side.value} {state.quantity} @ {state.average_entry_price} (State: {state.lifecycle_state.value})"

    @staticmethod
    def format_exposures(exposure: PositionExposureView) -> str:
        return f"Exposures[{exposure.symbol}]: Gross: {exposure.gross_exposure}, Net: {exposure.net_directional_exposure}, HedgeAdj: {exposure.hedge_adjusted_exposure}"

    @staticmethod
    def format_pnl(pnl: PositionPnLBreakdown) -> str:
        return f"PnL[{pnl.symbol}]: Realized: {pnl.realized_pnl}, Unrealized: {pnl.unrealized_pnl}, Fees: {pnl.total_fees}"

    @staticmethod
    def format_divergence(report: PositionDivergenceReport) -> str:
        return f"Divergence[{report.symbol}]: {report.severity.value} - {report.description}"

    @staticmethod
    def format_trust(verdict: PositionTrustVerdict) -> str:
        reasons = ", ".join(verdict.reasons) if verdict.reasons else "None"
        return f"TrustVerdict[{verdict.symbol}]: {verdict.verdict.value} (Reasons: {reasons})"
