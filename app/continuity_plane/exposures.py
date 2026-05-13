from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityExposureRecord

class ContinuityExposureManager:
    def __init__(self):
        self._exposures: Dict[str, ContinuityExposureRecord] = {}

    def record_exposure(self, record: ContinuityExposureRecord) -> None:
        self._exposures[record.exposure_id] = record

    def get_exposure(self, exposure_id: str) -> Optional[ContinuityExposureRecord]:
        return self._exposures.get(exposure_id)

    def list_exposures(self) -> List[ContinuityExposureRecord]:
        return list(self._exposures.values())
