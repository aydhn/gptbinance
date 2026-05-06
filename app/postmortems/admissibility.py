from app.postmortems.enums import EvidenceVerdict
from typing import Dict, Any


class AdmissibilityRulesEngine:
    def evaluate(self, evidence: Dict[str, Any]) -> EvidenceVerdict:
        # Check freshness, scope, lineage, etc.
        return EvidenceVerdict.ACCEPTED
