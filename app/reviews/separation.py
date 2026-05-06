from app.reviews.models import QueueItem, SeparationOfDutiesCheck
from app.reviews.enums import ReviewClass
from app.reviews.exceptions import SeparationOfDutiesViolation


class SeparationOfDutiesEngine:
    def check_adjudication_eligibility(
        self, item: QueueItem, adjudicator_id: str
    ) -> SeparationOfDutiesCheck:
        producer_id = item.request.producer_id

        if item.request.requires_dual_control and producer_id == adjudicator_id:
            return SeparationOfDutiesCheck(
                item_id=item.item_id,
                producer_id=producer_id,
                adjudicator_id=adjudicator_id,
                is_valid=False,
                reason="Dual control required. Producer cannot be final adjudicator.",
            )

        if item.request.is_high_risk and producer_id == adjudicator_id:
            return SeparationOfDutiesCheck(
                item_id=item.item_id,
                producer_id=producer_id,
                adjudicator_id=adjudicator_id,
                is_valid=False,
                reason="High-risk review. Producer cannot be final adjudicator.",
            )

        return SeparationOfDutiesCheck(
            item_id=item.item_id,
            producer_id=producer_id,
            adjudicator_id=adjudicator_id,
            is_valid=True,
            reason="Eligible.",
        )

    def enforce_adjudication(self, item: QueueItem, adjudicator_id: str):
        check = self.check_adjudication_eligibility(item, adjudicator_id)
        if not check.is_valid:
            raise SeparationOfDutiesViolation(check.reason)
