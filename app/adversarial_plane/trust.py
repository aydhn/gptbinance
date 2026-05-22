from typing import Dict, Any, List
from app.adversarial_plane.models import AdversarialTrustVerdict
from app.adversarial_plane.enums import TrustVerdict
from app.adversarial_plane.base import TrustEvaluatorBase

class DefaultTrustEvaluator(TrustEvaluatorBase):
    def evaluate(self, context: Dict[str, Any]) -> AdversarialTrustVerdict:
        factors = context.get("factors", {})
        blockers = context.get("blockers", [])
        caveats = context.get("caveats", [])

        verdict = TrustVerdict.TRUSTED
        if blockers:
            verdict = TrustVerdict.BLOCKED
        elif context.get("review_needed", False):
            verdict = TrustVerdict.REVIEW_REQUIRED
        elif len(caveats) > 2:
            verdict = TrustVerdict.DEGRADED
        elif len(caveats) > 0:
            verdict = TrustVerdict.CAUTION

        return AdversarialTrustVerdict(
            verdict_id=context.get("verdict_id", "default_verdict"),
            verdict=verdict,
            factors=factors,
            caveats=caveats,
            blockers=blockers
        )

class TrustManager:
    def __init__(self):
        self._verdicts = {}

    def add_verdict(self, verdict: AdversarialTrustVerdict):
        self._verdicts[verdict.verdict_id] = verdict

    def get_verdict(self, verdict_id: str) -> AdversarialTrustVerdict:
        return self._verdicts.get(verdict_id)

    def list_verdicts(self) -> List[AdversarialTrustVerdict]:
        return list(self._verdicts.values())
