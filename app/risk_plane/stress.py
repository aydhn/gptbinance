from pydantic import BaseModel


class StressScenarioResult(BaseModel):
    scenario_name: str
    simulated_drawdown: float
    collateral_haircut_impact: float
    margin_call_proximity: float


def run_gap_stress_scenario(
    current_value: float, exposure: float, gap_percent: float = -0.10
) -> StressScenarioResult:
    impact = abs(exposure) * gap_percent
    return StressScenarioResult(
        scenario_name=f"Gap {gap_percent*100:.1f}%",
        simulated_drawdown=abs(impact),
        collateral_haircut_impact=0.0,
        margin_call_proximity=0.0,  # simplified
    )
