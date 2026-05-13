from typing import Dict, List, Optional
from app.security_plane.models import ExposureRecord

class ExposureManager:
    def __init__(self):
        self._exposures: Dict[str, ExposureRecord] = {}

    def record_exposure(self, exposure: ExposureRecord) -> None:
        self._exposures[exposure.exposure_id] = exposure

    def list_exposures(self) -> List[ExposureRecord]:
        return list(self._exposures.values())
