from typing import Any
from app.postmortems.models import ContributingFactor
from typing import List


class ContributingFactorsRegistry:
    def identify_factors(self, causal_graph: Any) -> List[ContributingFactor]:
        factors = []
        if causal_graph and hasattr(causal_graph, "nodes"):
            for node in causal_graph.nodes:
                if node.node_type == "contributor":
                    factors.append(
                        ContributingFactor(
                            factor_id=f"cf_{node.node_id}",
                            description=f"Contributing factor: {node.description}",
                            severity="medium",
                        )
                    )
        return factors
