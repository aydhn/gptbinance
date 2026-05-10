from typing import Dict, List, Optional, Any
from app.postmortem_plane.base import PostmortemRegistryBase
from app.postmortem_plane.models import PostmortemDefinition
from app.postmortem_plane.enums import PostmortemClass
from app.postmortem_plane.exceptions import InvalidPostmortemDefinitionError

class CanonicalPostmortemRegistry(PostmortemRegistryBase):
    def __init__(self):
        self._postmortems: Dict[str, PostmortemDefinition] = {}

    def register_postmortem(self, postmortem: PostmortemDefinition) -> str:
        if not postmortem.postmortem_id:
            raise InvalidPostmortemDefinitionError("Postmortem ID is required")
        if not postmortem.source_incidents or not postmortem.source_incidents.incident_ids:
             raise InvalidPostmortemDefinitionError("Postmortem must link to at least one incident")

        self._postmortems[postmortem.postmortem_id] = postmortem
        return postmortem.postmortem_id

    def get_postmortem(self, postmortem_id: str) -> Optional[PostmortemDefinition]:
        return self._postmortems.get(postmortem_id)

    def list_postmortems(self, filters: Dict[str, Any] = None) -> List[PostmortemDefinition]:
        # Simple implementation, real one would filter
        return list(self._postmortems.values())

    def validate_mandatory_requirements(self, postmortem: PostmortemDefinition) -> bool:
        if postmortem.postmortem_class in [
            PostmortemClass.INCIDENT_FULL_RCA,
            PostmortemClass.RELEASE_FAILURE_POSTMORTEM,
            PostmortemClass.DATA_INTEGRITY_POSTMORTEM,
            PostmortemClass.EXECUTION_LOSS_POSTMORTEM
        ]:
            if not postmortem.root_causes:
                return False
            if not postmortem.preventive_actions:
                 return False
        return True
