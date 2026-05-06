import unittest
from app.reviews.models import ReviewScope
from app.reviews.scopes import validate_scope, narrow_scope
from app.reviews.exceptions import InvalidReviewRequestError


class TestReviewScopes(unittest.TestCase):
    def test_validate_scope(self):
        self.assertTrue(validate_scope(ReviewScope(workspace_id="ws-1")))
        with self.assertRaises(InvalidReviewRequestError):
            validate_scope(ReviewScope())

    def test_narrow_scope(self):
        s1 = ReviewScope(workspace_id="ws-1")
        s2 = ReviewScope(workspace_id="ws-1", profile_id="p-1")
        narrowed = narrow_scope(s1, s2)
        self.assertEqual(narrowed.workspace_id, "ws-1")
        self.assertEqual(narrowed.profile_id, "p-1")
        self.assertTrue(narrowed.narrow_explicitly)

        s3 = ReviewScope(workspace_id="ws-2")
        with self.assertRaises(InvalidReviewRequestError):
            narrow_scope(s1, s3)
