"""
mapping.py
"""
from typing import List, Dict
from app.crossbook.models import BookPositionRef, UnifiedExposureNode


class PositionMapper:
    def map_to_nodes(
        self, positions: List[BookPositionRef]
    ) -> Dict[str, UnifiedExposureNode]:
        nodes: Dict[str, UnifiedExposureNode] = {}
        for pos in positions:
            asset = pos.asset
            if asset not in nodes:
                nodes[asset] = UnifiedExposureNode(
                    node_id=f"node_{asset}",
                    asset=asset,
                    positions=[],
                    total_quantity=0.0,
                    total_notional=0.0,
                )

            nodes[asset].positions.append(pos)
            nodes[asset].total_quantity += pos.quantity
            nodes[asset].total_notional += pos.notional

        return nodes

    def extract_canonical_asset(self, symbol: str) -> str:
        # A simple naive canonical extraction
        if symbol.endswith("USDT"):
            return symbol[:-4]
        if symbol.endswith("BUSD"):
            return symbol[:-4]
        return symbol
