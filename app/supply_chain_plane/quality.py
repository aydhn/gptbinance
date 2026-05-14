from app.supply_chain_plane.models import ComponentRef


class SupplyChainQualityEvaluator:
    def evaluate(self, component_ref: ComponentRef) -> dict:
        return {"quality_verdict": "High", "warnings": []}
