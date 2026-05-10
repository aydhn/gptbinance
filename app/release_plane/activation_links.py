from typing import Dict
from app.release_plane.models import ReleaseRef
from app.release_plane.exceptions import ReleasePlaneError
import uuid

class ActivationLinkRecord:
    def __init__(self, link_id: str, activation_stage: str, release_ref: ReleaseRef, required_evidence: list):
        self.link_id = link_id
        self.activation_stage = activation_stage
        self.release_ref = release_ref
        self.required_evidence = required_evidence

class ActivationLinkManager:
    def __init__(self):
        self._links: Dict[str, ActivationLinkRecord] = {}

    def link_activation(self, activation_stage: str, release_id: str, required_evidence: list) -> ActivationLinkRecord:
        if not release_id:
             raise ReleasePlaneError("Release-less activation is strictly prohibited.")

        record = ActivationLinkRecord(
            link_id=f"act-link-{uuid.uuid4().hex[:8]}",
            activation_stage=activation_stage,
            release_ref=ReleaseRef(release_id=release_id),
            required_evidence=required_evidence
        )
        self._links[record.link_id] = record
        return record
