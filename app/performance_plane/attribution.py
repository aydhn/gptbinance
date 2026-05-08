from decimal import Decimal
import uuid
from typing import List

from app.performance_plane.models import AttributionTree, AttributionNode, ReturnSurface
from app.performance_plane.enums import AttributionClass


class AttributionTreeBuilder:
    def __init__(self, surface: ReturnSurface):
        self.surface = surface
        self.nodes: List[AttributionNode] = []

    def add_node(
        self,
        attribution_class: AttributionClass,
        value: Decimal,
        proof_notes: List[str] = None,
    ):
        self.nodes.append(
            AttributionNode(
                attribution_class=attribution_class,
                contribution_value=value,
                currency=self.surface.currency,
                proof_notes=proof_notes or [],
            )
        )

    def build(self) -> AttributionTree:
        explained_value = sum(node.contribution_value for node in self.nodes)
        residual = self.surface.value - explained_value

        return AttributionTree(
            tree_id=str(uuid.uuid4()),
            surface_id=self.surface.surface_id,
            nodes=self.nodes,
            residual_value=residual,
            currency=self.surface.currency,
        )
