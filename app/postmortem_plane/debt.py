from typing import List
from app.postmortem_plane.models import RemediationDebtRecord
from app.postmortem_plane.enums import DebtClass, DebtInterestClass

class RemediationDebtTracker:
    @staticmethod
    def track_debt(debt_id: str, action_ref: str, d_class: DebtClass, interest: DebtInterestClass, lineages: List[str] = None) -> RemediationDebtRecord:
        return RemediationDebtRecord(
            debt_id=debt_id,
            action_ref=action_ref,
            debt_class=d_class,
            interest_class=interest,
            lineage_refs=lineages or []
        )
