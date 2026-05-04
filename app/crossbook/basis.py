"""
basis.py
"""
from typing import List
from app.crossbook.models import ExposureGraphModel, BasisExposureReport
from app.crossbook.enums import BookType


class BasisAnalyzer:
    def analyze(self, graph: ExposureGraphModel) -> List[BasisExposureReport]:
        reports: List[BasisExposureReport] = []

        for asset, node in graph.nodes.items():
            has_spot = any(p.book_type == BookType.SPOT for p in node.positions)
            has_futures = any(p.book_type == BookType.FUTURES for p in node.positions)

            if has_spot and has_futures:
                # Mock basis logic
                reports.append(
                    BasisExposureReport(
                        asset=asset, basis_spread=0.001, is_widening=False
                    )
                )
        return reports
