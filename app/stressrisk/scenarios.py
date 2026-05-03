from app.stressrisk.models import StressScenario, ShockVector, StressScenarioSet
from app.stressrisk.enums import (
    ScenarioType,
    StressSource,
    ScenarioConfidence,
    ShockType,
)


class ScenarioRegistry:
    def __init__(self):
        self.scenarios = {
            "macro_gap_down": StressScenario(
                scenario_id="macro_gap_down",
                name="Macro Gap Down",
                scenario_type=ScenarioType.PRICE_GAP,
                source=StressSource.HYPOTHETICAL,
                confidence=ScenarioConfidence.HIGH,
                shocks=[ShockVector(shock_type=ShockType.PRICE, value_multiplier=0.8)],
                applicable_profiles=[
                    "live",
                    "paper",
                    "testnet",
                    "canary_live_caution",
                    "derivatives_testnet",
                ],
                description="Sudden 20% drop across the board.",
            ),
            "exchange_liquidity_freeze": StressScenario(
                scenario_id="exchange_liquidity_freeze",
                name="Exchange Liquidity Freeze",
                scenario_type=ScenarioType.LIQUIDITY_SHOCK,
                source=StressSource.HYPOTHETICAL,
                confidence=ScenarioConfidence.MEDIUM,
                shocks=[
                    ShockVector(shock_type=ShockType.LIQUIDITY, value_multiplier=0.1),
                    ShockVector(shock_type=ShockType.SPREAD, value_multiplier=5.0),
                ],
                applicable_profiles=[
                    "live",
                    "paper",
                    "testnet",
                    "canary_live_caution",
                    "derivatives_testnet",
                ],
                description="Liquidity drops 90%, spreads widen 5x.",
            ),
            "correlation_spike": StressScenario(
                scenario_id="correlation_spike",
                name="Correlation Spike",
                scenario_type=ScenarioType.CORRELATION_SPIKE,
                source=StressSource.HISTORICAL,
                confidence=ScenarioConfidence.HIGH,
                shocks=[
                    ShockVector(shock_type=ShockType.CORRELATION, absolute_addition=0.5)
                ],
                applicable_profiles=[
                    "live",
                    "paper",
                    "testnet",
                    "canary_live_caution",
                    "derivatives_testnet",
                ],
                description="Correlations approach 1.0, breaking diversification.",
            ),
            "funding_burden_spike": StressScenario(
                scenario_id="funding_burden_spike",
                name="Funding Burden Spike",
                scenario_type=ScenarioType.FUNDING_SPIKE,
                source=StressSource.HYPOTHETICAL,
                confidence=ScenarioConfidence.MEDIUM,
                shocks=[
                    ShockVector(shock_type=ShockType.FUNDING, value_multiplier=10.0)
                ],
                applicable_profiles=["derivatives_testnet", "paper"],
                description="Funding rates spike 10x.",
            ),
        }

    def get_scenario(self, scenario_id: str) -> StressScenario:
        return self.scenarios.get(scenario_id)

    def get_default_set(self) -> StressScenarioSet:
        return StressScenarioSet(
            set_id="default_tail_set",
            scenarios=list(self.scenarios.values()),
            description="Default tail risk scenario set.",
        )
