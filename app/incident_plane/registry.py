from typing import List

class CanonicalIncidentRegistry:
    FAMILIES = [
        "data_integrity_incident",
        "execution_integrity_incident",
        "risk_breach_incident",
        "release_integrity_incident",
        "workflow_integrity_incident",
        "control_integrity_incident",
        "performance_integrity_incident",
        "strategy_integrity_incident",
        "simulation_integrity_incident",
        "market_truth_incident",
        "capital_ledger_incident",
        "crossbook_conflict_incident"
    ]

    @staticmethod
    def is_valid_family(family: str) -> bool:
        return family in CanonicalIncidentRegistry.FAMILIES
