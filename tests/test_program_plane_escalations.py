import unittest
from app.program_plane.escalations import EscalationManager
class TestEsc(unittest.TestCase):
    def test_esc(self):
        e = EscalationManager()
        r = e.escalate("p1")
        self.assertFalse(r.is_resolved)
