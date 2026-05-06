from app.reviews.models import ReviewAdjudication, QueueItem, ReviewDecisionRecord
from app.reviews.enums import AdjudicationVerdict, ReviewState
from app.reviews.exceptions import AdjudicationError
from app.reviews.base import AdjudicationEngineBase
import uuid


class AdjudicationEngine(AdjudicationEngineBase):
    def adjudicate(
        self,
        item: QueueItem,
        adjudicator_id: str,
        verdict: AdjudicationVerdict,
        rationale: str,
        conditions: str = None,
        accepted_constraints: list = None,
        rejected_evidence: list = None,
    ) -> ReviewDecisionRecord:
        if not rationale:
            raise AdjudicationError("Rationale must be provided for adjudication.")

        adjudication = ReviewAdjudication(
            adjudication_id=str(uuid.uuid4()),
            item_id=item.item_id,
            adjudicator_id=adjudicator_id,
            verdict=verdict,
            rationale=rationale,
            conditions=conditions,
        )

        decision = ReviewDecisionRecord(
            decision_id=str(uuid.uuid4()),
            adjudication=adjudication,
            accepted_constraints=accepted_constraints or [],
            rejected_evidence=rejected_evidence or [],
        )

        return decision
