from app.simulation_plane.models import SlippageAssumption


class SlippageModelFactory:
    @staticmethod
    def create_fixed_bps(bps: float) -> SlippageAssumption:
        return SlippageAssumption(
            model_type="fixed_bps", value=bps, caveats=[f"Fixed slippage of {bps} bps."]
        )

    @staticmethod
    def create_volatility_aware() -> SlippageAssumption:
        return SlippageAssumption(
            model_type="volatility_aware",
            value=0.0,  # Dynamically calculated
            caveats=[
                "Volatility-aware slippage. Depends on exact market depth simulation."
            ],
        )
