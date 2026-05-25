from .models import DisputeRecord, DisputeTrustVerdictRecord, DisputeTrustVerdict
from .exceptions import *

class TrustedDisputeVerdictEngine:
    @staticmethod
    def evaluate(dispute: DisputeRecord) -> DisputeTrustVerdictRecord:
        blockers = []
        cautions = []
        factors = {
            "issue_clarity": True,
            "burden_rigor": True,
            "admissibility_integrity": True,
            "record_completeness": True,
            "review_path_discipline": True,
            "appeal_visibility": True
        }

        # Check Issue Burial
        unresolved_issues = [i for i in dispute.issues if not i.resolved]
        if dispute.disposition_posture and unresolved_issues:
            blockers.append("Issue Burial Detected: Resolved disposition with unresolved issues.")
            factors["issue_clarity"] = False
            raise DisputeBurialViolation("No issue burial allowed.")

        # Check Dismissal Theater
        if dispute.dismissals and not any(r for r in dispute.rulings if r.ruling_class.value == 'merits'):
            cautions.append("Dismissal Theater Risk: Dismissed without merits ruling.")

        # Check Off-Record Adjudication
        off_record_rulings = [r for r in dispute.rulings if not r.on_record]
        if off_record_rulings:
            blockers.append("Off-Record Adjudication Detected.")
            factors["record_completeness"] = False
            raise OffRecordAdjudicationViolation("No off-record adjudication.")

        # Check Appeal Starvation
        pending_appeals = [a for a in dispute.appeals if a.appeal_class.value == 'pending']
        if pending_appeals:
            cautions.append("Appeal Starvation Risk: Pending appeals.")

        verdict = DisputeTrustVerdict.TRUSTED
        if blockers:
            verdict = DisputeTrustVerdict.BLOCKED
        elif cautions:
            verdict = DisputeTrustVerdict.CAUTION

        return DisputeTrustVerdictRecord(
            verdict=verdict,
            factors=factors,
            blockers=blockers,
            cautions=cautions
        )
