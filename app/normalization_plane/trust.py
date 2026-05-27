from app.normalization_plane.models import NormalizationRecord, NormalizationTrustReport, NormalizationTrustVerdict
from app.normalization_plane.enums import ReentryGateStatus

class TrustVerdictEngine:
    def evaluate(self, record: NormalizationRecord) -> NormalizationTrustReport:
        blockers = []
        cautions = []
        verdict = NormalizationTrustVerdict.TRUSTED

        if record.reentry_gate and record.reentry_gate.status != ReentryGateStatus.CLEARED:
            cautions.append("Re-entry gate is not cleared.")
            verdict = NormalizationTrustVerdict.CAUTION

        for scar in record.residual_scars:
            if scar.is_hidden:
                blockers.append("Hidden residual scar detected.")
                verdict = NormalizationTrustVerdict.BLOCKED

        for lift in record.limit_lifts:
            if lift.is_premature:
                blockers.append("Premature limit lift detected.")
                verdict = NormalizationTrustVerdict.BLOCKED

        return NormalizationTrustReport(
            verdict=verdict,
            reentry_clarity="Clear" if not blockers else "Blocked",
            authorization_rigor="Strict",
            guardrail_integrity="Maintained",
            residual_scar_visibility="Hidden Scars Present" if any(s.is_hidden for s in record.residual_scars) else "Visible",
            blockers=blockers,
            cautions=cautions
        )
