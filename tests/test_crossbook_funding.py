from app.crossbook.funding import FundingAnalyzer

def test_funding_analyzer():
    analyzer = FundingAnalyzer()
    overlay = analyzer.analyze("BTCUSDT")
    assert overlay.expected_drag_usd_per_day == 0.0
