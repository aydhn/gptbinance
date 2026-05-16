import unittest
from app.program_plane.slack import SlackManager
class TestSlack(unittest.TestCase):
    def test_slack(self):
        m = SlackManager()
        s = m.evaluate_slack("p1")
        self.assertEqual(s.milestone_slack_days, 5)
