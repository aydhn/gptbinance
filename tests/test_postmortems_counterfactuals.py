from app.postmortems.counterfactuals import CounterfactualAnalyzer


def test_counterfactual_analyzer():
    analyzer = CounterfactualAnalyzer()
    assessments = analyzer.analyze({}, {})
    assert len(assessments) == 1
    assert assessments[0].assessment == "insufficient_evidence"
