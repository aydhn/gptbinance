from app.postmortems.models import CausalGraph, CausalNode, CausalEdge
from typing import Any


class CausalGraphBuilder:
    def build(self, chronology: Any, evidence: Any) -> CausalGraph:
        nodes = []
        edges = []

        # Based on chronology and evidence, map causal relations
        if chronology and getattr(chronology, "events", None):
            for i, evt in enumerate(chronology.events):
                node_id = f"evt_{i}"
                nodes.append(
                    CausalNode(
                        node_id=node_id,
                        description=evt.description,
                        node_type="trigger" if i == 0 else "contributor",
                    )
                )
                if i > 0:
                    edges.append(
                        CausalEdge(
                            source_id=f"evt_{i-1}",
                            target_id=node_id,
                            relationship="led_to",
                        )
                    )

        return CausalGraph(nodes=nodes, edges=edges)
