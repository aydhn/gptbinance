from typing import Dict, Any


class ReadinessDomains:
    # New readiness domains: ledger_integrity, performance_integrity
    @staticmethod
    def get_domains() -> list:
        return [
            "code_integrity",
            "model_integrity",
            "risk_integrity",
            "ledger_integrity",
            "performance_integrity",
        ]
