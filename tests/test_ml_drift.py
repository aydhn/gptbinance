from app.ml.drift import DriftChecker
from app.ml.enums import DriftSeverity


def test_drift_checker():
    checker = DriftChecker()
    report = checker.check_drift("run_1", None)

    assert report.run_id == "run_1"
    assert report.severity == DriftSeverity.NONE
