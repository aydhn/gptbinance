"""
funding.py
"""
from typing import List
from app.crossbook.models import ExposureGraphModel, FundingBurdenOverlay
from app.crossbook.enums import FundingBurdenClass, BookType


class FundingAnalyzer:
    def analyze(self, graph: ExposureGraphModel) -> FundingBurdenOverlay:
        symbols: List[str] = []
        total_drag = 0.0

        for asset, node in graph.nodes.items():
            futures_notional = sum(
                abs(p.notional)
                for p in node.positions
                if p.book_type == BookType.FUTURES
            )
            if futures_notional > 0:
                symbols.append(f"{asset}USDT")  # naive
                total_drag += futures_notional * 0.0001  # mock rate

        fbc = FundingBurdenClass.NEGLIGIBLE
        if total_drag > 100:
            fbc = FundingBurdenClass.NOTICEABLE
        if total_drag > 500:
            fbc = FundingBurdenClass.SEVERE

        return FundingBurdenOverlay(
            burden_class=fbc, symbols=symbols, total_expected_drag=total_drag
        )
