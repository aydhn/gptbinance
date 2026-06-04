
from app.renewal_plane.models import RenewalDebtRecord, RenewalDebtClass
from typing import List, Optional

class DebtManager:
    def evaluate(self, renewal_id: str) -> List[RenewalDebtRecord]:
        return []

    def get_severe_debt(self, renewal_id: str) -> Optional[RenewalDebtRecord]:
        return None
