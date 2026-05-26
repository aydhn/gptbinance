# comparisons.py
from typing import Dict, List, Optional
from pydantic import BaseModel
from app.insolvency_plane.models import InsolvencyObjectRef

class InsolvencyComparisonRecord(BaseModel):
    comparison_id: str
    type: str # filed_vs_allowed, support_vs_confirmation, restructure_vs_liquidation, local_vs_federated
    entity_a_ref: str
    entity_b_ref: str
    difference_description: str
    lineage_refs: List[str]

class InsolvencyComparisonManager:
    def __init__(self):
        self.comparisons: Dict[str, InsolvencyComparisonRecord] = {}

    def register_comparison(self, comparison: InsolvencyComparisonRecord):
        self.comparisons[comparison.comparison_id] = comparison

    def get_comparison(self, comparison_id: str) -> Optional[InsolvencyComparisonRecord]:
        return self.comparisons.get(comparison_id)

    def list_comparisons(self) -> List[InsolvencyComparisonRecord]:
        return list(self.comparisons.values())
