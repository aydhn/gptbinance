from app.stressrisk.models import StressScenario, ShockVector
from app.stressrisk.enums import (
    ScenarioType,
    StressSource,
    ScenarioConfidence,
    ShockType,
)


class HistoricalStressLibrary:
    def load_preset(self, window_name: str) -> StressScenario:
        if window_name == "march_2020_covid":
            return StressScenario(
                scenario_id="historical_march_2020",
                name="March 2020 Covid Crash",
                scenario_type=ScenarioType.PRICE_GAP,
                source=StressSource.HISTORICAL,
                confidence=ScenarioConfidence.HIGH,
                shocks=[ShockVector(shock_type=ShockType.PRICE, value_multiplier=0.5)],
                applicable_profiles=["all"],
                description="Replay of the extreme 50% drawdown.",
                expected_weak_points=["liquidation", "correlation"],
            )
        raise ValueError(f"Unknown historical preset: {window_name}")
