from app.experiments.timesplits import TimeSplitAnalyzer


def test_time_split_analyzer():
    analyzer = TimeSplitAnalyzer()
    results = analyzer.split_by_time({"dummy": "data"})
    assert "h1" in results
