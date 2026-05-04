from app.crossbook.basis import BasisAnalyzer

def test_basis_analyzer():
    analyzer = BasisAnalyzer()
    report = analyzer.analyze("BTCUSDT")
    assert report.basis_pct == 0.0
