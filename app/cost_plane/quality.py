from typing import List, Dict, Any

class QualityManager:
    def __init__(self):
        self._checks: List[Dict[str, Any]] = []

    def check_quality(self, warnings: List[str], severity: str) -> Dict[str, Any]:
        check = {
            "warnings": warnings,
            "severity": severity,
            "verdict": "pass" if not warnings else "fail"
        }
        self._checks.append(check)
        return check

    def list_checks(self) -> List[Dict[str, Any]]:
        return self._checks
