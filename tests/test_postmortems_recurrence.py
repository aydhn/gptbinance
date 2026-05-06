from app.postmortems.recurrence import RecurrenceScorer


def test_recurrence_scorer():
    scorer = RecurrenceScorer()
    report = scorer.score({}, {})
    assert report.score == 0.8  # Default base + no corrective
    assert "No corrective actions" in report.factors
