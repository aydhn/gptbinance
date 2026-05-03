from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.data_governance.models import GovernanceCatalogEntry, DatasetRef
from app.data_governance.enums import TrustLevel

class GovernanceCatalog:
    def __init__(self):
        self._entries: Dict[str, GovernanceCatalogEntry] = {}

    def _key(self, ref: DatasetRef) -> str:
        return f"{ref.dataset_id}:{ref.version}"

    def update_entry(self, entry: GovernanceCatalogEntry) -> None:
        self._entries[self._key(entry.dataset_ref)] = entry

    def get_entry(self, ref: DatasetRef) -> Optional[GovernanceCatalogEntry]:
        return self._entries.get(self._key(ref))

    def list_entries(self) -> List[GovernanceCatalogEntry]:
        return list(self._entries.values())
