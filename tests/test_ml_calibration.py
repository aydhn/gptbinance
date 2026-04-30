from app.ml.calibration import Calibrator
from app.ml.enums import CalibrationType


def test_calibrator():
    calibrator = Calibrator()
    report = calibrator.calibrate("run_1", None, None, CalibrationType.ISOTONIC)

    assert report.run_id == "run_1"
    assert report.calibrator_type == CalibrationType.ISOTONIC
