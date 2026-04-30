from app.ml.importance import ImportanceAnalyzer


def test_importance_analyzer():
    analyzer = ImportanceAnalyzer()
    summary = analyzer.analyze("run_1", None, None, None)

    assert summary.run_id == "run_1"
    assert summary.stable is True
