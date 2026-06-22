from typing import Dict, Any
from app.settlement_plane.models import MatchingRecord
from app.settlement_plane.enums import MatchClass

class MatchingEvaluator:
    def evaluate(self, context: Dict[str, Any]) -> MatchingRecord:
        is_matched = context.get("is_matched", False)
        is_partial = context.get("is_partial", False)

        if not is_matched:
            return MatchingRecord(
                id="match_false",
                match_class=MatchClass.FALSE_MATCH,
                details="False match or unmatched",
                lineage_refs=[]
            )

        if is_partial:
            return MatchingRecord(
                id="match_partial",
                match_class=MatchClass.PARTIAL_MATCH,
                details="Partial match",
                lineage_refs=[]
            )

        return MatchingRecord(
            id="match_clean",
            match_class=MatchClass.CLEAN_MATCH,
            details="Clean match",
            lineage_refs=[]
        )
