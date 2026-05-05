from app.experiments.comparisons import BaselineComparisonEvaluator


def test_baseline_comparison_evaluator():
    evaluator = BaselineComparisonEvaluator()
    res = evaluator.evaluate("run_1")
    assert res["run_id"] == "run_1"
    assert res["verdict"] == "improvement"
