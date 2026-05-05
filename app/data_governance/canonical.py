from typing import Dict, List, Optional
from app.data_governance.models import CanonicalId
from app.data_governance.enums import CanonicalEntityType
from app.data_governance.exceptions import CanonicalIdError


class CanonicalResolver:
    def __init__(self):
        self._mappings: Dict[CanonicalEntityType, Dict[str, CanonicalId]] = {
            t: {} for t in CanonicalEntityType
        }
        self._alias_index: Dict[CanonicalEntityType, Dict[str, str]] = {
            t: {} for t in CanonicalEntityType
        }

    def register(self, canonical_id: CanonicalId) -> None:
        self._mappings[canonical_id.entity_type][
            canonical_id.canonical_id
        ] = canonical_id
        for alias in canonical_id.aliases:
            if alias in self._alias_index[canonical_id.entity_type]:
                existing_canonical = self._alias_index[canonical_id.entity_type][alias]
                if existing_canonical != canonical_id.canonical_id:
                    # ambiguous alias
                    self._mappings[canonical_id.entity_type][
                        existing_canonical
                    ].is_ambiguous = True
                    canonical_id.is_ambiguous = True
            self._alias_index[canonical_id.entity_type][
                alias
            ] = canonical_id.canonical_id

    def resolve(
        self, alias: str, entity_type: CanonicalEntityType
    ) -> Optional[CanonicalId]:
        canonical_id_str = self._alias_index[entity_type].get(alias)
        if not canonical_id_str:
            return None
        return self._mappings[entity_type][canonical_id_str]
