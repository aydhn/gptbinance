from typing import Dict, List, Optional
from app.attestation_plane.models import AttestationObject
from app.attestation_plane.exceptions import InvalidAttestationObjectError

class CanonicalAttestationRegistry:
    def __init__(self):
        self._objects: Dict[str, AttestationObject] = {}

    def register(self, obj: AttestationObject):
        if not obj.attestation_id:
            raise InvalidAttestationObjectError("Missing attestation_id")
        self._objects[obj.attestation_id] = obj

    def get(self, attestation_id: str) -> Optional[AttestationObject]:
        return self._objects.get(attestation_id)

    def list_all(self) -> List[AttestationObject]:
        return list(self._objects.values())
