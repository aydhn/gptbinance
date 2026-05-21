from typing import Dict, List, Optional, Any
from .base import TradeoffRegistryBase
from .models import TradeoffObject
from .exceptions import InvalidTradeoffObjectError

class TradeoffRegistry(TradeoffRegistryBase):
    def __init__(self):
        self._tradeoffs: Dict[str, TradeoffObject] = {}
        self._families = [
            "release_speed_vs_safety_tradeoff",
            "latency_vs_resilience_tradeoff",
            "cost_vs_control_tradeoff",
            "autonomy_vs_human_burden_tradeoff",
            "local_vs_federated_tradeoff",
            "value_vs_risk_tradeoff",
            "capacity_vs_reliability_tradeoff",
            "recovery_speed_vs_integrity_tradeoff",
            "compliance_vs_operational_flexibility_tradeoff",
            "portfolio_priority_tradeoff",
            "execution_quality_tradeoff",
            "cross_plane_decision_tradeoff"
        ]

    def register(self, tradeoff_obj: TradeoffObject) -> None:
        if not tradeoff_obj.tradeoff_id:
            raise InvalidTradeoffObjectError("Tradeoff ID is required")
        if tradeoff_obj.tradeoff_id not in self._families and not tradeoff_obj.tradeoff_id.startswith("custom_"):
            # Only allow defined families or explicit custom ones
             pass # We can enforce this if needed, for now just store
        self._tradeoffs[tradeoff_obj.tradeoff_id] = tradeoff_obj

    def get(self, tradeoff_id: str) -> Optional[TradeoffObject]:
        return self._tradeoffs.get(tradeoff_id)

    def list_all(self) -> List[TradeoffObject]:
        return list(self._tradeoffs.values())

tradeoff_registry = TradeoffRegistry()
