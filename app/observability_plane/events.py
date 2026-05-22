from typing import Dict, Any, List

class CanonicalAdversarialEvents:
    def __init__(self):
        self.events = []

    def record_event(self, event_type: str, details: Dict[str, Any]):
        valid_events = {
            "exploit_surface_registered", "gaming_pattern_detected",
            "evidence_poisoning_suspected", "review_evasion_detected",
            "exploit_confirmed", "suspicion_refuted"
        }
        if event_type in valid_events:
            self.events.append({"type": event_type, "details": details})
