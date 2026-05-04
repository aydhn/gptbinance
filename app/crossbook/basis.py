from .models import BasisExposureReport

class BasisAnalyzer:
    def analyze(self, symbol: str) -> BasisExposureReport:
        return BasisExposureReport(symbol=symbol, spot_price=0.0, futures_price=0.0, basis_pct=0.0, caution=None)
