from datetime import datetime
from typing import Dict, List, Any
from app.portfolio.models import (
    ConcentrationSnapshot,
    PortfolioContext,
    PortfolioConfig,
)
from app.portfolio.enums import ConcentrationSeverity


class ConcentrationEvaluator:
    def __init__(self, config: PortfolioConfig):
        self.config = config

    def evaluate(
        self, context: PortfolioContext, timestamp: datetime
    ) -> ConcentrationSnapshot:
        symbol_conc = {}
        strategy_conc = {}
        cluster_conc = {}
        breaches = []
        severity = ConcentrationSeverity.NORMAL

        total_budget = context.budget.total_capital

        if total_budget > 0:
            # Symbol
            for sym, slv in context.symbol_sleeves.items():
                weight = slv.used_notional / total_budget
                symbol_conc[sym] = weight
                if weight > self.config.max_symbol_weight:
                    breaches.append(
                        f"Symbol {sym} weight {weight:.2f} > {self.config.max_symbol_weight:.2f}"
                    )
                    severity = ConcentrationSeverity.BREACH
                elif weight > self.config.max_symbol_weight * 0.8:
                    if severity != ConcentrationSeverity.BREACH:
                        severity = ConcentrationSeverity.CAUTION

            # Strategy
            for strat, slv in context.strategy_sleeves.items():
                weight = slv.used_notional / total_budget
                strategy_conc[strat] = weight
                if weight > self.config.max_strategy_sleeve_weight:
                    breaches.append(
                        f"Strategy {strat} weight {weight:.2f} > {self.config.max_strategy_sleeve_weight:.2f}"
                    )
                    severity = ConcentrationSeverity.BREACH
                elif weight > self.config.max_strategy_sleeve_weight * 0.8:
                    if severity != ConcentrationSeverity.BREACH:
                        severity = ConcentrationSeverity.CAUTION

            # Clusters
            for c_id, symbols in context.correlation.clusters.items():
                cluster_used = 0.0
                for s in symbols:
                    slv = context.symbol_sleeves.get(s)
                    if slv:
                        cluster_used += slv.used_notional
                weight = cluster_used / total_budget
                cluster_conc[c_id] = weight

                if weight > self.config.max_correlated_cluster_weight:
                    breaches.append(
                        f"Cluster {c_id} weight {weight:.2f} > {self.config.max_correlated_cluster_weight:.2f}"
                    )
                    severity = ConcentrationSeverity.BREACH
                elif weight > self.config.max_correlated_cluster_weight * 0.8:
                    if severity != ConcentrationSeverity.BREACH:
                        severity = ConcentrationSeverity.CAUTION

        # Directional Concentration
        directional_conc = {}
        if context.exposure.total_exposure > 0:
            directional_conc["long_ratio"] = (
                context.exposure.long_exposure / context.exposure.total_exposure
            )
            directional_conc["short_ratio"] = (
                context.exposure.short_exposure / context.exposure.total_exposure
            )

        return ConcentrationSnapshot(
            timestamp=timestamp,
            symbol_concentration=symbol_conc,
            strategy_concentration=strategy_conc,
            quote_concentration={},  # Mock
            directional_concentration=directional_conc,
            cluster_concentration=cluster_conc,
            severity=severity,
            breaches=breaches,
        )
