"""
liquidation.py
"""
from typing import List
from app.crossbook.models import (
    ExposureGraphModel,
    LiquidationSensitivityReport,
    CollateralPressureReport,
)
from app.crossbook.enums import LiquidationSensitivity


class LiquidationAnalyzer:
    def analyze(
        self, graph: ExposureGraphModel, col_report: CollateralPressureReport
    ) -> LiquidationSensitivityReport:
        sens = LiquidationSensitivity.SAFE
        assets: List[str] = []

        if col_report.pressure_ratio > 0.8:
            sens = LiquidationSensitivity.DANGEROUS
            assets = [d.asset for d in col_report.dependencies]
        elif col_report.pressure_ratio > 0.5:
            sens = LiquidationSensitivity.ELEVATED

        return LiquidationSensitivityReport(
            sensitivity=sens,
            contagion_risk_assets=assets,
            unwind_pressure=col_report.total_locked * 0.1,
        )
