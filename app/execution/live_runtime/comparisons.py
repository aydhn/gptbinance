from typing import Dict, Any


class LiveComparisonTracker:
    def __init__(self):
        self.shadow_intent_count = 0
        self.live_intent_count = 0
        self.live_veto_count = 0
        self.live_fill_count = 0

    def record_shadow_intent(self) -> None:
        self.shadow_intent_count += 1

    def record_live_intent(self) -> None:
        self.live_intent_count += 1

    def record_live_veto(self) -> None:
        self.live_veto_count += 1

    def record_live_fill(self) -> None:
        self.live_fill_count += 1

    def get_comparison_summary(self) -> Dict[str, Any]:
        return {
            "shadow_intents": self.shadow_intent_count,
            "live_intents": self.live_intent_count,
            "live_vetoes": self.live_veto_count,
            "live_fills": self.live_fill_count,
            "intent_drift": self.shadow_intent_count - self.live_intent_count,
        }
