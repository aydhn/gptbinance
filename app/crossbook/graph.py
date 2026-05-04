"""
graph.py
"""
from typing import List
from datetime import datetime, timezone

from app.crossbook.base import ExposureGraphBuilderBase
from app.crossbook.models import (
    ExposureGraphModel,
    BookPositionRef,
    UnifiedExposureEdge,
)
from app.crossbook.mapping import PositionMapper


class ExposureGraphBuilder(ExposureGraphBuilderBase):
    def __init__(self, mapper: PositionMapper):
        self.mapper = mapper

    def build(self, positions: List[BookPositionRef]) -> ExposureGraphModel:
        nodes = self.mapper.map_to_nodes(positions)
        edges: List[UnifiedExposureEdge] = []

        # Example naive edge generation: link assets if they share a quote currency?
        # For crossbook, edges might represent collateral backing or borrow deps.
        for asset, node in nodes.items():
            for pos in node.positions:
                if pos.is_borrowed:
                    edges.append(
                        UnifiedExposureEdge(
                            source_id=node.node_id,
                            target_id="node_USDT",  # Mocking quote dependency
                            edge_type="BORROW_DEPENDENCY",
                            weight=pos.notional,
                        )
                    )

        return ExposureGraphModel(
            nodes=nodes, edges=edges, timestamp=datetime.now(timezone.utc)
        )
