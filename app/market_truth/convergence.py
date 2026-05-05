from app.market_truth.base import ConvergenceCheckerBase
from app.market_truth.models import StreamConvergenceReport
from app.market_truth.enums import StreamType, ConvergenceVerdict


class WebsocketRestConvergenceEngine(ConvergenceCheckerBase):
    def check_convergence(
        self, stream_data: dict, snapshot_data: dict
    ) -> StreamConvergenceReport:
        # Example simplistic check for stream-snapshot convergence
        stream_val = stream_data.get("price", 0)
        snap_val = snapshot_data.get("price", 0)

        diff = (
            abs(float(stream_val) - float(snap_val))
            if stream_val and snap_val
            else 100.0
        )

        verdict = ConvergenceVerdict.ALIGNED
        if diff > 0.05:  # Arbitrary small tolerance
            verdict = ConvergenceVerdict.TRANSIENT_DIVERGENCE

        return StreamConvergenceReport(
            symbol=stream_data.get("symbol", "UNKNOWN"),
            stream_type=StreamType.TRADE,
            verdict=verdict,
            divergence_magnitude=diff,
        )
