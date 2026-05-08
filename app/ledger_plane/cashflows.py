from datetime import datetime, timezone
import uuid
from typing import Dict, Any
from decimal import Decimal

from app.ledger_plane.models import CashflowRecord
from app.ledger_plane.enums import CashflowClass
from app.performance_plane.models import AttributionNode
from app.performance_plane.enums import AttributionClass


class CashflowBuilder:
    @staticmethod
    def build(
        cashflow_class: CashflowClass,
        asset: str,
        amount: float,
        account_scope: str,
        direction: str,
        metadata: Dict[str, Any] = None,
    ) -> CashflowRecord:
        return CashflowRecord(
            id=str(uuid.uuid4()),
            cashflow_class=cashflow_class,
            asset=asset,
            amount=amount,
            account_scope=account_scope,
            direction=direction,
            timestamp=datetime.now(timezone.utc),
            metadata=metadata or {},
        )

    @staticmethod
    def export_fee_funding_carry_attribution(record: CashflowRecord) -> AttributionNode:
        multiplier = (
            Decimal("1") if record.direction.lower() == "inflow" else Decimal("-1")
        )
        impact = Decimal(str(record.amount)) * multiplier

        return AttributionNode(
            attribution_class=AttributionClass.FEE_FUNDING_CARRY,
            contribution_value=impact,
            currency=record.asset,
            proof_notes=[f"Ledger cashflow of class {record.cashflow_class.value}"],
        )
