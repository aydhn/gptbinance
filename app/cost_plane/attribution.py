from typing import List, Dict, Any

class AttributionManager:
    def __init__(self):
        self._attributions: List[Dict[str, Any]] = []

    def record_attribution(self, spend_id: str, workload: str, environment: str, strategy: str = None, release: str = None, tenant: str = None) -> Dict[str, Any]:
        record = {
            "spend_id": spend_id,
            "workload": workload,
            "environment": environment,
            "strategy": strategy,
            "release": release,
            "tenant": tenant,
            "completeness": 1.0 if workload and environment else 0.5
        }
        self._attributions.append(record)
        return record

    def list_records(self) -> List[Dict[str, Any]]:
        return self._attributions
