from typing import Dict, List
from app.representation_plane.models import RepresentationObject
from app.representation_plane.exceptions import InvalidRepresentationObjectError

class CanonicalRepresentationRegistry:
    def __init__(self):
        self._representations: Dict[str, RepresentationObject] = {}

    def register(self, rep: RepresentationObject) -> None:
        if not rep.representation_id:
            raise InvalidRepresentationObjectError("Representation must have an ID")
        self._representations[rep.representation_id] = rep

    def get(self, representation_id: str) -> RepresentationObject:
        return self._representations.get(representation_id)

    def list_all(self) -> List[RepresentationObject]:
        return list(self._representations.values())

representation_registry = CanonicalRepresentationRegistry()
