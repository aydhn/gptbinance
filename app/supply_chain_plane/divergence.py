from app.supply_chain_plane.models import ComponentRef, SupplyChainDivergenceReport


class DivergenceEvaluator:
    def evaluate(
        self, component_ref: ComponentRef, env1: str, env2: str
    ) -> SupplyChainDivergenceReport:
        return SupplyChainDivergenceReport(
            report_id=f"div-{component_ref.component_id}",
            component_ref=component_ref,
            divergence_type="None",
            severity="None",
            blast_radius="None",
        )
