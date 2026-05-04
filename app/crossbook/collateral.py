"""
collateral.py
"""
from typing import List
from app.crossbook.base import CollateralAnalyzerBase
from app.crossbook.models import (
    ExposureGraphModel,
    CollateralPressureReport,
    CollateralDependency,
)
from app.crossbook.enums import MarginMode


class CollateralAnalyzer(CollateralAnalyzerBase):
    def analyze(self, graph: ExposureGraphModel) -> CollateralPressureReport:
        deps: List[CollateralDependency] = []
        total_locked = 0.0
        total_usable = 0.0

        for asset, node in graph.nodes.items():
            locked = sum(
                p.notional
                for p in node.positions
                if p.margin_mode != MarginMode.NONE and p.quantity > 0
            )
            # Naive usability mocking
            usable = locked * 0.2 if locked > 0 else 0.0

            total_locked += locked
            total_usable += usable

            if locked > 0:
                deps.append(
                    CollateralDependency(
                        asset=asset,
                        locked_amount=locked,
                        usable_amount=usable,
                        is_cross=True,  # Mocked
                    )
                )

        ratio = (
            total_locked / (total_locked + total_usable)
            if (total_locked + total_usable) > 0
            else 0.0
        )

        return CollateralPressureReport(
            total_locked=total_locked,
            total_usable=total_usable,
            pressure_ratio=ratio,
            dependencies=deps,
        )
