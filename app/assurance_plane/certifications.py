from app.assurance_plane.models import CertificationRecord
from app.assurance_plane.enums import CertificationClass

def create_certification(certification_id: str, assurance_id: str, cert_class: CertificationClass, issuer: str, valid_until=None) -> CertificationRecord:
    return CertificationRecord(
        certification_id=certification_id,
        assurance_id=assurance_id,
        certification_class=cert_class,
        issuer=issuer,
        valid_until=valid_until
    )
