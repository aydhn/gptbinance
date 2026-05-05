from app.experiments.regimes import RegimeAnalyzer


def test_regime_analyzer():
    analyzer = RegimeAnalyzer()
    results = analyzer.split_by_regime({"dummy": "data"})
    assert "trend" in results
    assert "range" in results
