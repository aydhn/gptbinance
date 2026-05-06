from app.postmortems.root_causes import RootCauseEvaluator


def test_root_cause_evaluator():
    evaluator = RootCauseEvaluator()
    candidates = evaluator.evaluate({})
    assert len(candidates) == 1
    assert candidates[0].candidate_id == "rc_unknown"
