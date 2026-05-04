from .models import CollateralPressureReport

class CollateralAnalyzer:
    def analyze(self) -> CollateralPressureReport:
        return CollateralPressureReport(dependencies=[], overall_pressure=0.0, warning=None)
