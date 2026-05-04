from app.crossbook.collateral import CollateralAnalyzer

def test_collateral_analyzer():
    analyzer = CollateralAnalyzer()
    report = analyzer.analyze()
    assert report.overall_pressure == 0.0
