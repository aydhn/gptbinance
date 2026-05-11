from app.compliance_plane.models import CertificationRecord
from typing import Dict, List
from datetime import datetime, timezone


class CertificationManager:
    def __init__(self):
        self._certifications: Dict[str, CertificationRecord] = {}

    def register_certification(self, cert: CertificationRecord) -> None:
        self._certifications[cert.certification_id] = cert

    def get_active_certifications(self) -> List[CertificationRecord]:
        now = datetime.now(timezone.utc)
        return [c for c in self._certifications.values() if now <= c.expires_at]

    def list_certifications(self) -> List[CertificationRecord]:
        return list(self._certifications.values())
