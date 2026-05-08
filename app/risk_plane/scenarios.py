import uuid
from typing import List
from .models import RiskScenarioView


def generate_risk_scenarios(
    exposure: float, margin_usage: float
) -> List[RiskScenarioView]:
    scenarios = []

    # Gap down 10%
    impact = abs(exposure) * 0.10
    scenarios.append(
        RiskScenarioView(
            scenario_id=str(uuid.uuid4()),
            description="Gap down 10% market move",
            burden_summary=f"Drawdown burden: {impact:.2f}, Margin Pressure +{margin_usage*1.2:.2f}",
            evidence_refs=["scenario_engine"],
        )
    )

    # Collateral haircut
    scenarios.append(
        RiskScenarioView(
            scenario_id=str(uuid.uuid4()),
            description="Collateral 20% haircut",
            burden_summary="Reduces usable collateral by 20%, significantly increasing liquidation proximity.",
            evidence_refs=["collateral_stress"],
        )
    )

    return scenarios
