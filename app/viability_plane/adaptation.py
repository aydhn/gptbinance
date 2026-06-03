# Viability Integration: adaptation
from typing import Dict, Any

class AdaptationViabilityLinkage:
    def check_viability(self, posture: Dict[str, Any]) -> Dict[str, Any]:
        if not posture.get('is_sustainable'):
            return {"status": "caution", "reason": "no adaptation-safe claim under unsustainable posture", "proof_notes": "requires full viability transparency"}
        return {"status": "trusted", "reason": "viability posture supports adaptation"}
