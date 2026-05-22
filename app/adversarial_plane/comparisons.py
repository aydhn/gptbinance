from typing import List, Optional
from app.adversarial_plane.models import AdversarialComparisonRecord

def create_comparison(comparison_id: str, comparison_type: str, details: str, lineage_refs: Optional[List[str]] = None) -> AdversarialComparisonRecord:
    valid_types = {"benign_vs_malicious", "old_vs_hardened", "exploit_a_vs_b", "suspicion_vs_confirmation"}
    if comparison_type not in valid_types:
        raise ValueError(f"Invalid comparison type. Must be one of {valid_types}")
    return AdversarialComparisonRecord(
        comparison_id=comparison_id,
        comparison_type=comparison_type,
        details=details,
        lineage_refs=lineage_refs or []
    )

class ComparisonManager:
    def __init__(self):
        self._comparisons = {}

    def add_comparison(self, comp: AdversarialComparisonRecord):
        self._comparisons[comp.comparison_id] = comp

    def get_comparison(self, comparison_id: str) -> Optional[AdversarialComparisonRecord]:
        return self._comparisons.get(comparison_id)

    def list_comparisons(self) -> List[AdversarialComparisonRecord]:
        return list(self._comparisons.values())
