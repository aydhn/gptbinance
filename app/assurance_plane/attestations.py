from app.assurance_plane.models import AttestationRecord
from app.assurance_plane.enums import AttestationClass

def create_attestation(attestation_id: str, assurance_id: str, att_class: AttestationClass, attestor: str) -> AttestationRecord:
    return AttestationRecord(
        attestation_id=attestation_id,
        assurance_id=assurance_id,
        attestation_class=att_class,
        attestor=attestor
    )
