import unittest
from app.reviews.escalations import EscalationEngine
from app.reviews.enums import EscalationClass


class TestReviewEscalations(unittest.TestCase):
    def test_escalation(self):
        engine = EscalationEngine()
        esc = engine.escalate(
            "item1", EscalationClass.SLA_BREACH, "too long", "system", "manager"
        )
        self.assertEqual(esc.escalation_class, EscalationClass.SLA_BREACH)
