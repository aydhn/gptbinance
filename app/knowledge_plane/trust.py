from typing import List
from .models import KnowledgeTrustVerdict
from .enums import TrustVerdict, FreshnessClass

class TrustedKnowledgeVerdictEngine:
    def evaluate(self, knowledge_id: str, freshness: str, applicability: bool, has_conflicts: bool = False, is_superseded: bool = False) -> KnowledgeTrustVerdict:
        reasons = []
        verdict = TrustVerdict.TRUSTED

        if not applicability:
            return KnowledgeTrustVerdict(verdict=TrustVerdict.BLOCKED, reasons=["Not applicable in the current context."])

        if is_superseded:
            return KnowledgeTrustVerdict(verdict=TrustVerdict.BLOCKED, reasons=["Knowledge is superseded. Active guidance blocked."])

        if has_conflicts:
            verdict = TrustVerdict.DEGRADED
            reasons.append("Conflicting guidance detected.")

        if freshness == FreshnessClass.EXPIRED.value:
            verdict = TrustVerdict.CAUTION
            reasons.append("Knowledge is expired.")
        elif freshness == FreshnessClass.STALE.value:
            verdict = TrustVerdict.CAUTION
            reasons.append("Knowledge is stale.")
        elif freshness == FreshnessClass.REVIEW_DUE.value:
            if verdict == TrustVerdict.TRUSTED:
                verdict = TrustVerdict.REVIEW_REQUIRED
            reasons.append("Review is due.")

        return KnowledgeTrustVerdict(verdict=verdict, reasons=reasons)
