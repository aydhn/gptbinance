from app.decision_quality_plane.models import DecisionTrustVerdict, DecisionManifest
from app.decision_quality_plane.enums import TrustVerdict

class TrustVerdictEngine:
    def evaluate(self, manifest: DecisionManifest) -> DecisionTrustVerdict:
        blockers = []
        breakdown = {}

        # 1. Option Completeness
        has_noop = any(o.option_class.value == "defer_no_op" for o in manifest.options)
        if len(manifest.options) < 2 or not has_noop:
            blockers.append("Missing options or NO_OP baseline")
            breakdown["options"] = "FAILED"
        else:
            breakdown["options"] = "OK"

        # 2. Assumptions Clarity
        if not manifest.assumptions:
            blockers.append("Hidden assumptions risk: no explicit assumptions recorded")
            breakdown["assumptions"] = "FAILED"
        else:
            breakdown["assumptions"] = "OK"

        # 3. Rationale
        if not manifest.rationale:
            blockers.append("Missing rationale for chosen option")
            breakdown["rationale"] = "FAILED"
        else:
            breakdown["rationale"] = "OK"

        # 4. Confidence Calibration
        if manifest.confidence and manifest.confidence.confidence_level.value == "very_high" and not manifest.evidence:
            blockers.append("Overconfidence detected: VERY_HIGH confidence with 0 evidence")
            breakdown["confidence"] = "FAILED"
        else:
            breakdown["confidence"] = "OK"

        # 5. Premortem & Stop conditions
        if not manifest.premortems:
            blockers.append("Missing premortem for decision")
            breakdown["premortem"] = "FAILED"
        else:
            breakdown["premortem"] = "OK"

        if len(blockers) > 0:
            return DecisionTrustVerdict(
                decision_id=manifest.decision.decision_id,
                verdict=TrustVerdict.BLOCKED,
                breakdown=breakdown,
                blockers=blockers
            )

        return DecisionTrustVerdict(
            decision_id=manifest.decision.decision_id,
            verdict=TrustVerdict.TRUSTED,
            breakdown=breakdown
        )
