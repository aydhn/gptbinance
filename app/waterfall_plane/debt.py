from app.waterfall_plane.models import WaterfallDebtRecord
from app.waterfall_plane.enums import DebtClass

def register_debt(debt_id: str, debt_class: DebtClass, severity: str) -> WaterfallDebtRecord:
    return WaterfallDebtRecord(debt_id=debt_id, debt_class=debt_class, severity=severity)
