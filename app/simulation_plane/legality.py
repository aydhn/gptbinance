from app.simulation_plane.models import OrderLegalityAssumption


class LegalityModelFactory:
    @staticmethod
    def create_strict() -> OrderLegalityAssumption:
        return OrderLegalityAssumption(
            enforces_filters=True,
            caveats=["Enforces price/lot/notional filters based on snapshot."],
        )
