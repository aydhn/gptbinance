from app.crossbook.borrow import BorrowAnalyzer

def test_borrow_analyzer():
    analyzer = BorrowAnalyzer()
    report = analyzer.analyze()
    assert report.total_borrowed_usd == 0.0
