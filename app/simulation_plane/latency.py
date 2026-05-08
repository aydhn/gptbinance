from app.simulation_plane.models import LatencyAssumption


class LatencyModelFactory:
    @staticmethod
    def create_conservative_latency() -> LatencyAssumption:
        return LatencyAssumption(
            model_type="conservative",
            decision_to_order_ms=100,
            caveats=[
                "Conservative latency of 100ms. Approximates typical cloud-to-exchange network conditions."
            ],
        )
