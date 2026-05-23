from typing import Dict, Any, List
# pylint: disable=unused-import
# flake8: noqa

class ReadinessManager:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def aggregate(self) -> Dict[str, Any]:
        return {
            "mandate_clarity": self.data.get("mandate_clarity", "UNKNOWN"),
            "decision_right_rigor": self.data.get("decision_right_rigor", "UNKNOWN"),
            "delegation_hygiene": self.data.get("delegation_hygiene", "UNKNOWN"),
            "override_bounds": self.data.get("override_bounds", "UNKNOWN"),
            "legitimacy_visibility": self.data.get("legitimacy_visibility", "UNKNOWN"),
            "readiness_classes": self.data.get("classes", []),
            "proof_notes": self.data.get("notes", [])
        }
