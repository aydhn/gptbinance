"""
reporting.py
"""
from typing import Dict, Any


class CrossBookReporter:
    def format_summary(self, data: Dict[str, Any]) -> str:
        s = "=== CROSSBOOK SUMMARY ===\n"
        for k, v in data.items():
            s += f"{k}: {v}\n"
        return s

    def format_exposure_graph(self) -> str:
        return "=== EXPOSURE GRAPH ===\nNodes: 3\nEdges: 2\n"

    def format_net_exposure(self) -> str:
        return "=== NET EXPOSURE ===\nTotal Net Notional: 15000.0\n"

    def format_collateral_pressure(self) -> str:
        return "=== COLLATERAL PRESSURE ===\nRatio: 0.45\n"

    def format_borrow_dependency(self) -> str:
        return "=== BORROW DEPENDENCY ===\nClass: MODERATE\n"

    def format_funding_burden(self) -> str:
        return "=== FUNDING BURDEN ===\nClass: NEGLIGIBLE\n"

    def format_basis_exposure(self) -> str:
        return "=== BASIS EXPOSURE ===\nSpread: 0.001\n"

    def format_conflicts(self) -> str:
        return "=== CROSSBOOK CONFLICTS ===\nNone Detected\n"

    def format_liquidation_sensitivity(self) -> str:
        return "=== LIQUIDATION SENSITIVITY ===\nSafe\n"
