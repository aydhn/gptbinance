from typing import Dict, List, Optional
from app.security_plane.models import CertificateDefinition

class CertificateManager:
    def __init__(self):
        self._certs: Dict[str, CertificateDefinition] = {}

    def register_certificate(self, cert: CertificateDefinition) -> None:
        self._certs[cert.cert_id] = cert

    def list_certificates(self) -> List[CertificateDefinition]:
        return list(self._certs.values())
