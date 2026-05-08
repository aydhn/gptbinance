import uuid
from typing import List, Dict, Any
from app.performance_plane.models import AttributionNode
from app.performance_plane.enums import AttributionClass
from decimal import Decimal


class StrategyEngine:
    @staticmethod
    def execute(strategy_id: str, context: Dict[str, Any]) -> dict:
        # Dummy execution
        return {"strategy_id": strategy_id, "status": "executed"}

    @staticmethod
    def export_signal_attribution(
        strategy_id: str, pnl_impact: Decimal, currency: str
    ) -> AttributionNode:
        return AttributionNode(
            attribution_class=AttributionClass.SIGNAL_SELECTION,
            contribution_value=pnl_impact,
            currency=currency,
            proof_notes=[f"Signal generation by strategy {strategy_id}"],
        )
