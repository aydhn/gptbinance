from typing import Dict, Any
from app.settlement_plane.models import SettlementFinalityRecord
from app.settlement_plane.enums import FinalityClass

class FinalityEvaluator:
    def evaluate(self, context: Dict[str, Any]) -> SettlementFinalityRecord:
        is_final = context.get("is_final", False)
        has_reversal_window = context.get("has_reversal_window", False)

        if not is_final:
            return SettlementFinalityRecord(
                id="finality_none",
                finality_class=FinalityClass.NON_FINAL_POSTURE,
                details="Non-final posture",
                lineage_refs=[]
            )

        if has_reversal_window:
            return SettlementFinalityRecord(
                id="finality_cond",
                finality_class=FinalityClass.CONDITIONAL_FINALITY,
                details="Conditional finality due to reversal window",
                lineage_refs=[]
            )

        return SettlementFinalityRecord(
            id="finality_clean",
            finality_class=FinalityClass.CLEAN_FINALITY,
            details="Clean finality",
            lineage_refs=[]
        )
