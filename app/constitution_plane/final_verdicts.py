from typing import List
from app.constitution_plane.models import FinalVerdictRecord, DomainVerdictRecord, PrecedenceRecord
from app.constitution_plane.enums import VerdictClass

class FinalVerdictSynthesizer:
    def synthesize(self,
                   object_id: str,
                   domain_verdicts: List[DomainVerdictRecord],
                   precedences: List[PrecedenceRecord],
                   federated_domain_verdicts: List[str] = None,
                   portability_caveats: List[str] = None,
                   tenant_scoped_blockers: List[str] = None) -> FinalVerdictRecord:

        federated_domain_verdicts = federated_domain_verdicts or []
        portability_caveats = portability_caveats or []
        tenant_scoped_blockers = tenant_scoped_blockers or []

        if tenant_scoped_blockers:
            return FinalVerdictRecord(
                object_id=object_id,
                final_verdict=VerdictClass.BLOCKED,
                rationale="Blocked due to tenant-scoped federated blockers.",
                active_vetoes=[], applied_waivers=[], applied_overrides=[], unresolved_conflicts=[]
            )

        # 1. No majority-green theater: Check for ANY hard block or veto
        vetoes = [dv for dv in domain_verdicts if dv.verdict == VerdictClass.BLOCKED and not dv.is_stale]

        if vetoes:
            return FinalVerdictRecord(
                object_id=object_id,
                final_verdict=VerdictClass.BLOCKED,
                rationale=f"Hard vetoes detected from: {[v.domain for v in vetoes]}",
                active_vetoes=[v.domain for v in vetoes],
                applied_waivers=[],
                applied_overrides=[],
                unresolved_conflicts=[]
            )

        # 2. Check for stale evidence leading to cautions
        cautions = [dv for dv in domain_verdicts if dv.verdict == VerdictClass.PASS_WITH_CAUTION or dv.is_stale]

        # Determine verdict
        verdict = VerdictClass.PASS
        if len(cautions) > 2:
            verdict = VerdictClass.REVIEW_REQUIRED
            rationale = "Compound risk threshold exceeded due to multiple cautions/stale evidence."
        elif cautions:
            verdict = VerdictClass.PASS_WITH_CAUTION
            rationale = "Passed with cautions."
        else:
            rationale = "Constitutionally eligible. No vetoes or compound risks detected."

        return FinalVerdictRecord(
            object_id=object_id,
            final_verdict=verdict,
            rationale=rationale,
            active_vetoes=[],
            applied_waivers=[],
            applied_overrides=[],
            unresolved_conflicts=[]
        )

# Scenario extensions

# Scenario extensions
