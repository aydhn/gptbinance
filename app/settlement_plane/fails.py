from typing import Dict, Any
from app.settlement_plane.models import SettlementFailRecord
from app.settlement_plane.enums import FailClass

class FailEvaluator:
    def evaluate(self, context: Dict[str, Any]) -> SettlementFailRecord:
        is_failing = context.get("is_failing", False)
        is_hidden = context.get("is_hidden", False)
        is_chronic = context.get("is_chronic", False)

        if not is_failing:
            return SettlementFailRecord(
                id="fail_none",
                fail_class=FailClass.BOUNDED_FAIL,
                details="No active fail",
                lineage_refs=[]
            )

        if is_hidden:
            return SettlementFailRecord(
                id="fail_hidden",
                fail_class=FailClass.HIDDEN_FAIL,
                details="Hidden fail burial",
                lineage_refs=[]
            )

        if is_chronic:
            return SettlementFailRecord(
                id="fail_chronic",
                fail_class=FailClass.CHRONIC_FAIL,
                details="Chronic fail",
                lineage_refs=[]
            )

        return SettlementFailRecord(
            id="fail_explicit",
            fail_class=FailClass.EXPLICIT_FAIL,
            details="Explicit fail",
            lineage_refs=[]
        )
