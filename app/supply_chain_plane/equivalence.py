from typing import List, Dict
from app.supply_chain_plane.models import ComponentRef, SupplyChainEquivalenceReport
from app.supply_chain_plane.enums import EquivalenceVerdict


class EquivalenceEvaluator:
    def evaluate(
        self, component_ref: ComponentRef, environments: List[str]
    ) -> SupplyChainEquivalenceReport:
        # Simplified evaluation
        return SupplyChainEquivalenceReport(
            report_id=f"eq-{component_ref.component_id}",
            component_ref=component_ref,
            environments_compared=environments,
            verdict=EquivalenceVerdict.FULLY_EQUIVALENT,
            divergence_sources=[],
        )
