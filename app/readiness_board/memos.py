import uuid
from app.readiness_board.models import (
    FinalDecisionMemo,
    GoNoGoDecision,
    ReadinessDossier,
)
from app.readiness_board.enums import MemoClass, BoardVerdict
from app.readiness_board.storage import ReadinessBoardStorage


class MemoBuilder:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def build_memo(
        self, decision: GoNoGoDecision, dossier: ReadinessDossier
    ) -> FinalDecisionMemo:
        if decision.verdict == BoardVerdict.NO_GO:
            memo_class = MemoClass.BLOCKED
        elif decision.verdict == BoardVerdict.CONDITIONAL_GO:
            memo_class = MemoClass.CONDITIONAL
        else:
            memo_class = MemoClass.STANDARD

        summary = f"Decision for {dossier.candidate_id}: {decision.verdict.value.upper()}. Rationale: {decision.rationale}"

        memo = FinalDecisionMemo(
            memo_id=f"memo_{uuid.uuid4().hex[:8]}",
            decision_id=decision.decision_id,
            memo_class=memo_class,
            executive_summary=summary,
            accepted_risks=[
                f"Risk from domain {d.value}"
                for d, v in dossier.domain_verdicts.items()
                if v.verdict == "caution"
            ],
            next_steps=["Review findings"]
            if decision.verdict
            in [BoardVerdict.NO_GO, BoardVerdict.HOLD, BoardVerdict.NEEDS_REVIEW]
            else ["Proceed to next stage"],
        )
        self.storage.save_memo(memo)
        return memo
