from app.postmortem_plane.models import PostmortemDefinition, PostmortemTrustVerdict
from app.postmortem_plane.enums import TrustVerdict
from app.postmortem_plane.base import TrustEvaluatorBase
from app.postmortem_plane.quality import PostmortemQualityEvaluator

class TrustedPostmortemEngine(TrustEvaluatorBase):
    def evaluate_trust(self, postmortem: PostmortemDefinition) -> PostmortemTrustVerdict:
        quality = PostmortemQualityEvaluator.evaluate(postmortem)

        verdict = TrustVerdict.TRUSTED
        if "Missing root cause" in quality["warnings"]:
             verdict = TrustVerdict.DEGRADED

        has_debt = len(postmortem.debt_records) > 0
        has_recurrence = len(postmortem.recurrence_records) > 0

        if has_recurrence and not postmortem.preventive_actions:
             verdict = TrustVerdict.BLOCKED

        return PostmortemTrustVerdict(
            verdict=verdict,
            evidence_completeness=len(postmortem.evidence_reviews) > 0,
            causal_chain_quality=postmortem.causal_chain is not None,
            contributor_coverage=len(postmortem.contributors) > 0,
            action_quality=len(postmortem.corrective_actions) > 0,
            verification_integrity=all(a.verification_records for a in postmortem.corrective_actions),
            debt_visibility=True,
            recurrence_handling=True,
            policy_posture=True,
            breakdown_notes=f"Quality Score: {quality['quality_score']}, Warnings: {quality['warnings']}"
        )
