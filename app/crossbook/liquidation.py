from .models import LiquidationSensitivityReport
from .enums import LiquidationSensitivity

class LiquidationAnalyzer:
    def analyze(self) -> LiquidationSensitivityReport:
        return LiquidationSensitivityReport(sensitivity=LiquidationSensitivity.SAFE, contagion_risk=False, notes="Safe")
