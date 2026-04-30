from app.ml.evaluation import Evaluator


def test_evaluator():
    evaluator = Evaluator()
    report = evaluator.evaluate("run_1", None, None)

    assert report.run_id == "run_1"
    assert report.f1_score == 0.75
