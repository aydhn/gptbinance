from app.accountability_plane.models import AccountabilityObject, AccountabilityTrustVerdict
from app.accountability_plane.enums import TrustVerdict

class AccountabilityTrustEngine:
    @staticmethod
    def evaluate(acc_obj: AccountabilityObject, check_theater: bool = True) -> AccountabilityTrustVerdict:
        factors = {}

        # 1. Subject Clarity & Duty Integrity
        if not acc_obj.subject_refs or not acc_obj.duty_refs:
            factors["subject_duty"] = "Missing clear subject or duty mapping."
            return AccountabilityTrustVerdict(verdict=TrustVerdict.BLOCKED, factors=factors)

        # 2. Breach Evidence
        if not acc_obj.breach_refs:
            factors["breach_evidence"] = "Duty assigned but no proven breach evidence."
            return AccountabilityTrustVerdict(verdict=TrustVerdict.REVIEW_REQUIRED, factors=factors)

        # 3. Sanction Proportionality & Scapegoating Check
        if check_theater and acc_obj.breach_refs and not acc_obj.sanction_refs:
            factors["sanction"] = "Ownerless risk: Breach proven but no consequence applied."
            return AccountabilityTrustVerdict(verdict=TrustVerdict.CAUTION, factors=factors)

        # 4. Restitution Visibility
        if acc_obj.breach_refs and not acc_obj.restitution_refs:
            factors["restitution"] = "Unresolved restitution: Harm exists without remediation mapping."
            return AccountabilityTrustVerdict(verdict=TrustVerdict.DEGRADED, factors=factors)

        factors["integrity"] = "Accountability chain is intact and mapped."
        return AccountabilityTrustVerdict(verdict=TrustVerdict.TRUSTED, factors=factors)
