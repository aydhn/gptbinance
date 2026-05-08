from typing import List
from pydantic import BaseModel


class RiskFacingExposure(BaseModel):
    gross_exposure: float
    net_exposure: float
    hedge_adjusted_exposure: float
    sleeve_exposure: float
    caveats: List[str]
    lineage_refs: List[str]


def calculate_risk_facing_exposure(
    positions: List[dict], fake_hedge_masking_allowed: bool = False
) -> RiskFacingExposure:
    gross = sum(abs(p.get("notional", 0.0)) for p in positions)
    net = sum(p.get("notional", 0.0) for p in positions)
    sleeve = gross  # Simplified

    caveats = []
    if not fake_hedge_masking_allowed and abs(net) < gross:
        caveats.append(
            "Hedge masking disabled; using gross exposure for conservative risk limits."
        )
        hedge_adj = gross
    else:
        hedge_adj = abs(net)

    return RiskFacingExposure(
        gross_exposure=gross,
        net_exposure=net,
        hedge_adjusted_exposure=hedge_adj,
        sleeve_exposure=sleeve,
        caveats=caveats,
        lineage_refs=[p.get("position_id", "unknown") for p in positions],
    )
