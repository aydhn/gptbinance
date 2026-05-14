from typing import Dict, Optional, List
from app.supply_chain_plane.models import SignatureRecord


class SignatureRegistry:
    def __init__(self):
        self._signatures: Dict[str, SignatureRecord] = {}

    def register_signature(self, signature: SignatureRecord) -> None:
        self._signatures[signature.signature_id] = signature

    def get_signature(self, signature_id: str) -> Optional[SignatureRecord]:
        return self._signatures.get(signature_id)

    def get_signatures_for_artifact(self, artifact_id: str) -> List[SignatureRecord]:
        return [
            s
            for s in self._signatures.values()
            if s.artifact_ref.component_id == artifact_id
        ]
