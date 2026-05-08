from app.research_plane.models import ResearchItem, ResearchTrustVerdict
from app.research_plane.enums import TrustVerdict
from app.research_plane.quality import QualityChecker
from app.research_plane.contradictions import ContradictionTracker


class TrustVerdictEngine:
    def evaluate(self, item: ResearchItem) -> ResearchTrustVerdict:
        factors = {}
        caveats = []
        verdict = TrustVerdict.TRUSTED

        qc = QualityChecker()
        q_result = qc.check_quality(item)
        factors["quality_score"] = str(q_result["score"])

        if q_result["score"] < 80:
            verdict = TrustVerdict.DEGRADED
            caveats.extend(q_result["warnings"])

        ct = ContradictionTracker()
        c_result = ct.evaluate_burden(item.contradictions)
        factors["unresolved_contradictions"] = str(c_result["unresolved_count"])

        if c_result["unresolved_count"] > 0:
            if verdict == TrustVerdict.TRUSTED:
                verdict = TrustVerdict.CAUTION
            elif verdict == TrustVerdict.DEGRADED:
                pass  # keep degraded
            caveats.append(f"Unresolved contradictions: {c_result['unresolved_count']}")

        if item.invalidation:
            verdict = TrustVerdict.BLOCKED
            caveats.append(f"Invalidated: {item.invalidation.reason}")

        return ResearchTrustVerdict(
            hypothesis_ref=(
                item.hypotheses[0].hypothesis_id if item.hypotheses else "unknown"
            ),
            verdict=verdict,
            factors=factors,
            caveats=caveats,
        )
