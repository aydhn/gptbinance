from app.crossbook.liquidation import LiquidationAnalyzer
from app.crossbook.enums import LiquidationSensitivity

def test_liquidation_analyzer():
    analyzer = LiquidationAnalyzer()
    report = analyzer.analyze()
    assert report.sensitivity == LiquidationSensitivity.SAFE
