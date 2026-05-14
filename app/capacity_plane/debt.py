from datetime import datetime, timezone
from typing import Dict, List
from app.capacity_plane.models import CapacityDebtRecord

_debts: Dict[str, CapacityDebtRecord] = {}


def record_debt(
    debt_id: str, debt_type: str, severity: str, description: str
) -> CapacityDebtRecord:
    rec = CapacityDebtRecord(
        debt_id=debt_id,
        debt_type=debt_type,
        severity=severity,
        description=description,
        created_at=datetime.now(timezone.utc),
    )
    _debts[debt_id] = rec
    return rec


def list_debts() -> List[CapacityDebtRecord]:
    return list(_debts.values())
