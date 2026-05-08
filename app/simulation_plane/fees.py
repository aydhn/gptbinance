from app.simulation_plane.models import FeeFundingAssumption


class FeeFundingModelFactory:
    @staticmethod
    def create_default(futures: bool = False) -> FeeFundingAssumption:
        return FeeFundingAssumption(
            includes_fees=True,
            includes_funding=futures,
            caveats=["Includes standard tier maker/taker fees."]
            + (["Includes funding approximation."] if futures else []),
        )
