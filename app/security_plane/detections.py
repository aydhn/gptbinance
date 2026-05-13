from typing import Dict, List, Optional
from app.security_plane.models import SecurityDetectionRecord

class DetectionRegistry:
    def __init__(self):
        self._detections: Dict[str, SecurityDetectionRecord] = {}

    def register_detection(self, detection: SecurityDetectionRecord) -> None:
        self._detections[detection.detection_id] = detection

    def list_detections(self) -> List[SecurityDetectionRecord]:
        return list(self._detections.values())
