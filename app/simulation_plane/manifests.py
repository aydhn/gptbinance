from app.simulation_plane.models import (
    AssumptionManifest,
    FillAssumption,
    SlippageAssumption,
    LatencyAssumption,
    FeeFundingAssumption,
    OrderLegalityAssumption,
)


class ManifestBuilder:
    @staticmethod
    def build_default(manifest_id: str) -> AssumptionManifest:
        return AssumptionManifest(
            manifest_id=manifest_id,
            fill=FillAssumption(model_type="touch"),
            slippage=SlippageAssumption(model_type="fixed_bps", value=1.0),
            latency=LatencyAssumption(
                model_type="conservative", decision_to_order_ms=100
            ),
            fee_funding=FeeFundingAssumption(
                includes_fees=True, includes_funding=False
            ),
            legality=OrderLegalityAssumption(enforces_filters=True),
            caveats=["Default builder manifest."],
        )
