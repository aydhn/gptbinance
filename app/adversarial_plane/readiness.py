from typing import List, Optional, Dict, Any

class AdversarialReadinessAggregator:
    def __init__(self):
        self._components: Dict[str, Any] = {}

    def add_component(self, name: str, data: Any):
        self._components[name] = data

    def aggregate(self) -> Dict[str, Any]:
        return {
            "actor_coverage": self._components.get("actor_coverage", "unknown"),
            "exploit_visibility": self._components.get("exploit_visibility", "unknown"),
            "resistance_strength": self._components.get("resistance_strength", "unknown"),
            "gaming_cleanliness": self._components.get("gaming_cleanliness", "unknown"),
            "confirmation_refutation_discipline": self._components.get("confirmation_refutation_discipline", "unknown"),
            "readiness_classes": self._components.get("readiness_classes", []),
            "readiness_proof_notes": self._components.get("readiness_proof_notes", "")
        }
