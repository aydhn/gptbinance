from typing import List, Dict, Any

class FairnessManager:
    def __init__(self):
        self._checks: List[Dict[str, Any]] = []

    def evaluate_fairness(self, subsidy_detected: bool, workload_source: str, workload_target: str, severity: str, notes: str) -> Dict[str, Any]:
        check = {
            "subsidy_detected": subsidy_detected,
            "workload_source": workload_source,
            "workload_target": workload_target,
            "severity": severity,
            "notes": notes
        }
        self._checks.append(check)
        return check

    def list_checks(self) -> List[Dict[str, Any]]:
        return self._checks
