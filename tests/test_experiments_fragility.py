from app.experiments.fragility import FragilityAnalyzer


def test_fragility_analyzer():
    analyzer = FragilityAnalyzer()
    res = analyzer.analyze("run_1", {})
    assert res["run_id"] == "run_1"
    assert res["sample_size_warning"] is True
