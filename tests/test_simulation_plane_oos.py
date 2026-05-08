from app.simulation_plane.oos import OOSEvaluator
from app.simulation_plane.enums import OOSClass


def test_oos_no_train():
    evaluator = OOSEvaluator()
    report = evaluator.evaluate("run1", [])
    assert report.oos_class == OOSClass.LEAKAGE_SUSPECTED
