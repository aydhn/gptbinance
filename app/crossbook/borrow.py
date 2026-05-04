"""
borrow.py
"""
from typing import Dict
from app.crossbook.models import ExposureGraphModel, BorrowDependencyReport
from app.crossbook.enums import BorrowDependencyClass


class BorrowAnalyzer:
    def analyze(self, graph: ExposureGraphModel) -> BorrowDependencyReport:
        borrowed: Dict[str, float] = {}
        total = 0.0

        for asset, node in graph.nodes.items():
            b_amount = sum(abs(p.notional) for p in node.positions if p.is_borrowed)
            if b_amount > 0:
                borrowed[asset] = b_amount
                total += b_amount

        dep_class = BorrowDependencyClass.NONE
        if total > 50000:
            dep_class = BorrowDependencyClass.HIGH
        elif total > 10000:
            dep_class = BorrowDependencyClass.MODERATE

        return BorrowDependencyReport(
            borrowed_assets=borrowed,
            dependency_class=dep_class,
            total_borrow_value=total,
        )
