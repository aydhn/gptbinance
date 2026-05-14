from typing import Dict, List, Optional

class CostTracker:
    def __init__(self):
        self._costs: Dict[str, str] = {}

    def report_cost_burden(self, telemetry_id: str, burden: str) -> None:
        self._costs[telemetry_id] = burden

    def get_cost_burden(self, telemetry_id: str) -> Optional[str]:
        return self._costs.get(telemetry_id)

    def list_cost_burdens(self) -> Dict[str, str]:
        return self._costs.copy()



# Cost plane evaluation integration
def get_evidence_retention_cost_caution(evidence_retention_rationale: bool):
    if not evidence_retention_rationale:
        return "caution"
    return "ready"
