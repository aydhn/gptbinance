from typing import Dict, Any
from app.viability_plane.enums import TrustVerdict

class ViabilityTrustEngine:
    def evaluate_trust(self, posture: Dict[str, Any]) -> TrustVerdict:
        if posture.get('hidden_subsidy') or posture.get('phantom_profitability'):
            return TrustVerdict.BLOCKED
        if posture.get('thin_margin') or posture.get('deferred_maintenance'):
            return TrustVerdict.CAUTION
        return TrustVerdict.TRUSTED
