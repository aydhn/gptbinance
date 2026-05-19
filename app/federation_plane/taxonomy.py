from typing import Dict, List, Optional
from app.federation_plane.models import FederationTaxonomyRecord
from app.federation_plane.exceptions import FederationPlaneError


class TaxonomyRegistry:
    def __init__(self):
        self._records: Dict[str, FederationTaxonomyRecord] = {}

    def register(self, record: FederationTaxonomyRecord):
        if not record.taxonomy_id:
            raise FederationPlaneError("No taxonomy collapse allowed. ID required.")
        self._records[record.taxonomy_id] = record

    def get_taxonomy(self, taxonomy_id: str) -> Optional[FederationTaxonomyRecord]:
        return self._records.get(taxonomy_id)

    def list_taxonomies(self) -> List[FederationTaxonomyRecord]:
        return list(self._records.values())
