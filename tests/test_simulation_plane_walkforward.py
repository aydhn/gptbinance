from app.simulation_plane.walkforward import WalkForwardEvaluator
from app.simulation_plane.enums import WalkForwardClass


def test_walkforward_insufficient():
    evaluator = WalkForwardEvaluator()
    report = evaluator.evaluate("run1", [{"fold": 1}])
    assert report.wf_class == WalkForwardClass.INSUFFICIENT_FOLDS
