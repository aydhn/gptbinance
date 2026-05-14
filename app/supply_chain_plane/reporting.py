from typing import List, Dict, Any
from app.supply_chain_plane.models import ComponentDefinition, SupplyChainTrustVerdict


class SupplyChainReporter:
    def format_component_summary(self, components: List[ComponentDefinition]) -> str:
        lines = ["=== SUPPLY CHAIN COMPONENT REGISTRY ==="]
        for c in components:
            lines.append(f"- [{c.component_class.name}] {c.component_id} ({c.name})")
            lines.append(f"  Owner: {c.owner} | Criticality: {c.criticality}")
            lines.append(f"  Envs: {', '.join(c.supported_environments)}")
        return "\n".join(lines)

    def format_trust_verdict(self, verdict: SupplyChainTrustVerdict) -> str:
        lines = [f"=== TRUST VERDICT FOR {verdict.component_ref.component_id} ==="]
        lines.append(f"Verdict: {verdict.verdict.name}")
        lines.append("Breakdown:")
        for k, v in verdict.breakdown.items():
            lines.append(f"  - {k}: {v}")
        return "\n".join(lines)
