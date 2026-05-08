from app.simulation_plane.models import FillAssumption


class FillModelFactory:
    @staticmethod
    def create_touch_fill() -> FillAssumption:
        return FillAssumption(
            model_type="touch",
            caveats=[
                "Touch fill: assumes order is filled as soon as price is touched. Ignores queue priority."
            ],
        )

    @staticmethod
    def create_partial_fill(fill_ratio: float = 0.5) -> FillAssumption:
        return FillAssumption(
            model_type="partial",
            caveats=[f"Partial fill approximation at {fill_ratio}."],
        )
