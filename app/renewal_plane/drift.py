
from app.renewal_plane.models import RenewalDriftRecord, RenewalDriftClass

class DriftManager:
    def __init__(self):
        self.drifts = []

    def detect_drift(self, expected: str, actual: str) -> RenewalDriftRecord:
        if expected != actual:
            rec = RenewalDriftRecord(drift_id="drift_1", drift_class=RenewalDriftClass.CRITERIA_DRIFT)
            self.drifts.append(rec)
            return rec
        return None
