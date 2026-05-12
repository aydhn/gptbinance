from typing import Dict, List, Optional
from .models import TagDefinition
from .exceptions import InvalidDimensionOrTagError

class TagRegistry:
    def __init__(self):
        self._tags: Dict[str, TagDefinition] = {}

    def register_tag(self, tag: TagDefinition) -> None:
        if not tag.cardinality_expectation:
            raise InvalidDimensionOrTagError("Tag must declare cardinality expectation.")
        self._tags[tag.tag_id] = tag

    def get_tag(self, tag_id: str) -> Optional[TagDefinition]:
        return self._tags.get(tag_id)

    def list_tags(self) -> List[TagDefinition]:
        return list(self._tags.values())
