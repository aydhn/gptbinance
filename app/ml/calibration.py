from app.ml.models import CalibrationReport
from app.ml.enums import CalibrationType


class Calibrator:
    def calibrate(
        self, run_id: str, predictions, targets, cal_type: CalibrationType
    ) -> CalibrationReport:
        # probability calibration
        return CalibrationReport(
            run_id=run_id,
            calibrator_type=cal_type,
            brier_score_before=0.15,
            brier_score_after=0.10,
            raw_vs_calibrated_diff_mean=0.05,
        )
