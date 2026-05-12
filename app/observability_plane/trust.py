from typing import Dict, List, Optional
from .models import ObservabilityTrustVerdict
from .enums import TrustVerdict

class TrustVerdictEngine:
    def __init__(self):
        self._verdicts: Dict[str, ObservabilityTrustVerdict] = {}

    def report_verdict(self, context_id: str, verdict: ObservabilityTrustVerdict) -> None:
        self._verdicts[context_id] = verdict

    def get_verdict(self, context_id: str) -> Optional[ObservabilityTrustVerdict]:
        return self._verdicts.get(context_id)

    def list_verdicts(self) -> Dict[str, ObservabilityTrustVerdict]:
        return self._verdicts.copy()
