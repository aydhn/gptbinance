from app.simulation_plane.models import AssumptionManifest
from typing import List


class AssumptionEvaluator:
    def evaluate(self, manifest: AssumptionManifest) -> List[str]:
        caveats = []
        if manifest.latency.decision_to_order_ms == 0:
            caveats.append(
                "Zero latency assumption detected. Unrealistic for live execution."
            )

        if manifest.slippage.value == 0.0:
            caveats.append(
                "Zero slippage assumption detected. Unrealistic for live execution."
            )

        if not manifest.fee_funding.includes_fees:
            caveats.append("Fees are excluded. Expected returns will be overstated.")

        if not manifest.fee_funding.includes_funding:
            caveats.append("Funding rates are excluded. Relevant for futures.")

        if not manifest.legality.enforces_filters:
            caveats.append("Venue filters not enforced. Orders may be invalid in live.")

        return caveats + manifest.caveats
