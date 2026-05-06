import unittest
from app.reviews.enums import ReviewClass
from app.reviews.slas import get_sla_for_class


class TestReviewSLAs(unittest.TestCase):
    def test_sla(self):
        sla = get_sla_for_class(ReviewClass.INCIDENT_CONTAINMENT)
        self.assertEqual(sla.response_timeout_minutes, 15)
