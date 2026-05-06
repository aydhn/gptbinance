import unittest
from app.reviews.checklists import (
    generate_checklist_for_class,
    verify_checklist_complete,
)
from app.reviews.enums import ReviewClass, ChecklistVerdict
from app.reviews.exceptions import ChecklistIncompleteError


class TestReviewChecklists(unittest.TestCase):
    def test_checklist_generation_and_verification(self):
        checklist = generate_checklist_for_class(
            "item1", ReviewClass.BOARD_CONTRADICTION
        )
        self.assertTrue(len(checklist.items) > 0)

        with self.assertRaises(ChecklistIncompleteError):
            verify_checklist_complete(checklist)

        for item in checklist.items:
            item.verdict = ChecklistVerdict.COMPLETED

        verify_checklist_complete(checklist)
