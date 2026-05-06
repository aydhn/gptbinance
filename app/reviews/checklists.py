from app.reviews.models import ReviewChecklist, ChecklistItem
from app.reviews.enums import ChecklistVerdict, ReviewClass
from app.reviews.exceptions import ChecklistIncompleteError
from typing import List
import uuid


def generate_checklist_for_class(
    item_id: str, review_class: ReviewClass
) -> ReviewChecklist:
    items = []
    items.append(
        ChecklistItem(
            item_id=str(uuid.uuid4()),
            description="Verify review scope matches the request rationale.",
        )
    )
    items.append(
        ChecklistItem(
            item_id=str(uuid.uuid4()),
            description="Check evidence pack for completeness and freshness.",
        )
    )

    if review_class == ReviewClass.INCIDENT_CONTAINMENT:
        items.append(
            ChecklistItem(
                item_id=str(uuid.uuid4()),
                description="Verify containment actions do not introduce broader systemic risks.",
            )
        )
    elif review_class == ReviewClass.BOARD_CONTRADICTION:
        items.append(
            ChecklistItem(
                item_id=str(uuid.uuid4()),
                description="Confirm resolution of domain contradiction and update conditional readiness.",
            )
        )

    return ReviewChecklist(checklist_id=str(uuid.uuid4()), item_id=item_id, items=items)


def verify_checklist_complete(checklist: ReviewChecklist):
    if not checklist:
        raise ChecklistIncompleteError("Checklist is missing.")
    for item in checklist.items:
        if item.is_required and item.verdict == ChecklistVerdict.INCOMPLETE:
            raise ChecklistIncompleteError(
                f"Required checklist item '{item.description}' is incomplete."
            )
