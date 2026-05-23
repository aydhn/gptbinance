import uuid
from app.liability_plane.models import LiabilityDebtRecord
from app.liability_plane.repository import LiabilityRepository

class DebtManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def log_debt(self, liability_id: str, debt_type: str, severity: str, description: str) -> LiabilityDebtRecord:
        return LiabilityDebtRecord(
            debt_id=str(uuid.uuid4()),
            liability_id=liability_id,
            debt_type=debt_type,
            severity=severity,
            description=description
        )
