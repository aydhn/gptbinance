from typing import List, Dict, Any
from app.portfolio.models import PortfolioCandidate, PortfolioContext, OverlapReport
from app.portfolio.base import BaseOverlapEstimator
from app.portfolio.enums import OverlapType
from app.backtest.enums import OrderSide


class OverlapEstimator(BaseOverlapEstimator):
    def estimate_overlap(
        self, candidate: PortfolioCandidate, context: PortfolioContext
    ) -> OverlapReport:
        intent = candidate.intent
        symbol = intent.symbol
        side = intent.side

        overlapping_symbols = []
        severity = 0.0
        o_type = OverlapType.NONE

        # 1. Same Symbol Same Direction Check
        sleeve = context.symbol_sleeves.get(symbol)
        if sleeve and sleeve.used_notional > 0:
            # We assume used_notional here is absolute, but if we had directional exposure:
            # Since we only have gross used_notional in this simple sleeve, we assume it's overlapping.
            overlapping_symbols.append(symbol)
            o_type = OverlapType.SAME_SYMBOL_SAME_DIR
            severity = 5.0

        # 2. Correlated Cluster Check
        if o_type == OverlapType.NONE:
            for c_id, symbols in context.correlation.clusters.items():
                if symbol in symbols:
                    for s in symbols:
                        if s != symbol:
                            slv = context.symbol_sleeves.get(s)
                            if slv and slv.used_notional > 0:
                                overlapping_symbols.append(s)

                    if overlapping_symbols:
                        o_type = OverlapType.HIGH_CORR_SAME_DIR
                        severity = 3.0
                        break

        # Generate report
        report = OverlapReport(
            intent_id=intent.symbol,  # fallback
            overlap_type=o_type,
            overlapping_symbols=overlapping_symbols,
            overlap_severity_score=severity,
        )
        return report
