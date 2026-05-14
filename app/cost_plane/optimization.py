from app.cost_plane.models import OptimizationOpportunity
import uuid

class OptimizationManager:
    def __init__(self):
        self._opportunities: list[OptimizationOpportunity] = []

    def record_opportunity(self, cost_id: str, description: str, estimated_savings: float, currency: str, side_effect_caveats: list[str]) -> OptimizationOpportunity:
        opp = OptimizationOpportunity(
            opportunity_id=str(uuid.uuid4()),
            cost_id=cost_id,
            description=description,
            estimated_savings=estimated_savings,
            currency=currency,
            side_effect_caveats=side_effect_caveats
        )
        self._opportunities.append(opp)
        return opp

    def list_opportunities(self) -> list[OptimizationOpportunity]:
        return self._opportunities
