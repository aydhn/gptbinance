from typing import Dict, Any


class EvidenceBundleBuilder:
    def assemble(self, incident_id: str) -> Dict[str, Any]:
        return {"incident_id": incident_id, "evidence": []}


class EvidenceFreshnessChecker:
    def is_fresh(self, evidence: Dict[str, Any]) -> bool:
        return True
