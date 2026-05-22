from app.commitment_plane.models import CommitmentForecastReport

class ForecastingManager:
    @staticmethod
    def create_forecast(forecast_type: str, description: str, uncertainty_class: str) -> CommitmentForecastReport:
        valid_types = ['breach_likelihood', 'owner_overload', 'deadline_slip', 'relief_overuse', 'asymmetry_growth']
        if forecast_type not in valid_types:
            raise ValueError(f"Invalid forecast type. Must be one of {valid_types}")

        return CommitmentForecastReport(
            forecast_type=forecast_type,
            description=description,
            uncertainty_class=uncertainty_class
        )
